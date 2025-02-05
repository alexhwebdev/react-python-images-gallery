FROM node:15.14-alpine

WORKDIR /app

EXPOSE 3000

COPY package.json package-lock.json ./

RUN npm install --silent
# --silent : bc usually it generates lot of output during installation of packages and build process. Simply omit those logs.

COPY . ./

CMD ["npm", "start"]

# L122