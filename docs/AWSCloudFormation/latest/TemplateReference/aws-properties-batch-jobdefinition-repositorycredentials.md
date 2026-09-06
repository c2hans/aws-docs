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
