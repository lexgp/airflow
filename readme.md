
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

# Чтобы сгенерировал нам сразу пароль для входа
airflow standalone
cp /root/airflow/simple_auth_manager_passwords.json.generated /var/www/apache-airflow/
chmod 644 /var/www/apache-airflow/simple_auth_manager_passwords.json.generated
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
systemctl enable airflow-api-server
systemctl enable airflow-scheduler
systemctl start airflow-api-server
systemctl start airflow-scheduler
```

