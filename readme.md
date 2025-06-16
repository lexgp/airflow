
Начальная установка:

```bash
sudo apt install -y python3-venv
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
python3 -m venv venv

source venv/bin/activate

pip3 install wheel
pip3 install -r requirements.txt
export AIRFLOW_HOME=~/airflow
airflow db migrate
airflow standalone
```

Проверяем как работает

Запуск веб-интерфейса:

```bash
airflow api-server
```

Запуск плинировщика заданий:

```bash
airflow scheduler
```

Запустить на сервере, чтобы постоянно работало:

```bash
cp airflow-api-server.service /etc/systemd/system/airflow-api-server.service
cp airflow-scheduler.service /etc/systemd/system/airflow-scheduler.service

systemctl daemon-reexec
systemctl daemon-reload
systemctl enable airflow-webserver
systemctl enable airflow-scheduler
systemctl start airflow-webserver
systemctl start airflow-scheduler
```

