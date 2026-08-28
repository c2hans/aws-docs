---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-blockaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL BlockAction
<a name="aws-properties-wafv2-webacl-blockaction"></a>

Specifies that AWS WAF should block the request and optionally defines additional custom handling for the response to the web request.

This is used in the context of other settings, for example to specify values for a rule action or a web ACL default action.

## Syntax
<a name="aws-properties-wafv2-webacl-blockaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-blockaction-syntax.json"></a>

```
{
  "[CustomResponse](#cfn-wafv2-webacl-blockaction-customresponse)" : {{CustomResponse}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-blockaction-syntax.yaml"></a>

```
  [CustomResponse](#cfn-wafv2-webacl-blockaction-customresponse): {{
    CustomResponse}}
```

## Properties
<a name="aws-properties-wafv2-webacl-blockaction-properties"></a>

`CustomResponse`  <a name="cfn-wafv2-webacl-blockaction-customresponse"></a>
Defines a custom response for the web request.
For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the *AWS WAF Developer Guide*.
*Required*: No
*Type*: [CustomResponse](aws-properties-wafv2-webacl-customresponse.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-wafv2-webacl-blockaction--examples"></a>

**Topics**
+ [Set an block action](#aws-properties-wafv2-webacl-blockaction--examples--Set_an_block_action)
+ [Set a block action with a custom response setting](#aws-properties-wafv2-webacl-blockaction--examples--Set_a_block_action_with_a_custom_response_setting)

### Set an block action
<a name="aws-properties-wafv2-webacl-blockaction--examples--Set_an_block_action"></a>

The following shows an example block action specification.

#### YAML
<a name="aws-properties-wafv2-webacl-blockaction--examples--Set_an_block_action--yaml"></a>

```
Action:
  Block: {}
```

#### JSON
<a name="aws-properties-wafv2-webacl-blockaction--examples--Set_an_block_action--json"></a>

```
"Action": {
  "Block": {}
}
```

### Set a block action with a custom response setting
<a name="aws-properties-wafv2-webacl-blockaction--examples--Set_a_block_action_with_a_custom_response_setting"></a>

The following shows an example block action specification with a custom response setting.

#### YAML
<a name="aws-properties-wafv2-webacl-blockaction--examples--Set_a_block_action_with_a_custom_response_setting--yaml"></a>

```
Block:
  CustomResponse:
    ResponseCode: 503
    CustomResponseBodyKey: CustomResponseBodyKey1
    ResponseHeaders:
      - Name: BlockActionHeader1Name
        Value: BlockActionHeader1Value
      - Name: BlockActionHeader2Name
        Value: BlockActionHeader2Value
```

#### JSON
<a name="aws-properties-wafv2-webacl-blockaction--examples--Set_a_block_action_with_a_custom_response_setting--json"></a>

```
"Block": {
  "CustomResponse": {
    "ResponseCode": 503,
    "CustomResponseBodyKey": "CustomResponseBodyKey1",
    "ResponseHeaders": [
      {
        "Name": "BlockActionHeader1Name",
        "Value": "BlockActionHeader1Value"
      },
      {
        "Name": "BlockActionHeader2Name",
        "Value": "BlockActionHeader2Value"
      }
    ]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
