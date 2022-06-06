FROM node as builder

WORKDIR /build
ADD site/package.json site/package-lock.json ./
RUN npm install

ADD ./site .
RUN npm run build

FROM nginx

COPY --from=builder /build/dist /usr/share/nginx/html
COPY mime.types /etc/nginx/conf/mime.types
COPY nginx.conf /etc/nginx/nginx.conf
