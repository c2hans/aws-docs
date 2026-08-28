---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshoot-getencoded.html
---

# AWS CloudHSM extracting keys using JCE
<a name="troubleshoot-getencoded"></a>

Use the following sections to troubleshoot issues extracting AWS CloudHSM keys using JCE.

## getEncoded, getPrivateExponent, or getS returns null
<a name="w2aac37c21b5"></a>

`getEncoded`, `getPrivateExponent`, and `getS` will return null because they are by default disabled. To enable them, refer to [Key extraction using JCE for AWS CloudHSM](java-lib-configs-getencoded.md).

If `getEncoded`, `getPrivateExponent`, and `getS` return null after being enabled, your key does not meet the right prerequisites. For more information, refer to [Key extraction using JCE for AWS CloudHSM](java-lib-configs-getencoded.md).

## getEncoded, getPrivateExponent, or getS return key bytes outside of the HSM
<a name="w2aac37c21b7"></a>

You or someone with access to your system has enabled clear key extraction. See the following pages for more information, including how to reset this configuration to the default disabled state.
+ [Key extraction using JCE for AWS CloudHSM](java-lib-configs-getencoded.md)
+ [Protecting and extracting keys from an HSM](bp-hsm-key-management.md#best-practices-key-protection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
