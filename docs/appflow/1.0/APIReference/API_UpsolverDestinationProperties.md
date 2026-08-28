---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UpsolverDestinationProperties.html
---

# UpsolverDestinationProperties
<a name="API_UpsolverDestinationProperties"></a>

 The properties that are applied when Upsolver is used as a destination.

## Contents
<a name="API_UpsolverDestinationProperties_Contents"></a>

 ** bucketName **   <a name="appflow-Type-UpsolverDestinationProperties-bucketName"></a>
 The Upsolver Amazon S3 bucket name in which Amazon AppFlow places the transferred data.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 63.
Pattern: `^(upsolver-appflow)\S*`
Required: Yes

 ** s3OutputFormatConfig **   <a name="appflow-Type-UpsolverDestinationProperties-s3OutputFormatConfig"></a>
 The configuration that determines how data is formatted when Upsolver is used as the flow destination.
Type: [UpsolverS3OutputFormatConfig](API_UpsolverS3OutputFormatConfig.md) object
Required: Yes

 ** bucketPrefix **   <a name="appflow-Type-UpsolverDestinationProperties-bucketPrefix"></a>
 The object key for the destination Upsolver Amazon S3 bucket in which Amazon AppFlow places the files.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

## See Also
<a name="API_UpsolverDestinationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/UpsolverDestinationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/UpsolverDestinationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/UpsolverDestinationProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
