---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-tablebucket-storageclassconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TableBucket StorageClassConfiguration
<a name="aws-properties-s3tables-tablebucket-storageclassconfiguration"></a>

The configuration details for the storage class of tables or table buckets. This allows you to optimize storage costs by selecting the appropriate storage class based on your access patterns and performance requirements.

## Syntax
<a name="aws-properties-s3tables-tablebucket-storageclassconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-tablebucket-storageclassconfiguration-syntax.json"></a>

```
{
  "[StorageClass](#cfn-s3tables-tablebucket-storageclassconfiguration-storageclass)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3tables-tablebucket-storageclassconfiguration-syntax.yaml"></a>

```
  [StorageClass](#cfn-s3tables-tablebucket-storageclassconfiguration-storageclass): {{String}}
```

## Properties
<a name="aws-properties-s3tables-tablebucket-storageclassconfiguration-properties"></a>

`StorageClass`  <a name="cfn-s3tables-tablebucket-storageclassconfiguration-storageclass"></a>
The storage class for the table or table bucket. Valid values include storage classes optimized for different access patterns and cost profiles.
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | INTELLIGENT_TIERING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
