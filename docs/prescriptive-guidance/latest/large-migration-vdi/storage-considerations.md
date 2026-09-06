---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-vdi/storage-considerations.html
---

# Storage considerations for large VDI migrations
<a name="storage-considerations"></a>

User profiles or virtual hard disk (VHD) files for Citrix user personalization layer (UPL) will require some form of Server Message Block (SMB) file storage, ideally in close proximity to the VDIs. You can use [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) to address this requirement.

Careful capacity planning and performance testing is required when designing an Amazon FSx architecture. The design should cater for peak load, and  we highly recommend running full-scale performance tests.

Splitting UPL and profiles over multiple Amazon FSx file shares is also recommended. This helps you manage the different usage patterns that both solutions have on a file share. You can group multiple file shares into a common namespace by using [Distributed File System (DFS) Namespaces](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/group-file-systems.html).

Depending on your requirements for performance and storage capacity, distributing UPL and profile servers over multiple Amazon FSx file shares might be required.

When designing and testing a storage solution, consider how the application behaves if you lose access to storage. For example, if Amazon FSx fails over to the secondary host due to a reconfiguration, how will the VDI application react to the temporary loss of connectivity? This can disconnect all sessions, and a reconnect storm can add additional heavy load on the system. If possible, the system should be configured to minimize the effects of this behavior.
