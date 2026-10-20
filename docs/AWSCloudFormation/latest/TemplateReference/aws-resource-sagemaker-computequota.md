---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-computequota.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ComputeQuota
<a name="aws-resource-sagemaker-computequota"></a>

Create compute allocation definition. This defines how compute is allocated, shared, and borrowed for specified entities. Specifically, how to lend and borrow idle compute and assign a fair-share weight to the specified entities.

## Syntax
<a name="aws-resource-sagemaker-computequota-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-computequota-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::ComputeQuota",
  "Properties" : {
      "[ActivationState](#cfn-sagemaker-computequota-activationstate)" : {{String}},
      "[ClusterArn](#cfn-sagemaker-computequota-clusterarn)" : {{String}},
      "[ComputeQuotaConfig](#cfn-sagemaker-computequota-computequotaconfig)" : {{ComputeQuotaConfig}},
      "[ComputeQuotaTarget](#cfn-sagemaker-computequota-computequotatarget)" : {{ComputeQuotaTarget}},
      "[Description](#cfn-sagemaker-computequota-description)" : {{String}},
      "[Name](#cfn-sagemaker-computequota-name)" : {{String}},
      "[Tags](#cfn-sagemaker-computequota-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-computequota-syntax.yaml"></a>

```
Type: AWS::SageMaker::ComputeQuota
Properties:
  [ActivationState](#cfn-sagemaker-computequota-activationstate): {{String}}
  [ClusterArn](#cfn-sagemaker-computequota-clusterarn): {{String}}
  [ComputeQuotaConfig](#cfn-sagemaker-computequota-computequotaconfig): {{
    ComputeQuotaConfig}}
  [ComputeQuotaTarget](#cfn-sagemaker-computequota-computequotatarget): {{
    ComputeQuotaTarget}}
  [Description](#cfn-sagemaker-computequota-description): {{String}}
  [Name](#cfn-sagemaker-computequota-name): {{String}}
  [Tags](#cfn-sagemaker-computequota-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-computequota-properties"></a>

`ActivationState`  <a name="cfn-sagemaker-computequota-activationstate"></a>
The state of the compute allocation being described. Use to enable or disable compute allocation.
Default is `Enabled`.
*Required*: No
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterArn`  <a name="cfn-sagemaker-computequota-clusterarn"></a>
ARN of the cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}$`
*Minimum*: `20`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComputeQuotaConfig`  <a name="cfn-sagemaker-computequota-computequotaconfig"></a>
Configuration of the compute allocation definition. This includes the resource sharing option, and the setting to preempt low priority tasks.
*Required*: Yes
*Type*: [ComputeQuotaConfig](aws-properties-sagemaker-computequota-computequotaconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputeQuotaTarget`  <a name="cfn-sagemaker-computequota-computequotatarget"></a>
The target entity to allocate compute resources to.
*Required*: Yes
*Type*: [ComputeQuotaTarget](aws-properties-sagemaker-computequota-computequotatarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-sagemaker-computequota-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-computequota-name"></a>
Name of the compute allocation definition.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-computequota-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-computequota-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-computequota-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-computequota-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-computequota-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-computequota-return-values-fn--getatt-fn--getatt"></a>

`ComputeQuotaArn`  <a name="ComputeQuotaArn-fn::getatt"></a>
ARN of the compute allocation definition.

`ComputeQuotaId`  <a name="ComputeQuotaId-fn::getatt"></a>
ID of the compute allocation definition.

`ComputeQuotaVersion`  <a name="ComputeQuotaVersion-fn::getatt"></a>
Version of the compute allocation definition.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Creation time of the compute allocation definition.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Last modified time of the compute allocation definition.

`Status`  <a name="Status-fn::getatt"></a>
Status of the compute allocation definition.
