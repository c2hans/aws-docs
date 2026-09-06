---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusteraccountingdatabase.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterAccountingDatabase
<a name="aws-properties-sagemaker-cluster-clusteraccountingdatabase"></a>

<a name="aws-properties-sagemaker-cluster-clusteraccountingdatabase-description"></a>The `ClusterAccountingDatabase` property type specifies Property description not available. for an [AWS::SageMaker::Cluster](aws-resource-sagemaker-cluster.md).

## Syntax
<a name="aws-properties-sagemaker-cluster-clusteraccountingdatabase-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusteraccountingdatabase-syntax.json"></a>

```
{
  "[Endpoint](#cfn-sagemaker-cluster-clusteraccountingdatabase-endpoint)" : {{String}},
  "[Name](#cfn-sagemaker-cluster-clusteraccountingdatabase-name)" : {{String}},
  "[Port](#cfn-sagemaker-cluster-clusteraccountingdatabase-port)" : {{Integer}},
  "[SecretArn](#cfn-sagemaker-cluster-clusteraccountingdatabase-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusteraccountingdatabase-syntax.yaml"></a>

```
  [Endpoint](#cfn-sagemaker-cluster-clusteraccountingdatabase-endpoint): {{String}}
  [Name](#cfn-sagemaker-cluster-clusteraccountingdatabase-name): {{String}}
  [Port](#cfn-sagemaker-cluster-clusteraccountingdatabase-port): {{Integer}}
  [SecretArn](#cfn-sagemaker-cluster-clusteraccountingdatabase-secretarn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusteraccountingdatabase-properties"></a>

`Endpoint`  <a name="cfn-sagemaker-cluster-clusteraccountingdatabase-endpoint"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?=.{1,255}$)([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-cluster-clusteraccountingdatabase-name"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9$_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-sagemaker-cluster-clusteraccountingdatabase-port"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-sagemaker-cluster-clusteraccountingdatabase-secretarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
