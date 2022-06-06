FROM nginx

COPY site/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
