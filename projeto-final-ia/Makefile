.PHONY: install test build run deploy

install:
	pip install -r requirements.txt

test:
	pytest tests/test_main.py

build:
	docker build -t projeto-final-ia-image .

run:
	streamlit run src/main.py

deploy:
	echo "Simulando deploy. Rodando comandos Terraform..."
	cd terraform && terraform init && terraform apply -auto-approve