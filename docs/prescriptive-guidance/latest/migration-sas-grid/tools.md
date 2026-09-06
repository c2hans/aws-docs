---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/tools.html
---

# Automation and tooling
<a name="tools"></a>

Matching source and target topologies simplifies many variables that can affect migration efforts. In addition, matching topologies is a requirement for using the SAS Migration Utility. This tool assumes that every host machine, directory, and network component in the source environment will map one-to-one to its equivalent in the target environment.

You use the SAS Migration Utility to analyze and package your source environment. As the following diagram shows, the resulting package file is copied to the target system you have provisioned on AWS. It is then processed by the SAS Deployment Wizard as part of the initial SAS Enterprise BI Server software deployment on AWS.

![SAS Migration Utility and SAS Deployment Wizard tasks](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/images/guide-img/305d2670-30eb-46db-a41c-bed418267f47/images/6cd87054-dbf6-4347-a91e-2b1f39c8e98e.png)

The SAS Migration Utility is useful for migrating SAS metadata content and certain associated files stored in the configuration directory. The bulk of the physical files (SAS data sets, programs, external files, and so on) aren't part of the SAS Migration Utility process and have to be copied over to the target environment separately. To copy these physical files over, we recommend that you explore the use of [AWS DataSync](https://aws.amazon.com/datasync/).

After the majority of SAS content has been migrated to the new target system on AWS, you perform validation testing. Before you cut over to your production environment on AWS, you can perform one final promotion of any content that has been added or changed since the last migration.

![SAS Migration Utility and SAS Deployment Wizard tasks](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/images/guide-img/305d2670-30eb-46db-a41c-bed418267f47/images/3d622aa9-ad14-4181-abc1-7842cc7958c6.png)

For additional details on the SAS Migration Utility, see the [SAS 9.4 Intelligence Platform Migration Guide](https://documentation.sas.com/doc/en/bicdc/9.4/bimig/p01intellplatform00migrategd.htm) on the SAS website.
