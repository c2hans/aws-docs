---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/configure-migration-automation-server.html
---

# Step 7: Configure a migration automation server
<a name="configure-migration-automation-server"></a>

The migration automation server is used to run migration automation.

## Build a Windows server
<a name="build-a-windows-server"></a>

We recommend creating the server in your AWS account, but it can also be created in your on-premises environment. If built in an AWS account, it must be in the same AWS account and Region as Cloud Migration Factory. To review the server requirements, refer to [Migration automation server](components.md#comp-mes).

We recommend using the Windows Server 2025 Base image, but Windows Server 2019 or later is supported. Wherever you deploy the Windows instance, we recommend deploying it as a standard installation that meets your security and operational requirements.

**Note**
When launching the instance, assign a Key Pair to retrieve the administrator password for RDP access. No inbound connections are required on your security group if you are using Windows Server 2019 Base or higher, because you use AWS Systems Manager (SSM) to connect.

## Configure AWS permissions for the migration automation server
<a name="configure-aws-permissions-for-the-migration-automation-server"></a>

Depending on where you deploy the migration execution server, choose one of the options below to configure AWS permissions for the migration automation server. The IAM role or policy provides the permission to the automation server and the access to AWS Secrets Manager to get agent installation keys and factory service account credentials. You can deploy the migration automation server either to AWS as an EC2 instance or on-premises.

### Option 1: Configure an EC2 migration automation server in the same account and Region
<a name="option-1"></a>

1. Navigate to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home) and select the solution’s stack.

1. Select the **Outputs** tab, under the **Key** column, locate `AutomationServerInstanceProfile` and record the **Value** to use later in the deployment.

    **Outputs tab**
![cfn console outputs tab](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/cfn-console-outputs-tab.png)

1. Navigate to the [Amazon Elastic Compute Cloud (EC2)](https://console.aws.amazon.com/ec2/v2/home) console.

1. From the left navigation pane, select **Instances**.

1. On the **Instances** page, use the Filter Instances field and enter the name of the migration execution server to find the instance.

1. Select the instance and select **Actions** on the menu.

1. Select **Security** from the drop-down list, and then select **Modify IAM role**.
![f6 ec2 console](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/f6-ec2-console.png)

1. From the list of IAM roles, locate and select the IAM role containing the value for `AutomationServerInstanceProfile` that you recorded earlier in this procedure and choose **Save**.

1. Select the instance, then choose **Connect**.

1. On the **Session Manager** tab, verify that the status shows **Connected**.
**Note**
If the instance does not connect after a few minutes, try connecting by using RDP. You must update your security groups to allow external connections because SSM isn’t connected yet.

1. Add the following tag to the migration automation server EC2 instance: **Key**= `role` and **Value** = `mf_automation`.

    **EC2 console**
![add tag ec2](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/add-tag-ec2.png)

### Option 2: Configure an on-premises migration automation server
<a name="option-2"></a>

1. Navigate to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home) and select the solution’s stack.

1. Select the **Outputs** tab, under the **Key** column, locate `AutomationServerIAMPolicy` and record the value to use later in the deployment.

    **Outputs tab**
![outputs automation server iam policy](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/outputs-automation-server-iam-policy.png)

