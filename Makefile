# Simple makefile

EXE=Analysis.exe

SOURCES=$(wildcard srcs/*.C) rooutil/rooutil.cc
TMPOBJECTS=$(SOURCES:.C=.o)
OBJECTS=$(TMPOBJECTS:.cc=.o)

OPTIMIZE    = -O2
CC          = g++
CXX         = g++
CXXFLAGS    = -g $(OPTIMIZE) -Wall -fPIC -Wshadow -Woverloaded-virtual
LD          = g++
LDFLAGS     = -g $(OPTIMIZE)
SOFLAGS     = -g -shared
CXXFLAGS    = -g $(OPTIMIZE) -Wall -fPIC -Wshadow -Woverloaded-virtual
LDFLAGS     = -g $(OPTIMIZE)
ROOTLIBS    = $(shell root-config --libs)
ROOTCFLAGS  = $(shell root-config --cflags)
CXXFLAGS   += $(ROOTCFLAGS)
CFLAGS      = $(ROOTCFLAGS) -Wall -Wno-unused-function -g $(OPTIMIZE) -fPIC -fno-var-tracking
EXTRACFLAGS = $(shell rooutil-config) -IStopAnalysis/StopCORE/METCorr/
EXTRAFLAGS  = -fPIC -ITMultiDrawTreePlayer -Wunused-variable -lTMVA -lEG -lGenVector -lXMLIO -lMLP -lTreePlayer

$(EXE): $(OBJECTS)
	$(LD) $(CXXFLAGS) $(LDFLAGS) $(OBJECTS) $(ROOTLIBS) $(EXTRAFLAGS) -o $@

%.o: %.C
	$(CC) $(CFLAGS) $(EXTRACFLAGS) $< -c -o $@

%.o: %.cc
	$(CC) $(CFLAGS) $(EXTRACFLAGS) $< -c -o $@

clean:
	rm -f $(OBJECTS)
	rm -f $(EXE)

