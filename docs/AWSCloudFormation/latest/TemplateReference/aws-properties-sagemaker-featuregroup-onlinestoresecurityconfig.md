---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-featuregroup-onlinestoresecurityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::FeatureGroup OnlineStoreSecurityConfig
<a name="aws-properties-sagemaker-featuregroup-onlinestoresecurityconfig"></a>

The security configuration for `OnlineStore`.

## Syntax
<a name="aws-properties-sagemaker-featuregroup-onlinestoresecurityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-featuregroup-onlinestoresecurityconfig-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-sagemaker-featuregroup-onlinestoresecurityconfig-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-featuregroup-onlinestoresecurityconfig-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-sagemaker-featuregroup-onlinestoresecurityconfig-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-featuregroup-onlinestoresecurityconfig-properties"></a>

`KmsKeyId`  <a name="cfn-sagemaker-featuregroup-onlinestoresecurityconfig-kmskeyid"></a>
The AWS Key Management Service (KMS) key ARN that SageMaker Feature Store uses to encrypt the Amazon S3 objects at rest using Amazon S3 server-side encryption.
The caller (either user or IAM role) of `CreateFeatureGroup` must have below permissions to the `OnlineStore``KmsKeyId`:
+  `"kms:Encrypt"`
+  `"kms:Decrypt"`
+  `"kms:DescribeKey"`
+  `"kms:CreateGrant"`
+  `"kms:RetireGrant"`
+  `"kms:ReEncryptFrom"`
+  `"kms:ReEncryptTo"`
+  `"kms:GenerateDataKey"`
+  `"kms:ListAliases"`
+  `"kms:ListGrants"`
+  `"kms:RevokeGrant"`
The caller (either user or IAM role) to all DataPlane operations (`PutRecord`, `GetRecord`, `DeleteRecord`) must have the following permissions to the `KmsKeyId`:
+  `"kms:Decrypt"`
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
