---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-skillmdsourcefromurl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord SkillMdSourceFromUrl
<a name="aws-properties-agentregistry-registryrecord-skillmdsourcefromurl"></a>

URL-based source for SkillMd content. Synchronization is skipped; content is provided inline through the descriptor data.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-skillmdsourcefromurl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-skillmdsourcefromurl-syntax.json"></a>

```
{
  "[Url](#cfn-agentregistry-registryrecord-skillmdsourcefromurl-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-skillmdsourcefromurl-syntax.yaml"></a>

```
  [Url](#cfn-agentregistry-registryrecord-skillmdsourcefromurl-url): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-skillmdsourcefromurl-properties"></a>

`Url`  <a name="cfn-agentregistry-registryrecord-skillmdsourcefromurl-url"></a>
The URL source for the SkillMd document.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
