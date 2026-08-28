---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-descriptorsourcefromurl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord DescriptorSourceFromUrl
<a name="aws-properties-agentregistry-registryrecord-descriptorsourcefromurl"></a>

URL-based descriptor source configuration, with credential provider configurations for authenticated URL retrieval.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-descriptorsourcefromurl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-descriptorsourcefromurl-syntax.json"></a>

```
{
  "[CredentialProviderConfigurations](#cfn-agentregistry-registryrecord-descriptorsourcefromurl-credentialproviderconfigurations)" : {{[ RegistryRecordCredentialProviderConfiguration, ... ]}},
  "[Url](#cfn-agentregistry-registryrecord-descriptorsourcefromurl-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-descriptorsourcefromurl-syntax.yaml"></a>

```
  [CredentialProviderConfigurations](#cfn-agentregistry-registryrecord-descriptorsourcefromurl-credentialproviderconfigurations): {{
    - RegistryRecordCredentialProviderConfiguration}}
  [Url](#cfn-agentregistry-registryrecord-descriptorsourcefromurl-url): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-descriptorsourcefromurl-properties"></a>

`CredentialProviderConfigurations`  <a name="cfn-agentregistry-registryrecord-descriptorsourcefromurl-credentialproviderconfigurations"></a>
The credential providers used to authenticate when fetching descriptor content from the source URL.
*Required*: No
*Type*: Array of [RegistryRecordCredentialProviderConfiguration](aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-agentregistry-registryrecord-descriptorsourcefromurl-url"></a>
The URL from which the descriptor content is retrieved.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
