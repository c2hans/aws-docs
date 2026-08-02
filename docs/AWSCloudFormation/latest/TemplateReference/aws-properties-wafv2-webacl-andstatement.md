---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-andstatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL AndStatement
<a name="aws-properties-wafv2-webacl-andstatement"></a>

A logical rule statement used to combine other rule statements with AND logic. You provide more than one [Statement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html#cfn-wafv2-webacl-notstatement-statement) within the `AndStatement`.

## Syntax
<a name="aws-properties-wafv2-webacl-andstatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-andstatement-syntax.json"></a>

```
{
  "[Statements](#cfn-wafv2-webacl-andstatement-statements)" : {{[ Statement, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-andstatement-syntax.yaml"></a>

```
  [Statements](#cfn-wafv2-webacl-andstatement-statements): {{
    - Statement}}
```

## Properties
<a name="aws-properties-wafv2-webacl-andstatement-properties"></a>

`Statements`  <a name="cfn-wafv2-webacl-andstatement-statements"></a>
The statements to combine with AND logic. You can use any statements that can be nested.
*Required*: Yes
*Type*: Array of [Statement](aws-properties-wafv2-webacl-statement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
