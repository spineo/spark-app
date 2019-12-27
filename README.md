# SparkApp

Test an application using Apache Spark

Steps (example on Amazon Linux)

## 1. Spark can be installed separated

## 2. If needed, install Python (2 or 3) as 'root' user

## 3. Set up the pip installer and install the library (root)

```
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
export PATH=$PATH:~/.local/bin
pip install pyspark
