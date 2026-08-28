---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-codeartifact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage CodeArtifact
<a name="aws-properties-lambda-microvmimage-codeartifact"></a>

Contains the location of the code artifact for a MicroVM image.

## Syntax
<a name="aws-properties-lambda-microvmimage-codeartifact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-microvmimage-codeartifact-syntax.json"></a>

```
{
  "[Uri](#cfn-lambda-microvmimage-codeartifact-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-microvmimage-codeartifact-syntax.yaml"></a>

```
  [Uri](#cfn-lambda-microvmimage-codeartifact-uri): {{String}}
```

## Properties
<a name="aws-properties-lambda-microvmimage-codeartifact-properties"></a>

`Uri`  <a name="cfn-lambda-microvmimage-codeartifact-uri"></a>
The URI of the code artifact in Amazon S3.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\s]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
