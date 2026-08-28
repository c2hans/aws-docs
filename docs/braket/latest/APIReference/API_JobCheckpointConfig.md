---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_JobCheckpointConfig.html
---

# JobCheckpointConfig
<a name="API_JobCheckpointConfig"></a>

Contains information about the output locations for hybrid job checkpoint data.

## Contents
<a name="API_JobCheckpointConfig_Contents"></a>

 ** s3Uri **   <a name="braket-Type-JobCheckpointConfig-s3Uri"></a>
Identifies the S3 path where you want Amazon Braket to store checkpoint data. For example, `s3://bucket-name/key-name-prefix`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** localPath **   <a name="braket-Type-JobCheckpointConfig-localPath"></a>
(Optional) The local directory where checkpoint data is stored. The default directory is `/opt/braket/checkpoints/`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_JobCheckpointConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/JobCheckpointConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/JobCheckpointConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/JobCheckpointConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
