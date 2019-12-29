# SparkApp

Test application using PySpark that outputs alphabet characters counts from scanning a file

Steps (example on Amazon Linux)

### 1. If needed, install Python (2 or 3) as 'root' user (python 3 being the preferred option)

### 2. Set up the pip installer and install the library (root)

```
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
export PATH=$PATH:~/.local/bin (or, on Mac OS add this path to /etc/paths)
pip install pyspark --user
```

You may need to run it using python (i.e., python 2.7, no longer supported as of 2020) and/or python3 (python 3.7) which is recommwended

### 3. Run the application:

```
./SparkApp.py --infile /SomePath/SomeFile
```
