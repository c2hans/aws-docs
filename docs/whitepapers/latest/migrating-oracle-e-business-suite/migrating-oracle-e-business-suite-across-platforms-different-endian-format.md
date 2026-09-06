---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/migrating-oracle-e-business-suite-across-platforms-different-endian-format.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migrating Oracle E-Business Suite across platforms (different Endian format)
<a name="migrating-oracle-e-business-suite-across-platforms-different-endian-format"></a>

For some customers, it might be the case that the source and target platforms have a different endian format.

## Oracle E-Business Suite cross-platform migration using Oracle Transportable Tablespaces
<a name="oracle-e-business-suite-cross-platform-migration-using-oracle-transportable-tablespaces"></a>

### Application tier migration
<a name="application-tier-migration"></a>

 Cross-platform migration of Oracle E-Business Suite application tier is detailed in the Oracle Support Notes that follow.

 Cross-platform migration of Oracle E-Business Suite application tier process (high level):

1.  Prepare source and target systems for migration.

1.  Run `adpreclone.pl` on the source system.

1.  Generate a customer-specific manifest file and upload to the [MyOracleSupport](https://updates.oracle.com/PlatformMigration) website.

1.  Copy `APPL_TOP`, `COMMON_TOP/java`, `COMMON_TOP/webapps`, and so on to the target.

1.  Copy the source context file to the target.

1.  Generate the target context file using the pairs file and source context file on the target.

1.  Run Rapid Install Wizard with `-techstack` option to install technology components.

1.  Run AutoConfig on the target.

1.  Apply customer-specific patches (obtained from the manifest upload procedure).

1.  Review components and technology stack patchset level.

1.  Regenerate file system objects.

1.  Clean nodes.

1.  Run AutoConfig.

1.  Update printer and workflow settings.

1.  Start all services on the target.

 For details, refer to [Oracle Support Note \#2048954.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=140192166583787&parent=DOCUMENT&sourceId=2048954.1&id=2048954.1&_afrWindowMode=0&_adf.ctrl-state=ss7c2i22z_200) (sign-in required).

### Database migration
<a name="database-migration"></a>

 Transportable Tablespaces is an Oracle database feature that provides a faster way to move bulk data from one database to another, independent of the OS of the source and target. The Cross-Platform Transportable Tablespaces (XTTS) provides functionality in distributing data and database migration specifically across platforms of different endian (byte-ordering) formats.

 This migration method is particularly suited for very large databases where the relative size of metadata is small compared to the data.

 Refer to [Oracle Support Note \#2674405.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=138321626582382&parent=DOCUMENT&sourceId=2674405.1&id=2674405.1&_afrWindowMode=0&_adf.ctrl-state=ss7c2i22z_4) - Using Transportable Tablespaces to Migrate Oracle E-Business Suite Release 12.2 Using Oracle Database 19c Enterprise Edition. (sign-in required) This note also contains the procedure to migrate the Application tier.

 You can also perform incremental data transfer using Oracle Transportable Tablespace. For details, refer to [Oracle Support Note \#2471245.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=140140471825954&parent=DOCUMENT&sourceId=2674405.1&id=2471245.1&_afrWindowMode=0&_adf.ctrl-state=ss7c2i22z_151) - Reduce Transportable Tablespace Downtime using Cross-Platform Incremental Backup (sign-in required).

 Incremental backup is supported only for the same platforms, and from big endian platforms to Linux OS only. Following is the typical flow for migration using incremental backups when using XTTS.

![Diagram showing the typical flow for migration using incremental backups using XTTS](http://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/typical-migration-flow-using-xtts.jpg)
