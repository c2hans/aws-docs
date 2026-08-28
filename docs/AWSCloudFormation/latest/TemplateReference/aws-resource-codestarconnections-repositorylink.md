---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codestarconnections-repositorylink.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeStarConnections::RepositoryLink
<a name="aws-resource-codestarconnections-repositorylink"></a>

Information about the repository link resource, such as the repository link ARN, the associated connection ARN, encryption key ARN, and owner ID.

## Syntax
<a name="aws-resource-codestarconnections-repositorylink-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codestarconnections-repositorylink-syntax.json"></a>

```
{
  "Type" : "AWS::CodeStarConnections::RepositoryLink",
  "Properties" : {
      "[ConnectionArn](#cfn-codestarconnections-repositorylink-connectionarn)" : {{String}},
      "[EncryptionKeyArn](#cfn-codestarconnections-repositorylink-encryptionkeyarn)" : {{String}},
      "[OwnerId](#cfn-codestarconnections-repositorylink-ownerid)" : {{String}},
      "[RepositoryName](#cfn-codestarconnections-repositorylink-repositoryname)" : {{String}},
      "[Tags](#cfn-codestarconnections-repositorylink-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-codestarconnections-repositorylink-syntax.yaml"></a>

```
Type: AWS::CodeStarConnections::RepositoryLink
Properties:
  [ConnectionArn](#cfn-codestarconnections-repositorylink-connectionarn): {{String}}
  [EncryptionKeyArn](#cfn-codestarconnections-repositorylink-encryptionkeyarn): {{String}}
  [OwnerId](#cfn-codestarconnections-repositorylink-ownerid): {{String}}
  [RepositoryName](#cfn-codestarconnections-repositorylink-repositoryname): {{String}}
  [Tags](#cfn-codestarconnections-repositorylink-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-codestarconnections-repositorylink-properties"></a>

`ConnectionArn`  <a name="cfn-codestarconnections-repositorylink-connectionarn"></a>
The Amazon Resource Name (ARN) of the connection associated with the repository link.
*Required*: Yes
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn):.+:.+:[0-9]{12}:.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionKeyArn`  <a name="cfn-codestarconnections-repositorylink-encryptionkeyarn"></a>
The Amazon Resource Name (ARN) of the encryption key for the repository associated with the repository link.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn):.+:.+:[0-9]{12}:.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OwnerId`  <a name="cfn-codestarconnections-repositorylink-ownerid"></a>
The owner ID for the repository associated with the repository link, such as the owner ID in GitHub.
*Required*: Yes
*Type*: String
*Pattern*: `[a-za-z0-9_\.-]+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RepositoryName`  <a name="cfn-codestarconnections-repositorylink-repositoryname"></a>
The name of the repository associated with the repository link.
*Required*: Yes
*Type*: String
*Pattern*: `[a-za-z0-9_\.-]+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-codestarconnections-repositorylink-tags"></a>
The tags for the repository to be associated with the repository link.
*Required*: No
*Type*: Array of [Tag](aws-properties-codestarconnections-repositorylink-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-codestarconnections-repositorylink-return-values"></a>

### Ref
<a name="aws-resource-codestarconnections-repositorylink-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the repository link. For example:

 `arn:aws:codestar-connections:region:account-id:repository-link/repository-link-id`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-codestarconnections-repositorylink-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-codestarconnections-repositorylink-return-values-fn--getatt-fn--getatt"></a>

`ProviderType`  <a name="ProviderType-fn::getatt"></a>
The provider type for the connection associated with the repository link, such as GitHub.

`RepositoryLinkArn`  <a name="RepositoryLinkArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the repository link.

`RepositoryLinkId`  <a name="RepositoryLinkId-fn::getatt"></a>
The ID of the repository link.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
