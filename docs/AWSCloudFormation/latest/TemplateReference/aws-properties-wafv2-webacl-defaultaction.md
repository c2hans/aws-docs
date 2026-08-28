---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-defaultaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL DefaultAction
<a name="aws-properties-wafv2-webacl-defaultaction"></a>

In a [AWS::WAFv2::WebACL](aws-resource-wafv2-webacl.md), this is the action that you want AWS WAF to perform when a web request doesn't match any of the rules in the `WebACL`. The default action must be a terminating action.

## Syntax
<a name="aws-properties-wafv2-webacl-defaultaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-defaultaction-syntax.json"></a>

```
{
  "[Allow](#cfn-wafv2-webacl-defaultaction-allow)" : {{AllowAction}},
  "[Block](#cfn-wafv2-webacl-defaultaction-block)" : {{BlockAction}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-defaultaction-syntax.yaml"></a>

```
  [Allow](#cfn-wafv2-webacl-defaultaction-allow): {{
    AllowAction}}
  [Block](#cfn-wafv2-webacl-defaultaction-block): {{
    BlockAction}}
```

## Properties
<a name="aws-properties-wafv2-webacl-defaultaction-properties"></a>

`Allow`  <a name="cfn-wafv2-webacl-defaultaction-allow"></a>
Specifies that AWS WAF should allow requests by default.
*Required*: No
*Type*: [AllowAction](aws-properties-wafv2-webacl-allowaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Block`  <a name="cfn-wafv2-webacl-defaultaction-block"></a>
Specifies that AWS WAF should block requests by default.
*Required*: No
*Type*: [BlockAction](aws-properties-wafv2-webacl-blockaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-wafv2-webacl-defaultaction--examples"></a>

**Topics**
+ [Set a web ACL default action](#aws-properties-wafv2-webacl-defaultaction--examples--Set_a_web_ACL_default_action)
+ [Set a customized web ACL default action](#aws-properties-wafv2-webacl-defaultaction--examples--Set_a_customized_web_ACL_default_action)

### Set a web ACL default action
<a name="aws-properties-wafv2-webacl-defaultaction--examples--Set_a_web_ACL_default_action"></a>

The following shows an example web ACL default action specification that sets the default action to "Block".

#### YAML
<a name="aws-properties-wafv2-webacl-defaultaction--examples--Set_a_web_ACL_default_action--yaml"></a>

```
DefaultAction:
    Block: {}
```

#### JSON
<a name="aws-properties-wafv2-webacl-defaultaction--examples--Set_a_web_ACL_default_action--json"></a>

```
"DefaultAction": {
    "Block": {}
}
```

### Set a customized web ACL default action
<a name="aws-properties-wafv2-webacl-defaultaction--examples--Set_a_customized_web_ACL_default_action"></a>

The following shows an example web ACL default action specification with customization.

#### YAML
<a name="aws-properties-wafv2-webacl-defaultaction--examples--Set_a_customized_web_ACL_default_action--yaml"></a>

```
DefaultAction:
  Allow:
    CustomRequestHandling:
      InsertHeaders:
        - Name: AllowActionHeader1Name
          Value: AllowActionHeader1Value
        - Name: AllowActionHeader2Name
          Value: AllowActionHeader2Value
```

#### JSON
<a name="aws-properties-wafv2-webacl-defaultaction--examples--Set_a_customized_web_ACL_default_action--json"></a>

```
"DefaultAction": {
  "Allow": {
    "CustomRequestHandling": {
      "InsertHeaders": [
        {
          "Name": "AllowActionHeader1Name",
          "Value": "AllowActionHeader1Value"
        },
        {
          "Name": "AllowActionHeader2Name",
          "Value": "AllowActionHeader2Value"
        }
      ]
    }
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
