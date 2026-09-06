---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/migrating-for-oracle-e-business-suite-across-operating-systems-same-endian-format.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migrating for Oracle E-Business Suite across operating systems (same endian format)
<a name="migrating-for-oracle-e-business-suite-across-operating-systems-same-endian-format"></a>

 For some customers, it may be the case that source and target platforms are [little endian](https://chortle.ccsu.edu/assemblytutorial/Chapter-15/ass15_03.html), but OSs might be different. For example, RedHat Linux to SUSE Linux. In such cases, cloning utilities such as Rapid Clone and Smart Clone can’t be used. Rather, this would be considered as a "platform" migration. In such scenarios, you can still use the Oracle database tools such as Oracle RMAN, Oracle Data Guard, Oracle Transportable Tablespaces, and so on for migration, but you will need to install a new application tier using the Rapid Install utility and configure it as a target.

 This approach is mentioned in the following Oracle Support Notes (sign-in required):
+  [2048954.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=140369012911143&id=2048954.1&_adf.ctrl-state=ss7c2i22z_249) - Application Tier Platform Migration with Oracle E-Business Suite Release 12.2
+  [2011169.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=140393923515076&id=2011169.1&_adf.ctrl-state=ss7c2i22z_306) - Transportable Databases for Oracle E-Business Suite Release 12.2

 Transportable Database is the fastest way to migrate data between two platforms, because the process is fundamentally one of copying database files and then using Recovery Manager (RMAN) to convert data files (using the RMAN `convert database` command). The E-Business Suite Transportable Databases process for migration does, however, require that the source and target database be of the same release and patchset version.
