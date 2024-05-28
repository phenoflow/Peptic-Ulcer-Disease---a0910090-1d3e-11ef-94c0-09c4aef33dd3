# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Carolyn A Chew-Graham, Nav Kapur, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"J11yy00","system":"readv2"},{"code":"J13y300","system":"readv2"},{"code":"J110y00","system":"readv2"},{"code":"J130y00","system":"readv2"},{"code":"J13y100","system":"readv2"},{"code":"J13y000","system":"readv2"},{"code":"J11y.00","system":"readv2"},{"code":"J120y00","system":"readv2"},{"code":"J111y00","system":"readv2"},{"code":"J11yz00","system":"readv2"},{"code":"J12y.00","system":"readv2"},{"code":"J11y100","system":"readv2"},{"code":"J14y100","system":"readv2"},{"code":"J13y200","system":"readv2"},{"code":"J14yz00","system":"readv2"},{"code":"J11y000","system":"readv2"},{"code":"J14y.00","system":"readv2"},{"code":"J11y400","system":"readv2"},{"code":"J12yy00","system":"readv2"},{"code":"J12y300","system":"readv2"},{"code":"J11y200","system":"readv2"},{"code":"J12y200","system":"readv2"},{"code":"J13..00","system":"readv2"},{"code":"J13yz00","system":"readv2"},{"code":"J131y00","system":"readv2"},{"code":"J12yz00","system":"readv2"},{"code":"J12y400","system":"readv2"},{"code":"J13y400","system":"readv2"},{"code":"J14y200","system":"readv2"},{"code":"J12y000","system":"readv2"},{"code":"J13y.00","system":"readv2"},{"code":"J121y00","system":"readv2"},{"code":"K27","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('peptic-ulcer-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["peptic-ulcer-disease-unspec---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["peptic-ulcer-disease-unspec---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["peptic-ulcer-disease-unspec---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
