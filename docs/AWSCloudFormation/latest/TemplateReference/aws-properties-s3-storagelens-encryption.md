---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-storagelens-encryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::StorageLens Encryption
<a name="aws-properties-s3-storagelens-encryption"></a>

This resource contains the type of server-side encryption used to encrypt an Amazon S3 Storage Lens metrics export. For valid values, see the [ StorageLensDataExportEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensDataExportEncryption.html) in the *Amazon S3 API Reference*.

## Syntax
<a name="aws-properties-s3-storagelens-encryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-storagelens-encryption-syntax.json"></a>

```
{
  "[SSEKMS](#cfn-s3-storagelens-encryption-ssekms)" : {{SSEKMS}},
  "[SSES3](#cfn-s3-storagelens-encryption-sses3)" : {{Json}}
}
```

### YAML
<a name="aws-properties-s3-storagelens-encryption-syntax.yaml"></a>

```
  [SSEKMS](#cfn-s3-storagelens-encryption-ssekms): {{
    SSEKMS}}
  [SSES3](#cfn-s3-storagelens-encryption-sses3): {{Json}}
```

## Properties
<a name="aws-properties-s3-storagelens-encryption-properties"></a>

`SSEKMS`  <a name="cfn-s3-storagelens-encryption-ssekms"></a>
Specifies the use of AWS Key Management Service keys (SSE-KMS) to encrypt the S3 Storage Lens metrics export file.
*Required*: No
*Type*: [SSEKMS](aws-properties-s3-storagelens-ssekms.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SSES3`  <a name="cfn-s3-storagelens-encryption-sses3"></a>
Specifies the use of an Amazon S3-managed key (SSE-S3) to encrypt the S3 Storage Lens metrics export file.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
