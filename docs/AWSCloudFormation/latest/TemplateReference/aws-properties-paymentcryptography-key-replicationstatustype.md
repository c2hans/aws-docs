---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-paymentcryptography-key-replicationstatustype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PaymentCryptography::Key ReplicationStatusType
<a name="aws-properties-paymentcryptography-key-replicationstatustype"></a>

Represents the replication status information for a key in a replication region for [Multi-Region key replication](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html).

This structure contains details about the current state of key replication, including any status messages and operational information about the replication process.

## Syntax
<a name="aws-properties-paymentcryptography-key-replicationstatustype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-paymentcryptography-key-replicationstatustype-syntax.json"></a>

```
{
  "[Status](#cfn-paymentcryptography-key-replicationstatustype-status)" : {{String}},
  "[StatusMessage](#cfn-paymentcryptography-key-replicationstatustype-statusmessage)" : {{String}}
}
```

### YAML
<a name="aws-properties-paymentcryptography-key-replicationstatustype-syntax.yaml"></a>

```
  [Status](#cfn-paymentcryptography-key-replicationstatustype-status): {{String}}
  [StatusMessage](#cfn-paymentcryptography-key-replicationstatustype-statusmessage): {{String}}
```

## Properties
<a name="aws-properties-paymentcryptography-key-replicationstatustype-properties"></a>

`Status`  <a name="cfn-paymentcryptography-key-replicationstatustype-status"></a>
The current status of key replication in this AWS Region.
This field indicates whether the key replication is in progress, completed successfully, or has encountered an error. Possible values include states such as `SYNCRHONIZED`, `IN_PROGRESS`, `DELETE_IN_PROGRESS`, or `FAILED`. This provides visibility into the replication process for monitoring and troubleshooting purposes.
*Required*: Yes
*Type*: String
*Allowed values*: `IN_PROGRESS | DELETE_IN_PROGRESS | FAILED | SYNCHRONIZED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusMessage`  <a name="cfn-paymentcryptography-key-replicationstatustype-statusmessage"></a>
A message that provides additional information about the current replication status of the key.
This field contains details about any issues or progress updates related to key replication operations. It may include information about replication failures, synchronization status, or other operational details.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
