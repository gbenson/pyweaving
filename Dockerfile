FROM public.ecr.aws/lambda/python:3.9

ARG PYWEAVING_WHEEL
COPY dist/$PYWEAVING_WHEEL .
RUN  pip3 install $PYWEAVING_WHEEL --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
# (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]
