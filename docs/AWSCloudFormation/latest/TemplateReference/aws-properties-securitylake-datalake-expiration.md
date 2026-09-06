---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-datalake-expiration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::DataLake Expiration
<a name="aws-properties-securitylake-datalake-expiration"></a>

Provides data expiration details of the Amazon Security Lake object. You can specify your preferred Amazon S3 storage class and the time period for S3 objects to stay in that storage class before they expire. For more information about Amazon S3 Lifecycle configurations, see [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon Simple Storage Service User Guide*.

## Syntax
<a name="aws-properties-securitylake-datalake-expiration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-datalake-expiration-syntax.json"></a>

```
{
  "[Days](#cfn-securitylake-datalake-expiration-days)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-securitylake-datalake-expiration-syntax.yaml"></a>

```
  [Days](#cfn-securitylake-datalake-expiration-days): {{Integer}}
```

## Properties
<a name="aws-properties-securitylake-datalake-expiration-properties"></a>

`Days`  <a name="cfn-securitylake-datalake-expiration-days"></a>
The number of days before data expires in the Amazon Security Lake object.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
