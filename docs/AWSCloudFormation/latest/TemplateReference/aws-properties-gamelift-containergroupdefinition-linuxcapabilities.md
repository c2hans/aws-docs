---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containergroupdefinition-linuxcapabilities.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerGroupDefinition LinuxCapabilities
<a name="aws-properties-gamelift-containergroupdefinition-linuxcapabilities"></a>

A set of Linux capabilities that are added to a container's default Docker configuration for a container defined in the [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html). For more detailed information about these Linux capabilities, see the [capabilities(7)](https://man7.org/linux/man-pages/man7/capabilities.7.html) Linux manual page.

**Modifying capabilities on an existing container:** To remove a capability, update the `Include` list with only the needed capabilities. To revert back to default capabilities, omit `LinuxCapabilities` within the ContainerDefinition.

**Part of: **[GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html), [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html), [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html), [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

**Returned by: **[CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html), [DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html), [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html), [ListContainerGroupDefinitionVersions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitionVersions.html), [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

## Syntax
<a name="aws-properties-gamelift-containergroupdefinition-linuxcapabilities-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containergroupdefinition-linuxcapabilities-syntax.json"></a>

```
{
  "[Include](#cfn-gamelift-containergroupdefinition-linuxcapabilities-include)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-gamelift-containergroupdefinition-linuxcapabilities-syntax.yaml"></a>

```
  [Include](#cfn-gamelift-containergroupdefinition-linuxcapabilities-include): {{
    - String}}
```

## Properties
<a name="aws-properties-gamelift-containergroupdefinition-linuxcapabilities-properties"></a>

`Include`  <a name="cfn-gamelift-containergroupdefinition-linuxcapabilities-include"></a>
The list of Linux capabilities to add to the container's default configuration. Specify each capability as a string from the set of supported capability names (for example, `NET_BIND_SERVICE` or `SYS_PTRACE`).
*Required*: No
*Type*: Array of String
*Allowed values*: `AUDIT_CONTROL | AUDIT_WRITE | BLOCK_SUSPEND | CHOWN | DAC_OVERRIDE | DAC_READ_SEARCH | FOWNER | FSETID | IPC_LOCK | IPC_OWNER | KILL | LEASE | LINUX_IMMUTABLE | MAC_ADMIN | MAC_OVERRIDE | MKNOD | NET_ADMIN | NET_BIND_SERVICE | NET_BROADCAST | NET_RAW | SETFCAP | SETGID | SETPCAP | SETUID | SYS_ADMIN | SYS_BOOT | SYS_CHROOT | SYS_MODULE | SYS_NICE | SYS_PACCT | SYS_PTRACE | SYS_RAWIO | SYS_RESOURCE | SYS_TIME | SYS_TTY_CONFIG | SYSLOG | WAKE_ALARM`
*Minimum*: `0`
*Maximum*: `37`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
