---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-skillmdsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord SkillMdSource
<a name="aws-properties-agentregistry-registryrecord-skillmdsource"></a>

Source configuration for a SkillMd document. Unlike the descriptor sources for other record types, SkillMd does not support credential providers.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-skillmdsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-skillmdsource-syntax.json"></a>

```
{
  "[FromUrl](#cfn-agentregistry-registryrecord-skillmdsource-fromurl)" : {{SkillMdSourceFromUrl}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-skillmdsource-syntax.yaml"></a>

```
  [FromUrl](#cfn-agentregistry-registryrecord-skillmdsource-fromurl): {{
    SkillMdSourceFromUrl}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-skillmdsource-properties"></a>

`FromUrl`  <a name="cfn-agentregistry-registryrecord-skillmdsource-fromurl"></a>
URL-based source for the SkillMd content.
*Required*: No
*Type*: [SkillMdSourceFromUrl](aws-properties-agentregistry-registryrecord-skillmdsourcefromurl.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
