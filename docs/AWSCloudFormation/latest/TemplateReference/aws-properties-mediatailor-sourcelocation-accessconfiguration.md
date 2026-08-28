---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-sourcelocation-accessconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::SourceLocation AccessConfiguration
<a name="aws-properties-mediatailor-sourcelocation-accessconfiguration"></a>

Access configuration parameters.

## Syntax
<a name="aws-properties-mediatailor-sourcelocation-accessconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-sourcelocation-accessconfiguration-syntax.json"></a>

```
{
  "[AccessType](#cfn-mediatailor-sourcelocation-accessconfiguration-accesstype)" : {{String}},
  "[SecretsManagerAccessTokenConfiguration](#cfn-mediatailor-sourcelocation-accessconfiguration-secretsmanageraccesstokenconfiguration)" : {{SecretsManagerAccessTokenConfiguration}}
}
```

### YAML
<a name="aws-properties-mediatailor-sourcelocation-accessconfiguration-syntax.yaml"></a>

```
  [AccessType](#cfn-mediatailor-sourcelocation-accessconfiguration-accesstype): {{String}}
  [SecretsManagerAccessTokenConfiguration](#cfn-mediatailor-sourcelocation-accessconfiguration-secretsmanageraccesstokenconfiguration): {{
    SecretsManagerAccessTokenConfiguration}}
```

## Properties
<a name="aws-properties-mediatailor-sourcelocation-accessconfiguration-properties"></a>

`AccessType`  <a name="cfn-mediatailor-sourcelocation-accessconfiguration-accesstype"></a>
The type of authentication used to access content from `HttpConfiguration::BaseUrl` on your source location. Accepted value: `S3_SIGV4`.
`S3_SIGV4` - AWS Signature Version 4 authentication for Amazon S3 hosted virtual-style access. If your source location base URL is an Amazon S3 bucket, MediaTailor can use AWS Signature Version 4 (SigV4) authentication to access the bucket where your source content is stored. Your MediaTailor source location baseURL must follow the S3 virtual hosted-style request URL format. For example, https://bucket-name.s3.Region.amazonaws.com/key-name.
Before you can use `S3_SIGV4`, you must meet these requirements:
• You must allow MediaTailor to access your S3 bucket by granting mediatailor.amazonaws.com principal access in IAM. For information about configuring access in IAM, see Access management in the IAM User Guide.
• The mediatailor.amazonaws.com service principal must have permissions to read all top level manifests referenced by the VodSource packaging configurations.
• The caller of the API must have s3:GetObject IAM permissions to read all top level manifests referenced by your MediaTailor VodSource packaging configurations.
*Required*: No
*Type*: String
*Allowed values*: `S3_SIGV4 | SECRETS_MANAGER_ACCESS_TOKEN | AUTODETECT_SIGV4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManagerAccessTokenConfiguration`  <a name="cfn-mediatailor-sourcelocation-accessconfiguration-secretsmanageraccesstokenconfiguration"></a>
AWS Secrets Manager access token configuration parameters.
*Required*: No
*Type*: [SecretsManagerAccessTokenConfiguration](aws-properties-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
