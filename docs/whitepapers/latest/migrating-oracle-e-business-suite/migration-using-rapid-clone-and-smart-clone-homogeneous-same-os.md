---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/migration-using-rapid-clone-and-smart-clone-homogeneous-same-os.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Oracle E-Business Suite migration using Rapid Clone and Smart Clone (homogeneous - same OS)
<a name="migration-using-rapid-clone-and-smart-clone-homogeneous-same-os"></a>

## Migration using Rapid Clone
<a name="migration-using-rapid-clone"></a>

 If the source and target OS for Oracle E-Business Suite migration are the same platform, you can make use of the Oracle Rapid Clone tool to migrate their database to AWS.

**Note**
Cloning from a later version of an OS to an earlier one is not supported.

 Rapid Clone does not modify the source system. The `adpreclone.pl` script prepares the source system to be cloned by collecting information about the app-tier, database- tier, and by creating generic templates from existing files that contain source-specific hardcoded values.

 After running `adpreclone.pl`, you copy the relevant files and directories from the source system files to the target system, and then run the `adcfgclone.pl` configuration script. The values for various parameters are required to create the context file that will be used to configure the target system. A few of these values are calculated from the current target system, and `adcfgclone.pl `will prompt for the others.

 For migrating Oracle E-Business Suite using Rapid Clone, refer to [Oracle Support Note \#1383621.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=140495988718336&id=1383621.1&_adf.ctrl-state=ss7c2i22z_420) - Cloning Oracle E-Business Suite Release 12.2 with Rapid Clone (sign-in required).

## Migration using Smart Clone
<a name="migration-using-smart-clone"></a>

 Oracle Application Management Pack for Oracle E-Business Suite also provides the ability to clone an Oracle E-Business Suite system automatically using the Oracle Smart Clone procedure. Smart Clone expects, as a prerequisite, the target Oracle E-Business Suite database to be cloned and discovered in the Enterprise Manager. Smart Clone starts with taking the discovered target database as an input to configure a database target and then clones the applications tier of the source instance. It then applies that to the target Oracle E-Business Suite system.

 For more information on the Smart Clone procedure for migrating Oracle E-Business Suite, refer to [Cloning an Oracle E-Business Suite System](https://docs.oracle.com/cd/E24628_01/doc.121/e39873/T508706T512065.htm).

 Whether using Rapid Clone or Smart Clone, you can migrate the data from source to target using either Oracle RMAN, Data Guard, Data Pump, Transportable Tablespaces, or by directly copying the data files from the target database depending on the downtime available.
