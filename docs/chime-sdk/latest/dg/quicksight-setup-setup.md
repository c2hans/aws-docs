---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/quicksight-setup-setup.html
---

# Configuring an Quick dashboard for the Amazon Chime SDK
<a name="quicksight-setup-setup"></a>

Once you set up the data lake, you can configure an Quick dashboard with pre-defined metrics that visualize your data. You can use the following dashboards:
+ **Transcribe Call Analytics \+ Voice Analytics**. Metrics include summary and detailed visuals for turn-by-turn transcripts, issues detected, outcomes, entity detection, and voice profile ID matches.
+ **Transcribe \+ Voice Analytics**. Metrics include summary and detailed visuals for turn-by-turn transcripts, vocabulary matches, voice tone, and voice profile ID matches.

The following topics explain how to set up an Quick account if you don't already have one, and how to configure a dashboard.

**Topics**
+ [Creating a QuickSight account](#create-quicksight-account)
+ [Configuring your QuickSight account](#configure-qs-acct)
+ [Creating a QuickSight dashboard](#create-qs-dashboard)

## Creating a QuickSight account
<a name="create-quicksight-account"></a>

The steps in this section explain how to create an Quick account. If you already have an account, you can skip to [Creating a QuickSight dashboard](#create-qs-dashboard).

You can create a QuickSight account by:
+ Using Amazon CloudFormation templates.
+ Using the Amazon Chime SDK console.

### Prerequisites
<a name="qs-account-prereqs"></a>

Gather the following information before you start:
+ The name of your call analytics Amazon S3 bucket.
+ A notification email address. The system delivers QuickSight notifications to this address.

### Using CloudFormation templates to create an account
<a name="account-by-cft"></a>

The following steps explain how to create an Quick account by deploying an Amazon CloudFormation template. The process only subscribes you to an Enterprise account. For information about pricing, refer to [Quick Pricing](https://aws.amazon.com/quicksight/pricing/).

**To deploy the template**

1. Start the AWS console and log in to your AWS account.

1. Paste the following URL into your browser's address bar. Make sure to enter your Region as indicated.

   `https://{{region}}.console.aws.amazon.com/cloudformation/home?region={{region}}#/stacks/quickcreate?templateURL=https://chime-sdk-assets.s3.amazonaws.com/public_templates/AmazonChimeSDKQuickSightSubscription.yaml`.

1. On the **Quick create stack** page, enter the following:

   1. Under **Stack name** enter a name for your account.

   1. Under **QuickSightNotificationEmail** the email address that you gathered earlier.

   1. Under **QuickSightSubscriptionForDataVisualization**, choose **Create new AWS QuickSight account**.

   1. Under **S3BucketName**, enter the name of your Amazon S3 bucket.

   1. Select the **I acknowledge that AWS CloudFormation might create IAM resources.** checkbox.

1. Choose **Create stack**.

   The system takes approximately 10 minutes to create the stack.

1. When the build finishes, choose **Go to Quick** and enter your email address to sign in to your account.

### Using the console to create an account
<a name="account-by-console"></a>

The following steps explain how to use the Amazon Chime SDK console to create an Quick account. You must use an Enterprise or Enterprise \+ Q account.

**To use the console**

1. Start the Amazon Chime SDK console at [ https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home), search for **QuickSight**, and in the search results choose **QuickSight**.
![A search result that links to Quick.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/quicksightsetup-1.png)

1. Choose **Sign up for QuickSight**.

1. Choose **Enterprise** or **Enterprise \+ Q**, then choose **Continue**.

1. Enter your first name, last name, phone number, and the email address that you gathered previously, then choose **Continue**.

1. Do the following:

   1. Under **Authentication method**, choose an option.
**Note**
If you choose the option with federated users, you need the correct IAM permissions. For more information, refer to [ Signing up for an Quick subscription](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html) in the *Quick User Guide*.

   1. Under **QuickSight Region**, select a Region.

   1. Under **Account Info**, enter a name for the account and the email address that you gathered earlier.

   1. Under **QuickSight access to AWS Services**, use the default role, or choose **Use an existing role** and select a role from the list.

   1. (Optional) as needed, under **Allow access and autodiscovery for these resources**, choose additional resources.

   1. When done, choose **Finish**.

   1. When the build finishes, choose **Go to Quick** and enter your email address to sign in to your account.

## Configuring your QuickSight account
<a name="configure-qs-acct"></a>

After you log in to your QuickSight account, you need to configure security and add yourself to a group created by the setup process.

**To configure security**

1. Choose the profile icon in the upper-right corner, then choose **Manage QuickSight** from the resulting menu.
![A menu with the Manage QuickSight command.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/quicksightsetup-1-a.png)

1. In the navigation pane, choose **Security & permissions**.

1. Under **QuickSight access to AWS services**, choose **Manage**, and ensure the following services are selected.
   + Amazon Redshift
   + Amazon RDS
   + Amazon S3
   + Amazon Athena
   +  IAM

1. Choose the **Select Amazon S3 buckets** link.

1. Select the check box next to your Amazon S3 bucket, then select the checkbox to the right, in the **Write permission for Athena Workgroup** column.

1. Choose **Finish**.

1. Choose **Save**.

**To add yourself to the group**

1. In the navigation pane, choose **Manage groups**, then choose the group with **Admins** in the name. For example, *S3BucketName*–**Admins**.

1. Choose **Add user**, then enter your email alias in the box that appears.

   Your name appears as **Admin – ***your-alias*.

1. Choose **Add**.

## Creating a QuickSight dashboard
<a name="create-qs-dashboard"></a>

After you create a data lake, you can create a QuickSight dashboard that visualizes your data. You can use an Amazon CloudFormation template or the Amazon Chime SDK console to create the dashboard. The following steps explain both methods.

**To use a template**

1. Start the Amazon CloudFormation console.

1. Paste the following link into your browser's address bar: `https://{{region}}.console.aws.amazon.com/cloudformation/home?region={{region}}#/stacks/quickcreate?templateURL=https://chime-sdk-assets.s3.amazonaws.com/public_templates/AmazonChimeSDKQuickSightDashboards.yaml`

1. On the **Quick create stack** page, under **Stack name**, enter a name for the account.

1. Under **ActiveQuickSightAccount**, choose **True**.

1. Under **QuicksightDashboardSelection**, choose **Call Analytics – Transcribe Call Analytics and Voice Analytics dashboard** or **Call Analytics – Transcribe and Voice Analytics dashboard**.

1. Under **Amazon S3BucketName**, enter the URI of your Amazon S3 bucket.

1. Under **GlueDatabaseName**, enter the Glue database on which you want the QuickSight dashboard deployed.

1. Choose the **I acknowledge that AWS CloudFormation might create IAM resources** check box, then choose **Create stack**.

**To configure a QuickSight dashboard manually**

1. Navigate to your QuickSight account.

1. In the top-right corner choose the profile icon, then choose **Manage QuickSight**.
![The QuickSight account dialog box and Manage QuickSight command.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/quicksightsetup-1-a.png)

1. In the navigation pane, choose **Manage groups**, then choose the group created by the setup process.

1. Choose **Add User**, enter your email address, then choose **Add**.

   The system takes 10 minutes to deploy the page.

1. Use the Amazon Chime SDK console to log in to your QuickSight account and use the dashboard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
