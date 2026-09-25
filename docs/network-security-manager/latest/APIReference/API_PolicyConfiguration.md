---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_PolicyConfiguration.html
---

# PolicyConfiguration
<a name="API_PolicyConfiguration"></a>

Configuration settings that control a policy's behavior.

## Contents
<a name="API_PolicyConfiguration_Contents"></a>

 ** remediationEnabled **   <a name="networksecuritymanager-Type-PolicyConfiguration-remediationEnabled"></a>
Specifies whether AWS Network Security Manager automatically remediates noncompliant resources. Default: `false`.
Type: Boolean
Required: Yes

 ** resourcesCleanUp **   <a name="networksecuritymanager-Type-PolicyConfiguration-resourcesCleanUp"></a>
Specifies whether AWS Network Security Manager automatically removes the resources it created when they are no longer needed. Default: `false`.
Type: Boolean
Required: Yes

 ** wafConfig **   <a name="networksecuritymanager-Type-PolicyConfiguration-wafConfig"></a>
AWS WAF-specific policy settings. This is populated only for AWS WAF policies.
Type: [WafConfig](API_WafConfig.md) object
Required: No

## See Also
<a name="API_PolicyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/PolicyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/PolicyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/PolicyConfiguration)
