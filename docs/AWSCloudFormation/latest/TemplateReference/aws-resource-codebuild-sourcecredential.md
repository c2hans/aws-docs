---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-sourcecredential.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::SourceCredential
<a name="aws-resource-codebuild-sourcecredential"></a>

 Information about the credentials for a GitHub, GitHub Enterprise, or Bitbucket repository. We strongly recommend that you use AWS Secrets Manager to store your credentials. If you use Secrets Manager, you must have secrets in your secrets manager. For more information, see [ Using Dynamic References to Specify Template Values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager).

**Important**
 For security purposes, do not use plain text in your CloudFormation template to store your credentials.

## Syntax
<a name="aws-resource-codebuild-sourcecredential-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codebuild-sourcecredential-syntax.json"></a>

```
{
  "Type" : "AWS::CodeBuild::SourceCredential",
  "Properties" : {
      "[AuthType](#cfn-codebuild-sourcecredential-authtype)" : {{String}},
      "[ServerType](#cfn-codebuild-sourcecredential-servertype)" : {{String}},
      "[Token](#cfn-codebuild-sourcecredential-token)" : {{String}},
      "[Username](#cfn-codebuild-sourcecredential-username)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-codebuild-sourcecredential-syntax.yaml"></a>

```
Type: AWS::CodeBuild::SourceCredential
Properties:
  [AuthType](#cfn-codebuild-sourcecredential-authtype): {{String}}
  [ServerType](#cfn-codebuild-sourcecredential-servertype): {{String}}
  [Token](#cfn-codebuild-sourcecredential-token): {{String}}
  [Username](#cfn-codebuild-sourcecredential-username): {{String}}
```

## Properties
<a name="aws-resource-codebuild-sourcecredential-properties"></a>

`AuthType`  <a name="cfn-codebuild-sourcecredential-authtype"></a>
 The type of authentication used by the credentials. Valid options are OAUTH, BASIC\_AUTH, PERSONAL\_ACCESS\_TOKEN, CODECONNECTIONS, or SECRETS\_MANAGER.
*Required*: Yes
*Type*: String
*Allowed values*: `OAUTH | BASIC_AUTH | PERSONAL_ACCESS_TOKEN | CODECONNECTIONS | SECRETS_MANAGER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerType`  <a name="cfn-codebuild-sourcecredential-servertype"></a>
 The type of source provider. The valid options are GITHUB, GITHUB\_ENTERPRISE, GITLAB, GITLAB\_SELF\_MANAGED, or BITBUCKET.
*Required*: Yes
*Type*: String
*Allowed values*: `GITHUB | BITBUCKET | GITHUB_ENTERPRISE | GITLAB | GITLAB_SELF_MANAGED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Token`  <a name="cfn-codebuild-sourcecredential-token"></a>
 For GitHub or GitHub Enterprise, this is the personal access token. For Bitbucket, this is either the access token or the app password. For the `authType` CODECONNECTIONS, this is the `connectionArn`. For the `authType` SECRETS\_MANAGER, this is the `secretArn`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-codebuild-sourcecredential-username"></a>
 The Bitbucket username when the `authType` is BASIC\_AUTH. This parameter is not valid for other types of source providers or connections.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-resource-codebuild-sourcecredential--examples"></a>

**Topics**
+ [Create Bitbucket source credentials using AWS Secrets Manager](#aws-resource-codebuild-sourcecredential--examples--Create_Bitbucket_source_credentials_using)
+ [Create GitHub Enterprise source credentials using AWS Secrets Manager](#aws-resource-codebuild-sourcecredential--examples--Create_GitHub_Enterprise_source_credentials_using)
+ [Create GitHub source credentials using AWS Secrets Manager](#aws-resource-codebuild-sourcecredential--examples--Create_GitHub_source_credentials_using)
+ [Import source credentials for Bitbucket](#aws-resource-codebuild-sourcecredential--examples--Import_source_credentials_for_Bitbucket)
+ [Import source credentials for Github](#aws-resource-codebuild-sourcecredential--examples--Import_source_credentials_for_Github)

### Create Bitbucket source credentials using AWS Secrets Manager
<a name="aws-resource-codebuild-sourcecredential--examples--Create_Bitbucket_source_credentials_using"></a>

#### YAML
<a name="aws-resource-codebuild-sourcecredential--examples--Create_Bitbucket_source_credentials_using--yaml"></a>

```
CodeBuildSourceCredential:
  Type: 'AWS::CodeBuild::SourceCredential'
  Properties:
    Token: '{{resolve:secretsmanager:bitbucket:SecretString:token}}'
    ServerType: BITBUCKET
    Username: '{{resolve:secretsmanager:bitbucket:SecretString:username}}'
    AuthType: BASIC_AUTH
```

#### JSON
<a name="aws-resource-codebuild-sourcecredential--examples--Create_Bitbucket_source_credentials_using--json"></a>

```
{
   "CodeBuildSourceCredential": {
      "Type": "AWS::CodeBuild::SourceCredential",
      "Properties": {
         "Token": "{{resolve:secretsmanager:bitbucket:SecretString:token}}",
         "ServerType": "BITBUCKET",
         "Username": "{{resolve:secretsmanager:bitbucket:SecretString:username}}",
         "AuthType": "BASIC_AUTH"
      }
   }
}
```

### Create GitHub Enterprise source credentials using AWS Secrets Manager
<a name="aws-resource-codebuild-sourcecredential--examples--Create_GitHub_Enterprise_source_credentials_using"></a>

#### YAML
<a name="aws-resource-codebuild-sourcecredential--examples--Create_GitHub_Enterprise_source_credentials_using--yaml"></a>

```
Resources:
  CodeBuildSourceCredential:
    Type: 'AWS::CodeBuild::SourceCredential'
    Properties:
      Token: '{{resolve:secretsmanager:github_enterprise:SecretString:token}}'
      ServerType: GITHUB_ENTERPRISE
      AuthType: PERSONAL_ACCESS_TOKEN
```

#### JSON
<a name="aws-resource-codebuild-sourcecredential--examples--Create_GitHub_Enterprise_source_credentials_using--json"></a>

```
{
   "Resources": {
      "CodeBuildSourceCredential": {
         "Type": "AWS::CodeBuild::SourceCredential",
         "Properties": {
            "Token": "{{resolve:secretsmanager:github_enterprise:SecretString:token}}",
            "ServerType": "GITHUB_ENTERPRISE",
            "AuthType": "PERSONAL_ACCESS_TOKEN"
         }
      }
   }
}
```

### Create GitHub source credentials using AWS Secrets Manager
<a name="aws-resource-codebuild-sourcecredential--examples--Create_GitHub_source_credentials_using"></a>

#### YAML
<a name="aws-resource-codebuild-sourcecredential--examples--Create_GitHub_source_credentials_using--yaml"></a>

```
Resources:
  CodeBuildSourceCredential:
    Type: 'AWS::CodeBuild::SourceCredential'
    Properties:
      Token: '{{resolve:secretsmanager:github:SecretString:token}}'
      ServerType: GITHUB
      AuthType: PERSONAL_ACCESS_TOKEN
```

#### JSON
<a name="aws-resource-codebuild-sourcecredential--examples--Create_GitHub_source_credentials_using--json"></a>

```
{
   "Resources": {
      "CodeBuildSourceCredential": {
         "Type": "AWS::CodeBuild::SourceCredential",
         "Properties": {
            "Token": "{{resolve:secretsmanager:github:SecretString:token}}",
            "ServerType": "GITHUB",
            "AuthType": "PERSONAL_ACCESS_TOKEN"
         }
      }
   }
}
```

### Import source credentials for Bitbucket
<a name="aws-resource-codebuild-sourcecredential--examples--Import_source_credentials_for_Bitbucket"></a>

#### YAML
<a name="aws-resource-codebuild-sourcecredential--examples--Import_source_credentials_for_Bitbucket--yaml"></a>

```
Resources:
  MySourceCreds:
    Type: 'AWS::CodeBuild::SourceCredential'
    Properties:
      Token: '{{resolve:secretsmanager:bitbucket:SecretString:token}}'
      ServerType: BITBUCKET
      Username: '{{resolve:secretsmanager:bitbucket:SecretString:username}}'
      AuthType: BASIC_AUTH
  MyProject:
    Type: 'AWS::CodeBuild::Project'
    Properties:
      Name: myProjectName
      Description: A description about my project
      ServiceRole: testServiceRoleArn
      Artifacts:
        Type: NO_ARTIFACTS
      Environment:
        Type: LINUX_CONTAINER
        ComputeType: BUILD_GENERAL1_SMALL
        Image: 'aws/codebuild/standard:5.0'
      Source:
        Type: BITBUCKET
        Location: 'your-bitbucket-repo-url'
    DependsOn: MySourceCreds
```

#### JSON
<a name="aws-resource-codebuild-sourcecredential--examples--Import_source_credentials_for_Bitbucket--json"></a>

```
{
    "Resources": {
        "MySourceCreds": {
            "Type": "AWS::CodeBuild::SourceCredential",
            "Properties": {
                "Token": "{{resolve:secretsmanager:bitbucket:SecretString:token}}",
                "ServerType": "BITBUCKET",
                "Username": "{{resolve:secretsmanager:bitbucket:SecretString:username}}",
                "AuthType": "BASIC_AUTH"
            }
        },
        "MyProject": {
            "Type": "AWS::CodeBuild::Project",
            "Properties": {
                "Name": "myProjectName",
                "Description": "A description about my project",
                "ServiceRole": "testServiceRoleAr",
                "Artifacts": {
                    "Type": "NO_ARTIFACTS"
                },
                "Environment": {
                    "Type": "LINUX_CONTAINER",
                    "ComputeType": "BUILD_GENERAL1_SMALL",
                    "Image": "aws/codebuild/standard:5.0"
                },
                "Source": {
                    "Type": "BITBUCKET",
                    "Location": "your-bitbucket-repo-url"
                }
            },
            "DependsOn": "MySourceCreds"
        }
    }
}
```

### Import source credentials for Github
<a name="aws-resource-codebuild-sourcecredential--examples--Import_source_credentials_for_Github"></a>

#### YAML
<a name="aws-resource-codebuild-sourcecredential--examples--Import_source_credentials_for_Github--yaml"></a>

```
Resources:
  MySourceCreds:
    Type: 'AWS::CodeBuild::SourceCredential'
    Properties:
      Token: '{{resolve:secretsmanager:github:SecretString:token}}'
      ServerType: GITHUB
      AuthType: PERSONAL_ACCESS_TOKEN
  MyProject:
    Type: 'AWS::CodeBuild::Project'
    Properties:
      Name: myProjectName
      Description: A description about my project
      ServiceRole: testServiceRoleArn
      Artifacts:
        Type: NO_ARTIFACTS
      Environment:
        Type: LINUX_CONTAINER
        ComputeType: BUILD_GENERAL1_SMALL
        Image: 'aws/codebuild/standard:5.0'
      Source:
        Type: GITHUB
        Location: 'your-github-repo-url'
    DependsOn: MySourceCreds
```

#### JSON
<a name="aws-resource-codebuild-sourcecredential--examples--Import_source_credentials_for_Github--json"></a>

```
{
    "Resources": {
        "MySourceCreds": {
            "Type": "AWS::CodeBuild::SourceCredential",
            "Properties": {
                "Token": "{{resolve:secretsmanager:github:SecretString:token}}",
                "ServerType": "GITHUB",
                "AuthType": "PERSONAL_ACCESS_TOKEN"
            }
        },
        "MyProject": {
            "Type": "AWS::CodeBuild::Project",
            "Properties": {
                "Name": "myProjectName",
                "Description": "A description about my project",
                "ServiceRole": "testServiceRoleArn",
                "Artifacts": {
                    "Type": "NO_ARTIFACTS"
                },
                "Environment": {
                    "Type": "LINUX_CONTAINER",
                    "ComputeType": "BUILD_GENERAL1_SMALL",
                    "Image": "aws/codebuild/standard:5.0"
                },
                "Source": {
                    "Type": "GITHUB",
                    "Location": "your-github-repo-url"
                }
            },
            "DependsOn": "MySourceCreds"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
