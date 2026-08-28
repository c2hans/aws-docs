---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaLinuxProcessParams.html
---

# LambdaLinuxProcessParams
<a name="API_LambdaLinuxProcessParams"></a>

Contains parameters for a Linux process that contains an AWS Lambda function.

## Contents
<a name="API_LambdaLinuxProcessParams_Contents"></a>

 ** containerParams **   <a name="greengrassv2-Type-LambdaLinuxProcessParams-containerParams"></a>
The parameters for the container in which the Lambda function runs.
Type: [LambdaContainerParams](API_LambdaContainerParams.md) object
Required: No

 ** isolationMode **   <a name="greengrassv2-Type-LambdaLinuxProcessParams-isolationMode"></a>
The isolation mode for the process that contains the Lambda function. The process can run in an isolated runtime environment inside the AWS IoT Greengrass container, or as a regular process outside any container.
Default: `GreengrassContainer`
Type: String
Valid Values: `GreengrassContainer | NoContainer`
Required: No

## See Also
<a name="API_LambdaLinuxProcessParams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/LambdaLinuxProcessParams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/LambdaLinuxProcessParams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/LambdaLinuxProcessParams)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
