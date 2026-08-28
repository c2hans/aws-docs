---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/shared-storage-config-ontap-zfs-v3.html
---

# Configure FSx for ONTAP, FSx for OpenZFS, and File Cache shared storage
<a name="shared-storage-config-ontap-zfs-v3"></a>

For FSx for ONTAP, FSx for OpenZFS, and File Cache, you can use [`FsxOntapSettings`](SharedStorage-v3.md#SharedStorage-v3-FsxOntapSettings) / [`VolumeId`](SharedStorage-v3.md#yaml-SharedStorage-FsxOntapSettings-VolumeId), [`FsxOpenZfsSettings`](SharedStorage-v3.md#SharedStorage-v3-FsxOpenZfsSettings) / [`VolumeId`](SharedStorage-v3.md#yaml-SharedStorage-FsxOpenZfsSettings-VolumeId), and [`FileCacheSettings`](SharedStorage-v3.md#SharedStorage-v3-FsxFileCacheSettings) / [`FileCacheId`](SharedStorage-v3.md#yaml-SharedStorage-FsxFileCacheSettings-FileCacheId) to specify mounting an external existing volume or File Cache for your cluster.

AWS ParallelCluster managed shared storage isn't supported for FSx for ONTAP, FSx for OpenZFS, and File Cache.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
