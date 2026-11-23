---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_AnalyticsConfig.html
---

# AnalyticsConfig

Specifies the security analytics configuration for the web ACL. Security analytics shows the web ACL's request log data from multiple AWS Regions in a single dashboard in the AWS WAF console.

When you enable security analytics, you authorize AWS to transfer and store full request logs outside the AWS Region where the web ACL is hosted. For regional web ACLs, security analytics is disabled by default when you omit this configuration. For web ACLs that protect CloudFront distributions (global web ACLs), security analytics is enabled by default. For more information, see [Enabling security analytics for a protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-security-analytics-enabling.html) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_AnalyticsConfig_Contents"></a>

 ** Mode **   <a name="WAF-Type-AnalyticsConfig-Mode"></a>
The security analytics mode for the web ACL. Valid values:
+  `CROSS_REGION` - Enables security analytics. AWS WAF transfers and stores the web ACL's request logs outside the AWS Region where the web ACL is hosted, for aggregation and processing.
+  `DISABLED` - Disables security analytics. AWS WAF stops transferring the web ACL's request logs.
Type: String
Valid Values: `CROSS_REGION | DISABLED`
Required: Yes

## See Also
<a name="API_AnalyticsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/AnalyticsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/AnalyticsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/AnalyticsConfig)
