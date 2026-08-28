---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Tmpfs.html
---

# Tmpfs
<a name="API_Tmpfs"></a>

The container path, mount options, and size of the tmpfs mount.

## Contents
<a name="API_Tmpfs_Contents"></a>

 ** containerPath **   <a name="ECS-Type-Tmpfs-containerPath"></a>
The absolute file path where the tmpfs volume is to be mounted.
Type: String
Required: Yes

 ** size **   <a name="ECS-Type-Tmpfs-size"></a>
The maximum size (in MiB) of the tmpfs volume.
Type: Integer
Required: Yes

 ** mountOptions **   <a name="ECS-Type-Tmpfs-mountOptions"></a>
The list of tmpfs volume mount options.
Valid values: `"defaults" | "ro" | "rw" | "suid" | "nosuid" | "dev" | "nodev" | "exec" | "noexec" | "sync" | "async" | "dirsync" | "remount" | "mand" | "nomand" | "atime" | "noatime" | "diratime" | "nodiratime" | "bind" | "rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime" | "norelatime" | "strictatime" | "nostrictatime" | "mode" | "uid" | "gid" | "nr_inodes" | "nr_blocks" | "mpol"`
Type: Array of strings
Required: No

## See Also
<a name="API_Tmpfs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Tmpfs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Tmpfs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Tmpfs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
