---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResourceTypeRequest.html
---

# ResourceTypeRequest
<a name="API_ResourceTypeRequest"></a>

A resource type to check for image references. Associated options can also be specified if the resource type is an EC2 instance or launch template.

## Contents
<a name="API_ResourceTypeRequest_Contents"></a>

 ** ResourceType **
The resource type.
Type: String
Valid Values: `ec2:Instance | ec2:LaunchTemplate | ssm:Parameter | imagebuilder:ImageRecipe | imagebuilder:ContainerRecipe`
Required: No

 ** ResourceTypeOption.N **
The options that affect the scope of the response. Valid only when `ResourceType` is `ec2:Instance` or `ec2:LaunchTemplate`.
Type: Array of [ResourceTypeOption](API_ResourceTypeOption.md) objects
Required: No

## See Also
<a name="API_ResourceTypeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ResourceTypeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ResourceTypeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ResourceTypeRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
