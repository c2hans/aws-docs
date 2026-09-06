---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-querydefinition-queryparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::QueryDefinition QueryParameter
<a name="aws-properties-logs-querydefinition-queryparameter"></a>

This structure defines a query parameter for a saved CloudWatch Logs Insights query definition. Query parameters are supported only for Logs Insights QL queries. They are placeholder variables that you can reference in a query string using the `{{parameterName}}` syntax. Each parameter can include a default value and a description.

## Syntax
<a name="aws-properties-logs-querydefinition-queryparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-querydefinition-queryparameter-syntax.json"></a>

```
{
  "[DefaultValue](#cfn-logs-querydefinition-queryparameter-defaultvalue)" : {{String}},
  "[Description](#cfn-logs-querydefinition-queryparameter-description)" : {{String}},
  "[Name](#cfn-logs-querydefinition-queryparameter-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-querydefinition-queryparameter-syntax.yaml"></a>

```
  [DefaultValue](#cfn-logs-querydefinition-queryparameter-defaultvalue): {{String}}
  [Description](#cfn-logs-querydefinition-queryparameter-description): {{String}}
  [Name](#cfn-logs-querydefinition-queryparameter-name): {{String}}
```

## Properties
<a name="aws-properties-logs-querydefinition-queryparameter-properties"></a>

`DefaultValue`  <a name="cfn-logs-querydefinition-queryparameter-defaultvalue"></a>
The default value to use for this query parameter if no value is supplied at execution time.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-logs-querydefinition-queryparameter-description"></a>
A description of the query parameter that explains its purpose or expected values.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-logs-querydefinition-queryparameter-name"></a>
The name of the query parameter. A query parameter name must start with a letter or underscore, and contain only letters, digits, and underscores.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_][a-zA-Z0-9_]*$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
