---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-replicationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::ReplicationConfig
<a name="aws-resource-dms-replicationconfig"></a>

Creates a configuration that you can later provide to configure and start an AWS DMS Serverless replication. You can also provide options to validate the configuration inputs before you start the replication.

## Syntax
<a name="aws-resource-dms-replicationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dms-replicationconfig-syntax.json"></a>

```
{
  "Type" : "AWS::DMS::ReplicationConfig",
  "Properties" : {
      "[ComputeConfig](#cfn-dms-replicationconfig-computeconfig)" : {{ComputeConfig}},
      "[ReplicationConfigIdentifier](#cfn-dms-replicationconfig-replicationconfigidentifier)" : {{String}},
      "[ReplicationSettings](#cfn-dms-replicationconfig-replicationsettings)" : {{Json}},
      "[ReplicationType](#cfn-dms-replicationconfig-replicationtype)" : {{String}},
      "[ResourceIdentifier](#cfn-dms-replicationconfig-resourceidentifier)" : {{String}},
      "[SourceEndpointArn](#cfn-dms-replicationconfig-sourceendpointarn)" : {{String}},
      "[SupplementalSettings](#cfn-dms-replicationconfig-supplementalsettings)" : {{Json}},
      "[TableMappings](#cfn-dms-replicationconfig-tablemappings)" : {{Json}},
      "[Tags](#cfn-dms-replicationconfig-tags)" : {{[ Tag, ... ]}},
      "[TargetEndpointArn](#cfn-dms-replicationconfig-targetendpointarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-dms-replicationconfig-syntax.yaml"></a>

```
Type: AWS::DMS::ReplicationConfig
Properties:
  [ComputeConfig](#cfn-dms-replicationconfig-computeconfig): {{
    ComputeConfig}}
  [ReplicationConfigIdentifier](#cfn-dms-replicationconfig-replicationconfigidentifier): {{String}}
  [ReplicationSettings](#cfn-dms-replicationconfig-replicationsettings): {{Json}}
  [ReplicationType](#cfn-dms-replicationconfig-replicationtype): {{String}}
  [ResourceIdentifier](#cfn-dms-replicationconfig-resourceidentifier): {{String}}
  [SourceEndpointArn](#cfn-dms-replicationconfig-sourceendpointarn): {{String}}
  [SupplementalSettings](#cfn-dms-replicationconfig-supplementalsettings): {{Json}}
  [TableMappings](#cfn-dms-replicationconfig-tablemappings): {{Json}}
  [Tags](#cfn-dms-replicationconfig-tags): {{
    - Tag}}
  [TargetEndpointArn](#cfn-dms-replicationconfig-targetendpointarn): {{String}}
```

## Properties
<a name="aws-resource-dms-replicationconfig-properties"></a>

`ComputeConfig`  <a name="cfn-dms-replicationconfig-computeconfig"></a>
Configuration parameters for provisioning an AWS DMS Serverless replication.
*Required*: Yes
*Type*: [ComputeConfig](aws-properties-dms-replicationconfig-computeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationConfigIdentifier`  <a name="cfn-dms-replicationconfig-replicationconfigidentifier"></a>
A unique identifier that you want to use to create a `ReplicationConfigArn` that is returned as part of the output from this action. You can then pass this output `ReplicationConfigArn` as the value of the `ReplicationConfigArn` option for other actions to identify both AWS DMS Serverless replications and replication configurations that you want those actions to operate on. For some actions, you can also use either this unique identifier or a corresponding ARN in action filters to identify the specific replication and replication configuration to operate on.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationSettings`  <a name="cfn-dms-replicationconfig-replicationsettings"></a>
Optional JSON settings for AWS DMS Serverless replications that are provisioned using this replication configuration. For example, see [ Change processing tuning settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ChangeProcessingTuning.html).
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationType`  <a name="cfn-dms-replicationconfig-replicationtype"></a>
The type of AWS DMS Serverless replication to provision using this replication configuration.
Possible values:
+  `"full-load"`
+  `"cdc"`
+  `"full-load-and-cdc"`
*Required*: Yes
*Type*: String
*Allowed values*: `full-load | full-load-and-cdc | cdc`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceIdentifier`  <a name="cfn-dms-replicationconfig-resourceidentifier"></a>
Optional unique value or name that you set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource. For more information, see [ Fine-grained access control using resource names and tags](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.FineGrainedAccess).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceEndpointArn`  <a name="cfn-dms-replicationconfig-sourceendpointarn"></a>
The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SupplementalSettings`  <a name="cfn-dms-replicationconfig-supplementalsettings"></a>
Optional JSON settings for specifying supplemental data. For more information, see [ Specifying supplemental data for task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html).
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableMappings`  <a name="cfn-dms-replicationconfig-tablemappings"></a>
JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration. For more information, see [ Specifying table selection and transformations rules using JSON](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.html).
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-dms-replicationconfig-tags"></a>
One or more optional tags associated with resources used by the AWS DMS Serverless replication. For more information, see [ Tagging resources in AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-dms-replicationconfig-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetEndpointArn`  <a name="cfn-dms-replicationconfig-targetendpointarn"></a>
The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS serverless replication configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-dms-replicationconfig-return-values"></a>

### Ref
<a name="aws-resource-dms-replicationconfig-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-dms-replicationconfig-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-dms-replicationconfig-return-values-fn--getatt-fn--getatt"></a>

`ReplicationConfigArn`  <a name="ReplicationConfigArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of this AWS DMS Serverless replication configuration.
