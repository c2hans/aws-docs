---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_S3MonitoringConfiguration.html
---

# S3MonitoringConfiguration
<a name="API_S3MonitoringConfiguration"></a>

 Amazon S3 configuration for monitoring log publishing. You can configure your jobs to send log information to Amazon S3.

## Contents
<a name="API_S3MonitoringConfiguration_Contents"></a>

 ** logUri **   <a name="emroneks-Type-S3MonitoringConfiguration-logUri"></a>
Amazon S3 destination URI for log publishing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\r\n\t]*`
Required: Yes

 ** encryptionKeyArn **   <a name="emroneks-Type-S3MonitoringConfiguration-encryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the encryption key for logs.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `^(arn:(aws[a-zA-Z0-9-]*):kms:.+:(\d{12})?:key\/[(0-9a-zA-Z)-?]+|\$\{[a-zA-Z]\w*\})$`
Required: No

## See Also
<a name="API_S3MonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/S3MonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/S3MonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/S3MonitoringConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
