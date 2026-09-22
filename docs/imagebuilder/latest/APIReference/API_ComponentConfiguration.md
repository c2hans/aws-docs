---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ComponentConfiguration.html
---

# ComponentConfiguration
<a name="API_ComponentConfiguration"></a>

Configuration details of the component. You can specify each component only once in a recipe, regardless of version. Components with a status of `DEPRECATED` or `DISABLED` can't be added to new recipes.

## Contents
<a name="API_ComponentConfiguration_Contents"></a>

 ** componentArn **   <a name="imagebuilder-Type-ComponentConfiguration-componentArn"></a>
The Amazon Resource Name (ARN) of the component. You can specify a build version ARN, or a component version ARN whose version segments can use `x` wildcards, for example `1.x.x`.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):component/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`
Required: Yes

 ** parameters **   <a name="imagebuilder-Type-ComponentConfiguration-parameters"></a>
A group of parameter settings that Image Builder uses to configure the component for a specific recipe. You must supply a value for every component parameter that has no default value, and you can only supply parameters that the component defines.
Type: Array of [ComponentParameter](API_ComponentParameter.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_ComponentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ComponentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ComponentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ComponentConfiguration)
