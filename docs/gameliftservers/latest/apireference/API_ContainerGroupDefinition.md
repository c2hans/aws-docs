---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ContainerGroupDefinition.html
---

# ContainerGroupDefinition
<a name="API_ContainerGroupDefinition"></a>

The properties that describe a container group resource. You can update all properties of a container group definition properties. Updates to a container group definition are saved as new versions.

 **Used with:** [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html)

 **Returned by:** [DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html), [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html), [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

## Contents
<a name="API_ContainerGroupDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="gameliftservers-Type-ContainerGroupDefinition-Name"></a>
A descriptive identifier for the container group definition. The name value is unique in an AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: Yes

 ** ContainerGroupDefinitionArn **   <a name="gameliftservers-Type-ContainerGroupDefinition-ContainerGroupDefinitionArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to an Amazon GameLift Servers `ContainerGroupDefinition` resource. It uniquely identifies the resource across all AWS Regions. Format is `arn:aws:gamelift:[region]::containergroupdefinition/[container group definition name]:[version]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: No

 ** ContainerGroupType **   <a name="gameliftservers-Type-ContainerGroupDefinition-ContainerGroupType"></a>
The type of container group. Container group type determines how Amazon GameLift Servers deploys the container group on each fleet instance.
Type: String
Valid Values: `GAME_SERVER | PER_INSTANCE`
Required: No

 ** CreationTime **   <a name="gameliftservers-Type-ContainerGroupDefinition-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** GameServerContainerDefinition **   <a name="gameliftservers-Type-ContainerGroupDefinition-GameServerContainerDefinition"></a>
The definition for the game server container in this group. This property is used only when the container group type is `GAME_SERVER`. This container definition specifies a container image with the game server build.
Type: [GameServerContainerDefinition](API_GameServerContainerDefinition.md) object
Required: No

 ** OperatingSystem **   <a name="gameliftservers-Type-ContainerGroupDefinition-OperatingSystem"></a>
The platform that all containers in the container group definition run on.
Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the [Amazon Linux 2 FAQs](http://aws.amazon.com/amazon-linux-2/faqs/). For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [ Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)
Type: String
Valid Values: `AMAZON_LINUX_2023`
Required: No

 ** Status **   <a name="gameliftservers-Type-ContainerGroupDefinition-Status"></a>
Current status of the container group definition resource. Values include:
+  `COPYING` -- Amazon GameLift Servers is in the process of making copies of all container images that are defined in the group. While in this state, the resource can't be used to create a container fleet.
+  `READY` -- Amazon GameLift Servers has copied the registry images for all containers that are defined in the group. You can use a container group definition in this status to create a container fleet.
+  `FAILED` -- Amazon GameLift Servers failed to create a valid container group definition resource. For more details on the cause of the failure, see `StatusReason`. A container group definition resource in failed status will be deleted within a few minutes.
Type: String
Valid Values: `READY | COPYING | FAILED`
Required: No

 ** StatusReason **   <a name="gameliftservers-Type-ContainerGroupDefinition-StatusReason"></a>
Additional information about a container group definition that's in `FAILED` status. Possible reasons include:
+ An internal issue prevented Amazon GameLift Servers from creating the container group definition resource. Delete the failed resource and call [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html)again.
+ An access-denied message means that you don't have permissions to access the container image on ECR. See [ IAM permission examples](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-iam-policy-examples.html.html) for help setting up required IAM permissions for Amazon GameLift Servers.
+ The `ImageUri` value for at least one of the containers in the container group definition was invalid or not found in the current AWS account.
+ At least one of the container images referenced in the container group definition exceeds the allowed size. For size limits, see [ Amazon GameLift Servers endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/gamelift.html).
+ At least one of the container images referenced in the container group definition uses a different operating system than the one defined for the container group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** SupportContainerDefinitions **   <a name="gameliftservers-Type-ContainerGroupDefinition-SupportContainerDefinitions"></a>
The set of definitions for support containers in this group. A container group definition might have zero support container definitions. Support container can be used in any type of container group.
Type: Array of [SupportContainerDefinition](API_SupportContainerDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** TotalMemoryLimitMebibytes **   <a name="gameliftservers-Type-ContainerGroupDefinition-TotalMemoryLimitMebibytes"></a>
The amount of memory (in MiB) on a fleet instance to allocate for the container group. All containers in the group share these resources.
You can set a limit for each container definition in the group. If individual containers have limits, this total value must be greater than any individual container's memory limit.
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 1024000.
Required: No

 ** TotalVcpuLimit **   <a name="gameliftservers-Type-ContainerGroupDefinition-TotalVcpuLimit"></a>
The amount of vCPU units on a fleet instance to allocate for the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share these resources. You can set a limit for each container definition in the group. If individual containers have limits, this total value must be equal to or greater than the sum of the limits for each container in the group.
Type: Double
Valid Range: Minimum value of 0.125. Maximum value of 10.
Required: No

 ** VersionDescription **   <a name="gameliftservers-Type-ContainerGroupDefinition-VersionDescription"></a>
An optional description that was provided for a container group definition update. Each version can have a unique description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** VersionNumber **   <a name="gameliftservers-Type-ContainerGroupDefinition-VersionNumber"></a>
Indicates the version of a particular container group definition. This number is incremented automatically when you update a container group definition. You can view, update, or delete individual versions or the entire container group definition.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ContainerGroupDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ContainerGroupDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ContainerGroupDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ContainerGroupDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
