---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CloudWatchDimensionConfiguration.html
---

# CloudWatchDimensionConfiguration
<a name="API_CloudWatchDimensionConfiguration"></a>

An object that defines the dimension configuration to use when you send Amazon Pinpoint email events to Amazon CloudWatch.

## Contents
<a name="API_CloudWatchDimensionConfiguration_Contents"></a>

 ** DefaultDimensionValue **   <a name="pinpoint-Type-CloudWatchDimensionConfiguration-DefaultDimensionValue"></a>
The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email. This value has to meet the following criteria:
+ It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), or dashes (-).
+ It can contain no more than 256 characters.
Type: String
Required: Yes

 ** DimensionName **   <a name="pinpoint-Type-CloudWatchDimensionConfiguration-DimensionName"></a>
The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:
+ It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), or dashes (-).
+ It can contain no more than 256 characters.
Type: String
Required: Yes

 ** DimensionValueSource **   <a name="pinpoint-Type-CloudWatchDimensionConfiguration-DimensionValueSource"></a>
The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose `messageTag`. If you want Amazon Pinpoint to use your own email headers, choose `emailHeader`. If you want Amazon Pinpoint to use link tags, choose `linkTags`.
Type: String
Valid Values: `MESSAGE_TAG | EMAIL_HEADER | LINK_TAG`
Required: Yes

## See Also
<a name="API_CloudWatchDimensionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/CloudWatchDimensionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/CloudWatchDimensionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/CloudWatchDimensionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
