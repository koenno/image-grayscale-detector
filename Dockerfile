FROM continuumio/miniconda3

WORKDIR /app

COPY . .

RUN conda create --name detect-grayscale --file requirements.txt -y

SHELL ["conda", "run", "-n", "detect-grayscale", "/bin/bash", "-c"]

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "detect-grayscale", "python", "run.py"]
