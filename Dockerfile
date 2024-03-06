FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt .
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY main.py ${LAMBDA_TASK_ROOT}
COPY ./* ./A/
COPY __init__.py .
CMD [ "app.handler" ]
