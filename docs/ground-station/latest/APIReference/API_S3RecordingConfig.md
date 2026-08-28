---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_S3RecordingConfig.html
---

# S3RecordingConfig
<a name="API_S3RecordingConfig"></a>

Information about an S3 recording `Config`.

## Contents
<a name="API_S3RecordingConfig_Contents"></a>

 ** bucketArn **   <a name="groundstation-Type-S3RecordingConfig-bucketArn"></a>
ARN of the bucket to record to.
Type: String
Required: Yes

 ** roleArn **   <a name="groundstation-Type-S3RecordingConfig-roleArn"></a>
ARN of the role Ground Station assumes to write data to the bucket.
Type: String
Length Constraints: Minimum length of 30. Maximum length of 165.
Pattern: `arn:[a-z0-9-.]{1,63}:iam::[0-9]{12}:role/[\w+=,.@-]{1,64}`
Required: Yes

 ** prefix **   <a name="groundstation-Type-S3RecordingConfig-prefix"></a>
S3 Key prefix to prefice data files.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 900.
Pattern: `([a-zA-Z0-9_\-=/]|\{satellite_id\}|\{config\-name}|\{s3\-config-id}|\{year\}|\{month\}|\{day\}){1,900}`
Required: No

## See Also
<a name="API_S3RecordingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/S3RecordingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/S3RecordingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/S3RecordingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
