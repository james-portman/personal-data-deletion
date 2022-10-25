#!/usr/bin/env python
import json
import urllib
import urllib.parse

TYPE_JOB_WEBSITE = "job website"
TYPE_RECRUITER = "recruiter"

# set company names as exclusions - those you don't want to contact
exclusions = []

companies = {
	"cwjobs": {
		"type": TYPE_JOB_WEBSITE,
		"website": "https://www.cwjobs.co.uk",
		"data_controller": "Totaljobs",
		"email": "dataprotectionofficerUK@stepstone.co.uk"
	},
	"modis": {
		"type": TYPE_RECRUITER,
		"email": "privacy@modis.co.uk"
	},
	"reed": {
		"type": TYPE_JOB_WEBSITE,
		"website": "https://www.reed.co.uk",
		"email": "dpo@reedonline.co.uk"
	}
}

################################################################################

personal_data = json.load(open(".personal-data.json"))
print(personal_data)

email_bccs = []
for company in companies:
	if company in exclusions:
		print("Company %s excluded, skipping" % company)
		continue
	print(company)
	email_bccs.append(companies[company]["email"])

print(email_bccs)
email_bccs_string = ','.join(email_bccs)

body = urllib.parse.quote_plus(f"""{personal_data["full_name"]}, {personal_data["address"]}

Please delete any data you hold for me.
Further to this, please let me know any other parties you may have shared my data with in the last three months.
If possible I would also appreciate if you contacted them on my behalf, asking them to delete my data.

Thanks,
{personal_data["full_name"]}
""")
subject = urllib.parse.quote_plus("Personal data deletion")
to_address = personal_data["email"]
print(f'https://mail.google.com/mail/?view=cm&fs=1&to={to_address}&bcc={email_bccs_string}&su={subject}&body={body}')
