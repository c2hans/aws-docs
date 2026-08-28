---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-featuregroup-throughputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::FeatureGroup ThroughputConfig
<a name="aws-properties-sagemaker-featuregroup-throughputconfig"></a>

Used to set feature group throughput configuration. There are two modes: `ON_DEMAND` and `PROVISIONED`. With on-demand mode, you are charged for data reads and writes that your application performs on your feature group. You do not need to specify read and write throughput because Feature Store accommodates your workloads as they ramp up and down. You can switch a feature group to on-demand only once in a 24 hour period. With provisioned throughput mode, you specify the read and write capacity per second that you expect your application to require, and you are billed based on those limits. Exceeding provisioned throughput will result in your requests being throttled.

Note: `PROVISIONED` throughput mode is supported only for feature groups that are offline-only, or use the [`Standard`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OnlineStoreConfig.html#sagemaker-Type-OnlineStoreConfig-StorageType) tier online store.

## Syntax
<a name="aws-properties-sagemaker-featuregroup-throughputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-featuregroup-throughputconfig-syntax.json"></a>

```
{
  "[ProvisionedReadCapacityUnits](#cfn-sagemaker-featuregroup-throughputconfig-provisionedreadcapacityunits)" : {{Integer}},
  "[ProvisionedWriteCapacityUnits](#cfn-sagemaker-featuregroup-throughputconfig-provisionedwritecapacityunits)" : {{Integer}},
  "[ThroughputMode](#cfn-sagemaker-featuregroup-throughputconfig-throughputmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-featuregroup-throughputconfig-syntax.yaml"></a>

```
  [ProvisionedReadCapacityUnits](#cfn-sagemaker-featuregroup-throughputconfig-provisionedreadcapacityunits): {{Integer}}
  [ProvisionedWriteCapacityUnits](#cfn-sagemaker-featuregroup-throughputconfig-provisionedwritecapacityunits): {{Integer}}
  [ThroughputMode](#cfn-sagemaker-featuregroup-throughputconfig-throughputmode): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-featuregroup-throughputconfig-properties"></a>

`ProvisionedReadCapacityUnits`  <a name="cfn-sagemaker-featuregroup-throughputconfig-provisionedreadcapacityunits"></a>
 For provisioned feature groups with online store enabled, this indicates the read throughput you are billed for and can consume without throttling.
This field is not applicable for on-demand feature groups.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProvisionedWriteCapacityUnits`  <a name="cfn-sagemaker-featuregroup-throughputconfig-provisionedwritecapacityunits"></a>
 For provisioned feature groups, this indicates the write throughput you are billed for and can consume without throttling.
This field is not applicable for on-demand feature groups.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThroughputMode`  <a name="cfn-sagemaker-featuregroup-throughputconfig-throughputmode"></a>
The mode used for your feature group throughput: `ON_DEMAND` or `PROVISIONED`.
*Required*: Yes
*Type*: String
*Allowed values*: `OnDemand | Provisioned`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
