sudo docker build -t portfolio_api:latest .
sudo docker run -d -p 8088:8088 portfolio_api:latest