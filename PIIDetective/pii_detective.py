from file_reader import read_text_from_file
from pii_regex import pii_regex,doc_pii_regex 


def pii_detect(file):
    results = []
    text = read_text_from_file(file)
    if isinstance(text, list):
        text = ' '.join(text)
    for label, pattern in {**pii_regex, **doc_pii_regex}.items():
        matches = pattern.findall(text)
        if matches:
            for match in matches:
                results.append((label, match))
    return results



