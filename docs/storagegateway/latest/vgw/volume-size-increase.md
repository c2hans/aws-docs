---
source_url: https://docs.aws.amazon.com/storagegateway/latest/vgw/volume-size-increase.html
---

# Adding and expanding volumes
<a name="volume-size-increase"></a>

As your application needs grow, you might need to add more volumes to your gateway, or expand the size of existing volumes. When you add or expand volumes, you must consider the size of the cache storage and upload buffer you allocated to the gateway. The gateway must have sufficient buffer and cache space for new volumes. For more information, see [Determining the size of upload buffer to allocate](decide-local-disks-and-sizes.md#CachedLocalDiskUploadBufferSizing-common).

You can add volumes using the Storage Gateway console or Storage Gateway API. For instructions on how to add a volume using the Storage Gateway console, see [Creating a storage volume](GettingStartedCreateVolumes.md). For information about using the Storage Gateway API to add volumes, see [CreateCachediSCSIVolume](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateCachediSCSIVolume.html).

You can expand the size of existing volumes using either of the following methods:
+ Create a snapshot of the volume you want to expand and then use the snapshot to create a new volume of a larger size. For information about how to create a snapshot, see [Creating a recovery snapshot](snapshot.md). For information about how to use a snapshot to create a new volume, see [Creating a storage volume](GettingStartedCreateVolumes.md).
+ Use the cached volume you want to expand to clone a new volume of a larger size. For information about how to clone a volume, see [Cloning a cached volume from a recovery point](clone-volume.md). For information about how to create a volume, see [Creating a storage volume](GettingStartedCreateVolumes.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
