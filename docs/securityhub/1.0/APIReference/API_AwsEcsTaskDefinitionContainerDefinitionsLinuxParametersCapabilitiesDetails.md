---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails"></a>

The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails_Contents"></a>

 ** Add **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails-Add"></a>
The Linux capabilities for the container that are added to the default configuration provided by Docker. Valid values are as follows:
Valid values: `"ALL"` \| `"AUDIT_CONTROL"` \|` "AUDIT_WRITE"` \| `"BLOCK_SUSPEND"` \| `"CHOWN"` \| `"DAC_OVERRIDE"` \| `"DAC_READ_SEARCH"` \| `"FOWNER"` \| `"FSETID"` \| `"IPC_LOCK"` \| `"IPC_OWNER"` \| `"KILL"` \| `"LEASE"` \| `"LINUX_IMMUTABLE"` \| `"MAC_ADMIN"` \|` "MAC_OVERRIDE"` \| `"MKNOD"` \| `"NET_ADMIN"` \| `"NET_BIND_SERVICE"` \| `"NET_BROADCAST"` \| `"NET_RAW"` \| `"SETFCAP"` \| `"SETGID"` \| `"SETPCAP"` \| `"SETUID"` \| `"SYS_ADMIN"` \| `"SYS_BOOT"` \| `"SYS_CHROOT"` \| `"SYS_MODULE"` \| `"SYS_NICE"` \| `"SYS_PACCT"` \| `"SYS_PTRACE"` \| `"SYS_RAWIO"` \| `"SYS_RESOURCE"` \| `"SYS_TIME"` \| `"SYS_TTY_CONFIG"` \| `"SYSLOG"` \| `"WAKE_ALARM"`
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Drop **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails-Drop"></a>
The Linux capabilities for the container that are dropped from the default configuration provided by Docker.
Valid values: `"ALL"` \| `"AUDIT_CONTROL"` \|` "AUDIT_WRITE"` \| `"BLOCK_SUSPEND"` \| `"CHOWN"` \| `"DAC_OVERRIDE"` \| `"DAC_READ_SEARCH"` \| `"FOWNER"` \| `"FSETID"` \| `"IPC_LOCK"` \| `"IPC_OWNER"` \| `"KILL"` \| `"LEASE"` \| `"LINUX_IMMUTABLE"` \| `"MAC_ADMIN"` \|` "MAC_OVERRIDE"` \| `"MKNOD"` \| `"NET_ADMIN"` \| `"NET_BIND_SERVICE"` \| `"NET_BROADCAST"` \| `"NET_RAW"` \| `"SETFCAP"` \| `"SETGID"` \| `"SETPCAP"` \| `"SETUID"` \| `"SYS_ADMIN"` \| `"SYS_BOOT"` \| `"SYS_CHROOT"` \| `"SYS_MODULE"` \| `"SYS_NICE"` \| `"SYS_PACCT"` \| `"SYS_PTRACE"` \| `"SYS_RAWIO"` \| `"SYS_RESOURCE"` \| `"SYS_TIME"` \| `"SYS_TTY_CONFIG"` \| `"SYSLOG"` \| `"WAKE_ALARM"`
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
