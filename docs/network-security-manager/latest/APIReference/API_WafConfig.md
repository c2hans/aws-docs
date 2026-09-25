---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_WafConfig.html
---

# WafConfig
<a name="API_WafConfig"></a>

AWS WAF-specific policy configuration settings.

## Contents
<a name="API_WafConfig_Contents"></a>

 ** conflictResolution **   <a name="networksecuritymanager-Type-WafConfig-conflictResolution"></a>
The conflict-resolution strategy for AWS WAF policies. Required for AWS WAF policies.
Type: String
Valid Values: `MERGE_WHERE_APPLICABLE`
Required: Yes

 ** existingCustomerWebACLResolution **   <a name="networksecuritymanager-Type-WafConfig-existingCustomerWebACLResolution"></a>
Determines how AWS Network Security Manager handles remediation when a resource already has a customer-created web ACL. Required for AWS WAF policies.
Type: String
Valid Values: `RETROFIT | OVERRIDE_ASSOCIATION | NO_REMEDIATION`
Required: Yes

## See Also
<a name="API_WafConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/WafConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/WafConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/WafConfig)
