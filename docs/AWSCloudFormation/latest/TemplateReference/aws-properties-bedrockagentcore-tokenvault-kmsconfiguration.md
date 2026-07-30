---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-tokenvault-kmsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::TokenVault KmsConfiguration
<a name="aws-properties-bedrockagentcore-tokenvault-kmsconfiguration"></a>

Contains the KMS configuration for a resource.

## Syntax
<a name="aws-properties-bedrockagentcore-tokenvault-kmsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-tokenvault-kmsconfiguration-syntax.json"></a>

```
{
  "[KeyType](#cfn-bedrockagentcore-tokenvault-kmsconfiguration-keytype)" : {{String}},
  "[KmsKeyArn](#cfn-bedrockagentcore-tokenvault-kmsconfiguration-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-tokenvault-kmsconfiguration-syntax.yaml"></a>

```
  [KeyType](#cfn-bedrockagentcore-tokenvault-kmsconfiguration-keytype): {{String}}
  [KmsKeyArn](#cfn-bedrockagentcore-tokenvault-kmsconfiguration-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-tokenvault-kmsconfiguration-properties"></a>

`KeyType`  <a name="cfn-bedrockagentcore-tokenvault-kmsconfiguration-keytype"></a>
The type of KMS key (CustomerManagedKey or ServiceManagedKey).
*Required*: Yes
*Type*: String
*Allowed values*: `CustomerManagedKey | ServiceManagedKey`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-bedrockagentcore-tokenvault-kmsconfiguration-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
