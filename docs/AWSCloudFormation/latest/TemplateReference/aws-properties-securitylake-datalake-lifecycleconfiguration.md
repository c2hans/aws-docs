---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-datalake-lifecycleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::DataLake LifecycleConfiguration
<a name="aws-properties-securitylake-datalake-lifecycleconfiguration"></a>

Provides lifecycle details of Amazon Security Lake object. To manage your data so that it is stored cost effectively, you can configure retention settings for the data. You can specify your preferred Amazon S3 storage class and the time period for Amazon S3 objects to stay in that storage class before they transition to a different storage class or expire. For more information about Amazon S3 Lifecycle configurations, see [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon Simple Storage Service User Guide*.

In Security Lake, you specify retention settings at the Region level. For example, you might choose to transition all S3 objects in a specific AWS Region to the `S3 Standard-IA` storage class 30 days after they're written to the data lake. The default Amazon S3 storage class is S3 Standard.

**Important**
Security Lake doesn't support Amazon S3 Object Lock. When the data lake buckets are created, S3 Object Lock is disabled by default. Enabling S3 Object Lock with default retention mode interrupts the delivery of normalized log data to the data lake.

## Syntax
<a name="aws-properties-securitylake-datalake-lifecycleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-datalake-lifecycleconfiguration-syntax.json"></a>

```
{
  "[Expiration](#cfn-securitylake-datalake-lifecycleconfiguration-expiration)" : {{Expiration}},
  "[Transitions](#cfn-securitylake-datalake-lifecycleconfiguration-transitions)" : {{[ Transitions, ... ]}}
}
```

### YAML
<a name="aws-properties-securitylake-datalake-lifecycleconfiguration-syntax.yaml"></a>

```
  [Expiration](#cfn-securitylake-datalake-lifecycleconfiguration-expiration): {{
    Expiration}}
  [Transitions](#cfn-securitylake-datalake-lifecycleconfiguration-transitions): {{
    - Transitions}}
```

## Properties
<a name="aws-properties-securitylake-datalake-lifecycleconfiguration-properties"></a>

`Expiration`  <a name="cfn-securitylake-datalake-lifecycleconfiguration-expiration"></a>
Provides data expiration details of the Amazon Security Lake object.
*Required*: No
*Type*: [Expiration](aws-properties-securitylake-datalake-expiration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Transitions`  <a name="cfn-securitylake-datalake-lifecycleconfiguration-transitions"></a>
Provides data storage transition details of Amazon Security Lake object. By configuring these settings, you can specify your preferred Amazon S3 storage class and the time period for S3 objects to stay in that storage class before they transition to a different storage class.
*Required*: No
*Type*: [Array](aws-properties-securitylake-datalake-transitions.md) of [Transitions](aws-properties-securitylake-datalake-transitions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
