# Define o provedor de nuvem (simulação AWS)
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"  # Região onde a infraestrutura será criada (simulação)
}

# Simulação de um servidor EC2 para rodar o agente
resource "aws_instance" "app_server" {
  # O ID da imagem (AMI) é apenas um placeholder para demonstração
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "projeto-final-ia-server"
    Project = "DevOps_AI"
  }
}

# Simulação de um bucket S3 para armazenar logs ou backups
resource "aws_s3_bucket" "app_logs" {
  bucket = "projeto-final-ia-logs-bucket"
  acl    = "private"
  
  tags = {
    Name = "projeto-final-ia-logs"
    Project = "DevOps_AI"
  }
}