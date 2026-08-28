---
source_url: https://docs.aws.amazon.com/evs/latest/userguide/evs-env-secret-rotation.html
---

# Secret management lifecycle
<a name="evs-env-secret-rotation"></a>

Amazon EVS uses AWS Secrets Manager to create, encrypt, and store secrets in your account on initial environment deployment. These secrets contain the VCF credentials needed to install and access VCF management appliances such as vCenter Server, NSX, and SDDC Manager, as well as the ESX host root password. Amazon EVS also deletes managed secrets on your behalf when the EVS environment is deleted.

You are responsible for secret lifecyle management, including secret rotation. Amazon EVS does not provide managed rotation of your secrets. We recommend that you rotate secrets regularly on a set rotation window to ensure that secrets are not long-lived. For more information, see [Rotation schedules](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_schedule.html) in the * AWS Secrets Manager User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
