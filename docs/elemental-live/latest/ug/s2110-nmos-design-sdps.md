---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-nmos-design-sdps.html
---

# Determine the SDPs to create
<a name="s2110-nmos-design-sdps"></a>

Determine the number of SDPs you will create in Elemental Live. Here are the rules:
+ The input must include one and only one video SDP.
+ Plan to create one SDP for each audio stream you want to extract. Following example 2 above, you must create three audio SDPs.
+ Plan to create one SDP for the captions ancillary stream (if any).
+ Plan to create one SDP for the SCTE-104 stream (if any).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
