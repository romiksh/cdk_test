FROM --platform=linux/amd64 nginx:1.27.0-alpine-slim

ADD ./nginx.conf /etc/nginx/conf.d/default.conf
ADD ./index.html /etc/nginx/html/index.html

EXPOSE 80

STOPSIGNAL SIGTERM
CMD ["nginx", "-g", "daemon off;"]
