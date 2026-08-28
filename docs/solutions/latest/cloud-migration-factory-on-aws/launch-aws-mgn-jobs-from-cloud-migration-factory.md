---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/launch-aws-mgn-jobs-from-cloud-migration-factory.html
---

# Launch AWS MGN jobs from Cloud Migration Factory
<a name="launch-aws-mgn-jobs-from-cloud-migration-factory"></a>

The Cloud Migration Factory on AWS solution has built in automation to initiate and manage Rehost migration using AWS MGN. These automations allow migration teams to manage all aspects of their migration from a single user interface, combining the key actions available within the AWS MGN service console, with the AWS Cloud Migration Factory automation library that extends the functionality with prebuilt scripts for mass migrations, which helps to increase the speed of the migration activities. Refer to List of automated migration activities for AWS Application Migration Service (AWS MGN) for a full list of AWS MGN automation jobs available. Using AWS Cloud Migration Factory also provides seamless multi account migrations using AWS MGN as the Cloud Migration Factory has the ability to assume roles in different target accounts automatically based on the Cloud Migration Factory application and server definitions being migrated.

## Prerequisite activities
<a name="prerequisite-activities"></a>

1. Target account AWS CMF CloudFormation deployed into each target account. For more information, review the [AWS CloudFormation templates](aws-cloudformation-templates.md) section in this document.

1.  [AWS MGN is initialized in each target account](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize.html).

## Initial definition
<a name="initial-definition"></a>

Definition of the on-premises inventory is performed through the creation of wave, application and server items using either the user interface, or through the import of a CSV intake form. These definitions are used to provide the on-premise server identities and also the target EC2 parameters and well as other required data to manage the migration activity.

### User interface definition
<a name="user-interface-definition"></a>

In order to use the AWS MGN functionality, you need to create a wave record, with associated application records, and finally one or more server records associated to the applications. The wave record is used to group the applications, and does not provide parameters to the automation, whereas the application record defines the target AWS account ID and AWS Region that the application will be migrated to. The server records provide the automations actions and AWS MGN integration the target parameters for the EC2 instances, such as instance type, subnets, security groups, etc.

When defining a server in the AWS CMF datastore for use with the AWS MGN functionality the server needs to be configured with a **Migration Strategy** of **Rehost**. Once Rehost is selected then the additional attributes required for this functionality will be shown on the screen. The following attributes are required to be populated in order to successfully initiate an AWS MGN migration job:

#### Required
<a name="required"></a>

 **Server OS Family** - Set to either linux or windows depending on the OS family.

 **Server OS Version** - Set to the detailed OS version running on the server.

 **Instance Type** - EC2 instance type to be used.

 **Tenancy** - Shared hosting, dedicated host.

 **Security Group Ids** - List of security groups that will be assigned to the instance when the final cutover is initiated.

 **Security Group Ids - Test** - List of security groups that will be assigned to the instance when the testing is initiated.

#### Conditional
<a name="conditional"></a>

 **Subnet Ids** - Subnet ID to assign this EC2 instance to when the final cutover is initiated. (not applicable when **Network Interface ID** specified)

 **Subnet Ids - Test** - Subnet ID to assign this EC2 instance to when testing is initiated. (not applicable when **Network Interface ID -Test** specified)

 **Network Interface ID** - ENI ID to be used when the final cutover is initiated.

 **Network Interface ID - Test** - ENI ID to be used when testing is initiated.

 **Dedicated Host ID** - Dedicated host ID that the instance will be launched on. (only applicable when **Tenancy** is set to **Dedicated host**).

#### Optional
<a name="optional"></a>

 **Tags** - EC2 Instance tags to be applied to instance.

All other attributes not listed here do not have any bearing on the AWS MGN Jobs initiated from within the AWS CMF solution.

### Intake form definition
<a name="intake-form-definition"></a>

Intake forms can contain the details to create or update multiple types of record with the datastore in a single row of the csv file, this enables the import of related data. In the example below, the wave, application and server records will be created and related to each other automatically during the import.

To import the intake form, follow the same process as other data imports into the Cloud Migration Factory on AWS solution covered in [Importing data](metadata-management.md#importing-data).

## Initiating a job
<a name="initiating-a-job"></a>

Initiating an AWS MGN job from AWS CMF is performed against a wave, from the wave list view select the wave, and then from the **Actions** select **Rehost**>**MGN**.

This screen requires the user to make the following choices before they can **Submit** the job.

1. Select the AWS MGN **Action** to perform against the applications and servers in the wave. These actions mostly replicate those available in the AWS MGN service console and API, with the exception of **Validate Launch Template** (see below for details on this action). For details of the effects of each action, refer to AWS MGN user guide.

1. Select the **Wave** to run the action against.

1. Select the **Applications** from the wave that the action will be run against. This list will only show applications that are associated to the Wave selected.

1. Once all options are correct, choose **Submit**.

The automation will now initiate the selected action against each selected application’s target AWS account, as specified in the Application record. The results of the action will be displayed in the notification message, including any errors.

### Validate launch template
<a name="validate-launch-template"></a>

This action is used to validate the configuration data stored in CMF for each server is valid before attempting cutover activities. In order to run this action, you must have successfully deployed the AWS MGN agents onto the source server.

The validations performed for each server are:
+ Verify instance type is valid.
+ Verify IAM instance profile exists.
+ Security groups exist for both test and live.
+ Subnets exist for both test and live (if ENI not specified).
+ Dedicated host exists (if specified).
  + If dedicated host is specified then the following checks are made:
    + Does the dedicated host support the instance type specified?
    + Does the dedicated host have free capacity for all the requirements of this wave, based on instance types required?
+ ENI exists (if specified).

The results of the action will be displayed in the notification message, including any errors.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
