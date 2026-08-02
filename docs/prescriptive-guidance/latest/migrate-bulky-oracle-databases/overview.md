---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/overview.html
---

# Overview
<a name="overview"></a>

This is the conceptual process of migrating Oracle databases to AWS using Oracle XTTS and RMAN incremental backups with Snowball, Direct Connect, and FSx for Lustre.

The following diagram shows the high-level migration steps for an Oracle database across different endian formats.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-bulky-oracle-databases/images/guide-img/c09fd9a4-3278-4711-9038-c55dfc694acd/images/91d5f172-1bf7-405e-8c31-b625411c11be.png)

1. Make a full backup of all the tablespaces.

1. Use Snowball to move the backup from the source stage to the target stage.

1. Convert the tablespaces to the target database.

1. Make incremental backups.

1. Use Direct Connect to transfer incremental backups from the source stage to the target stage.

1. Roll forward the incremental backups, converting them and applying them to the target database.

1. Export and import metadata for all tablespaces being transported.

Before cutover, you can minimize downtime by doing the following:
+ Exporting and importing the metadata of nonsegment-based objects, including USER, PACKAGE\_SPEC, PACKAGE\_BODY, PROCEDURE, and FUNCTION
+ Increasing parallelism for full backup and incremental backup
+ Converting data files
+ Rolling forward backups during migration

The Oracle document Reduce Transportable Tablespace Downtime using Cross Platform Incremental Backup ([2471245.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=114983393292188&id=2471245.1)) explains how to use Oracle XTTS with RMAN incremental backups. The document also includes details on requirements and recommendations. The document doesn't describe how to migrate an Oracle database from an on-premises environment to Oracle on AWS or how to parallelize each migration step to minimize downtime.

This guide provides a way to parallelize the phases, minimizing migration downtime in mission-critical system environments with tremendously large data sizes.

Following an initial setup phase, the high-level steps for using Oracle XTTS with RMAN incremental backups include the following phases.

## Phase 1 - Prepare phase
<a name="phase-1---prepare-phase.732c5a49-e92a-5127-9b19-651cc42eb328"></a>

The prepare phase consists of the following steps.

1. An initial full backup (level=0) of the tablespaces is taken on the source database to the source stage, which is NAS storage.

1. The backup copies are transferred using Snowball to the target stage, which is FSx for Lustre integrated with Amazon Simple Storage Service (Amazon S3).

1. Backup tablespaces are restored and converted to the target database with little-endian format.

The steps in this phase are run only once during migration. The data being transported are fully accessible in the source database during this phase.

## Phase 2 - Roll-forward phase
<a name="phase-2---roll-forward-phase.4d84b7d5-878e-5f54-86fd-60fc5a06275f"></a>

The roll-forward phase consists of the following steps.

1. An incremental backup is taken from the source database to the source stage.

1. Incremental backup copies are transferred to the target stage over Direct Connect.

1. Incremental backup copies are converted to the target database with little-endian format. The copies are then applied to the initial target database, which is called the roll-forward step.

You can run this phase multiple times. Each successive incremental backup should take less time and will bring the destination data file copies more current with the source database. As in phase 1, the source data being transported are fully accessible during this phase.

## Phase 3 - Transport phase
<a name="phase-3---transport-phase.6dee653e-a55c-5974-930f-275f4a8f4001"></a>

The third phase includes the following steps.

1. The tablespaces being transported are changed to read only.

1. A final incremental backup is taken from the source database.

1. The metadata is exported.

1. Backups are transferred and applied to the destination.

1. Object metadata is imported.

At this point, the system change number (SCN) of the destination database is consistent with that of source database.

The metadata of transportable tablespaces are exported from the source database and imported into the destination database. The metadata includes information for the user, role, package, procedure, function, table, and index.

Finally, the tablespaces are made read/write for full access on the destination database from application.
