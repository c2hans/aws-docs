---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-userdefinedfunction-resourceuri.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::UserDefinedFunction ResourceUri
<a name="aws-properties-glue-userdefinedfunction-resourceuri"></a>

The URIs for function resources.

## Syntax
<a name="aws-properties-glue-userdefinedfunction-resourceuri-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-userdefinedfunction-resourceuri-syntax.json"></a>

```
{
  "[ResourceType](#cfn-glue-userdefinedfunction-resourceuri-resourcetype)" : {{String}},
  "[Uri](#cfn-glue-userdefinedfunction-resourceuri-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-userdefinedfunction-resourceuri-syntax.yaml"></a>

```
  [ResourceType](#cfn-glue-userdefinedfunction-resourceuri-resourcetype): {{String}}
  [Uri](#cfn-glue-userdefinedfunction-resourceuri-uri): {{String}}
```

## Properties
<a name="aws-properties-glue-userdefinedfunction-resourceuri-properties"></a>

`ResourceType`  <a name="cfn-glue-userdefinedfunction-resourceuri-resourcetype"></a>
The type of the resource.
*Required*: No
*Type*: String
*Allowed values*: `JAR | FILE | ARCHIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uri`  <a name="cfn-glue-userdefinedfunction-resourceuri-uri"></a>
The URI for accessing the resource.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
