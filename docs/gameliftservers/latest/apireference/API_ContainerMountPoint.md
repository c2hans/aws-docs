---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ContainerMountPoint.html
---

# ContainerMountPoint
<a name="API_ContainerMountPoint"></a>

A mount point that binds a container to a file or directory on the host system.

 **Part of:** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html), [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html), [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html), [https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

## Contents
<a name="API_ContainerMountPoint_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InstancePath **   <a name="gameliftservers-Type-ContainerMountPoint-InstancePath"></a>
The path to the source file or directory.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\/[\s\S]*$`
Required: Yes

 ** AccessLevel **   <a name="gameliftservers-Type-ContainerMountPoint-AccessLevel"></a>
The type of access for the container.
Type: String
Valid Values: `READ_ONLY | READ_AND_WRITE`
Required: No

 ** ContainerPath **   <a name="gameliftservers-Type-ContainerMountPoint-ContainerPath"></a>
The mount path on the container. If this property isn't set, the instance path is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(\/+[^\/]+\/*)+$`
Required: No

## See Also
<a name="API_ContainerMountPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ContainerMountPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ContainerMountPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ContainerMountPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
