---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_S3DestinationProperties.html
---

# S3DestinationProperties
<a name="API_S3DestinationProperties"></a>

 The properties that are applied when Amazon S3 is used as a destination.

## Contents
<a name="API_S3DestinationProperties_Contents"></a>

 ** bucketName **   <a name="appflow-Type-S3DestinationProperties-bucketName"></a>
 The Amazon S3 bucket name in which Amazon AppFlow places the transferred data.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `\S+`
Required: Yes

 ** bucketPrefix **   <a name="appflow-Type-S3DestinationProperties-bucketPrefix"></a>
 The object key for the destination bucket in which Amazon AppFlow places the files.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** s3OutputFormatConfig **   <a name="appflow-Type-S3DestinationProperties-s3OutputFormatConfig"></a>
 The configuration that determines how Amazon AppFlow should format the flow output data when Amazon S3 is used as the destination.
Type: [S3OutputFormatConfig](API_S3OutputFormatConfig.md) object
Required: No

## See Also
<a name="API_S3DestinationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/S3DestinationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/S3DestinationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/S3DestinationProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
