---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_LinuxCapabilities.html
---

# LinuxCapabilities
<a name="API_LinuxCapabilities"></a>

A set of Linux capabilities that are added to a container's default Docker configuration for a container defined in the [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html). For more detailed information about these Linux capabilities, see the [capabilities(7)](https://man7.org/linux/man-pages/man7/capabilities.7.html) Linux manual page.

 **Modifying capabilities on an existing container:** To remove a capability, update the `Include` list with only the needed capabilities. To revert back to default capabilities, omit `LinuxCapabilities` within the ContainerDefinition.

 **Part of: ** [GameServerContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html), [GameServerContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html), [SupportContainerDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html), [SupportContainerDefinitionInput](https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html)

 **Returned by: ** [CreateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html), [DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html), [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html), [ListContainerGroupDefinitionVersions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitionVersions.html), [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html)

## Contents
<a name="API_LinuxCapabilities_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Include **   <a name="gameliftservers-Type-LinuxCapabilities-Include"></a>
The list of Linux capabilities to add to the container's default configuration. Specify each capability as a string from the set of supported capability names (for example, `NET_BIND_SERVICE` or `SYS_PTRACE`).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 37 items.
Valid Values: `AUDIT_CONTROL | AUDIT_WRITE | BLOCK_SUSPEND | CHOWN | DAC_OVERRIDE | DAC_READ_SEARCH | FOWNER | FSETID | IPC_LOCK | IPC_OWNER | KILL | LEASE | LINUX_IMMUTABLE | MAC_ADMIN | MAC_OVERRIDE | MKNOD | NET_ADMIN | NET_BIND_SERVICE | NET_BROADCAST | NET_RAW | SETFCAP | SETGID | SETPCAP | SETUID | SYS_ADMIN | SYS_BOOT | SYS_CHROOT | SYS_MODULE | SYS_NICE | SYS_PACCT | SYS_PTRACE | SYS_RAWIO | SYS_RESOURCE | SYS_TIME | SYS_TTY_CONFIG | SYSLOG | WAKE_ALARM`
Required: No

## See Also
<a name="API_LinuxCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/LinuxCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/LinuxCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/LinuxCapabilities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
