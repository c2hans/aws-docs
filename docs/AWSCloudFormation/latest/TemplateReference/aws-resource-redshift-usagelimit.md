---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-usagelimit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::UsageLimit
<a name="aws-resource-redshift-usagelimit"></a>

Describes a usage limit object for a cluster.

## Syntax
<a name="aws-resource-redshift-usagelimit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshift-usagelimit-syntax.json"></a>

```
{
  "Type" : "AWS::Redshift::UsageLimit",
  "Properties" : {
      "[Amount](#cfn-redshift-usagelimit-amount)" : {{Number}},
      "[BreachAction](#cfn-redshift-usagelimit-breachaction)" : {{String}},
      "[ClusterIdentifier](#cfn-redshift-usagelimit-clusteridentifier)" : {{String}},
      "[FeatureType](#cfn-redshift-usagelimit-featuretype)" : {{String}},
      "[LimitType](#cfn-redshift-usagelimit-limittype)" : {{String}},
      "[Period](#cfn-redshift-usagelimit-period)" : {{String}},
      "[Tags](#cfn-redshift-usagelimit-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-redshift-usagelimit-syntax.yaml"></a>

```
Type: AWS::Redshift::UsageLimit
Properties:
  [Amount](#cfn-redshift-usagelimit-amount): {{Number}}
  [BreachAction](#cfn-redshift-usagelimit-breachaction): {{String}}
  [ClusterIdentifier](#cfn-redshift-usagelimit-clusteridentifier): {{String}}
  [FeatureType](#cfn-redshift-usagelimit-featuretype): {{String}}
  [LimitType](#cfn-redshift-usagelimit-limittype): {{String}}
  [Period](#cfn-redshift-usagelimit-period): {{String}}
  [Tags](#cfn-redshift-usagelimit-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-redshift-usagelimit-properties"></a>

`Amount`  <a name="cfn-redshift-usagelimit-amount"></a>
The limit amount. If time-based, this amount is in minutes. If data-based, this amount is in terabytes (TB).
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BreachAction`  <a name="cfn-redshift-usagelimit-breachaction"></a>
The action that Amazon Redshift takes when the limit is reached. Possible values are:
+ **log** - To log an event in a system table. The default is log.
+ **emit-metric** - To emit CloudWatch metrics.
+ **disable** - To disable the feature until the next usage period begins.
*Required*: No
*Type*: String
*Allowed values*: `log | emit-metric | disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterIdentifier`  <a name="cfn-redshift-usagelimit-clusteridentifier"></a>
The identifier of the cluster with a usage limit.
*Required*: Yes
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FeatureType`  <a name="cfn-redshift-usagelimit-featuretype"></a>
The Amazon Redshift feature to which the limit applies.
*Required*: Yes
*Type*: String
*Allowed values*: `spectrum | concurrency-scaling | cross-region-datasharing | extra-compute-for-automatic-optimization`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LimitType`  <a name="cfn-redshift-usagelimit-limittype"></a>
The type of limit. Depending on the feature type, this can be based on a time duration or data size.
*Required*: Yes
*Type*: String
*Allowed values*: `time | data-scanned`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Period`  <a name="cfn-redshift-usagelimit-period"></a>
The time period that the amount applies to. A `weekly` period begins on Sunday. The default is `monthly`.
*Required*: No
*Type*: String
*Allowed values*: `daily | weekly | monthly`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-redshift-usagelimit-tags"></a>
A list of tag instances.
*Required*: No
*Type*: Array of [Tag](aws-properties-redshift-usagelimit-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-redshift-usagelimit-return-values"></a>

### Ref
<a name="aws-resource-redshift-usagelimit-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-redshift-usagelimit-return-values-fn--getatt"></a>

####
<a name="aws-resource-redshift-usagelimit-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`UsageLimitId`  <a name="UsageLimitId-fn::getatt"></a>
The identifier of the usage limit.
