FROM ubuntu:24.04
WORKDIR /app
COPY . .
RUN chmod +x greet
ENV GREETING=Hello
ENV NAME=World
CMD ["./greet"]
