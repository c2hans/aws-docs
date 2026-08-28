---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_using_trusted_keys_control_key_wrap.html
---

# How to mark a key as trusted with the AWS CloudHSM Management Utility
<a name="cloudhsm_using_trusted_keys_control_key_wrap"></a>

The content in this section provides instructions on using the AWS CloudHSM management Utility (CMU) to mark a key as trusted.

1. Using the [loginHSM](cloudhsm_mgmt_util-loginLogout.md) command, log in as a crypto officer (CO).

1. Use the [Set the attributes of AWS CloudHSM keys using CMU](cloudhsm_mgmt_util-setAttribute.md) command with `OBJ_ATTR_TRUSTED` (value `134`) set to true (`1`).

   ```
   aws-cloudhsm > setAttribute {{<Key Handle>}} 134 1
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
