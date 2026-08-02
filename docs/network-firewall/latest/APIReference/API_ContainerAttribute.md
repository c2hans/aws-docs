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
