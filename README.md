![LFIscanner](https://user-images.githubusercontent.com/75953873/177439268-5a14bd8b-c2ce-4ba1-98a8-e014bd9e0829.png)

<h1 align="center"></h1>

Local File Inclusion (LFI) scanner.

## Usage
| COMMAND | DESCRIPTION |
| ------------- | ------------- |
| -t / --target | Target |
| -p / --payload | Payload file |
| -e / --extract | Extract content |
| -h / --help | Request help |

## Instalación / Installation
```
> git clone https://github.com/R3LI4NT/LFIscanner

> cd LFIscanner
> python3 -m venv <myenv> (make a virtual directory to avoid installing system dependencies)   
> pip install -r requirements.txt
```

</br>

</br>


`EXAMPLE:` **Linux LFI**
```python
python3 LFIscanner.py -t http://94.237.61.133:39139/index.php?language= -wc 0 -os linux
```