# https://github.com/vercel/next.js/tree/canary/examples/with-docker-compose
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000