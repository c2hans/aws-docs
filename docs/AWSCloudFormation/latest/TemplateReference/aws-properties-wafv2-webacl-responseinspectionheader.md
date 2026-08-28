---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-responseinspectionheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ResponseInspectionHeader
<a name="aws-properties-wafv2-webacl-responseinspectionheader"></a>

Configures inspection of the response header. This is part of the `ResponseInspection` configuration for `AWSManagedRulesATPRuleSet` and `AWSManagedRulesACFPRuleSet`.

**Note**
Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.

## Syntax
<a name="aws-properties-wafv2-webacl-responseinspectionheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-responseinspectionheader-syntax.json"></a>

```
{
  "[FailureValues](#cfn-wafv2-webacl-responseinspectionheader-failurevalues)" : {{[ String, ... ]}},
  "[Name](#cfn-wafv2-webacl-responseinspectionheader-name)" : {{String}},
  "[SuccessValues](#cfn-wafv2-webacl-responseinspectionheader-successvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-responseinspectionheader-syntax.yaml"></a>

```
  [FailureValues](#cfn-wafv2-webacl-responseinspectionheader-failurevalues): {{
    - String}}
  [Name](#cfn-wafv2-webacl-responseinspectionheader-name): {{String}}
  [SuccessValues](#cfn-wafv2-webacl-responseinspectionheader-successvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-responseinspectionheader-properties"></a>

`FailureValues`  <a name="cfn-wafv2-webacl-responseinspectionheader-failurevalues"></a>
Values in the response header with the specified name that indicate a failed login or account creation attempt. To be counted as a failure, the value must be an exact match, including case. Each value must be unique among the success and failure values.
JSON examples: `"FailureValues": [ "LoginFailed", "Failed login" ]` and `"FailureValues": [ "AccountCreationFailed" ]`
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `100 | 3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wafv2-webacl-responseinspectionheader-name"></a>
The name of the header to match against. The name must be an exact match, including case.
JSON example: `"Name": [ "RequestResult" ]`
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessValues`  <a name="cfn-wafv2-webacl-responseinspectionheader-successvalues"></a>
Values in the response header with the specified name that indicate a successful login or account creation attempt. To be counted as a success, the value must be an exact match, including case. Each value must be unique among the success and failure values.
JSON examples: `"SuccessValues": [ "LoginPassed", "Successful login" ]` and `"SuccessValues": [ "AccountCreated", "Successful account creation" ]`
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `100 | 3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
