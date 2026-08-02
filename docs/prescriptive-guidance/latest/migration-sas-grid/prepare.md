---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/prepare.html
---

# Prepare – Discovery and assessment
<a name="prepare"></a>

## Prepare current SAS Grid workload assessment
<a name="workload"></a>
+ Goal: Capture the infrastructure requirements for SAS Grid on AWS.
+ Tasks:
  + Gather RHEL performance information by running the [gather\_info.sh script](https://support.sas.com/kb/57/825.html) on every system in the SAS infrastructure.
  + Test throughput for your SAS file systems by running the [rhel\_iotest.sh script](https://support.sas.com/kb/59/680.html).
  + Use the [nmon command](https://support.sas.com/kb/48/290.html) to monitor the performance of SAS on a Linux system.
    + Run **nmon** for several days for an average to above-average workload.
    + Collect data every 5 minutes for 24 hours.
  + Return all logs and files to SAS for analysis.
  + Analyze current utilization patterns and present infrastructure estimate in AWS.
+ Skills/roles: SAS consultant, SAS technical support, SAS Performance Lab

## Prepare SAS security assessment
<a name="security"></a>
+ Goal: Gather requirements to create SAS security design documentation.
+ Tasks:
  + Gather requirements:
    + Define functional security requirements for the SAS environment.
    + Determine whether compliance to an external standard is required.
    + Define user personas such as administrators, analysts, and report viewers.
    + Define organizational hierarchy, and determine how content will be organized and secured.
  + Document SAS security design, including:
    + Metadata authorization model, which defines groups, roles, folders, server metadata, and access control templates.
    + File system security design, which identifies high-level, key SAS directories; the location, ownership, and permissions of those directories; and special files in those directories.
    + SAS security design specification document.
+ Skills/roles: SAS consultant

## Prepare SAS Grid migration assessment
<a name="migration"></a>
+ Goal: Review high-level SAS migration requirements, and use the SAS Migration Utility to analyze your SAS content and validate that it can be migrated successfully.
+ Tasks:
  + Review [high-level SAS migration requirements](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=n01019intelplatform00migrate.htm&docsetVersion=9.4).
  + Inventory the source SAS deployment:
    + [Complete a migration utility checklist](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=n02005intelplatform00migrate.htm&docsetVersion=9.4&locale=en#n02007intelplatform00migrate).
    + [Check backups in SAS](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=n02005intelplatform00migrate.htm&docsetVersion=9.4&locale=en#n02022intelplatform00migrate).
    + [Prepare your metadata repositories](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=n02005intelplatform00migrate.htm&docsetVersion=9.4&locale=en#n02008intelplatform00migrate).
    + [Review SAS Migration Utility requirements](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=n02005intelplatform00migrate.htm&docsetVersion=9.4&locale=en#n02010intelplatform00migrate).
    + [Download the SAS Migration Utility](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=n02005intelplatform00migrate.htm&docsetVersion=9.4&locale=en#n02011intelplatform00migrate).
    + [Develop a common SAS Migration Utility properties file](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=n02005intelplatform00migrate.htm&docsetVersion=9.4&locale=en#n02012intelplatform00migrate).
    + [Review product-specific SAS Migration Utility properties](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=n02005intelplatform00migrate.htm&docsetVersion=9.4&locale=en#n02013intelplatform00migrate).
    + [Create a migration analysis report](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=n02005intelplatform00migrate.htm&docsetVersion=9.4&locale=en#n02014intelplatform00migrate).
    + View and analyze your [migration analysis report](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=n02005intelplatform00migrate.htm&docsetVersion=9.4&locale=en#n02015intelplatform00migrate) and [migration log](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=n02005intelplatform00migrate.htm&docsetVersion=9.4&locale=en#n02016intelplatform00migrate).
+ Skills/roles: SAS consultant

## Set up a new AWS environment (for new AWS users only)
<a name="setup"></a>
+ Goal: If you're a SAS customer who is new to AWS, you can use [AWS Control Tower](https://aws.amazon.com/controltower/) to set up a base environment. To migrate SAS Grid to AWS, you must add a VPC to your existing environment at a minimum.
+ Tasks:
  + Use AWS Control Tower to set up a well-architected, multi-account environment that is based on security, compliance, and other AWS best practices. You could work within a single account. However, as your environment grows, it will be easier to manage it through a multi-account infrastructure.
  + When the new AWS environment is set up, configure authentication:
    + For Windows servers, use [AWS Directory Service](https://aws.amazon.com/directoryservice/) or [Active Directory Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html) to connect to your existing on-premises Microsoft Active Directory. For added security, use multi-factor authentication (MFA). For more information about using AD Connector with MFA, see [Enable MFA for AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_mfa.html) in the Directory Service documentation.
    + For Linux instances, you can use Directory Service with certain EC2 Linux instances. For details, see [Manually Join a Linux Instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_linux_instance.html) in the Directory Service documentation.
    + If on-premises access required, see [Access to an on-premises network](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/how-it-works.html#scenario) in the AWS Client VPN documentation.
+ Skills/roles: AWS architect
