---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-fieldidentifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL FieldIdentifier
<a name="aws-properties-wafv2-webacl-fieldidentifier"></a>

The identifier of a field in the web request payload that contains customer data.

This data type is used to specify fields in the `RequestInspection` and `RequestInspectionACFP` configurations, which are used in the managed rule group configurations `AWSManagedRulesATPRuleSet` and `AWSManagedRulesACFPRuleSet`, respectively.

## Syntax
<a name="aws-properties-wafv2-webacl-fieldidentifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-fieldidentifier-syntax.json"></a>

```
{
  "[Identifier](#cfn-wafv2-webacl-fieldidentifier-identifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-fieldidentifier-syntax.yaml"></a>

```
  [Identifier](#cfn-wafv2-webacl-fieldidentifier-identifier): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-fieldidentifier-properties"></a>

`Identifier`  <a name="cfn-wafv2-webacl-fieldidentifier-identifier"></a>
The name of the field.
When the `PayloadType` in the request inspection is `JSON`, this identifier must be in JSON pointer syntax. For example `/form/username`. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).
When the `PayloadType` is `FORM_ENCODED`, use the HTML form names. For example, `username`.
For more information, see the descriptions for each field type in the request inspection properties.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
