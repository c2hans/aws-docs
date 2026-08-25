---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord RegistryRecordIamCredentialProvider
<a name="aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider"></a>

The configuration for an IAM role credential provider that signs requests to a registry record's source with AWS Signature Version 4 (SigV4).

## Syntax
<a name="aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider-syntax.json"></a>

```
{
  "[Region](#cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-region)" : {{String}},
  "[RoleArn](#cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-rolearn)" : {{String}},
  "[Service](#cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-service)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider-syntax.yaml"></a>

```
  [Region](#cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-region): {{String}}
  [RoleArn](#cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-rolearn): {{String}}
  [Service](#cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-service): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider-properties"></a>

`Region`  <a name="cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-region"></a>
The AWS Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role to assume for request signing.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Service`  <a name="cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-service"></a>
The service name to use for request signing, such as `execute-api`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
