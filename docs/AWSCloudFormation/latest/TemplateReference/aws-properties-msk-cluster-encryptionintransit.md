---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-encryptionintransit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster EncryptionInTransit
<a name="aws-properties-msk-cluster-encryptionintransit"></a>

The settings for encrypting data in transit.

## Syntax
<a name="aws-properties-msk-cluster-encryptionintransit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-encryptionintransit-syntax.json"></a>

```
{
  "[ClientBroker](#cfn-msk-cluster-encryptionintransit-clientbroker)" : {{String}},
  "[InCluster](#cfn-msk-cluster-encryptionintransit-incluster)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-msk-cluster-encryptionintransit-syntax.yaml"></a>

```
  [ClientBroker](#cfn-msk-cluster-encryptionintransit-clientbroker): {{String}}
  [InCluster](#cfn-msk-cluster-encryptionintransit-incluster): {{Boolean}}
```

## Properties
<a name="aws-properties-msk-cluster-encryptionintransit-properties"></a>

`ClientBroker`  <a name="cfn-msk-cluster-encryptionintransit-clientbroker"></a>
Indicates the encryption setting for data in transit between clients and brokers. You must set it to one of the following values.
+ `TLS`: Indicates that client-broker communication is enabled with TLS only.
+ `TLS_PLAINTEXT`: Indicates that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.
+ `PLAINTEXT`: Indicates that client-broker communication is enabled in plaintext only.
The default value is `TLS`.
*Required*: No
*Type*: String
*Allowed values*: `TLS | TLS_PLAINTEXT | PLAINTEXT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InCluster`  <a name="cfn-msk-cluster-encryptionintransit-incluster"></a>
When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.
The default value is true.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