1. Navigate to the [AWS Identity and Access Management (IAM)](https://console.aws.amazon.com/iam/home) console.

1. From the left navigation pane, select **Users**, then choose **Add users**.

1. In the **User name** field, create a new user.

1. Choose **Next**.

1. On the **Set permissions** page, under **Permissions options**, select **Attach policies directly**. A list of policies displays.

1. From the list of policies, locate and select the policy containing the value for `AutomationServerIAMPolicy` that you recorded in [Launch the stack](launch-the-stack.md).

1. Choose **Next**, then verify that the correct policy is selected.

1. Choose **Create user**.

1. After you’re redirected to the **Users** page, choose the user you created in the previous step, and then choose the **Security credentials** tab.

1. In the **Access keys** section, choose **Create access key**.
**Note**
Access keys consist of an access key ID and secret access key, which are used to sign programmatic requests that you make to AWS. If you don’t have access keys, you can create them from the AWS Management Console. As a best practice, do not use the root user access keys for any task where it’s not required. Instead, [create a new administrator IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) with access keys for yourself.
The only time that you can view or download the secret access key is when you create the keys. You cannot recover them later. However, you can create new access keys at any time. You must also have permissions to perform the required IAM actions. For more information, see [Permissions required to access IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_permissions-required.html) in the *IAM User Guide*.

1. To view the new access key pair, choose **Show**. You will not have access to the secret access key again after this dialog box closes. Your credentials will look something like this:
   +  `Access key ID: AKIAIOSFODNN7EXAMPLE`
   +  `Secret access key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

1. To download the key pair, choose **Download .csv file**. Store the keys in a secure location. You will not have access to the secret access key again after this dialog box closes.
**Important**
Keep the keys confidential to protect your AWS account and never email them. Do not share them outside your organization, even if an inquiry appears to come from AWS or Amazon.com. No one who legitimately represents Amazon will ever ask you for your secret key.

1. After you download the `0csv` file, choose **Close**. When you create an access key, the key pair is active by default, and you can use the pair right away.

1. Use your remote desktop protocol (RDP) to log in to the migration execution server.

1. Signed in as an administrator, open a command prompt (`CMD.exe`).

1. Run the following command to configure the AWS credentials on the server. Replace {{<your\_access\_key\_id>}}, {{<your\_secret\_access key>}}, and {{<your\_region>}} with your values:

   ```
   SETX /m AWS_ACCESS_KEY_ID <your_access_key_id>
   SETX /m AWS_SECRET_ACCESS_KEY <your_secret_access key>
   SETX /m AWS_DEFAULT_REGION <your_region>
   ```

1. Reboot automation server.

1. Install the SSM agent using Hybrid mode (on-prem servers).

   1. Create a hybrid activation; see [Create an activation (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-managed-instance-activation.html#create-managed-instance-activation-console) in the *AWS Systems Manager User Guide*. During this process, when asked to provide an IAM Role, select an existing IAM role and choose the role with the suffix **-automation-server** which was automatically created when the Cloud Migration Factory stack was deployed.

   1. Log in to the migration automation server as administrator.

   1. Install the SSM Agent; see [Install SSM Agent for a hybrid and multicloud environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-install-managed-win.html) in the *AWS Systems Manager User Guide*. Use the hybrid activation created in step 20.a.

   1. After the SSM Agent is installed, in the SSM console, choose **Fleet Manager**. Identify the node ID that has the **mi-** prefix and an **Online** status.

       **Fleet Manager**
![fleet manager](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/fleet-manager.png)

   1. Select the **Node ID** and make sure that the IAM role is the one you selected with **automation-server** suffix.

   1. Add the following tag for this Hybrid node: **Key** = `role` and **Value** = `mf_automation`. All lower case.

       **Tag - hybrid node**
![tag hybrid node](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/tag-hybrid-node.png)

## Install required software to support the automations
<a name="installing-required-software"></a>

1. To connect to the migration automation server, in the EC2 console, select the instance, and choose **Connect** > **RDP client** > **Connect using Fleet Manager** > **Fleet Manager Remote Desktop**. Log in as Administrator.

1. Download [Python v3.14.4](https://www.python.org/ftp/python/3.14.4/python-3.14.4-amd64.exe). Other versions of Python might also work if installed for all users using the standalone Python installer (not the Python install manager).

1. Run the Python installer and choose **Customize installation**.

1. Choose **Next**, and select **Install for all users** and **Add Python to environment variables**. Choose **Install**.

    **Migration Factory web interface Attribute Details tab**
![python advanced options](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/python-advanced-options.png)

1. Verify that you have administrator privileges, open `cmd.exe`, and run the following commands to install the Python packages one at a time:

   ```
   python -m pip install requests
   python -m pip install paramiko
   python -m pip install boto3
   ```

   If any of these commands fail, upgrade pip by running the following command:

   ```
   python -m pip install --upgrade pip
   ```

1. Install the AWS CLI (Command Line Interface) by running the following command:

   ```
   msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
   ```

   For more information, refer to [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS CLI User Guide*.

1. Open PowerShell, then install the PowerShell for AWS module, ensuring that you have the \*-Scope AllUsers \* parameter included in the command.

   ```
   Install-Module -Name AWSPowerShell -Scope AllUsers
   ```

   For more information, refer to [Installing the AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up-windows.html#ps-installing-awswindowspowershell) in the *AWS Tools for PowerShell User Guide*.

1. To enable script execution, open PowerShell as Administrator and run the following command:

   ```
   Set-ExecutionPolicy RemoteSigned
   ```
