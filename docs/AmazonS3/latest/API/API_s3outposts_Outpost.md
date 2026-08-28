---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_Outpost.html
---

# Outpost
<a name="API_s3outposts_Outpost"></a>

Contains the details for the Outpost object.

## Contents
<a name="API_s3outposts_Outpost_Contents"></a>

 ** CapacityInBytes **   <a name="AmazonS3-Type-s3outposts_Outpost-CapacityInBytes"></a>
The Amazon S3 capacity of the outpost in bytes.
Type: Long
Required: No

 ** OutpostArn **   <a name="AmazonS3-Type-s3outposts_Outpost-OutpostArn"></a>
Specifies the unique Amazon Resource Name (ARN) for the outpost.
Type: String
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|ec2)$`
Required: No

 ** OutpostId **   <a name="AmazonS3-Type-s3outposts_Outpost-OutpostId"></a>
Specifies the unique identifier for the outpost.
Type: String
Pattern: `^(op-[a-f0-9]{17}|\d{12}|ec2)$`
Required: No

 ** OwnerId **   <a name="AmazonS3-Type-s3outposts_Outpost-OwnerId"></a>
Returns the AWS account ID of the outpost owner. Useful for comparing owned versus shared outposts.
Type: String
Pattern: `^\d{12}$`
Required: No

 ** S3OutpostArn **   <a name="AmazonS3-Type-s3outposts_Outpost-S3OutpostArn"></a>
Specifies the unique S3 on Outposts ARN for use with AWS Resource Access Manager (AWS RAM).
Type: String
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|\d{12})/s3$`
Required: No

## See Also
<a name="API_s3outposts_Outpost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/Outpost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/Outpost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/Outpost)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
