---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_SnsAction.html
---

# SnsAction
<a name="API_SnsAction"></a>

Describes an action to publish to an Amazon SNS topic.

## Contents
<a name="API_SnsAction_Contents"></a>

 ** roleArn **   <a name="iot-Type-SnsAction-roleArn"></a>
The ARN of the IAM role that grants access.
Type: String
Required: Yes

 ** targetArn **   <a name="iot-Type-SnsAction-targetArn"></a>
The ARN of the SNS topic.
Type: String
Required: Yes

 ** messageFormat **   <a name="iot-Type-SnsAction-messageFormat"></a>
(Optional) The message format of the message to publish. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see [https://docs.aws.amazon.com/sns/latest/dg/json-formats.html](https://docs.aws.amazon.com/sns/latest/dg/json-formats.html) refer to their official documentation.
Type: String
Valid Values: `RAW | JSON`
Required: No

## See Also
<a name="API_SnsAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/SnsAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/SnsAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/SnsAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
