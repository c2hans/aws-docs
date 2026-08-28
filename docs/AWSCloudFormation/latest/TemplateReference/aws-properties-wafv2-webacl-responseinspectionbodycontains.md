---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-responseinspectionbodycontains.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ResponseInspectionBodyContains
<a name="aws-properties-wafv2-webacl-responseinspectionbodycontains"></a>

Configures inspection of the response body. AWS WAF can inspect the first 65,536 bytes (64 KB) of the response body. This is part of the `ResponseInspection` configuration for `AWSManagedRulesATPRuleSet` and `AWSManagedRulesACFPRuleSet`.

**Note**
Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.

## Syntax
<a name="aws-properties-wafv2-webacl-responseinspectionbodycontains-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-responseinspectionbodycontains-syntax.json"></a>

```
{
  "[FailureStrings](#cfn-wafv2-webacl-responseinspectionbodycontains-failurestrings)" : {{[ String, ... ]}},
  "[SuccessStrings](#cfn-wafv2-webacl-responseinspectionbodycontains-successstrings)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-responseinspectionbodycontains-syntax.yaml"></a>

```
  [FailureStrings](#cfn-wafv2-webacl-responseinspectionbodycontains-failurestrings): {{
    - String}}
  [SuccessStrings](#cfn-wafv2-webacl-responseinspectionbodycontains-successstrings): {{
    - String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-responseinspectionbodycontains-properties"></a>

`FailureStrings`  <a name="cfn-wafv2-webacl-responseinspectionbodycontains-failurestrings"></a>
Strings in the body of the response that indicate a failed login or account creation attempt. To be counted as a failure, the string can be anywhere in the body and must be an exact match, including case. Each string must be unique among the success and failure strings.
JSON example: `"FailureStrings": [ "Request failed" ]`
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `100 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessStrings`  <a name="cfn-wafv2-webacl-responseinspectionbodycontains-successstrings"></a>
Strings in the body of the response that indicate a successful login or account creation attempt. To be counted as a success, the string can be anywhere in the body and must be an exact match, including case. Each string must be unique among the success and failure strings.
JSON examples: `"SuccessStrings": [ "Login successful" ]` and `"SuccessStrings": [ "Account creation successful", "Welcome to our site!" ]`
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `100 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
