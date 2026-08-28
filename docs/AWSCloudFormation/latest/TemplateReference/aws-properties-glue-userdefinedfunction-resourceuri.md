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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
