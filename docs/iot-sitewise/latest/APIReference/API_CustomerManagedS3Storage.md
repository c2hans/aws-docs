---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CustomerManagedS3Storage.html
---

# CustomerManagedS3Storage
<a name="API_CustomerManagedS3Storage"></a>

Contains information about a customer managed Amazon S3 bucket.

## Contents
<a name="API_CustomerManagedS3Storage_Contents"></a>

 ** roleArn **   <a name="iotsitewise-Type-CustomerManagedS3Storage-roleArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the AWS Identity and Access Management role that allows AWS IoT SiteWise to send data to Amazon S3.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** s3ResourceArn **   <a name="iotsitewise-Type-CustomerManagedS3Storage-s3ResourceArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Amazon S3 object. For more information about how to find the ARN for an Amazon S3 object, see [Amazon S3 resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-arn-format.html) in the *Amazon Simple Storage Service User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

## See Also
<a name="API_CustomerManagedS3Storage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CustomerManagedS3Storage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CustomerManagedS3Storage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CustomerManagedS3Storage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
