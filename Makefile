VENV = venv
PYTHON = python
DATA_PREP_SCRIPT = scripts/data_prep.py
TRAIN_MODEL_SCRIPT = scripts/train_model.py
TEST_MODEL_SCRIPT = scripts/test_model.py
EVALUATE_MODEL_SCRIPT = scripts/evaluate_model.py
DEPLOY_MODEL_SCRIPT = scripts/deploy_model.py
RETRAIN_MODEL_SCRIPT = scripts/retrain_model.py
REQUIREMENTS_FILE = requirements.txt

all: install data train test evaluate deploy retrain

$(VENV)/Scripts/activate: 
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "Installing dependencies..."
	$(VENV)/Scripts/pip install -r $(REQUIREMENTS_FILE)

install: $(VENV)/Scripts/activate

data: $(VENV)/Scripts/activate
	@echo "Preparing data..."
	$(VENV)/Scripts/python $(DATA_PREP_SCRIPT)

train: $(VENV)/Scripts/activate
	@echo "Training model..."
	$(VENV)/Scripts/python $(TRAIN_MODEL_SCRIPT)

test: $(VENV)/Scripts/activate
	@echo "Training model..."
	$(VENV)/Scripts/python $(TEST_MODEL_SCRIPT)

evaluate: $(VENV)/Scripts/activate
	@echo "Evaluating model..."
	$(VENV)/Scripts/python $(EVALUATE_MODEL_SCRIPT)

deploy: $(VENV)/Scripts/activate
	@echo "Deploying model..."
	$(VENV)/Scripts/python $(DEPLOY_MODEL_SCRIPT)

retrain: $(VENV)/Scripts/activate
	@echo "Checking accuracy and retraining if needed..."
	$(VENV)/Scripts/python $(RETRAIN_MODEL_SCRIPT)


.PHONY: all install data train test evaluate deploy retrain