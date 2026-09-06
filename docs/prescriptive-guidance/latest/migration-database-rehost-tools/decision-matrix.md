---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-database-rehost-tools/decision-matrix.html
---

# Decision matrix
<a name="decision-matrix"></a>

Although each migration is unique and has its own challenges, limitations, and multiple factors to consider, there are common criteria that you can use to identify the most appropriate migration strategy and service for your use case. Identifying and prioritizing these factors help you narrow down the choice. Use the following table as a decision tree: Start from the most important factor for your use case and choose the best tool for your migration.

**Note**
The following table provides high-level directional factors to consider; it doesn't include an exhaustive list of criteria for a migration project. The purpose is to provide a generalized comparison of two vastly different data migration methods: block-level replication (provided by MGN) compared with logical data-level replication (provided by a multitude of native database migration tools). These two methods are applicable in many migration scenarios and can sometimes be used together, but they also have unique advantages that the table highlights.

|  |
| --- |
| Criteria | AWS Transform MGN | Database tools (native tools or AWS DMS) |
| --- |--- |--- |
| Architecture | Physical (block level) | Logical, database engine level |
| Scale | Large-scale migration | Granular; scale limitations |
| Speed vs. complexity | Fast exit scenario; reduced complexity | Slower, more complex approach; requires more planning and testing |
| Timeline | Supports aggressive timeline | Requires additional effort and time |
| Migration type | Lift and shift as is (one to one only) | Replatforming or modernization with decomposition and consolidation options (one to many, many to one) |
| Pre-provisioning | Not required; automatic migration | Database and infrastructure provisioning required |
| Downtime | Downtime required, within RTO of minutes | Near-zero downtime possible but very expensive (through sync/async extended clusters, CDC replication, and similar methods) |
| Data change rate | Might have networking or performance limits | More options available |
| Limitations | Doesn't support most clustered systems;\* supports only x86 platforms\*\* | Native database tools support clustered databases and non-x86 platforms; AWS DMS covers most database engines |

\* The block-level replication method doesn't support network-attached storage (NAS), shared drives such as NFS shares, or CIFS/SMB shares. It supports only block-level storage that's directly attached to the migrated system at the time of migration. (For more information, see the[ MGN FAQ on SAN/NAS support](https://docs.aws.amazon.com/mgn/latest/ug/General-Questions-FAQ.html#SAN-NAS-Support).) This limits the applicability of replication through MGN for most clustered systems, because the majority of clusters rely on shared storage of various implementations. For more information, see *Advantages* and *Disadvantages* in the [Migration with AWS Transform MGN](mgn.md) section earlier in this guide.

\*\* The block-level replication method requires you to install an AWS Replication Agent at the OS level, and that agent supports only x86 platforms that are based on the Windows or Linux operating system (see [Operating systems supported by MGN](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)). Non-x86 platforms are out of scope for this migration method. These include ARM, RISC/CISC systems, PowerPC variations, IBM systems such as pSeries, iSeries, zSeries, and their respective operating systems such as AIX, HP-UX, Solaris, Linux for PowerPC, zLinux on mainframes, and other non-x86 architectures.
