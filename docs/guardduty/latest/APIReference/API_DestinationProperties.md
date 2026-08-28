---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DestinationProperties.html
---

# DestinationProperties
<a name="API_DestinationProperties"></a>

Contains the Amazon Resource Name (ARN) of the resource to publish to, such as an S3 bucket, and the ARN of the KMS key to use to encrypt published findings.

## Contents
<a name="API_DestinationProperties_Contents"></a>

 ** destinationArn **   <a name="guardduty-Type-DestinationProperties-destinationArn"></a>
The ARN of the resource to publish to.
To specify an S3 bucket folder use the following format: `arn:aws:s3:::DOC-EXAMPLE-BUCKET/myFolder/`
Type: String
Required: No

 ** kmsKeyArn **   <a name="guardduty-Type-DestinationProperties-kmsKeyArn"></a>
The ARN of the KMS key to use for encryption.
Type: String
Required: No

## See Also
<a name="API_DestinationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DestinationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DestinationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DestinationProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
