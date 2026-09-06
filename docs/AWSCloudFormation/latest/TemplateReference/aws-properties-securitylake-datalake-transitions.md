---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-datalake-transitions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::DataLake Transitions
<a name="aws-properties-securitylake-datalake-transitions"></a>

Provides transition lifecycle details of the Amazon Security Lake object. For more information about Amazon S3 Lifecycle configurations, see [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon Simple Storage Service User Guide*.

## Syntax
<a name="aws-properties-securitylake-datalake-transitions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-datalake-transitions-syntax.json"></a>

```
{
  "[Days](#cfn-securitylake-datalake-transitions-days)" : {{Integer}},
  "[StorageClass](#cfn-securitylake-datalake-transitions-storageclass)" : {{String}}
}
```

### YAML
<a name="aws-properties-securitylake-datalake-transitions-syntax.yaml"></a>

```
  [Days](#cfn-securitylake-datalake-transitions-days): {{Integer}}
  [StorageClass](#cfn-securitylake-datalake-transitions-storageclass): {{String}}
```

## Properties
<a name="aws-properties-securitylake-datalake-transitions-properties"></a>

`Days`  <a name="cfn-securitylake-datalake-transitions-days"></a>
The number of days before data transitions to a different S3 Storage Class in the Amazon Security Lake object.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageClass`  <a name="cfn-securitylake-datalake-transitions-storageclass"></a>
The list of storage classes that you can choose from based on the data access, resiliency, and cost requirements of your workloads. The default storage class is **S3 Standard**. For information about other storage classes, see [Setting the storage class of an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/sc-howtoset.html) in the *Amazon S3 User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
