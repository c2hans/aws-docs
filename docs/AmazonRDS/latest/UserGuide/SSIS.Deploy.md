---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSIS.Deploy.html
---

# Deploying an SSIS project
<a name="SSIS.Deploy"></a>

On RDS, you can't deploy SSIS projects directly by using SQL Server Management Studio (SSMS) or SSIS procedures. To download project files from Amazon S3 and then deploy them, use RDS stored procedures.

To run the stored procedures, log in as any user that you granted permissions for running the stored procedures. For more information, see [Setting up a Windows-authenticated user for SSIS](SSIS.Permissions.md#SSIS.Use.Auth).

**To deploy the SSIS project**

1. Download the project (.ispac) file.

   ```
   exec msdb.dbo.rds_download_from_s3
   @s3_arn_of_file='arn:aws:s3:::{{bucket_name}}/{{ssisproject}}.ispac',
   @rds_file_path='D:\S3\{{ssisproject}}.ispac',
   @overwrite_file=1;
   ```

1. Submit the deployment task, making sure of the following:
   + The folder is present in the SSIS catalog.
   + The project name matches the project name that you used while developing the SSIS project.

   ```
   exec msdb.dbo.rds_msbi_task
   @task_type='SSIS_DEPLOY_PROJECT',
   @folder_name='{{DEMO}}',
   @project_name='{{ssisproject}}',
   @file_path='D:\S3\{{ssisproject}}.ispac';
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
