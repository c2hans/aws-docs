---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-repositorycredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition RepositoryCredentials
<a name="aws-properties-batch-jobdefinition-repositorycredentials"></a>

The repository credentials for private registry authentication.

## Syntax
<a name="aws-properties-batch-jobdefinition-repositorycredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-repositorycredentials-syntax.json"></a>

```
{
  "[CredentialsParameter](#cfn-batch-jobdefinition-repositorycredentials-credentialsparameter)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-repositorycredentials-syntax.yaml"></a>

```
  [CredentialsParameter](#cfn-batch-jobdefinition-repositorycredentials-credentialsparameter): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-repositorycredentials-properties"></a>

`CredentialsParameter`  <a name="cfn-batch-jobdefinition-repositorycredentials-credentialsparameter"></a>
The Amazon Resource Name (ARN) of the secret containing the private repository credentials.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
