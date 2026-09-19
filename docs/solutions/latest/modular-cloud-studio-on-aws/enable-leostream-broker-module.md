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

<table>
<thead>
  <tr><th> <b>Parameter</b> </th><th> <b>Default</b> </th><th> <b>Description</b> </th></tr>
</thead>
<tbody>
  <tr><td>Leostream Broker Fully Qualified Domain Name (optional)</td><td> <i>Optional input</i> </td><td>Specify the FQDN that will be routed to the broker load balancer. If no accompanying Certificate ID is supplied, a self-signed certificate will be generated for this domain. (This parameter is required if you specified a Certificate ID).</td></tr>
  <tr><td>Leostream Broker Certificate ID (optional)</td><td> <i>Optional input</i> </td><td>Specify the Certificate ID or ARN imported from AWS Certificate Manager to validate your FQDN. If you leave this field blank, the module will create a self-signed certificate from the domain you previously provided. See <a href="https://docs.aws.amazon.c%20om/acm/latest/userguide/acm-public-cer%20tificates.html#request-public-console">Get certificates ready in AWS Certificate Manager</a> for more information on how to set up a certificate. </td></tr>
  <tr><td>Leostream License Contact Email</td><td> {{&lt;_Requires input_&gt;}} </td><td>Contact email to use for the Leostream license. The free Leostream Broker license included in this module will be registered under this email.</td></tr>
  <tr><td>Leostream License Contact Name</td><td> {{&lt;_Requires input_&gt;}} </td><td>Contact name to use for the Leostream license. The free Leostream Broker license included in this module will be registered under this name.</td></tr>
  <tr><td>Leostream Broker Package Location</td><td> <a href="https://s3.amazonaws.com/downloads.leostream.com/leostream-broker-2024.1.7-1.x86_64.rpm">https://s3.amazonaws.com/downloads.leostream.com/leostream-broker-2024.1.7-1.x86_64.rpm</a> </td><td>Amazon S3 download URL for the Leostream Broker RPM package.</td></tr>
  <tr><td>Leostream Broker Max Instances Count</td><td>5</td><td>The maximum amount of Leostream Broker instances that the Auto Scaling Group can scale up to.</td></tr>
  <tr><td>Workstation Provision Threshold</td><td>1</td><td>Start provisioning new workstations if the number of available workstations is less than this threshold. The Leostream Broker will not provision if the number of workstations reaches the set maximum count. The initial value must be an integer of 1 or greater. If you need a different value later, you can open the Leostream console and change the value to any non-negative integer, including 0. </td></tr>
  <tr><td>Workstation Max Count</td><td> <code>2</code> </td><td>Maximum number of workstations to be provisioned by the Leostream Broker. This number applies for each Windows and Linux pool.</td></tr>
  <tr><td>Workstation Windows2022 AMI</td><td> <code>Yes</code> </td><td>Select if you want to deploy the Windows AMI.</td></tr>
  <tr><td>Amazon DCV Windows Server URL</td><td> <code>https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/Servers/nice-dcv-server-x64-Release-2024.0-18131.msi</code> </td><td>URL to download the Amazon DCV Windows server file.</td></tr>
  <tr><td>Leostream Windows Agent URL</td><td> <code>https://downloads.leostream.com/LeostreamAgentSetup2024-1-4-0.exe</code> </td><td>URL to download the Leostream Windows agent file.</td></tr>
  <tr><td>Workstation Rocky Linux8 AMI</td><td> <code>No</code> </td><td>Select if you want to deploy the Linux AMI. If you select Yes, ensure that you have subscribed <a href="http://aws.amazon.com/marketplace/pp/prodview-2otariyxb3mqu">Rocky Linux 8</a> on the AWS Marketplace.</td></tr>
  <tr><td>Amazon DCV Linux Server URL</td><td> <code>https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/Servers/nice-dcv-2024.0-18131-el8-x86_64.tgz</code> </td><td>URL to download the Amazon DCV Linux server file.</td></tr>
  <tr><td>Leostream Linux Agent URL</td><td> <code>https://downloads.leostream.com/LeostreamAgentJava-5.3.18.0.jar</code> </td><td>URL to download the Leostream Linux agent file.</td></tr>
</tbody>
</table>

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
