---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util.html
---

# AWS CloudHSM Management Utility (CMU)
<a name="cloudhsm_mgmt_util"></a>

The **cloudhsm\_mgmt\_util** command line tool helps crypto officers manage users in the hardware security modules (HSMs) in AWS CloudHSM clusters. The AWS CloudHSM Management Utility (CMU) includes tools that create, delete, and list users, and change user passwords.

The CMU and Key Management Utility (KMU) are part of [the Client SDK 3 suite](choose-client-sdk.md). Client SDK 3 and its related command line tools (Key Management Utility and CloudHSM Management Utility) are only available in the HSM type *hsm1.medium*.

cloudhsm\_mgmt\_util also includes commands that allow crypto users (CUs) to share keys and get and set key attributes. These commands complement the key management commands in the primary key management tool, [key\_mgmt\_util](key_mgmt_util.md).

For a quick start, see [Getting started with AWS CloudHSM Management Utility (CMU)](cloudhsm_mgmt_util-getting-started.md). For detailed information about the cloudhsm\_mgmt\_util commands and examples of using the commands, see [Reference for AWS CloudHSM Management Utility commands](cloudhsm_mgmt_util-reference.md).

**Topics**
+ [Supported platforms](cmu-support.md)
+ [Getting started](cloudhsm_mgmt_util-getting-started.md)
+ [Install the client (Linux)](cmu-install-and-configure-client-linux.md)
+ [Install the client (Windows)](cmu-install-and-configure-client-win.md)
+ [Reference](cloudhsm_mgmt_util-reference.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
