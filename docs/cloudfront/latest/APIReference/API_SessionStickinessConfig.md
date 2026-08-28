---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_SessionStickinessConfig.html
---

# SessionStickinessConfig
<a name="API_SessionStickinessConfig"></a>

Session stickiness provides the ability to define multiple requests from a single viewer as a single session. This prevents the potentially inconsistent experience of sending some of a given user's requests to your staging distribution, while others are sent to your primary distribution. Define the session duration using TTL values.

## Contents
<a name="API_SessionStickinessConfig_Contents"></a>

 ** IdleTTL **   <a name="cloudfront-Type-SessionStickinessConfig-IdleTTL"></a>
The amount of time after which you want sessions to cease if no requests are received. Allowed values are 300–3600 seconds (5–60 minutes).
The value must be less than or equal to `MaximumTTL`.
Type: Integer
Required: Yes

 ** MaximumTTL **   <a name="cloudfront-Type-SessionStickinessConfig-MaximumTTL"></a>
The maximum amount of time to consider requests from the viewer as being part of the same session. Allowed values are 300–3600 seconds (5–60 minutes).
The value must be greater than or equal to `IdleTTL`.
Type: Integer
Required: Yes

## See Also
<a name="API_SessionStickinessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/SessionStickinessConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/SessionStickinessConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/SessionStickinessConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
