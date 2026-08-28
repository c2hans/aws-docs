---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_KinesisDataStreamData.html
---

# KinesisDataStreamData
<a name="API_KinesisDataStreamData"></a>

Information for telemetry delivery to Kinesis Data Streams.

## Contents
<a name="API_KinesisDataStreamData_Contents"></a>

 ** kinesisDataStreamArn **   <a name="groundstation-Type-KinesisDataStreamData-kinesisDataStreamArn"></a>
ARN of the Kinesis Data Stream to deliver telemetry to.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 275.
Pattern: `arn:[a-z0-9-.]{1,63}:kinesis:[-a-z0-9]{1,50}:[0-9]{12}:stream/[a-zA-Z0-9_.-]{1,128}`
Required: Yes

 ** kinesisRoleArn **   <a name="groundstation-Type-KinesisDataStreamData-kinesisRoleArn"></a>
ARN of the IAM Role used by AWS Ground Station to deliver telemetry.
Type: String
Length Constraints: Minimum length of 30. Maximum length of 165.
Pattern: `arn:[a-z0-9-.]{1,63}:iam::[0-9]{12}:role/[\w+=,.@-]{1,64}`
Required: Yes

## See Also
<a name="API_KinesisDataStreamData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/KinesisDataStreamData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/KinesisDataStreamData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/KinesisDataStreamData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
