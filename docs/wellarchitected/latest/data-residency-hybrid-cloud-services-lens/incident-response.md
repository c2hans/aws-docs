---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/incident-response.html
---

# Incident response
<a name="incident-response"></a>

| DRHCSEC09: Have your incident responders been trained on your data residency policies? |
| --- |
|   |

 Incident responders should be aware of your data residency policies, and they should check for data that is located in unapproved locations.

| DRHCSEC10: Have your threat models been updated to cover data in unauthorized locations? |
| --- |
|   |

 While threat models typically focus on exfiltration of data, they should be updated to include scenarios where data gets stored in locations that aren't compliant with data residency regulations and control objectives.

**Topics**
+ [DRHCSEC09-BP01 Train and test incident responders on policies specific to data residency](drhcsec09-bp01.md)
+ [DRHCSEC10-BP01 Update your threat models to cover the accidental or malicious storage of data in unauthorized locations](drhcsec10-bp01.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
