---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_DataProtectionConfig.html
---

# DataProtectionConfig
<a name="API_DataProtectionConfig"></a>

Specifies data protection to apply to the web request data for the web ACL. This is a web ACL level data protection option.

The data protection that you configure for the web ACL alters the data that's available for any other data collection activity, including your AWS WAF logging destinations, web ACL request sampling, and Amazon Security Lake data collection and management. Your other option for data protection is in the logging configuration, which only affects logging.

This is part of the data protection configuration for a web ACL.

## Contents
<a name="API_DataProtectionConfig_Contents"></a>

 ** DataProtections **   <a name="WAF-Type-DataProtectionConfig-DataProtections"></a>
An array of data protection configurations for specific web request field types. This is defined for each web ACL. AWS WAF applies the specified protection to all web requests that the web ACL inspects.
Type: Array of [DataProtection](API_DataProtection.md) objects
Array Members: Minimum number of 1 item. Maximum number of 26 items.
Required: Yes

## See Also
<a name="API_DataProtectionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/DataProtectionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/DataProtectionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/DataProtectionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
