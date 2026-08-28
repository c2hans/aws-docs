---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-hub-s3storageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Hub S3StorageConfig
<a name="aws-properties-sagemaker-hub-s3storageconfig"></a>

The Amazon Simple Storage (Amazon S3) location and security configuration for `OfflineStore`.

## Syntax
<a name="aws-properties-sagemaker-hub-s3storageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-hub-s3storageconfig-syntax.json"></a>

```
{
  "[S3OutputPath](#cfn-sagemaker-hub-s3storageconfig-s3outputpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-hub-s3storageconfig-syntax.yaml"></a>

```
  [S3OutputPath](#cfn-sagemaker-hub-s3storageconfig-s3outputpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-hub-s3storageconfig-properties"></a>

`S3OutputPath`  <a name="cfn-sagemaker-hub-s3storageconfig-s3outputpath"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
