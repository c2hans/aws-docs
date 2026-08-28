---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-encryptionatrest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster EncryptionAtRest
<a name="aws-properties-msk-cluster-encryptionatrest"></a>

The data-volume encryption details. You can't update encryption at rest settings for existing clusters.

## Syntax
<a name="aws-properties-msk-cluster-encryptionatrest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-encryptionatrest-syntax.json"></a>

```
{
  "[DataVolumeKMSKeyId](#cfn-msk-cluster-encryptionatrest-datavolumekmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-cluster-encryptionatrest-syntax.yaml"></a>

```
  [DataVolumeKMSKeyId](#cfn-msk-cluster-encryptionatrest-datavolumekmskeyid): {{String}}
```

## Properties
<a name="aws-properties-msk-cluster-encryptionatrest-properties"></a>

`DataVolumeKMSKeyId`  <a name="cfn-msk-cluster-encryptionatrest-datavolumekmskeyid"></a>
The ARN of the Amazon KMS key for encrypting data at rest. If you don't specify a KMS key, MSK creates one for you and uses it.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
