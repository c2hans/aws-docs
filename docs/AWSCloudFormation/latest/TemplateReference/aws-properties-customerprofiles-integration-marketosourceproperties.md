---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-marketosourceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration MarketoSourceProperties
<a name="aws-properties-customerprofiles-integration-marketosourceproperties"></a>

The properties that are applied when Marketo is being used as a source.

## Syntax
<a name="aws-properties-customerprofiles-integration-marketosourceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-marketosourceproperties-syntax.json"></a>

```
{
  "[Object](#cfn-customerprofiles-integration-marketosourceproperties-object)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-marketosourceproperties-syntax.yaml"></a>

```
  [Object](#cfn-customerprofiles-integration-marketosourceproperties-object): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-marketosourceproperties-properties"></a>

`Object`  <a name="cfn-customerprofiles-integration-marketosourceproperties-object"></a>
The object specified in the Marketo flow source.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
