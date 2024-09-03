from pii_detective import pii_detect


detected_pii = pii_detect('Adhr_crdSubro.pdf')
for label, match in detected_pii:
    print(f"Detected {label}: {match}")