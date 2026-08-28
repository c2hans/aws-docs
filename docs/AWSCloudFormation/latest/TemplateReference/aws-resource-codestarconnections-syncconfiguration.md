---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codestarconnections-syncconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeStarConnections::SyncConfiguration
<a name="aws-resource-codestarconnections-syncconfiguration"></a>

Information, such as repository, branch, provider, and resource names for a specific sync configuration.

## Syntax
<a name="aws-resource-codestarconnections-syncconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codestarconnections-syncconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::CodeStarConnections::SyncConfiguration",
  "Properties" : {
      "[Branch](#cfn-codestarconnections-syncconfiguration-branch)" : {{String}},
      "[ConfigFile](#cfn-codestarconnections-syncconfiguration-configfile)" : {{String}},
      "[PublishDeploymentStatus](#cfn-codestarconnections-syncconfiguration-publishdeploymentstatus)" : {{String}},
      "[RepositoryLinkId](#cfn-codestarconnections-syncconfiguration-repositorylinkid)" : {{String}},
      "[ResourceName](#cfn-codestarconnections-syncconfiguration-resourcename)" : {{String}},
      "[RoleArn](#cfn-codestarconnections-syncconfiguration-rolearn)" : {{String}},
      "[SyncType](#cfn-codestarconnections-syncconfiguration-synctype)" : {{String}},
      "[TriggerResourceUpdateOn](#cfn-codestarconnections-syncconfiguration-triggerresourceupdateon)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-codestarconnections-syncconfiguration-syntax.yaml"></a>

```
Type: AWS::CodeStarConnections::SyncConfiguration
Properties:
  [Branch](#cfn-codestarconnections-syncconfiguration-branch): {{String}}
  [ConfigFile](#cfn-codestarconnections-syncconfiguration-configfile): {{String}}
  [PublishDeploymentStatus](#cfn-codestarconnections-syncconfiguration-publishdeploymentstatus): {{String}}
  [RepositoryLinkId](#cfn-codestarconnections-syncconfiguration-repositorylinkid): {{String}}
  [ResourceName](#cfn-codestarconnections-syncconfiguration-resourcename): {{String}}
  [RoleArn](#cfn-codestarconnections-syncconfiguration-rolearn): {{String}}
  [SyncType](#cfn-codestarconnections-syncconfiguration-synctype): {{String}}
  [TriggerResourceUpdateOn](#cfn-codestarconnections-syncconfiguration-triggerresourceupdateon): {{String}}
```

## Properties
<a name="aws-resource-codestarconnections-syncconfiguration-properties"></a>

`Branch`  <a name="cfn-codestarconnections-syncconfiguration-branch"></a>
The branch associated with a specific sync configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigFile`  <a name="cfn-codestarconnections-syncconfiguration-configfile"></a>
The file path to the configuration file associated with a specific sync configuration. The path should point to an actual file in the sync configurations linked repository.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublishDeploymentStatus`  <a name="cfn-codestarconnections-syncconfiguration-publishdeploymentstatus"></a>
Whether to enable or disable publishing of deployment status to source providers.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepositoryLinkId`  <a name="cfn-codestarconnections-syncconfiguration-repositorylinkid"></a>
The ID of the repository link associated with a specific sync configuration.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceName`  <a name="cfn-codestarconnections-syncconfiguration-resourcename"></a>
The name of the connection resource associated with a specific sync configuration.
*Required*: Yes
*Type*: String
*Pattern*: `[a-za-z0-9_\.-]+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-codestarconnections-syncconfiguration-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with a specific sync configuration.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws(-[\w]+)*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SyncType`  <a name="cfn-codestarconnections-syncconfiguration-synctype"></a>
The type of sync for a specific sync configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `CFN_STACK_SYNC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TriggerResourceUpdateOn`  <a name="cfn-codestarconnections-syncconfiguration-triggerresourceupdateon"></a>
When to trigger Git sync to begin the stack update.
*Required*: No
*Type*: String
*Allowed values*: `ANY_CHANGE | FILE_CHANGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-codestarconnections-syncconfiguration-return-values"></a>

### Ref
<a name="aws-resource-codestarconnections-syncconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the sync configuration.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-codestarconnections-syncconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-codestarconnections-syncconfiguration-return-values-fn--getatt-fn--getatt"></a>

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The owner ID for the repository associated with a specific sync configuration, such as the owner ID in GitHub.

`ProviderType`  <a name="ProviderType-fn::getatt"></a>
The connection provider type associated with the sync configuration, such as GitHub.

`RepositoryName`  <a name="RepositoryName-fn::getatt"></a>
The name of the repository associated with the sync configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
