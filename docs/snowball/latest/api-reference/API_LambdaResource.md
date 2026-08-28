---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_LambdaResource.html
---

# LambdaResource
<a name="API_LambdaResource"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Identifies

## Contents
<a name="API_LambdaResource_Contents"></a>

 ** EventTriggers **   <a name="Snowball-Type-LambdaResource-EventTriggers"></a>
The array of ARNs for [S3Resource](API_S3Resource.md) objects to trigger the [LambdaResource](#API_LambdaResource) objects associated with this job.
Type: Array of [EventTriggerDefinition](API_EventTriggerDefinition.md) objects
Required: No

 ** LambdaArn **   <a name="Snowball-Type-LambdaResource-LambdaArn"></a>
An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:*`
Required: No

## See Also
<a name="API_LambdaResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/LambdaResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/LambdaResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/LambdaResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
