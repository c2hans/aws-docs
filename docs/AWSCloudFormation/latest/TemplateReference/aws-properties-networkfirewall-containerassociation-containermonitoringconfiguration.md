---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-containerassociation-containermonitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::ContainerAssociation ContainerMonitoringConfiguration
<a name="aws-properties-networkfirewall-containerassociation-containermonitoringconfiguration"></a>

Contains the monitoring configuration for a single cluster in a container association. Specifies the cluster ARN and optional attribute filters to narrow which containers are tracked.

## Syntax
<a name="aws-properties-networkfirewall-containerassociation-containermonitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-containerassociation-containermonitoringconfiguration-syntax.json"></a>

```
{
  "[AttributeFilters](#cfn-networkfirewall-containerassociation-containermonitoringconfiguration-attributefilters)" : {{[ ContainerAttribute, ... ]}},
  "[ClusterArn](#cfn-networkfirewall-containerassociation-containermonitoringconfiguration-clusterarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-containerassociation-containermonitoringconfiguration-syntax.yaml"></a>

```
  [AttributeFilters](#cfn-networkfirewall-containerassociation-containermonitoringconfiguration-attributefilters): {{
    - ContainerAttribute}}
  [ClusterArn](#cfn-networkfirewall-containerassociation-containermonitoringconfiguration-clusterarn): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-containerassociation-containermonitoringconfiguration-properties"></a>

`AttributeFilters`  <a name="cfn-networkfirewall-containerassociation-containermonitoringconfiguration-attributefilters"></a>
Key-value pairs that filter which containers are tracked. For Amazon EKS, you can filter by namespace and Kubernetes labels. For Amazon ECS, you can filter by container instance attributes (EC2 launch type only).
Attribute values can contain wildcard patterns, for example `payments-*`. Attribute keys must match exactly.
*Required*: No
*Type*: Array of [ContainerAttribute](aws-properties-networkfirewall-containerassociation-containerattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterArn`  <a name="cfn-networkfirewall-containerassociation-containermonitoringconfiguration-clusterarn"></a>
The ARN of the Amazon ECS or Amazon EKS cluster to monitor. The cluster must be in the same Region and account as the container association.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
