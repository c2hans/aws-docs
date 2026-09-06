---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_LoggingConfiguration.html
---

# LoggingConfiguration
<a name="API_waf_LoggingConfiguration"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The Amazon Data Firehose, `RedactedFields` information, and the web ACL Amazon Resource Name (ARN).

## Contents
<a name="API_waf_LoggingConfiguration_Contents"></a>

 ** LogDestinationConfigs **   <a name="WAF-Type-waf_LoggingConfiguration-LogDestinationConfigs"></a>
An array of Amazon Data Firehose ARNs.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `.*\S.*`
Required: Yes

 ** ResourceArn **   <a name="WAF-Type-waf_LoggingConfiguration-ResourceArn"></a>
The Amazon Resource Name (ARN) of the web ACL that you want to associate with `LogDestinationConfigs`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `.*\S.*`
Required: Yes

 ** RedactedFields **   <a name="WAF-Type-waf_LoggingConfiguration-RedactedFields"></a>
The parts of the request that you want redacted from the logs. For example, if you redact the cookie field, the cookie field in the firehose will be `xxx`.
Type: Array of [FieldToMatch](API_waf_FieldToMatch.md) objects
Required: No

## See Also
<a name="API_waf_LoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/LoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/LoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/LoggingConfiguration)
