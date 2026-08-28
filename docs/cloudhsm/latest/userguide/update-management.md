---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/update-management.html
---

# Update management in AWS CloudHSM
<a name="update-management"></a>

AWS manages the firmware. Firmware is maintained by a third party, and must be evaluated by NIST for FIPS 140-2 Level 3 or FIPS 140-3 Level 3 compliance depending on the hsm type. Only firmware that has been cryptographically signed by the FIPS key, which AWS does not have access to, can be installed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
