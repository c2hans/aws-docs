---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/import-a-region.html
---

# Import a Region
<a name="import-a-region"></a>

**Note**
The following section only applies when the solution’s account discovery mode is self-managed. For information on how account discovery works in AWS Organizations mode, see the [AWS Organizations Account Discovery Mode](aws-organizations-account-discovery-mode.md) section.

Importing a Region requires certain infrastructure to be deployed. This infrastructure consists of *Global* and *Regional* resources:

 **Global** – Resources that are deployed once in an account and reused for each Region imported.
+ An IAM role (WorkloadDiscoveryRole)

 **Regional** – Resources that are deployed in each Region imported.
+ An AWS Config Delivery Channel
+ An Amazon S3 bucket for AWS Config
+ An IAM role (ConfigRole)

There are two options to deploy this infrastructure:
+ AWS CloudFormation StackSets (recommended)
+ AWS CloudFormation

## Import a Region
<a name="import-a-region-1"></a>

These steps guide you through importing a Region and deploying the AWS CloudFormation templates.

1. Sign in to Workload Discovery on AWS. Refer to [Log in to Workload Discovery on AWS](log-in-to-workload-discovery-on-aws.md) for the URL.

1. In the navigation menu, select **Accounts**.

1. Choose **Import**.

1. Select the import method:

   1.  **Add Accounts & Regions** using a CSV file.

   1.  **Add Accounts & Regions** using a form.

### CSV file
<a name="csv-file"></a>

Provide a Comma Separated Value (CSV) file that contains the Regions to be imported in the following format.

```
"accountId","accountName","region"
123456789012,"test-account-1",eu-west-2
123456789013,"test-account-2",eu-west-1
123456789013,"test-account-2",eu-west-2
123456789014,"test-account-3",eu-west-3
```

1. Select **Upload a CSV**.

1. Locate and open your CSV file.

1. Review the **Regions** table, then select **Import**.

1. In the modal dialog, download the Global resources template and Regional Resources template.

