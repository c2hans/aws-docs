---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codestar-githubrepository-s3.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeStar::GitHubRepository S3
<a name="aws-properties-codestar-githubrepository-s3"></a>

The `S3` property type specifies information about the Amazon S3 bucket that contains the code to be committed to the new repository.

`S3` is a property of the `AWS::CodeStar::GitHubRepository` resource.

## Syntax
<a name="aws-properties-codestar-githubrepository-s3-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codestar-githubrepository-s3-syntax.json"></a>

```
{
  "[Bucket](#cfn-codestar-githubrepository-s3-bucket)" : {{String}},
  "[Key](#cfn-codestar-githubrepository-s3-key)" : {{String}},
  "[ObjectVersion](#cfn-codestar-githubrepository-s3-objectversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-codestar-githubrepository-s3-syntax.yaml"></a>

```
  [Bucket](#cfn-codestar-githubrepository-s3-bucket): {{String}}
  [Key](#cfn-codestar-githubrepository-s3-key): {{String}}
  [ObjectVersion](#cfn-codestar-githubrepository-s3-objectversion): {{String}}
```

## Properties
<a name="aws-properties-codestar-githubrepository-s3-properties"></a>

`Bucket`  <a name="cfn-codestar-githubrepository-s3-bucket"></a>
The name of the Amazon S3 bucket that contains the ZIP file with the content to be committed to the new repository.
*Required*: Yes
*Type*: String
*Update requires*: Updates are not supported.

`Key`  <a name="cfn-codestar-githubrepository-s3-key"></a>
The S3 object key or file name for the ZIP file.
*Required*: Yes
*Type*: String
*Update requires*: Updates are not supported.

`ObjectVersion`  <a name="cfn-codestar-githubrepository-s3-objectversion"></a>
The object version of the ZIP file, if versioning is enabled for the Amazon S3 bucket.
*Required*: No
*Type*: String
*Update requires*: Updates are not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
