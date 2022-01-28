from pathlib import Path


def read_resources(file_name: str, separator="\n") -> list[str]:
    base_path = Path(__file__).parent.as_posix()
    f = open("{0}/resources/{1}.txt".format(base_path, Path(file_name).stem))
    return f.read()[:-1].split(separator)
