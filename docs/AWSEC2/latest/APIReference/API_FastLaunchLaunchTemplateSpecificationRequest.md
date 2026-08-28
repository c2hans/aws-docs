---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FastLaunchLaunchTemplateSpecificationRequest.html
---

# FastLaunchLaunchTemplateSpecificationRequest
<a name="API_FastLaunchLaunchTemplateSpecificationRequest"></a>

Request to create a launch template for a Windows fast launch enabled AMI.

**Note**
Note - You can specify either the `LaunchTemplateName` or the `LaunchTemplateId`, but not both.

## Contents
<a name="API_FastLaunchLaunchTemplateSpecificationRequest_Contents"></a>

 ** Version **
Specify the version of the launch template that the AMI should use for Windows fast launch.
Type: String
Required: Yes

 ** LaunchTemplateId **
Specify the ID of the launch template that the AMI should use for Windows fast launch.
Type: String
Required: No

 ** LaunchTemplateName **
Specify the name of the launch template that the AMI should use for Windows fast launch.
Type: String
Required: No

## See Also
<a name="API_FastLaunchLaunchTemplateSpecificationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FastLaunchLaunchTemplateSpecificationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FastLaunchLaunchTemplateSpecificationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FastLaunchLaunchTemplateSpecificationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
