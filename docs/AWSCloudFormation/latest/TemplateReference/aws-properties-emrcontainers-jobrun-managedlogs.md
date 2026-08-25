---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobrun-managedlogs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobRun ManagedLogs
<a name="aws-properties-emrcontainers-jobrun-managedlogs"></a>

The entity that provides configuration control over managed logs.

## Syntax
<a name="aws-properties-emrcontainers-jobrun-managedlogs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobrun-managedlogs-syntax.json"></a>

```
{
  "[AllowAWSToRetainLogs](#cfn-emrcontainers-jobrun-managedlogs-allowawstoretainlogs)" : {{String}},
  "[EncryptionKeyArn](#cfn-emrcontainers-jobrun-managedlogs-encryptionkeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobrun-managedlogs-syntax.yaml"></a>

```
  [AllowAWSToRetainLogs](#cfn-emrcontainers-jobrun-managedlogs-allowawstoretainlogs): {{String}}
  [EncryptionKeyArn](#cfn-emrcontainers-jobrun-managedlogs-encryptionkeyarn): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-jobrun-managedlogs-properties"></a>

`AllowAWSToRetainLogs`  <a name="cfn-emrcontainers-jobrun-managedlogs-allowawstoretainlogs"></a>
Determines whether AWS can retain logs.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionKeyArn`  <a name="cfn-emrcontainers-jobrun-managedlogs-encryptionkeyarn"></a>
The Amazon resource name (ARN) of the encryption key for logs.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z0-9-]*):kms:.+:(\d{12})?:key\/[(0-9a-zA-Z)-?]+|\$\{[a-zA-Z]\w*\})$`
*Minimum*: `3`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
