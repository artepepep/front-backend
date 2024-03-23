FROM node:alpine

CMD [ "mkdir", "/app/www/" ]

WORKDIR /app/www

COPY ./marketplace/nextjs/ .

RUN npm install pm2 -g

RUN npm install

RUN npm run build

EXPOSE 3000

CMD [ "npm", "start" ]