---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-keys-chsm-cli.html
---

# Key management with CloudHSM CLI
<a name="manage-keys-chsm-cli"></a>

If using the [latest SDK version series](use-hsm.md), use [CloudHSM CLI](cloudhsm_cli.md) to manage the keys in your AWS CloudHSM cluster. For more details, see the topics below.
+ [Using trusted keys](manage-keys-cloudhsm-cli-trusted.md) describes how to use CloudHSM CLI to create trusted keys to secure data.
+ [Generating keys](manage-keys-cloudhsm-cli-generate.md) includes instructions on creating keys, including symmetric keys, RSA keys, and EC keys.
+ [Deleting keys](manage-keys-cloudhsm-cli-delete.md) describes how key owners delete keys.
+ [Sharing and unsharing keys](manage-keys-cloudhsm-cli-share.md) details how key owners share and unshare keys.
+ [Filtering keys](manage-keys-cloudhsm-cli-filtering.md) offers guidelines on how to use filters to find keys.
+ [Manage key quorum authentication (M of N) ](key-quorum-auth-chsm-cli.md) offers guidelines on how to setup and use quorum authentication with keys.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
