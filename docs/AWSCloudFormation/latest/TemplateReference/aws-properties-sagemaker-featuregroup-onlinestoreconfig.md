---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-featuregroup-onlinestoreconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::FeatureGroup OnlineStoreConfig
<a name="aws-properties-sagemaker-featuregroup-onlinestoreconfig"></a>

Use this to specify the AWS Key Management Service (KMS) Key ID, or `KMSKeyId`, for at rest data encryption. You can turn `OnlineStore` on or off by specifying the `EnableOnlineStore` flag at General Assembly.

The default value is `False`.

## Syntax
<a name="aws-properties-sagemaker-featuregroup-onlinestoreconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-featuregroup-onlinestoreconfig-syntax.json"></a>

```
{
  "[EnableOnlineStore](#cfn-sagemaker-featuregroup-onlinestoreconfig-enableonlinestore)" : {{Boolean}},
  "[SecurityConfig](#cfn-sagemaker-featuregroup-onlinestoreconfig-securityconfig)" : {{OnlineStoreSecurityConfig}},
  "[StorageType](#cfn-sagemaker-featuregroup-onlinestoreconfig-storagetype)" : {{String}},
  "[TtlDuration](#cfn-sagemaker-featuregroup-onlinestoreconfig-ttlduration)" : {{TtlDuration}}
}
```

### YAML
<a name="aws-properties-sagemaker-featuregroup-onlinestoreconfig-syntax.yaml"></a>

```
  [EnableOnlineStore](#cfn-sagemaker-featuregroup-onlinestoreconfig-enableonlinestore): {{Boolean}}
  [SecurityConfig](#cfn-sagemaker-featuregroup-onlinestoreconfig-securityconfig): {{
    OnlineStoreSecurityConfig}}
  [StorageType](#cfn-sagemaker-featuregroup-onlinestoreconfig-storagetype): {{String}}
  [TtlDuration](#cfn-sagemaker-featuregroup-onlinestoreconfig-ttlduration): {{
    TtlDuration}}
```

## Properties
<a name="aws-properties-sagemaker-featuregroup-onlinestoreconfig-properties"></a>

`EnableOnlineStore`  <a name="cfn-sagemaker-featuregroup-onlinestoreconfig-enableonlinestore"></a>
Turn `OnlineStore` off by specifying `False` for the `EnableOnlineStore` flag. Turn `OnlineStore` on by specifying `True` for the `EnableOnlineStore` flag.
The default value is `False`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityConfig`  <a name="cfn-sagemaker-featuregroup-onlinestoreconfig-securityconfig"></a>
Use to specify KMS Key ID (`KMSKeyId`) for at-rest encryption of your `OnlineStore`.
*Required*: No
*Type*: [OnlineStoreSecurityConfig](aws-properties-sagemaker-featuregroup-onlinestoresecurityconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageType`  <a name="cfn-sagemaker-featuregroup-onlinestoreconfig-storagetype"></a>
Option for different tiers of low latency storage for real-time data retrieval.
+ `Standard`: A managed low latency data store for feature groups.
+ `InMemory`: A managed data store for feature groups that supports very low latency retrieval.
*Required*: No
*Type*: String
*Allowed values*: `Standard | InMemory`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TtlDuration`  <a name="cfn-sagemaker-featuregroup-onlinestoreconfig-ttlduration"></a>
Time to live duration, where the record is hard deleted after the expiration time is reached; `ExpiresAt` = `EventTime` \+ `TtlDuration`. For information on HardDelete, see the [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html) API in the Amazon SageMaker API Reference guide.
*Required*: No
*Type*: [TtlDuration](aws-properties-sagemaker-featuregroup-ttlduration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
