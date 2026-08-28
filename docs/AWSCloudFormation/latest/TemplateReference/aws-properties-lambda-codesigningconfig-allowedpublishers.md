---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-codesigningconfig-allowedpublishers.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::CodeSigningConfig AllowedPublishers
<a name="aws-properties-lambda-codesigningconfig-allowedpublishers"></a>

List of signing profiles that can sign a code package.

## Syntax
<a name="aws-properties-lambda-codesigningconfig-allowedpublishers-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-codesigningconfig-allowedpublishers-syntax.json"></a>

```
{
  "[SigningProfileVersionArns](#cfn-lambda-codesigningconfig-allowedpublishers-signingprofileversionarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-lambda-codesigningconfig-allowedpublishers-syntax.yaml"></a>

```
  [SigningProfileVersionArns](#cfn-lambda-codesigningconfig-allowedpublishers-signingprofileversionarns): {{
    - String}}
```

## Properties
<a name="aws-properties-lambda-codesigningconfig-allowedpublishers-properties"></a>

`SigningProfileVersionArns`  <a name="cfn-lambda-codesigningconfig-allowedpublishers-signingprofileversionarns"></a>
The Amazon Resource Name (ARN) for each of the signing profiles. A signing profile defines a trusted user who can sign a code package.
*Required*: Yes
*Type*: Array of String
*Minimum*: `12 | 1`
*Maximum*: `1024 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
