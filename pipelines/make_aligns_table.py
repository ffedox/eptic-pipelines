import os
import pandas as pd
import xml.etree.ElementTree as ET

# Directory containing XML files
xml_dir = "/home/afedotova/EPTIC25/eptic.v3/2. bertalign_alignments"
output_excel_path = os.path.join(xml_dir, "alignments.xlsx")

# Dictionary to store results
alignment_dict = {}

# Loop through all XML files in the directory
for file_name in os.listdir(xml_dir):
    if file_name.endswith(".xml"):
        file_path = os.path.join(xml_dir, file_name)
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Process each link element
            for link in root.findall("link"):
                xtargets = link.attrib.get("xtargets", "")
                if not xtargets:
                    continue

                try:
                    t1_targets, t2_targets = xtargets.split(";")
                    t1_id = t1_targets.split(":")[0] if ":" in t1_targets else None
                    t2_id = t2_targets.split(":")[0] if ":" in t2_targets else None

                    if t1_id and t2_id:
                        key = (t1_id, t2_id)
                        if key not in alignment_dict:
                            alignment_dict[key] = []
                        alignment_dict[key].append(ET.tostring(link, encoding="unicode").strip())
                except ValueError:
                    continue  # Skip malformed entries

        except ET.ParseError:
            print(f"Skipping malformed XML file: {file_name}")

# Convert to DataFrame
data = [
    {"t1_id": t1, "t2_id": t2, "alignment_file": "\n".join(alignments)}
    for (t1, t2), alignments in alignment_dict.items()
]

df = pd.DataFrame(data, columns=["t1_id", "t2_id", "alignment_file"])

# Save to Excel
df.to_excel(output_excel_path, index=False)
print(f"Final alignments saved to: {output_excel_path}")
