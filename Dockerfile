# Static server for the relationship map. Mount ./data over /usr/share/nginx/html/data to see new research without rebuilding.
FROM nginx:1.27-alpine
COPY index.html /usr/share/nginx/html/index.html
COPY vendor/ /usr/share/nginx/html/vendor/
COPY data/ /usr/share/nginx/html/data/
RUN printf 'server {\n  listen 80;\n  root /usr/share/nginx/html;\n  location / { try_files $uri $uri/ =404; }\n  location /data/ { add_header Cache-Control "no-store"; }\n}\n' > /etc/nginx/conf.d/default.conf
EXPOSE 80
