#!/usr/bin/zsh
sassfile=/home/ivan/Документы/PROJECT/Kaliningrad-master.online/static/main.scss
cssfile=/home/ivan/Документы/PROJECT/Kaliningrad-master.online/static/style.css
#pipenv shell
flask run&
sass --watch "$sassfile" "$cssfile"&
