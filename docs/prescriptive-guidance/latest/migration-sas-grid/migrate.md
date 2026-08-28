---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/migrate.html
---

# Migrate – SAS content to AWS
<a name="migrate"></a>

## Migrate Active Directory identities
<a name="identity"></a>
+ Goal: Define user IDs (UIDs) and group IDs (GIDs), and configure mapping.
+ Tasks:
  + Define new UID/GID attributes for users and groups.
  + Map users to UIDs and security groups to GIDs.
+ Skills/roles: SAS consultant

## Migrate Linux files, directories, and permissions
<a name="linux"></a>
+ Goal: Transfer Linux files and directories, while maintaining the directory structure on AWS.
+ Tasks:
  + Transfer your existing directory structures and files to the file system on AWS. (For example, you can use [FSx for Lustre](https://aws.amazon.com/fsx/lustre/).)
  + Make sure that the directory structure and file paths are consistent in the source and target environments to minimize code changes.
+ Skills/roles: SAS consultant

## Migrate SAS metadata
<a name="metadata"></a>
+ Goal: Implement metadata security design and synchronize SAS metadata content.
+ Tasks:
  + Implement SAS metadata security design on AWS.
  + Synchronize users and groups from your existing corporate Active Directory, where appropriate, based on the security design.
  + Migrate all other SAS metadata folders and objects via export/import from your existing environment.
+ Skills/roles: SAS consultant

## Perform post-migration validation and acceptance testing
<a name="validation"></a>
+ Goal: Perform functional and system testing, sign off on the migration, and create post-migration reports. For details, see [Performing Post-Migration Tasks](https://go.documentation.sas.com/?docsetId=bimig&docsetTarget=p05intellplatform00migrategd.htm&docsetVersion=9.4) in the SAS documentation.
+ Tasks:
  + Perform functional testing of the SAS application on AWS.
  + Perform system testing of SAS applications on AWS.
  + Prepare post-installation documentation.
+ Skills/roles: SAS consultant

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
