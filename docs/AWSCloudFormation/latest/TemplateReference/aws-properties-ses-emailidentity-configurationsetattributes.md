---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-emailidentity-configurationsetattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::EmailIdentity ConfigurationSetAttributes
<a name="aws-properties-ses-emailidentity-configurationsetattributes"></a>

Used to associate a configuration set with an email identity.

## Syntax
<a name="aws-properties-ses-emailidentity-configurationsetattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-emailidentity-configurationsetattributes-syntax.json"></a>

```
{
  "[ConfigurationSetName](#cfn-ses-emailidentity-configurationsetattributes-configurationsetname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-emailidentity-configurationsetattributes-syntax.yaml"></a>

```
  [ConfigurationSetName](#cfn-ses-emailidentity-configurationsetattributes-configurationsetname): {{String}}
```

## Properties
<a name="aws-properties-ses-emailidentity-configurationsetattributes-properties"></a>

`ConfigurationSetName`  <a name="cfn-ses-emailidentity-configurationsetattributes-configurationsetname"></a>
The configuration set to associate with an email identity.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
