#include <portaudio.h>
#include <sndfile.h>
#include <iostream>

#define FRAMES_PER_BUFFER 512

typedef struct {
    SNDFILE* file;
    SF_INFO sfinfo;
} AudioData;

static int paCallback(const void* inputBuffer, void* outputBuffer,
                      unsigned long framesPerBuffer,
                      const PaStreamCallbackTimeInfo* timeInfo,
                      PaStreamCallbackFlags statusFlags,
                      void* userData) {
    AudioData* data = (AudioData*)userData;
    float* out = (float*)outputBuffer;

    sf_count_t readCount = sf_readf_float(data->file, out, framesPerBuffer);
    if (readCount < framesPerBuffer) {
        // Fill rest with 0s (silence)
        std::fill(out + readCount * data->sfinfo.channels, 
                  out + framesPerBuffer * data->sfinfo.channels, 0.0f);
        return paComplete;
    }

    return paContinue;
}

int main() {
    Pa_Initialize();

    int medias[4];

    AudioData data;
    for (int i = 0; i <= 3; i++)
    {
        data.sfinfo.format = 0;

        std::string path = "data/sounds/cats/cat" + std::to_string(i) + ".wav";
        
        data.file = sf_open(path.c_str(), SFM_READ, &data.sfinfo);
        if (!data.file)
        {
            std::cerr << "Error abriendo archivo de audio\n";
            return 1;
        }

        std::cout << data.sfinfo.samplerate << "\n";
        medias[i] += data.sfinfo.samplerate;


        PaStream *stream;
        Pa_OpenDefaultStream(&stream,
                             0,                    // No input
                             data.sfinfo.channels, // Output channels
                             paFloat32,
                             data.sfinfo.samplerate,
                             FRAMES_PER_BUFFER,
                             paCallback,
                             &data);
        Pa_StartStream(stream);
        while (Pa_IsStreamActive(stream))
            Pa_Sleep(100);
        Pa_StopStream(stream);
        Pa_CloseStream(stream);

        sf_close(data.file);
    }

    std::cout << "----------------Media----------------------\n";
    int media = 0;
    for(int i = 0; i <= 3; i++){
        media += medias[i];
    }

    media = media / 4;
    std::cout << "media es: "<< media << "hz\n";

    Pa_Terminate();
    return 0;
}
