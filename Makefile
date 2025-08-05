# Makefile for setting up Python virtual environment and installing requirements

PYTHON := python3
VENV_DIR := .venv
ACTIVATE := $(VENV_DIR)/bin/activate
REQ := requirements.txt

.PHONY: help setup install clean

help:
	@echo "make setup     - Create virtual environment and install dependencies"
	@echo "make install   - Install dependencies into existing venv"
	@echo "make clean     - Remove virtual environment"

setup:
	$(PYTHON) -m venv $(VENV_DIR)
	@. $(ACTIVATE) && \
	pip install --upgrade pip && \
	pip install -r $(REQ) && \
	echo "🛠️  Preloading matplotlib to build font cache..." && \
	python -c "import matplotlib.pyplot as plt; plt.figure()" && \
	echo "✅ Virtual environment set up in $(VENV_DIR)" && \
	echo "🐍 Python path inside venv: $$(which python)"
	echo "💡 Run 'source $(ACTIVATE)' to activate it" && \
	

install:
	. $(ACTIVATE) && pip install -r $(REQ)

clean:
	rm -rf $(VENV_DIR)
	@echo "🧹 Removed virtual environment"
	@echo "⚠️  If your shell prompt still shows (.venv), run 'deactivate'"