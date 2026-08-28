---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ComponentConfiguration.html
---

# ComponentConfiguration
<a name="API_ComponentConfiguration"></a>

Configuration details of the component.

## Contents
<a name="API_ComponentConfiguration_Contents"></a>

 ** componentArn **   <a name="imagebuilder-Type-ComponentConfiguration-componentArn"></a>
The Amazon Resource Name (ARN) of the component.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):component/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`
Required: Yes

 ** parameters **   <a name="imagebuilder-Type-ComponentConfiguration-parameters"></a>
A group of parameter settings that Image Builder uses to configure the component for a specific recipe.
Type: Array of [ComponentParameter](API_ComponentParameter.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_ComponentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ComponentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ComponentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ComponentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
