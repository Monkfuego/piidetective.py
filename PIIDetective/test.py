from pii_detective import pii_detect


detected_pii = pii_detect('Put the fucking file name here')
for label, match in detected_pii:
    print(f"Detected {label}: {match}")
