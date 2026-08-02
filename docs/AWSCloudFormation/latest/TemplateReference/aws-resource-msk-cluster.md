---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-msk-cluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster
<a name="aws-resource-msk-cluster"></a>

Creates a new MSK cluster.

## Syntax
<a name="aws-resource-msk-cluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-msk-cluster-syntax.json"></a>

```
{
  "Type" : "AWS::MSK::Cluster",
  "Properties" : {
      "[BrokerNodeGroupInfo](#cfn-msk-cluster-brokernodegroupinfo)" : {{BrokerNodeGroupInfo}},
      "[ClientAuthentication](#cfn-msk-cluster-clientauthentication)" : {{ClientAuthentication}},
      "[ClusterName](#cfn-msk-cluster-clustername)" : {{String}},
      "[ConfigurationInfo](#cfn-msk-cluster-configurationinfo)" : {{ConfigurationInfo}},
      "[EncryptionInfo](#cfn-msk-cluster-encryptioninfo)" : {{EncryptionInfo}},
      "[EnhancedMonitoring](#cfn-msk-cluster-enhancedmonitoring)" : {{String}},
      "[KafkaVersion](#cfn-msk-cluster-kafkaversion)" : {{String}},
      "[LoggingInfo](#cfn-msk-cluster-logginginfo)" : {{LoggingInfo}},
      "[NumberOfBrokerNodes](#cfn-msk-cluster-numberofbrokernodes)" : {{Integer}},
      "[OpenMonitoring](#cfn-msk-cluster-openmonitoring)" : {{OpenMonitoring}},
      "[Rebalancing](#cfn-msk-cluster-rebalancing)" : {{Rebalancing}},
      "[StorageMode](#cfn-msk-cluster-storagemode)" : {{String}},
      "[Tags](#cfn-msk-cluster-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ZookeeperAccess](#cfn-msk-cluster-zookeeperaccess)" : {{ZookeeperAccess}}
    }
}
```

### YAML
<a name="aws-resource-msk-cluster-syntax.yaml"></a>

```
Type: AWS::MSK::Cluster
Properties:
  [BrokerNodeGroupInfo](#cfn-msk-cluster-brokernodegroupinfo): {{
    BrokerNodeGroupInfo}}
  [ClientAuthentication](#cfn-msk-cluster-clientauthentication): {{
    ClientAuthentication}}
  [ClusterName](#cfn-msk-cluster-clustername): {{String}}
  [ConfigurationInfo](#cfn-msk-cluster-configurationinfo): {{
    ConfigurationInfo}}
  [EncryptionInfo](#cfn-msk-cluster-encryptioninfo): {{
    EncryptionInfo}}
  [EnhancedMonitoring](#cfn-msk-cluster-enhancedmonitoring): {{String}}
  [KafkaVersion](#cfn-msk-cluster-kafkaversion): {{String}}
  [LoggingInfo](#cfn-msk-cluster-logginginfo): {{
    LoggingInfo}}
  [NumberOfBrokerNodes](#cfn-msk-cluster-numberofbrokernodes): {{Integer}}
  [OpenMonitoring](#cfn-msk-cluster-openmonitoring): {{
    OpenMonitoring}}
  [Rebalancing](#cfn-msk-cluster-rebalancing): {{
    Rebalancing}}
  [StorageMode](#cfn-msk-cluster-storagemode): {{String}}
  [Tags](#cfn-msk-cluster-tags): {{
    {{Key}}: {{Value}}}}
  [ZookeeperAccess](#cfn-msk-cluster-zookeeperaccess): {{
    ZookeeperAccess}}
```

## Properties
<a name="aws-resource-msk-cluster-properties"></a>

`BrokerNodeGroupInfo`  <a name="cfn-msk-cluster-brokernodegroupinfo"></a>
Information about the broker nodes in the cluster.
*Required*: Yes
*Type*: [BrokerNodeGroupInfo](aws-properties-msk-cluster-brokernodegroupinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientAuthentication`  <a name="cfn-msk-cluster-clientauthentication"></a>
Includes all client authentication related information.
*Required*: No
*Type*: [ClientAuthentication](aws-properties-msk-cluster-clientauthentication.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterName`  <a name="cfn-msk-cluster-clustername"></a>
The name of the cluster.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConfigurationInfo`  <a name="cfn-msk-cluster-configurationinfo"></a>
Represents the configuration that you want MSK to use for the cluster.
*Required*: No
*Type*: [ConfigurationInfo](aws-properties-msk-cluster-configurationinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionInfo`  <a name="cfn-msk-cluster-encryptioninfo"></a>
Includes all encryption-related information.
*Required*: No
*Type*: [EncryptionInfo](aws-properties-msk-cluster-encryptioninfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnhancedMonitoring`  <a name="cfn-msk-cluster-enhancedmonitoring"></a>
Specifies the level of monitoring for the MSK cluster.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | PER_BROKER | PER_TOPIC_PER_BROKER | PER_TOPIC_PER_PARTITION`
*Minimum*: `7`
*Maximum*: `23`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KafkaVersion`  <a name="cfn-msk-cluster-kafkaversion"></a>
The version of Apache Kafka. You can use Amazon MSK to create clusters that use [supported Apache Kafka versions](https://docs.aws.amazon.com/msk/latest/developerguide/supported-kafka-versions.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoggingInfo`  <a name="cfn-msk-cluster-logginginfo"></a>
Logging info details for the cluster.
*Required*: No
*Type*: [LoggingInfo](aws-properties-msk-cluster-logginginfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfBrokerNodes`  <a name="cfn-msk-cluster-numberofbrokernodes"></a>
The number of broker nodes in the cluster.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenMonitoring`  <a name="cfn-msk-cluster-openmonitoring"></a>
The settings for open monitoring.
*Required*: No
*Type*: [OpenMonitoring](aws-properties-msk-cluster-openmonitoring.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rebalancing`  <a name="cfn-msk-cluster-rebalancing"></a>
Property description not available.
*Required*: No
*Type*: [Rebalancing](aws-properties-msk-cluster-rebalancing.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageMode`  <a name="cfn-msk-cluster-storagemode"></a>
This controls storage mode for supported storage tiers.
*Required*: No
*Type*: String
*Allowed values*: `LOCAL | TIERED`
*Minimum*: `5`
*Maximum*: `6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-msk-cluster-tags"></a>
An arbitrary set of tags (key-value pairs) for the cluster.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ZookeeperAccess`  <a name="cfn-msk-cluster-zookeeperaccess"></a>
Property description not available.
*Required*: No
*Type*: [ZookeeperAccess](aws-properties-msk-cluster-zookeeperaccess.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-msk-cluster-return-values"></a>

### Ref
<a name="aws-resource-msk-cluster-return-values-ref"></a>

When you provide the logical ID of this resource to the `Ref` intrinsic function, `Ref` returns the ARN of the created MSK cluster. For example, `arn:aws:kafka:us-east-1:123456789012:cluster/myCluster/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2`.

### Fn::GetAtt
<a name="aws-resource-msk-cluster-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

####
<a name="aws-resource-msk-cluster-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the MSK cluster.

`CurrentVersion`  <a name="CurrentVersion-fn::getatt"></a>
Property description not available.
