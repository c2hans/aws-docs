---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_LaunchTemplateSpecification.html
---

# LaunchTemplateSpecification
<a name="API_LaunchTemplateSpecification"></a>

An Amazon Elastic Compute Cloud launch template that contains configuration settings and game server code to be deployed to all instances in a game server group. The launch template is specified when creating a new game server group.

## Contents
<a name="API_LaunchTemplateSpecification_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LaunchTemplateId **   <a name="gameliftservers-Type-LaunchTemplateSpecification-LaunchTemplateId"></a>
A unique identifier for an existing Amazon EC2 launch template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]+`
Required: No

 ** LaunchTemplateName **   <a name="gameliftservers-Type-LaunchTemplateSpecification-LaunchTemplateName"></a>
A readable identifier for an existing Amazon EC2 launch template.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9\(\)\.\-/_]+`
Required: No

 ** Version **   <a name="gameliftservers-Type-LaunchTemplateSpecification-Version"></a>
The version of the Amazon EC2 launch template to use. If no version is specified, the default version will be used. With Amazon EC2, you can specify a default version for a launch template. If none is set, the default is the first version created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]+`
Required: No

## See Also
<a name="API_LaunchTemplateSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/LaunchTemplateSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/LaunchTemplateSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/LaunchTemplateSpecification)
