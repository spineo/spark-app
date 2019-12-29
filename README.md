# SparkApp

Test application using PySpark that outputs alphabet characters counts from scanning a file

Steps (example on Amazon Linux)

## 1. If needed, install Python (2 or 3) as 'root' user

## 2. Set up the pip installer and install the library (root)

```
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
export PATH=$PATH:~/.local/bin (or, on Mac OS add this path to /etc/paths)
pip install pyspark --user
```

## 3. Run the application:

```
./SparkApp.py --infile /SomePath/SomeFile
```
