---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enable-leostream-broker-module.html
---

# Step 3: Enable Leostream Broker module
<a name="enable-leostream-broker-module"></a>

Follow these steps to enable the Leostream Broker module.

**Note**
Modular Cloud Studio on AWS allows you to deploy and manage a scalable, secure, and global content production infrastructure in the cloud. This includes custom modules, developed by AWS Partners or other third parties, that you can choose to use ("Third-Party Modules"). AWS does not own or otherwise have any control over Third-Party Modules.
Your use of the Third-Party Modules is governed by any terms provided to you by the Third-Party Module providers when you acquired your license to use them (for example, their terms of service, license agreement, acceptable use policy, and privacy policy). You are responsible for ensuring that your use of the Third-Party Modules comply with any terms governing them, and any laws, rules, regulations, policies, or standards that apply to you.
You are also responsible for making your own independent assessment of the Third-Party Modules that you use. AWS does not make any representations, warranties, or guarantees regarding the Third-Party Modules, which are "Third-Party Content" under your agreement with AWS. Modular Cloud Studio on AWS is offered to you as "AWS Content" under your agreement with AWS.

When you use MCS to deploy the Leostream Broker module, a 30-day trial license is automatically provided. During this trial period, you might see an `Invalid License` message upon logging in to the Leostream Connection Broker. However, you can inspect the remaining days of the trial within the Connection Broker interface. To continue using the Leostream Broker module beyond the 30-day trial period, you must contact Leostream directly to obtain a full license, then update the license key.

**Note**
Make sure your account has access to use the *g4dn.xlarge* EC2 instance type if you want to use Windows or Linux workstation AMI. Otherwise, the deployment will fail. See [service quotas](https://docs.aws.amazon.com/general/latest/gr/ec2-service.html#limits_ec2) for more details.

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. Select **Workstation Management** from the left navigation pane.

1. Choose **Deploy New Module**.

1. For **Select Region**, select the Region where you want the Leostream Broker module. There should be only one hub Region option if you have not deployed any spoke Regions.

1. For **Select Workstation Management module**, select **Leostream Broker** and choose **Next**.

1. For **Configure workstation management settings**, review the parameters for this module and modify them as necessary. This module uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enable-leostream-broker-module.html)

1. For **Configure Tag Settings**, review the tags for this module and modify them as necessary. By default, this module uses tags defined in the main solution stack.

1. Choose **Next**.

1. On the **Review** page, verify all the parameters you provided and choose **Deploy Module** if you confirm they are correct.

1. The status of the Leostream Broker will be shown as **Enabling in progress**. The deployment of this module takes approximately 1 hour. If you selected Yes on either **Workstation Windows 2022 AMI** or **Workstation Rocky Linux 8 AMI**, the deployment might take up to 3 hours. After the deployment is complete, the status of the storage module will be shown as **Enabled**.

1. Leostream broker’s local **Admin** user is created for managing the application. To retrieve the Leostream local **Admin** credentials, you can sign in to the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager), and select the secret: `/[MCSDeploymentID]/WorkstationManagement/Leostream/Console/AdminUserCredentials`. Choose the **Overview** tab, then choose the **Retrieve secret value** button to display the user login and password. Alternatively, you can access the credentials directly by clicking the **View** button on the MCS Web UI and following the direct link to the secret.

1. Modular Cloud Studio on AWS automatically configures Leostream Broker internal resources during the deployment process of this module. The updated resources include:
   + Remote Authentication Servers
   + AWS Center
   + EC2 Workstation Pools
   + Policies
   + Power Control Plans and Release Plans
