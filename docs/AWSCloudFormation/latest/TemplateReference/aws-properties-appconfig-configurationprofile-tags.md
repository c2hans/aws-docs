---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-configurationprofile-tags.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::ConfigurationProfile Tags
<a name="aws-properties-appconfig-configurationprofile-tags"></a>

Metadata to assign to the configuration profile. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

## Syntax
<a name="aws-properties-appconfig-configurationprofile-tags-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appconfig-configurationprofile-tags-syntax.json"></a>

```
{
  "[Key](#cfn-appconfig-configurationprofile-tags-key)" : {{String}},
  "[Value](#cfn-appconfig-configurationprofile-tags-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appconfig-configurationprofile-tags-syntax.yaml"></a>

```
  [Key](#cfn-appconfig-configurationprofile-tags-key): {{String}}
  [Value](#cfn-appconfig-configurationprofile-tags-value): {{String}}
```

## Properties
<a name="aws-properties-appconfig-configurationprofile-tags-properties"></a>

`Key`  <a name="cfn-appconfig-configurationprofile-tags-key"></a>
The key-value string map. The valid character set is `[a-zA-Z+-=._:/]`. The tag key can be up to 128 characters and must not start with `aws:`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appconfig-configurationprofile-tags-value"></a>
The tag value can be up to 256 characters.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
