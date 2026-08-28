---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Destination.html
---

# Destination
<a name="API_Destination"></a>

Contains details of the Amazon S3 bucket and AWS KMS key used to export findings.

## Contents
<a name="API_Destination_Contents"></a>

 ** bucketName **   <a name="inspector2-Type-Destination-bucketName"></a>
The name of the Amazon S3 bucket to export findings to.
Type: String
Required: Yes

 ** kmsKeyArn **   <a name="inspector2-Type-Destination-kmsKeyArn"></a>
The ARN of the KMS key used to encrypt data when exporting findings.
Type: String
Required: Yes

 ** keyPrefix **   <a name="inspector2-Type-Destination-keyPrefix"></a>
The prefix that the findings will be written under.
Type: String
Required: No

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Destination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
