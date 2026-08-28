---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspaces-workspacespool.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::WorkspacesPool
<a name="aws-resource-workspaces-workspacespool"></a>

Describes a pool of WorkSpaces.

## Syntax
<a name="aws-resource-workspaces-workspacespool-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspaces-workspacespool-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpaces::WorkspacesPool",
  "Properties" : {
      "[ApplicationSettings](#cfn-workspaces-workspacespool-applicationsettings)" : {{ApplicationSettings}},
      "[BundleId](#cfn-workspaces-workspacespool-bundleid)" : {{String}},
      "[Capacity](#cfn-workspaces-workspacespool-capacity)" : {{Capacity}},
      "[Description](#cfn-workspaces-workspacespool-description)" : {{String}},
      "[DirectoryId](#cfn-workspaces-workspacespool-directoryid)" : {{String}},
      "[PoolName](#cfn-workspaces-workspacespool-poolname)" : {{String}},
      "[RunningMode](#cfn-workspaces-workspacespool-runningmode)" : {{String}},
      "[TimeoutSettings](#cfn-workspaces-workspacespool-timeoutsettings)" : {{TimeoutSettings}}
    }
}
```

### YAML
<a name="aws-resource-workspaces-workspacespool-syntax.yaml"></a>

```
Type: AWS::WorkSpaces::WorkspacesPool
Properties:
  [ApplicationSettings](#cfn-workspaces-workspacespool-applicationsettings): {{
    ApplicationSettings}}
  [BundleId](#cfn-workspaces-workspacespool-bundleid): {{String}}
  [Capacity](#cfn-workspaces-workspacespool-capacity): {{
    Capacity}}
  [Description](#cfn-workspaces-workspacespool-description): {{String}}
  [DirectoryId](#cfn-workspaces-workspacespool-directoryid): {{String}}
  [PoolName](#cfn-workspaces-workspacespool-poolname): {{String}}
  [RunningMode](#cfn-workspaces-workspacespool-runningmode): {{String}}
  [TimeoutSettings](#cfn-workspaces-workspacespool-timeoutsettings): {{
    TimeoutSettings}}
```

## Properties
<a name="aws-resource-workspaces-workspacespool-properties"></a>

`ApplicationSettings`  <a name="cfn-workspaces-workspacespool-applicationsettings"></a>
The persistent application settings for users of the pool.
*Required*: No
*Type*: [ApplicationSettings](aws-properties-workspaces-workspacespool-applicationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BundleId`  <a name="cfn-workspaces-workspacespool-bundleid"></a>
The identifier of the bundle used by the pool.
*Required*: Yes
*Type*: String
*Pattern*: `^wsb-[0-9a-z]{8,63}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Capacity`  <a name="cfn-workspaces-workspacespool-capacity"></a>
Describes the user capacity for the pool.
*Required*: Yes
*Type*: [Capacity](aws-properties-workspaces-workspacespool-capacity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-workspaces-workspacespool-description"></a>
The description of the pool.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_./() -]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DirectoryId`  <a name="cfn-workspaces-workspacespool-directoryid"></a>
The identifier of the directory used by the pool.
*Required*: Yes
*Type*: String
*Pattern*: `^wsd-[0-9a-z]{8,63}$`
*Minimum*: `10`
*Maximum*: `65`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PoolName`  <a name="cfn-workspaces-workspacespool-poolname"></a>
The name of the pool.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RunningMode`  <a name="cfn-workspaces-workspacespool-runningmode"></a>
The running mode of the pool.
*Required*: No
*Type*: String
*Allowed values*: `ALWAYS_ON | AUTO_STOP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutSettings`  <a name="cfn-workspaces-workspacespool-timeoutsettings"></a>
The amount of time that a pool session remains active after users disconnect. If they try to reconnect to the pool session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new pool instance.
*Required*: No
*Type*: [TimeoutSettings](aws-properties-workspaces-workspacespool-timeoutsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-workspaces-workspacespool-return-values"></a>

### Ref
<a name="aws-resource-workspaces-workspacespool-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-workspaces-workspacespool-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-workspaces-workspacespool-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time the pool was created.

`PoolArn`  <a name="PoolArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the pool.

`PoolId`  <a name="PoolId-fn::getatt"></a>
The identifier of the pool.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
