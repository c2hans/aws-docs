---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ContainerAttribute.html
---

# ContainerAttribute
<a name="API_ContainerAttribute"></a>

A key-value filter pair used in container association monitoring configurations to narrow which containers are tracked.

## Contents
<a name="API_ContainerAttribute_Contents"></a>

 ** Key **   <a name="networkfirewall-Type-ContainerAttribute-Key"></a>
The attribute key to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** Value **   <a name="networkfirewall-Type-ContainerAttribute-Value"></a>
The attribute value to match.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

## See Also
<a name="API_ContainerAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ContainerAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ContainerAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ContainerAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
