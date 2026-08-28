---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/run-automation-from-console.html
---

# Run automation from console
<a name="run-automation-from-console"></a>

The Cloud Migration Factory on AWS solution provides an automation engine allowing users to run jobs in the form of scripts against the inventory within the datastore. With this feature, you can manage, customize, and deploy all automations required to complete the end-to-end migration activities.

Jobs initiated from AWS CMF can be run either by using an AWS Systems Manager (SSM) Automation Document or an automation server that can be hosted in the AWS Cloud or on-premise. These servers need to run Windows with the SSM agent installed, along with Python and Microsoft PowerShell. You can also install other frameworks as required for custom automations. Refer to [Build a migration automation server](configure-migration-automation-server.md) for details of the automation server build. At least one automation server is required to run jobs from the AWS CMF console.

## When to Use Each Platform
<a name="when-to-use-each-platform"></a>

### Use Traditional Automation Server when:
<a name="use-traditional-automation-server-when"></a>
+ Scripts require direct network connectivity to on-premises systems
+ Custom software installations or dependencies are needed
+ Consistent Windows-based execution environment is required
+ Complex authentication mechanisms with on-premises systems are involved

### Use SSM Automation Document when:
<a name="use-ssm-automation-document-when"></a>
+ Performing AWS-native operations
+ No special software dependencies are required
+ Scalability and parallel execution are important
+ Minimal maintenance overhead is desired

On deployment, you can use scripts for the most common tasks needed to rehost workloads using AWS MGN. Download the scripts from the web interface and use it as a starting point for custom scripts. For details on creating custom automation script, refer to [Scripts management](scripts-management.md).

To initiate a job from the console, select a wave to run the automation against, then select **Actions**, and choose **Run Automation**. Or, you can select a job to run the automation against, then select **Actions**, and choose **Run Automation**.

From the **Run Automation**:

1. Enter the **Job Name**. This will be used to identify the job in the log.

**Note**
Job names do not have to be unique, as all jobs are also allocated a unique ID and timestamps to further identify them.

1. Select the **Script Name** from the list. This is a list of all scripts that have been loaded into the AWS CMF instance. When the job is submitted, the default version of the script selected will be run. To check the details of the script, including the current default version, choose **Related details** under the script name. Refer to **Change default version of script package** for details about updating the default version of scripts. When you select the script to run, the required parameters are shown under **Script Arguments**.

1. From the **Instance ID**, select the automation server for the job from the list.

**Note**
The list will only show instances that have the SSM agent installed and where either the EC2 instance, or for non-EC2 hosted automation servers, the Managed Instance tag of `role` is set to `mf_automation`.

1. In **Script Arguments**, enter the required input arguments for the script.

1. Once you have entered all the required parameters and verified them, choose **Submit Automation Job**.

When you submit the automation job, the following process is initiated:

1. A job record will be created with the AWS Cloud Migration Factory **Jobs** view containing the details of the job and current status.

1. An AWS Systems Manager automation job will be created, and will start to run the AWS Cloud Migration Factory SSM automation document against the automation server provided via the **Instance ID**. The automation document:

   1. Downloads the current default version of the script package from the AWS Cloud Migration Factory S3 bucket to the automation server into the `C:\migration\scripts` directory\*.\*

   1. Unzips and verifies the package.

   1. Launches the master file python script specified in the `package-structure.yml` included in the zip.

1. Once the master file python script has been launched, any output from the script is captured by the SSM agent and fed into CloudWatch. It is then captured regularly and stored in the AWS Cloud Migration Factory datastore with the original job record, providing a complete audit of the job run.

   1. If the script requires credentials to AWS Cloud Migration Factory then the script will contact AWS Secrets Manager to obtain the service account credentials. If the credentials are incorrect or not present then the script will return a failure.

   1. If the script has a requirement to access other secrets stored using the AWS Cloud Migration Factory Credentials Manager feature, then it will contact AWS Secrets Manager to access those credentials. If this is not possible then the script will return a failure.

1. Once the master file python script exits, the outcome of this script will determine the status provided to the AWS Cloud Migration Factory job record. A non-zero return will set `Job Status` to `Failed`.

## Script Execution Platforms
<a name="script-execution-platforms"></a>

The Cloud Migration Factory supports two compute platforms for executing automation scripts:

### Traditional Automation Server
<a name="traditional-automation-server"></a>

The default execution method using a Windows-based automation server. This requires maintaining a dedicated server with the required software installations and configurations as detailed in the "Build a Migration Automation Server" section.

### SSM Automation Document
<a name="ssm-automation-document"></a>

Scripts can be executed directly through AWS Systems Manager Automation Documents by specifying "SSM Automation Document" as the Compute Platform in the Package-Structure.yaml file. This option:
+ Eliminates the need for a dedicated automation server
+ Leverages AWS Systems Manager’s native automation capabilities
+ Reduces maintenance overhead
+ Provides better scalability and reliability

To use the SSM Automation Document platform:

1. In your script package’s Package-Structure.yaml file, set: ` yaml ComputePlatform: "SSM Automation Document" `

**Note**
Currently, if a failure occurs in the initial run of the AWS SSM document, it is not shown in the web interface. Failures are only logged once the master file python is launched.
All jobs initiated from the console will timeout after 12 hours if they have not returned a success or failure status.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
