---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-responseinspectionjson.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ResponseInspectionJson
<a name="aws-properties-wafv2-webacl-responseinspectionjson"></a>

Configures inspection of the response JSON. AWS WAF can inspect the first 65,536 bytes (64 KB) of the response JSON. This is part of the `ResponseInspection` configuration for `AWSManagedRulesATPRuleSet` and `AWSManagedRulesACFPRuleSet`.

**Note**
Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.

## Syntax
<a name="aws-properties-wafv2-webacl-responseinspectionjson-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-responseinspectionjson-syntax.json"></a>

```
{
  "[FailureValues](#cfn-wafv2-webacl-responseinspectionjson-failurevalues)" : {{[ String, ... ]}},
  "[Identifier](#cfn-wafv2-webacl-responseinspectionjson-identifier)" : {{String}},
  "[SuccessValues](#cfn-wafv2-webacl-responseinspectionjson-successvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-responseinspectionjson-syntax.yaml"></a>

```
  [FailureValues](#cfn-wafv2-webacl-responseinspectionjson-failurevalues): {{
    - String}}
  [Identifier](#cfn-wafv2-webacl-responseinspectionjson-identifier): {{String}}
  [SuccessValues](#cfn-wafv2-webacl-responseinspectionjson-successvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-responseinspectionjson-properties"></a>

`FailureValues`  <a name="cfn-wafv2-webacl-responseinspectionjson-failurevalues"></a>
Values for the specified identifier in the response JSON that indicate a failed login or account creation attempt. To be counted as a failure, the value must be an exact match, including case. Each value must be unique among the success and failure values.
JSON example: `"FailureValues": [ "False", "Failed" ]`
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `100 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Identifier`  <a name="cfn-wafv2-webacl-responseinspectionjson-identifier"></a>
The identifier for the value to match against in the JSON. The identifier must be an exact match, including case.
JSON examples: `"Identifier": [ "/login/success" ]` and `"Identifier": [ "/sign-up/success" ]`
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessValues`  <a name="cfn-wafv2-webacl-responseinspectionjson-successvalues"></a>
Values for the specified identifier in the response JSON that indicate a successful login or account creation attempt. To be counted as a success, the value must be an exact match, including case. Each value must be unique among the success and failure values.
JSON example: `"SuccessValues": [ "True", "Succeeded" ]`
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `100 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