1. Deploy the CloudFormation templates in the relevant accounts (refer to [Deploy the AWS CloudFormation templates](#deploy-the-aws-cloudformation-templates) section).

1. Once the global and regional resource templates have been deployed, select both boxes to confirm that the installation is complete and choose **Import**.

### Form
<a name="form"></a>

Provide the Regions to import using the form:

1. For **Account ID**, enter a 12-digit account ID or select an existing account ID.

1. For **Account name**, enter an account name or use a pre-populated value when selecting an existing account ID.

1. Select the Regions to import.

1. Select **Add** to populate the Regions in the **Regions** table below.

1. Review the **Regions** table, then select **Import**.

1. In the modal dialog, download the Global resources template and Regional Resources template.

1. Deploy the CloudFormation templates in the relevant accounts (refer to [Deploy the AWS CloudFormation templates](#deploy-the-aws-cloudformation-templates) section).

1. Once the global and regional resource templates have been deployed, select both boxes to confirm the installation is complete and choose **Import**.

## Deploy the AWS CloudFormation templates
<a name="deploy-the-aws-cloudformation-templates"></a>

Global resources must be deployed once per account. Do not deploy this template when importing a Region from an account that contains a Region that is already imported into Workload Discovery on AWS. If the Region has already been imported, follow the instructions in [Deploy the stack to provision the Regional resources](#deploy-the-stack-to-provision-the-regional-resources-using-cloudformation).

## Use CloudFormation StackSets to provision Global resources across accounts
<a name="use-cloudformation-stacksets-to-provision-global-resources-across-accounts"></a>

**Important**
First, complete the [Prerequisites for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html) to activate StackSets in your target accounts.

1. In the [administrator account](https://docs.amazonaws.cn/en_us/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stacksets-concepts-accts), sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. From the navigation menu, select **StackSets**.

1. Choose **Create StackSet**.

1. On the **Choose a template** page, under **Permissions**:

   1. If you’re using AWS Organizations, choose either **Service managed permissions** or **Self service permissions**. For details, refer to [Using StackSets in an AWS Organization](aws-organizations-account-discovery-mode.md).

   1. If you’re not using AWS Organizations, enter the IAM run role name used when following the StackSets prerequisite steps. For details, refer to [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html).

1. Under **Specify template**, select **Upload a template file**. Choose the `global-resources.template` file (downloaded earlier when you [imported a Region](#import-a-region-1) either by CSV file or form), and choose **Next**.

1. On the **Specify StackSet details** page, assign a name to your StackSet. For information about naming character limitations, refer to [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/import-a-region.html)

1. Choose **Next**.

1. On the **Configure StackSet options** page, choose **Next**.

1. On the **Set deployment options** page, under **Accounts**, enter the account IDs for deploying the account role in the **Account numbers** box.

1. Under **Specify regions**, select a **Region** to install the stack.

1. Under **Deployment options**, select **Parallel**, and then choose **Next**.

1. On the **Review** page, check the box acknowledging that AWS CloudFormation might create IAM resources with custom names.

1. Choose **Submit**.

## Use CloudFormation StackSets to provision Regional resources
<a name="use-cloudformation-stacksets-to-provision-regional-resources"></a>

**Important**
First, complete the [Prerequisites for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html) to activate StackSets in your target accounts.
If you have some Regions with AWS Config installed and some without, you must perform two StackSet operations, one for the Regions with AWS Config installed and one for those without.

1. In the [administrator account](https://docs.amazonaws.cn/en_us/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stacksets-concepts-accts), sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. From the navigation menu, select **StackSets**.

1. Choose **Create StackSet**.

1. On the Choose a template page, under **Permissions**:

   1. If you’re using AWS Organizations, choose either **Service managed permissions** or **Self service permissions**. For details, refer to [Using StackSets in an AWS Organization](aws-organizations-account-discovery-mode.md).

   1. If you’re not using AWS Organizations, enter the IAM run role name used when following the StackSets prerequisite steps. For details, refer to [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html).

1. Under **Specify template**, select **Upload a template file**. Choose the `regional-resources.template` file (downloaded earlier when you [imported a Region](#import-a-region-1) either by CSV file or form), and choose **Next**.

1. On the **Specify StackSet details** page, assign a name to your StackSet. For information about naming character limitations, refer to [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/import-a-region.html)

1. Choose **Next**.

1. On the **Configure StackSet options** page, choose **Next**.

1. On the **Set deployment options** page, under **Accounts**, enter the account IDs to deploy the account role to in the **Account numbers** box.

1. Under **Specify regions**, select a **Region** to install the stack. This installs the stack in these Regions in all the accounts entered in step 6.

1. Under **Deployment options**, select **Parallel**, and then choose **Next**.

1. On the **Review** page, check the box acknowledging that AWS CloudFormation might create IAM resources with custom names.

1. Choose **Submit**.

## Deploy the stack to provision the Global resources using CloudFormation
<a name="deploy-the-stack-to-provision-the-global-resources-using-cloudformation"></a>

Global resources must be deployed once per account. Do not deploy this template when importing a Region from an account that contains a Region that is already imported into Workload Discovery on AWS.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Choose **Create stack**, and then select **With new resources (standard)**.

1. On the **Create stack** page, in the **Specify template** section, select **Upload a template file**.

1. Choose **Choose file** and select the `global-resources.template` file that (downloaded earlier when you [imported a Region](#import-a-region-1) either by CSV file or form), and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, refer to [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the \_AWS Identity and Access Management*\_User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/import-a-region.html)

1. Choose **Next**.

1. Select the box acknowledging that AWS CloudFormation might create IAM resources with custom names.

1. Choose **Create stack**.

The new Regions will be scanned during the next discovery process, which runs at 15-minute intervals, for example: 15:00, 15:15, 15:30, 15:45.

## Deploy the stack to provision the Regional resources using CloudFormation
<a name="deploy-the-stack-to-provision-the-regional-resources-using-cloudformation"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Choose **Create stack**, and then select **With new resources (standard)**.

1. On the **Create stack** page, in the **Specify template** section, select **Upload a template file**.

1. Choose **Choose file** and select the `regional-resources.template` file (downloaded earlier when you [imported a Region](#import-a-region-1) either by CSV file or form), and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, refer to [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/import-a-region.html)

1. Choose **Next**.

1. Select the box acknowledging that AWS CloudFormation might create IAM resources with custom names.

1. Choose **Create stack**.

The new Regions will be scanned during the next discovery process, which runs at 15-minute intervals, for example, 15:00, 15:15, 15:30, 15:45.

## Verify the Region was imported correctly
<a name="verify-the-region-was-imported-correctly"></a>

1. Sign in to the solution’s web UI (or refresh the page if it’s already loaded). Refer to [Log in to Workload Discovery on AWS](log-in-to-workload-discovery-on-aws.md) for the URL.

1. From the left navigation panel, under **Settings**, select **Imported Regions**.

The Region, account name, and account ID appear in the table. The **Last Scanned** column shows the last discovered resources in that Region.

**Note**
If the **Last Scanned** column stays blank for more than 30 minutes, refer to [Debugging the discovery component](aws-organizations-account-discovery-mode.md).
