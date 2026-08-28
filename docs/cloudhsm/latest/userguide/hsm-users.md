---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-users.html
---

# Users in AWS CloudHSM
<a name="hsm-users"></a>

Unlike most AWS services and resources, you do not use AWS Identity and Access Management (IAM) users or IAM policies to access resources within your AWS CloudHSM cluster. Instead, you use *HSM users* directly on HSMs in your AWS CloudHSM cluster.

HSM users are distinct from IAM users. IAM users who have the correct credentials can create HSMs by interacting with resources through the AWS API. Since E2E encryption is not visible to AWS, you must use HSM user credentials to authenticate operations on the HSM because credentials takes place directly on the HSM. The HSM authenticates each HSM user by means of credentials that you define and manage. Each HSM user has a *type* that determines which operations that user can perform on the HSM. Each HSM authenticates each HSM user by means of credentials that you define using [CloudHSM CLI](cloudhsm_cli.md).

If you are using the [previous SDK version series](choose-client-sdk.md), then you will use [CloudHSM Management Utility (CMU)](cloudhsm_mgmt_util.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
