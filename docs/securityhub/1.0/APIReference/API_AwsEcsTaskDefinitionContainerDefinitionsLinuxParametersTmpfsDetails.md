---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails"></a>

The container path, mount options, and size (in MiB) of a tmpfs mount.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails_Contents"></a>

 ** ContainerPath **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails-ContainerPath"></a>
The absolute file path where the tmpfs volume is to be mounted.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MountOptions **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails-MountOptions"></a>
The list of tmpfs volume mount options.
Valid values: `"defaults"` \| `"ro"` \| `"rw"` \| `"suid"` \| `"nosuid"` \| `"dev"` \| `"nodev"` \|` "exec"` \| `"noexec"` \| `"sync"` \| `"async"` \| `"dirsync"` \| `"remount"` \| `"mand"` \| `"nomand"` \| `"atime"` \| `"noatime"` \| `"diratime"` \| `"nodiratime"` \| `"bind"` \| `"rbind"` \| `"unbindable"` \| `"runbindable"` \| `"private"` \| `"rprivate"` \| `"shared"` \| `"rshared"` \| `"slave"` \| `"rslave"` \| `"relatime"` \| `"norelatime"` \| `"strictatime"` \| `"nostrictatime"` \|` "mode"` \| `"uid"` \| `"gid"` \| `"nr_inodes"` \|` "nr_blocks"` \| `"mpol"`
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Size **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails-Size"></a>
The maximum size (in MiB) of the tmpfs volume.
Type: Integer
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
