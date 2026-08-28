---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-singlequeryargument.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL SingleQueryArgument
<a name="aws-properties-wafv2-webacl-singlequeryargument"></a>

Inspect one query argument in the web request, identified by name, for example *UserName* or *SalesRegion*. The name isn't case sensitive.

This is used to indicate the web request component to inspect, in the [FieldToMatch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch) specification.

Example JSON: `"SingleQueryArgument": { "Name": "myArgument" }`

## Syntax
<a name="aws-properties-wafv2-webacl-singlequeryargument-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-singlequeryargument-syntax.json"></a>

```
{
  "[Name](#cfn-wafv2-webacl-singlequeryargument-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-singlequeryargument-syntax.yaml"></a>

```
  [Name](#cfn-wafv2-webacl-singlequeryargument-name): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-singlequeryargument-properties"></a>

`Name`  <a name="cfn-wafv2-webacl-singlequeryargument-name"></a>
The name of the query argument to inspect.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
