---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codestar-githubrepository-code.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeStar::GitHubRepository Code
<a name="aws-properties-codestar-githubrepository-code"></a>

The `Code` property type specifies information about code to be committed.

`Code` is a property of the `AWS::CodeStar::GitHubRepository` resource.

## Syntax
<a name="aws-properties-codestar-githubrepository-code-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codestar-githubrepository-code-syntax.json"></a>

```
{
  "[S3](#cfn-codestar-githubrepository-code-s3)" : {{S3}}
}
```

### YAML
<a name="aws-properties-codestar-githubrepository-code-syntax.yaml"></a>

```
  [S3](#cfn-codestar-githubrepository-code-s3): {{
    S3}}
```

## Properties
<a name="aws-properties-codestar-githubrepository-code-properties"></a>

`S3`  <a name="cfn-codestar-githubrepository-code-s3"></a>
Information about the Amazon S3 bucket that contains a ZIP file of code to be committed to the repository.
*Required*: Yes
*Type*: [S3](aws-properties-codestar-githubrepository-s3.md)
*Update requires*: Updates are not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
