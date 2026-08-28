---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elementalinference-dictionary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElementalInference::Dictionary
<a name="aws-resource-elementalinference-dictionary"></a>

<a name="aws-resource-elementalinference-dictionary-description"></a>The `AWS::ElementalInference::Dictionary` resource Property description not available. for ElementalInference.

## Syntax
<a name="aws-resource-elementalinference-dictionary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elementalinference-dictionary-syntax.json"></a>

```
{
  "Type" : "AWS::ElementalInference::Dictionary",
  "Properties" : {
      "[Entries](#cfn-elementalinference-dictionary-entries)" : {{String}},
      "[Language](#cfn-elementalinference-dictionary-language)" : {{String}},
      "[Name](#cfn-elementalinference-dictionary-name)" : {{String}},
      "[Tags](#cfn-elementalinference-dictionary-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-elementalinference-dictionary-syntax.yaml"></a>

```
Type: AWS::ElementalInference::Dictionary
Properties:
  [Entries](#cfn-elementalinference-dictionary-entries): {{String}}
  [Language](#cfn-elementalinference-dictionary-language): {{String}}
  [Name](#cfn-elementalinference-dictionary-name): {{String}}
  [Tags](#cfn-elementalinference-dictionary-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-elementalinference-dictionary-properties"></a>

`Entries`  <a name="cfn-elementalinference-dictionary-entries"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `40960`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Language`  <a name="cfn-elementalinference-dictionary-language"></a>
The language of the dictionary.
*Required*: Yes
*Type*: String
*Allowed values*: `eng | fra | ita | deu | spa | por`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-elementalinference-dictionary-name"></a>
The name of the dictionary.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-elementalinference-dictionary-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elementalinference-dictionary-return-values"></a>

### Ref
<a name="aws-resource-elementalinference-dictionary-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-elementalinference-dictionary-return-values-fn--getatt"></a>

####
<a name="aws-resource-elementalinference-dictionary-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the dictionary.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the dictionary.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
