---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-notstatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL NotStatement
<a name="aws-properties-wafv2-webacl-notstatement"></a>

A logical rule statement used to negate the results of another rule statement. You provide one [Statement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html#cfn-wafv2-webacl-notstatement-statement) within the `NotStatement`.

## Syntax
<a name="aws-properties-wafv2-webacl-notstatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-notstatement-syntax.json"></a>

```
{
  "[Statement](#cfn-wafv2-webacl-notstatement-statement)" : {{Statement}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-notstatement-syntax.yaml"></a>

```
  [Statement](#cfn-wafv2-webacl-notstatement-statement): {{
    Statement}}
```

## Properties
<a name="aws-properties-wafv2-webacl-notstatement-properties"></a>

`Statement`  <a name="cfn-wafv2-webacl-notstatement-statement"></a>
The statement to negate. You can use any statement that can be nested.
*Required*: Yes
*Type*: [Statement](aws-properties-wafv2-webacl-statement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
