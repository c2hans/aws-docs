---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-body.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup Body
<a name="aws-properties-wafv2-rulegroup-body"></a>

Inspect the body of the web request. The body immediately follows the request headers.

This is used to indicate the web request component to inspect, in the [FieldToMatch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch) specification.

## Syntax
<a name="aws-properties-wafv2-rulegroup-body-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-body-syntax.json"></a>

```
{
  "[OversizeHandling](#cfn-wafv2-rulegroup-body-oversizehandling)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-body-syntax.yaml"></a>

```
  [OversizeHandling](#cfn-wafv2-rulegroup-body-oversizehandling): {{String}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-body-properties"></a>

`OversizeHandling`  <a name="cfn-wafv2-rulegroup-body-oversizehandling"></a>
What AWS WAF should do if the body is larger than AWS WAF can inspect.
AWS WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to AWS WAF for inspection.
+ For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).
+ For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL `AssociationConfig`, for additional processing fees.
+ For AWS Amplify, use the CloudFront limit.
The options for oversize handling are the following:
+ `CONTINUE` - Inspect the available body contents normally, according to the rule inspection criteria.
+ `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+ `NO_MATCH` - Treat the web request as not matching the rule statement.
You can combine the `MATCH` or `NO_MATCH` settings for oversize handling with your rule and web ACL action settings, so that you block any request whose body is over the limit.
Default: `CONTINUE`
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | MATCH | NO_MATCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-wafv2-rulegroup-body--examples"></a>

### Set the Body specification
<a name="aws-properties-wafv2-rulegroup-body--examples--Set_the_Body_specification"></a>

The following shows an example Body field to match specification.

#### YAML
<a name="aws-properties-wafv2-rulegroup-body--examples--Set_the_Body_specification--yaml"></a>

```
FieldToMatch:
  Body:
    OversizeHandling: MATCH
```

#### JSON
<a name="aws-properties-wafv2-rulegroup-body--examples--Set_the_Body_specification--json"></a>

```
"FieldToMatch": {
  "Body": {
    "OversizeHandling": "MATCH"
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
