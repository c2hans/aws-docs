---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-userdefinedfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::UserDefinedFunction
<a name="aws-resource-glue-userdefinedfunction"></a>

Represents the equivalent of a Hive user-defined function (`UDF`) definition.

## Syntax
<a name="aws-resource-glue-userdefinedfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-userdefinedfunction-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::UserDefinedFunction",
  "Properties" : {
      "[ClassName](#cfn-glue-userdefinedfunction-classname)" : {{String}},
      "[DatabaseName](#cfn-glue-userdefinedfunction-databasename)" : {{String}},
      "[FunctionName](#cfn-glue-userdefinedfunction-functionname)" : {{String}},
      "[FunctionType](#cfn-glue-userdefinedfunction-functiontype)" : {{String}},
      "[OwnerName](#cfn-glue-userdefinedfunction-ownername)" : {{String}},
      "[OwnerType](#cfn-glue-userdefinedfunction-ownertype)" : {{String}},
      "[ResourceUris](#cfn-glue-userdefinedfunction-resourceuris)" : {{[ ResourceUri, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-glue-userdefinedfunction-syntax.yaml"></a>

```
Type: AWS::Glue::UserDefinedFunction
Properties:
  [ClassName](#cfn-glue-userdefinedfunction-classname): {{String}}
  [DatabaseName](#cfn-glue-userdefinedfunction-databasename): {{String}}
  [FunctionName](#cfn-glue-userdefinedfunction-functionname): {{String}}
  [FunctionType](#cfn-glue-userdefinedfunction-functiontype): {{String}}
  [OwnerName](#cfn-glue-userdefinedfunction-ownername): {{String}}
  [OwnerType](#cfn-glue-userdefinedfunction-ownertype): {{String}}
  [ResourceUris](#cfn-glue-userdefinedfunction-resourceuris): {{
    - ResourceUri}}
```

## Properties
<a name="aws-resource-glue-userdefinedfunction-properties"></a>

`ClassName`  <a name="cfn-glue-userdefinedfunction-classname"></a>
The Java class that contains the function code.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-glue-userdefinedfunction-databasename"></a>
The name of the catalog database that contains the function.
*Required*: Yes
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FunctionName`  <a name="cfn-glue-userdefinedfunction-functionname"></a>
The name of the function.
*Required*: Yes
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FunctionType`  <a name="cfn-glue-userdefinedfunction-functiontype"></a>
The type of the function.
*Required*: No
*Type*: String
*Allowed values*: `REGULAR_FUNCTION | AGGREGATE_FUNCTION | STORED_PROCEDURE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OwnerName`  <a name="cfn-glue-userdefinedfunction-ownername"></a>
The owner of the function.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OwnerType`  <a name="cfn-glue-userdefinedfunction-ownertype"></a>
The owner type.
*Required*: No
*Type*: String
*Allowed values*: `USER | ROLE | GROUP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceUris`  <a name="cfn-glue-userdefinedfunction-resourceuris"></a>
The resource URIs for the function.
*Required*: No
*Type*: Array of [ResourceUri](aws-properties-glue-userdefinedfunction-resourceuri.md)
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-glue-userdefinedfunction-return-values"></a>

### Ref
<a name="aws-resource-glue-userdefinedfunction-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-glue-userdefinedfunction-return-values-fn--getatt"></a>

####
<a name="aws-resource-glue-userdefinedfunction-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
