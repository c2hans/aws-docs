---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codestar-githubrepository.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeStar::GitHubRepository
<a name="aws-resource-codestar-githubrepository"></a>

The `AWS::CodeStar::GitHubRepository` resource creates a GitHub repository where users can store source code for use with AWS workflows. You must provide a location for the source code ZIP file in the CloudFormation template, so the code can be uploaded to the created repository. You must have created a personal access token in GitHub to provide in the CloudFormation template. AWS uses this token to connect to GitHub on your behalf.

## Syntax
<a name="aws-resource-codestar-githubrepository-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codestar-githubrepository-syntax.json"></a>

```
{
  "Type" : "AWS::CodeStar::GitHubRepository",
  "Properties" : {
      "[Code](#cfn-codestar-githubrepository-code)" : {{Code}},
      "[ConnectionArn](#cfn-codestar-githubrepository-connectionarn)" : {{String}},
      "[EnableIssues](#cfn-codestar-githubrepository-enableissues)" : {{Boolean}},
      "[IsPrivate](#cfn-codestar-githubrepository-isprivate)" : {{Boolean}},
      "[RepositoryAccessToken](#cfn-codestar-githubrepository-repositoryaccesstoken)" : {{String}},
      "[RepositoryDescription](#cfn-codestar-githubrepository-repositorydescription)" : {{String}},
      "[RepositoryName](#cfn-codestar-githubrepository-repositoryname)" : {{String}},
      "[RepositoryOwner](#cfn-codestar-githubrepository-repositoryowner)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-codestar-githubrepository-syntax.yaml"></a>

```
Type: AWS::CodeStar::GitHubRepository
Properties:
  [Code](#cfn-codestar-githubrepository-code): {{
    Code}}
  [ConnectionArn](#cfn-codestar-githubrepository-connectionarn): {{String}}
  [EnableIssues](#cfn-codestar-githubrepository-enableissues): {{Boolean}}
  [IsPrivate](#cfn-codestar-githubrepository-isprivate): {{Boolean}}
  [RepositoryAccessToken](#cfn-codestar-githubrepository-repositoryaccesstoken): {{String}}
  [RepositoryDescription](#cfn-codestar-githubrepository-repositorydescription): {{String}}
  [RepositoryName](#cfn-codestar-githubrepository-repositoryname): {{String}}
  [RepositoryOwner](#cfn-codestar-githubrepository-repositoryowner): {{String}}
```

## Properties
<a name="aws-resource-codestar-githubrepository-properties"></a>

`Code`  <a name="cfn-codestar-githubrepository-code"></a>
Information about code to be committed to a repository after it is created in an CloudFormation stack.
*Required*: No
*Type*: [Code](aws-properties-codestar-githubrepository-code.md)
*Update requires*: Updates are not supported.

`ConnectionArn`  <a name="cfn-codestar-githubrepository-connectionarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableIssues`  <a name="cfn-codestar-githubrepository-enableissues"></a>
Indicates whether to enable issues for the GitHub repository. You can use GitHub issues to track information and bugs for your repository.
*Required*: No
*Type*: Boolean
*Update requires*: Updates are not supported.

`IsPrivate`  <a name="cfn-codestar-githubrepository-isprivate"></a>
Indicates whether the GitHub repository is a private repository. If so, you choose who can see and commit to this repository.
*Required*: No
*Type*: Boolean
*Update requires*: Updates are not supported.

`RepositoryAccessToken`  <a name="cfn-codestar-githubrepository-repositoryaccesstoken"></a>
The GitHub user's personal access token for the GitHub repository.
*Required*: No
*Type*: String
*Update requires*: Updates are not supported.

`RepositoryDescription`  <a name="cfn-codestar-githubrepository-repositorydescription"></a>
A comment or description about the new repository. This description is displayed in GitHub after the repository is created.
*Required*: No
*Type*: String
*Update requires*: Updates are not supported.

`RepositoryName`  <a name="cfn-codestar-githubrepository-repositoryname"></a>
The name of the repository you want to create in GitHub with CloudFormation stack creation.
*Required*: Yes
*Type*: String
*Update requires*: Updates are not supported.

`RepositoryOwner`  <a name="cfn-codestar-githubrepository-repositoryowner"></a>
The GitHub user name for the owner of the GitHub repository to be created. If this repository should be owned by a GitHub organization, provide its name.
*Required*: Yes
*Type*: String
*Update requires*: Updates are not supported.

## Return values
<a name="aws-resource-codestar-githubrepository-return-values"></a>

### Ref
<a name="aws-resource-codestar-githubrepository-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string combination of the repository owner and the repository name, such as `my-github-account/my-github-repo`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-codestar-githubrepository-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-codestar-githubrepository-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The repository ID.

## Examples
<a name="aws-resource-codestar-githubrepository--examples"></a>

### GitHub Repository Resource Configuration
<a name="aws-resource-codestar-githubrepository--examples--GitHub_Repository_Resource_Configuration"></a>

The following example for the `AWS::CodeStar::GitHubRepository` resource creates a private GitHub repository with issues enabled.

When passing secret parameters, do not enter the value directly into the template. The value is rendered as plain text and is readable. Instead, enter secret parameters using one of the following methods:
+ Pass the value in as a `NoEcho` parameter. For more information, see [Referencing a Parameter in a Template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#parameters-section-structure-referencing).
+ Store the GitHub token in AWS Secrets Manager and [retrieve it](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager) through the resource property. The following example shows the token ID as the parameter stored in AWS Secrets Manager with this value: `resolve:secretsmanager:your-secret-manager-name:SecretString:your-secret-manager-key`.

#### JSON
<a name="aws-resource-codestar-githubrepository--examples--GitHub_Repository_Resource_Configuration--json"></a>

```
{
    "MyRepo": {
        "Type": "AWS::CodeStar::GitHubRepository",
        "Properties": {
            "Code": {
                "S3": {
                    "Bucket": "amzn-s3-demo-bucket",
                    "Key": "sourcecode.zip",
                    "ObjectVersion": "1"
                }
            },
            "EnableIssues": true,
            "IsPrivate": true,
            "RepositoryAccessToken": "{{resolve:secretsmanager:your-secret-manager-name:SecretString:your-secret-manager-key}}",
            "RepositoryDescription": "a description",
            "RepositoryName": "my-github-repo",
            "RepositoryOwner": "my-github-account"
        }
    }
}
```

#### YAML
<a name="aws-resource-codestar-githubrepository--examples--GitHub_Repository_Resource_Configuration--yaml"></a>

```
MyRepo:
  Type: AWS::CodeStar::GitHubRepository
  Properties:
    Code:
      S3:
        Bucket: "amzn-s3-demo-bucket"
        Key: "sourcecode.zip"
        ObjectVersion: "1"
    EnableIssues: true
    IsPrivate: true
    RepositoryAccessToken: '{{resolve:secretsmanager:your-secret-manager-name:SecretString:your-secret-manager-key}}'
    RepositoryDescription: a description
    RepositoryName: my-github-repo
    RepositoryOwner: my-github-account
```
