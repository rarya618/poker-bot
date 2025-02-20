# Define the virtual environment directory
VENV_DIR=venv

# Define Python executable
PYTHON=python

# Create and activate virtual environment
setup: 
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt

# Activate the virtual environment (For manual use)
activate:
	@echo "Run the following command to activate the virtual environment:"
	@echo "source $(VENV_DIR)/bin/activate"

# Run the bot
run:
	$(VENV_DIR)/bin/python src/main.py

# Save dependencies
freeze:
	$(VENV_DIR)/bin/pip freeze > requirements.txt

# Remove virtual environment
clean:
	rm -rf $(VENV_DIR)

