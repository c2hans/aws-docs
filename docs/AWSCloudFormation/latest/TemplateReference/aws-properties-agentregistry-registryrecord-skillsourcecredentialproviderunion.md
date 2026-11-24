---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderunion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord SkillSourceCredentialProviderUnion

The credential provider details of an agent skills source.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderunion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderunion-syntax.json"></a>

```json
{
  "[IamCredentialProvider](#cfn-agentregistry-registryrecord-skillsourcecredentialproviderunion-iamcredentialprovider)" : {{RegistryRecordIamCredentialProvider}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderunion-syntax.yaml"></a>

```yaml
  [IamCredentialProvider](#cfn-agentregistry-registryrecord-skillsourcecredentialproviderunion-iamcredentialprovider): {{
    RegistryRecordIamCredentialProvider}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-skillsourcecredentialproviderunion-properties"></a>

`IamCredentialProvider`  <a name="cfn-agentregistry-registryrecord-skillsourcecredentialproviderunion-iamcredentialprovider"></a>
The IAM role that the registry assumes to read the source. For an Amazon S3 source, omit `Service` or set it to `s3`, and omit `Region` or set it to the registry's Region.
*Required*: No
*Type*: [RegistryRecordIamCredentialProvider](aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
