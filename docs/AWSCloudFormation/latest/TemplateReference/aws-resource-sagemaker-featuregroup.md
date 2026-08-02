---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-featuregroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::FeatureGroup
<a name="aws-resource-sagemaker-featuregroup"></a>

Create a new `FeatureGroup`. A `FeatureGroup` is a group of `Features` defined in the `FeatureStore` to describe a `Record`.

The `FeatureGroup` defines the schema and features contained in the FeatureGroup. A `FeatureGroup` definition is composed of a list of `Features`, a `RecordIdentifierFeatureName`, an `EventTimeFeatureName` and configurations for its `OnlineStore` and `OfflineStore`. Check [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) to see the `FeatureGroup`s quota for your AWS account.

**Important**
You must include at least one of `OnlineStoreConfig` and `OfflineStoreConfig` to create a `FeatureGroup`.

## Syntax
<a name="aws-resource-sagemaker-featuregroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-featuregroup-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::FeatureGroup",
  "Properties" : {
      "[Description](#cfn-sagemaker-featuregroup-description)" : {{String}},
      "[EventTimeFeatureName](#cfn-sagemaker-featuregroup-eventtimefeaturename)" : {{String}},
      "[FeatureDefinitions](#cfn-sagemaker-featuregroup-featuredefinitions)" : {{[ FeatureDefinition, ... ]}},
      "[FeatureGroupName](#cfn-sagemaker-featuregroup-featuregroupname)" : {{String}},
      "[OfflineStoreConfig](#cfn-sagemaker-featuregroup-offlinestoreconfig)" : {{OfflineStoreConfig}},
      "[OnlineStoreConfig](#cfn-sagemaker-featuregroup-onlinestoreconfig)" : {{OnlineStoreConfig}},
      "[RecordIdentifierFeatureName](#cfn-sagemaker-featuregroup-recordidentifierfeaturename)" : {{String}},
      "[RoleArn](#cfn-sagemaker-featuregroup-rolearn)" : {{String}},
      "[Tags](#cfn-sagemaker-featuregroup-tags)" : {{[ Tag, ... ]}},
      "[ThroughputConfig](#cfn-sagemaker-featuregroup-throughputconfig)" : {{ThroughputConfig}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-featuregroup-syntax.yaml"></a>

```
Type: AWS::SageMaker::FeatureGroup
Properties:
  [Description](#cfn-sagemaker-featuregroup-description): {{String}}
  [EventTimeFeatureName](#cfn-sagemaker-featuregroup-eventtimefeaturename): {{String}}
  [FeatureDefinitions](#cfn-sagemaker-featuregroup-featuredefinitions): {{
    - FeatureDefinition}}
  [FeatureGroupName](#cfn-sagemaker-featuregroup-featuregroupname): {{String}}
  [OfflineStoreConfig](#cfn-sagemaker-featuregroup-offlinestoreconfig): {{
    OfflineStoreConfig}}
  [OnlineStoreConfig](#cfn-sagemaker-featuregroup-onlinestoreconfig): {{
    OnlineStoreConfig}}
  [RecordIdentifierFeatureName](#cfn-sagemaker-featuregroup-recordidentifierfeaturename): {{String}}
  [RoleArn](#cfn-sagemaker-featuregroup-rolearn): {{String}}
  [Tags](#cfn-sagemaker-featuregroup-tags): {{
    - Tag}}
  [ThroughputConfig](#cfn-sagemaker-featuregroup-throughputconfig): {{
    ThroughputConfig}}
```

## Properties
<a name="aws-resource-sagemaker-featuregroup-properties"></a>

`Description`  <a name="cfn-sagemaker-featuregroup-description"></a>
A free form description of a `FeatureGroup`.
*Required*: No
*Type*: String
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EventTimeFeatureName`  <a name="cfn-sagemaker-featuregroup-eventtimefeaturename"></a>
The name of the feature that stores the `EventTime` of a Record in a `FeatureGroup`.
A `EventTime` is point in time when a new event occurs that corresponds to the creation or update of a `Record` in `FeatureGroup`. All `Records` in the `FeatureGroup` must have a corresponding `EventTime`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FeatureDefinitions`  <a name="cfn-sagemaker-featuregroup-featuredefinitions"></a>
A list of `Feature`s. Each `Feature` must include a `FeatureName` and a `FeatureType`.
Valid `FeatureType`s are `Integral`, `Fractional` and `String`.
`FeatureName`s cannot be any of the following: `is_deleted`, `write_time`, `api_invocation_time`.
You can create up to 2,500 `FeatureDefinition`s per `FeatureGroup`.
*Required*: Yes
*Type*: Array of [FeatureDefinition](aws-properties-sagemaker-featuregroup-featuredefinition.md)
*Minimum*: `1`
*Maximum*: `2500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FeatureGroupName`  <a name="cfn-sagemaker-featuregroup-featuregroupname"></a>
The name of the `FeatureGroup`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OfflineStoreConfig`  <a name="cfn-sagemaker-featuregroup-offlinestoreconfig"></a>
The configuration of an `OfflineStore`.
*Required*: No
*Type*: [OfflineStoreConfig](aws-properties-sagemaker-featuregroup-offlinestoreconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OnlineStoreConfig`  <a name="cfn-sagemaker-featuregroup-onlinestoreconfig"></a>
The configuration of an `OnlineStore`.
*Required*: No
*Type*: [OnlineStoreConfig](aws-properties-sagemaker-featuregroup-onlinestoreconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordIdentifierFeatureName`  <a name="cfn-sagemaker-featuregroup-recordidentifierfeaturename"></a>
The name of the `Feature` whose value uniquely identifies a `Record` defined in the `FeatureGroup``FeatureDefinitions`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,63}`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-sagemaker-featuregroup-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM execution role used to create the feature group.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-featuregroup-tags"></a>
Tags used to define a `FeatureGroup`.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-featuregroup-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ThroughputConfig`  <a name="cfn-sagemaker-featuregroup-throughputconfig"></a>
Used to set feature group throughput configuration. There are two modes: `ON_DEMAND` and `PROVISIONED`. With on-demand mode, you are charged for data reads and writes that your application performs on your feature group. You do not need to specify read and write throughput because Feature Store accommodates your workloads as they ramp up and down. You can switch a feature group to on-demand only once in a 24 hour period. With provisioned throughput mode, you specify the read and write capacity per second that you expect your application to require, and you are billed based on those limits. Exceeding provisioned throughput will result in your requests being throttled.
Note: `PROVISIONED` throughput mode is supported only for feature groups that are offline-only, or use the [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig-StorageType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig-StorageType) tier online store.
*Required*: No
*Type*: [ThroughputConfig](aws-properties-sagemaker-featuregroup-throughputconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-featuregroup-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-featuregroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `FeatureGroupName` of the feature group.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-featuregroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-featuregroup-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time a `FeatureGroup` was created.

`FeatureGroupStatus`  <a name="FeatureGroupStatus-fn::getatt"></a>
A `FeatureGroup` status.
