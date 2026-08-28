---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_CloudWatchDimensionConfiguration.html
---

# CloudWatchDimensionConfiguration
<a name="API_CloudWatchDimensionConfiguration"></a>

Contains the dimension configuration to use when you publish email sending events to Amazon CloudWatch.

For information about publishing email sending events to Amazon CloudWatch, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html).

## Contents
<a name="API_CloudWatchDimensionConfiguration_Contents"></a>

 ** DefaultDimensionValue **
The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must meet the following requirements:
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), dashes (-), at signs (@), or periods (.).
+ Contain 256 characters or fewer.
Type: String
Required: Yes

 ** DimensionName **
The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must meet the following requirements:
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), dashes (-), or colons (:).
+ Contain 256 characters or fewer.
Type: String
Required: Yes

 ** DimensionValueSource **
The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. To use the message tags that you specify using an `X-SES-MESSAGE-TAGS` header or a parameter to the `SendEmail`/`SendRawEmail` API, specify `messageTag`. To use your own email headers, specify `emailHeader`. To put a custom tag on any link included in your email, specify `linkTag`.
Type: String
Valid Values: `messageTag | emailHeader | linkTag`
Required: Yes

## See Also
<a name="API_CloudWatchDimensionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/CloudWatchDimensionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/CloudWatchDimensionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/CloudWatchDimensionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
