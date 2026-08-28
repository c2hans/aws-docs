---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_JobResource.html
---

# JobResource
<a name="API_JobResource"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Contains an array of AWS resource objects. Each object represents an Amazon S3 bucket, an AWS Lambda function, or an Amazon Machine Image (AMI) based on Amazon EC2 that is associated with a particular job.

## Contents
<a name="API_JobResource_Contents"></a>

 ** Ec2AmiResources **   <a name="Snowball-Type-JobResource-Ec2AmiResources"></a>
The Amazon Machine Images (AMIs) associated with this job.
Type: Array of [Ec2AmiResource](API_Ec2AmiResource.md) objects
Required: No

 ** LambdaResources **   <a name="Snowball-Type-JobResource-LambdaResources"></a>
The Python-language Lambda functions for this job.
Type: Array of [LambdaResource](API_LambdaResource.md) objects
Required: No

 ** S3Resources **   <a name="Snowball-Type-JobResource-S3Resources"></a>
An array of `S3Resource` objects.
Type: Array of [S3Resource](API_S3Resource.md) objects
Required: No

## See Also
<a name="API_JobResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/JobResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/JobResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/JobResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
