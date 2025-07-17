CC = g++
CFLAGS = -Wall -g
SRC = src-core/main.cpp
COMPILED_FILE = Lockency
CLIB = -I./lib/portaudio/include ./lib/portaudio/lib/.libs/libportaudio.a -lrt -lasound -ljack -pthread

# Regla principal
compile: main.cpp 
	g++ -o $@ $^ $(CLIB)

run: (COMPILED_FILE)
	./$<


clean:
	rm -rf $(BUILD_DIR)
.PHONY: clean

install-deps:
	mkdir -p lib

	curl -L http://files.portaudio.com/archives/pa_stable_v190700_20210406.tgz | tar -zx -C lib
	cd lib/portaudio && ./configure && $(MAKE) -j
.PHONY: install-deps


