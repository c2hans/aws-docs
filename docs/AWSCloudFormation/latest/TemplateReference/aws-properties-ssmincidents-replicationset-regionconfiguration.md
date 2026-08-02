---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-replicationset-regionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ReplicationSet RegionConfiguration
<a name="aws-properties-ssmincidents-replicationset-regionconfiguration"></a>

The `RegionConfiguration` property specifies the Region and AWS Key Management Service key to add to the replication set.

## Syntax
<a name="aws-properties-ssmincidents-replicationset-regionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-replicationset-regionconfiguration-syntax.json"></a>

```
{
  "[SseKmsKeyId](#cfn-ssmincidents-replicationset-regionconfiguration-ssekmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmincidents-replicationset-regionconfiguration-syntax.yaml"></a>

```
  [SseKmsKeyId](#cfn-ssmincidents-replicationset-regionconfiguration-ssekmskeyid): {{String}}
```

## Properties
<a name="aws-properties-ssmincidents-replicationset-regionconfiguration-properties"></a>

`SseKmsKeyId`  <a name="cfn-ssmincidents-replicationset-regionconfiguration-ssekmskeyid"></a>
The AWS Key Management Service key ID to use to encrypt your replication set.
*Required*: Yes
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
