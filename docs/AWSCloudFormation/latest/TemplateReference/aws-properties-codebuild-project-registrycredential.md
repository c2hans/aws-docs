---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-registrycredential.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Project RegistryCredential
<a name="aws-properties-codebuild-project-registrycredential"></a>

`RegistryCredential` is a property of the [AWS CodeBuild Project Environment ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html) property type that specifies information about credentials that provide access to a private Docker registry. When this is set:
+ `imagePullCredentialsType` must be set to `SERVICE_ROLE`.
+  images cannot be curated or an Amazon ECR image.

 For more information, see [Private Registry with AWS Secrets Manager Sample for AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-private-registry.html).

## Syntax
<a name="aws-properties-codebuild-project-registrycredential-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-project-registrycredential-syntax.json"></a>

```
{
  "[Credential](#cfn-codebuild-project-registrycredential-credential)" : {{String}},
  "[CredentialProvider](#cfn-codebuild-project-registrycredential-credentialprovider)" : {{String}}
}
```

### YAML
<a name="aws-properties-codebuild-project-registrycredential-syntax.yaml"></a>

```
  [Credential](#cfn-codebuild-project-registrycredential-credential): {{String}}
  [CredentialProvider](#cfn-codebuild-project-registrycredential-credentialprovider): {{String}}
```

## Properties
<a name="aws-properties-codebuild-project-registrycredential-properties"></a>

`Credential`  <a name="cfn-codebuild-project-registrycredential-credential"></a>
 The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.
 The `credential` can use the name of the credentials only if they exist in your current AWS Region.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialProvider`  <a name="cfn-codebuild-project-registrycredential-credentialprovider"></a>
 The service that created the credentials to access a private Docker registry. The valid value, SECRETS\_MANAGER, is for AWS Secrets Manager.
*Required*: Yes
*Type*: String
*Allowed values*: `SECRETS_MANAGER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-codebuild-project-registrycredential--seealso"></a>
+ [ RegistryCredential](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_RegistryCredential.html) in the *AWS CodeBuild API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
