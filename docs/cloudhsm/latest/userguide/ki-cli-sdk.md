---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-cli-sdk.html
---

# Known issues for the CloudHSM CLI for AWS CloudHSM
<a name="ki-cli-sdk"></a>

The following issues impact the CloudHSM CLI for AWS CloudHSM.

**Topics**
+ [The `key-reference` filter fails to select session keys](#ki-cli-1)

## The `key-reference` filter fails to select session keys
<a name="ki-cli-1"></a>

Commands that use `key-reference` to filter session (ephemeral) keys fail with the error `UX000: Ephemeral key is not expected because we cannot build it without HSM Connection`.

The [key set-attribute](cloudhsm_cli-key-set-attribute.md) command is not affected and can select session keys by `key-reference`.
+ **Workaround: **Use attribute-based filters (such as `attr.label`) to select session keys. If multiple session keys share identical attributes, use [key set-attribute](cloudhsm_cli-key-set-attribute.md) with the `key-reference` filter to assign unique labels first, then filter by label.
+ **Resolution status: **This issue has been resolved in [Client SDK 5.18.0](latest-releases.md#client-version-5-18-0). The `key-reference` filter now selects session (ephemeral) keys in the CloudHSM CLI and JCE. Upgrade to version 5.18.0 or later to benefit from the fix.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
