---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-containergroupdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerGroupDefinition
<a name="aws-resource-gamelift-containergroupdefinition"></a>

The properties that describe a container group resource. You can update all properties of a container group definition properties. Updates to a container group definition are saved as new versions.

 **Used with:** [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html)

**Returned by:**[DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html), [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html), [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

## Syntax
<a name="aws-resource-gamelift-containergroupdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-gamelift-containergroupdefinition-syntax.json"></a>

```
{
  "Type" : "AWS::GameLift::ContainerGroupDefinition",
  "Properties" : {
      "[ContainerGroupType](#cfn-gamelift-containergroupdefinition-containergrouptype)" : {{String}},
      "[GameServerContainerDefinition](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition)" : {{GameServerContainerDefinition}},
      "[Name](#cfn-gamelift-containergroupdefinition-name)" : {{String}},
      "[OperatingSystem](#cfn-gamelift-containergroupdefinition-operatingsystem)" : {{String}},
      "[SourceVersionNumber](#cfn-gamelift-containergroupdefinition-sourceversionnumber)" : {{Integer}},
      "[SupportContainerDefinitions](#cfn-gamelift-containergroupdefinition-supportcontainerdefinitions)" : {{[ SupportContainerDefinition, ... ]}},
      "[Tags](#cfn-gamelift-containergroupdefinition-tags)" : {{[ Tag, ... ]}},
      "[TotalMemoryLimitMebibytes](#cfn-gamelift-containergroupdefinition-totalmemorylimitmebibytes)" : {{Integer}},
      "[TotalVcpuLimit](#cfn-gamelift-containergroupdefinition-totalvcpulimit)" : {{Number}},
      "[VersionDescription](#cfn-gamelift-containergroupdefinition-versiondescription)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-gamelift-containergroupdefinition-syntax.yaml"></a>

```
Type: AWS::GameLift::ContainerGroupDefinition
Properties:
  [ContainerGroupType](#cfn-gamelift-containergroupdefinition-containergrouptype): {{String}}
  [GameServerContainerDefinition](#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition): {{
    GameServerContainerDefinition}}
  [Name](#cfn-gamelift-containergroupdefinition-name): {{String}}
  [OperatingSystem](#cfn-gamelift-containergroupdefinition-operatingsystem): {{String}}
  [SourceVersionNumber](#cfn-gamelift-containergroupdefinition-sourceversionnumber): {{Integer}}
  [SupportContainerDefinitions](#cfn-gamelift-containergroupdefinition-supportcontainerdefinitions): {{
    - SupportContainerDefinition}}
  [Tags](#cfn-gamelift-containergroupdefinition-tags): {{
    - Tag}}
  [TotalMemoryLimitMebibytes](#cfn-gamelift-containergroupdefinition-totalmemorylimitmebibytes): {{Integer}}
  [TotalVcpuLimit](#cfn-gamelift-containergroupdefinition-totalvcpulimit): {{Number}}
  [VersionDescription](#cfn-gamelift-containergroupdefinition-versiondescription): {{String}}
```

## Properties
<a name="aws-resource-gamelift-containergroupdefinition-properties"></a>

`ContainerGroupType`  <a name="cfn-gamelift-containergroupdefinition-containergrouptype"></a>
The type of container group. Container group type determines how Amazon GameLift Servers deploys the container group on each fleet instance.
*Required*: No
*Type*: String
*Allowed values*: `GAME_SERVER | PER_INSTANCE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GameServerContainerDefinition`  <a name="cfn-gamelift-containergroupdefinition-gameservercontainerdefinition"></a>
The definition for the game server container in this group. This property is used only when the container group type is `GAME_SERVER`. This container definition specifies a container image with the game server build.
*Required*: No
*Type*: [GameServerContainerDefinition](aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-gamelift-containergroupdefinition-name"></a>
A descriptive identifier for the container group definition. The name value is unique in an AWS Region.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OperatingSystem`  <a name="cfn-gamelift-containergroupdefinition-operatingsystem"></a>
The platform that all containers in the container group definition run on.
Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/). For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [ Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)
*Required*: Yes
*Type*: String
*Allowed values*: `AMAZON_LINUX_2023`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceVersionNumber`  <a name="cfn-gamelift-containergroupdefinition-sourceversionnumber"></a>
The container group definition version to update. The new version starts with values from the source version, and then updates values included in this request.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SupportContainerDefinitions`  <a name="cfn-gamelift-containergroupdefinition-supportcontainerdefinitions"></a>
The set of definitions for support containers in this group. A container group definition might have zero support container definitions. Support container can be used in any type of container group.
*Required*: No
*Type*: Array of [SupportContainerDefinition](aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-gamelift-containergroupdefinition-tags"></a>
A list of labels to assign to the container group definition resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*.
*Required*: No
*Type*: Array of [Tag](aws-properties-gamelift-containergroupdefinition-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalMemoryLimitMebibytes`  <a name="cfn-gamelift-containergroupdefinition-totalmemorylimitmebibytes"></a>
The amount of memory (in MiB) on a fleet instance to allocate for the container group. All containers in the group share these resources.
You can set a limit for each container definition in the group. If individual containers have limits, this total value must be greater than any individual container's memory limit.
*Required*: Yes
*Type*: Integer
*Minimum*: `4`
*Maximum*: `1024000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalVcpuLimit`  <a name="cfn-gamelift-containergroupdefinition-totalvcpulimit"></a>
The amount of vCPU units on a fleet instance to allocate for the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share these resources. You can set a limit for each container definition in the group. If individual containers have limits, this total value must be equal to or greater than the sum of the limits for each container in the group.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionDescription`  <a name="cfn-gamelift-containergroupdefinition-versiondescription"></a>
An optional description that was provided for a container group definition update. Each version can have a unique description.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-gamelift-containergroupdefinition-return-values"></a>

### Ref
<a name="aws-resource-gamelift-containergroupdefinition-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-gamelift-containergroupdefinition-return-values-fn--getatt"></a>

####
<a name="aws-resource-gamelift-containergroupdefinition-return-values-fn--getatt-fn--getatt"></a>

`ContainerGroupDefinitionArn`  <a name="ContainerGroupDefinitionArn-fn::getatt"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to an Amazon GameLift Servers `ContainerGroupDefinition` resource. It uniquely identifies the resource across all AWS Regions. Format is `arn:aws:gamelift:[region]::containergroupdefinition/[container group definition name]:[version]`.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).

`Status`  <a name="Status-fn::getatt"></a>
Current status of the container group definition resource. Values include:
+ `COPYING` -- Amazon GameLift Servers is in the process of making copies of all container images that are defined in the group. While in this state, the resource can't be used to create a container fleet.
+ `READY` -- Amazon GameLift Servers has copied the registry images for all containers that are defined in the group. You can use a container group definition in this status to create a container fleet.
+ `FAILED` -- Amazon GameLift Servers failed to create a valid container group definition resource. For more details on the cause of the failure, see `StatusReason`. A container group definition resource in failed status will be deleted within a few minutes.

`StatusReason`  <a name="StatusReason-fn::getatt"></a>
Additional information about a container group definition that's in `FAILED` status. Possible reasons include:
+ An internal issue prevented Amazon GameLift Servers from creating the container group definition resource. Delete the failed resource and call [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html)again.
+ An access-denied message means that you don't have permissions to access the container image on ECR. See [ IAM permission examples](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-iam-policy-examples.html.html) for help setting up required IAM permissions for Amazon GameLift Servers.
+ The `ImageUri` value for at least one of the containers in the container group definition was invalid or not found in the current AWS account.
+ At least one of the container images referenced in the container group definition exceeds the allowed size. For size limits, see [ Amazon GameLift Servers endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/gamelift.html).
+ At least one of the container images referenced in the container group definition uses a different operating system than the one defined for the container group.

`VersionNumber`  <a name="VersionNumber-fn::getatt"></a>
Indicates the version of a particular container group definition. This number is incremented automatically when you update a container group definition. You can view, update, or delete individual versions or the entire container group definition.
