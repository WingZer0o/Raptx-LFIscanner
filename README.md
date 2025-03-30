![LFIscanner](https://user-images.githubusercontent.com/75953873/177439268-5a14bd8b-c2ce-4ba1-98a8-e014bd9e0829.png)

<h1 align="center"></h1>

Local File Inclusion (LFI) scanner.

## Usage
| COMMAND | DESCRIPTION |
| ------------- | ------------- |
| -t / --target | Target of the host example: http://94.237.61.133:39139/index.php?language= |
| -th / --threads | (Optional): Amount of threads to execute requests in parallel in batch fashion |
| -wc / --walkcount | The number of directories you want to walk up |
| -w / --wordlist | Specify path to your wordlist you want
| -h / --help | Get help |
| -nrf / --nonrecursivefilter | An argument to help by pass non recursive path traversals filters by appending ....// instead of ../ |

## Instalación / Installation
```
> git clone https://github.com/R4ptX/Raptx-LFIscanner

> cd LFIscanner
> python3 -m venv <myenv> (make a virtual directory to avoid installing system dependencies)   
> source myenv/bin/activate
> pip install -r requirements.txt
```

</br>

</br>


`EXAMPLE:` **Linux LFI**
```python
python3 LFIscanner.py -t http://83.136.253.25:53734/index.php?language= -wc 5 -w ~/Tools/Raptx-LFIscanner/payloads/linux.txt
```
