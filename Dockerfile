FROM python:3-alpine

WORKDIR /usr/src/app

COPY . .

ENV PYTHONPATH /usr/src/app

# Run FWT Generator - with default args - generates fwt_file.txt
RUN [ "python", "scripts/FWTGenerator.py" ]

# Run FWT Converter - with default args - using fwt_file.txt
CMD [ "python", "scripts/FWTConverter.py", "-f", "fwt_file.txt" ]