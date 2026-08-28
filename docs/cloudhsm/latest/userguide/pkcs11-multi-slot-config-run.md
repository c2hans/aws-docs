---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-multi-slot-config-run.html
---

# Configure the PKCS \#11 library for multi-slot functionality for AWS CloudHSM
<a name="pkcs11-multi-slot-config-run"></a>

To configure your PKCS \#11 library for multi-slot functionality for AWS CloudHSM, follow these steps:

1. Identify the clusters you want to connect to using multi-slot functionality.

1. Add these clusters to your PKCS \#11 configuration by following the instructions in [Add a cluster with multi-slot functionality for AWS CloudHSM](pkcs11-multi-slot-add-cluster.md)

1. The next time your PKCS\#11 application runs, it will have multi-slot functionality.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
