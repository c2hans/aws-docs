---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaFunctionRecipeSource.html
---

# LambdaFunctionRecipeSource
<a name="API_LambdaFunctionRecipeSource"></a>

Contains information about an AWS Lambda function to import to create a component.

## Contents
<a name="API_LambdaFunctionRecipeSource_Contents"></a>

 ** lambdaArn **   <a name="greengrassv2-Type-LambdaFunctionRecipeSource-lambdaArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Lambda function. The ARN must include the version of the function to import. You can't use version aliases like `$LATEST`.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** componentDependencies **   <a name="greengrassv2-Type-LambdaFunctionRecipeSource-componentDependencies"></a>
The component versions on which this Lambda function component depends.
Type: String to [ComponentDependencyRequirement](API_ComponentDependencyRequirement.md) object map
Key Length Constraints: Minimum length of 1.
Required: No

 ** componentLambdaParameters **   <a name="greengrassv2-Type-LambdaFunctionRecipeSource-componentLambdaParameters"></a>
The system and runtime parameters for the Lambda function as it runs on the Greengrass core device.
Type: [LambdaExecutionParameters](API_LambdaExecutionParameters.md) object
Required: No

 ** componentName **   <a name="greengrassv2-Type-LambdaFunctionRecipeSource-componentName"></a>
The name of the component.
Defaults to the name of the Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** componentPlatforms **   <a name="greengrassv2-Type-LambdaFunctionRecipeSource-componentPlatforms"></a>
The platforms that the component version supports.
Type: Array of [ComponentPlatform](API_ComponentPlatform.md) objects
Required: No

 ** componentVersion **   <a name="greengrassv2-Type-LambdaFunctionRecipeSource-componentVersion"></a>
The version of the component.
Defaults to the version of the Lambda function as a semantic version. For example, if your function version is `3`, the component version becomes `3.0.0`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_LambdaFunctionRecipeSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/LambdaFunctionRecipeSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/LambdaFunctionRecipeSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/LambdaFunctionRecipeSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
