---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-dataprotect.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL DataProtect
<a name="aws-properties-wafv2-webacl-dataprotect"></a>

<a name="aws-properties-wafv2-webacl-dataprotect-description"></a>The `DataProtect` property type specifies Property description not available. for an [AWS::WAFv2::WebACL](aws-resource-wafv2-webacl.md).

## Syntax
<a name="aws-properties-wafv2-webacl-dataprotect-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-dataprotect-syntax.json"></a>

```
{
  "[Action](#cfn-wafv2-webacl-dataprotect-action)" : {{String}},
  "[ExcludeRateBasedDetails](#cfn-wafv2-webacl-dataprotect-excluderatebaseddetails)" : {{Boolean}},
  "[ExcludeRuleMatchDetails](#cfn-wafv2-webacl-dataprotect-excluderulematchdetails)" : {{Boolean}},
  "[Field](#cfn-wafv2-webacl-dataprotect-field)" : {{FieldToProtect}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-dataprotect-syntax.yaml"></a>

```
  [Action](#cfn-wafv2-webacl-dataprotect-action): {{String}}
  [ExcludeRateBasedDetails](#cfn-wafv2-webacl-dataprotect-excluderatebaseddetails): {{Boolean}}
  [ExcludeRuleMatchDetails](#cfn-wafv2-webacl-dataprotect-excluderulematchdetails): {{Boolean}}
  [Field](#cfn-wafv2-webacl-dataprotect-field): {{
    FieldToProtect}}
```

## Properties
<a name="aws-properties-wafv2-webacl-dataprotect-properties"></a>

`Action`  <a name="cfn-wafv2-webacl-dataprotect-action"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `SUBSTITUTION | HASH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeRateBasedDetails`  <a name="cfn-wafv2-webacl-dataprotect-excluderatebaseddetails"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeRuleMatchDetails`  <a name="cfn-wafv2-webacl-dataprotect-excluderulematchdetails"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Field`  <a name="cfn-wafv2-webacl-dataprotect-field"></a>
Property description not available.
*Required*: Yes
*Type*: [FieldToProtect](aws-properties-wafv2-webacl-fieldtoprotect.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
