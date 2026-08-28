---
source_url: https://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/using-microsoft-power-bi-desktop-in-the-aws-cloud.html
---

# Using Microsoft Power BI Desktop in the AWS Cloud
<a name="using-microsoft-power-bi-desktop-in-the-aws-cloud"></a>

Using the Microsoft Power BI Desktop in the AWS Cloud is a popular solution for many of the challenges described in the previous section. In this model, customers host the Microsoft Power BI Desktop in the AWS Cloud, and then access it remotely on premises. The following diagram shows an example.

![A diagram depicting Microsoft Power BI Desktop deployed in the AWS Cloud](http://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/images/powerbi5.png)

*Microsoft Power BI Desktop deployed in the AWS Cloud *

Although the diagram depicts user connectivity to the desktop occurring through the internet, Site-to-Site VPN and Direct Connect are both valid connection types too. Because only graphical management traffic is transmitted, the bandwidth requirements are well suited for typical internet connections.

In this model the Microsoft Power BI Desktop is hosted within the Amazon VPC in a public subnet and has direct network connectivity to data sources with private IP addresses, such as Amazon RDS and Amazon Redshift. You can connect to Amazon Athena and other regional services by using a VPC endpoint connection as the destination (pictured in the diagram), or by using the regional public service endpoint.

There are a number of options for hosting Microsoft Power BI Desktop in the AWS Cloud:

## Option 1: Install Microsoft Power BI Desktop on an Amazon EC2 instance
<a name="option-1-install-microsoft-power-bi-desktop-on-an-amazon-ec2-instance"></a>

In this option, you create one or more Amazon EC2 instances with Microsoft Windows Server installed. Your users connect to the instance using a Remote Desktop Protocol (RDP) application and install, configure, and use Microsoft Power BI as they would as if it was installed on their laptop. By default, Windows Server installations are limited to two concurrent RDP client sessions. If you require more, you can buy Client Access Licenses from a Microsoft reseller. You might find that increasing the number of simultaneous users on a single server causes resource contention. You may achieve a better user experience by increasing the number of instances, each with fewer users.

## Option 2: Install Microsoft Power BI in an Amazon WorkSpaces environment
<a name="option-2-install-microsoft-power-bi-in-an-amazon-workspaces-environment"></a>

Amazon WorkSpaces is a managed, secure Desktop-as-a-Service (DaaS) solution. You can use Amazon WorkSpaces to provision either Windows or Linux desktops in just a few minutes and quickly scale to provide thousands of desktops to workers across the globe.

In this option, you provision Microsoft Windows Desktops with Microsoft Power BI Desktop installed for your users. Users can access the Windows desktop using a lightweight client application that is available for Android, iOS, Fire, Mac, PC, Chromebook, and Linux devices.

Using Amazon WorkSpaces, Microsoft Power BI Desktop users have dedicated resources, and desktops can be automatically stopped to save costs. This option also has the advantage of allowing non-Windows devices to access Amazon WorkSpaces, as well as providing users a desktop environment for performing other tasks, such as accessing Microsoft Office or other Windows applications.

## Option 3: Install Microsoft Power BI in an Amazon AppStream 2.0 environment
<a name="option-3-install-microsoft-power-bi-in-an-amazon-appstream-2.0-environment"></a>

Amazon AppStream 2.0 is a fully-managed application streaming service. You centrally manage your desktop applications on AppStream 2.0 and securely deliver them to any computer. You can easily scale to any number of users across the globe without acquiring, provisioning, and operating hardware or infrastructure.

In this option, you provide your on-premises users just the Microsoft Power BI Desktop application, streamed to an HTML5-compliant web browser, with no plugins required. Like the Amazon WorkSpaces option, non-Windows devices can connect and users have access to dedicated resources.

One downside to this option is that by default, AppStream 2.0 applications are limited to 1 GB of storage capacity, which may not be suitable for saving larger models and reports. The capacity can be increased by combining file storage from Amazon FSx for Windows File Server, but this introduces additional complexity that customers should be aware of.

 *Table 4 — Considerations for Power BI Desktop running in the AWS Cloud *

|  Criteria  |  Considerations for Power BI Desktop running in the AWS Cloud  |
| --- | --- |
|  Network connectivity  | Network connectivity to data sources is straightforward because both the data consumer and the data sources reside in the AWS Cloud. Data sources that reside in an Amazon VPC, such as Amazon RDS and Amazon Redshift, can be accessed directly. Data sources that use regional endpoints can be accessed through the Amazon VPC internet gateway, or an Amazon VPC endpoint. <br />Connectivity to the Microsoft Power BI Desktop occurs over the internet, Site-to-Site VPN, or AWS Direct Connect. All three options have modest requirements that most internet connections can meet.  |
|  Security  | **IP access control** <br />Customers can use a combination of routing and security groups to control access to data sources stored in the AWS Cloud. <br />For the first option (using Amazon EC2), you can additionally use a combination of routing and security groups to allow only specific on-premises CIDR ranges. <br />**Encryption in transit** <br />We recommend that data sources within an Amazon VPC are configured to use encryption for transmission of data. Regional services already make use of TLS encryption. <br />Management access is encrypted for all three options. <br />**Authentication** <br />AWS recommends that you authenticate with AWS data sources using an identity that has read-only access only to the datasets required. <br />All three options require the use of an authentication mechanism in order for the remote user to prove their identity before accessing the environment that hosts Microsoft Power BI Desktop. This mechanism is typically sign-in credentials, but MFA options are available as well.  |
|  Performance  | When running in the AWS Cloud, Microsoft Power BI Desktop performance is typically better than when run on premises. Both networking and compute instances are likely to be modern and have higher specifications, and there is likely to be low latency between the application and the data sources.  |
|  Cost  | By placing Microsoft Power BI Desktop in the AWS Cloud, data transfer charges can be significantly reduced or removed entirely. Use care when accessing data sources across Availability Zones, in different VPC’s, or in different Regions, because data transfer charges can apply. <br />For each option, there are additional cost considerations that need to be factored in. Amazon EC2, Amazon WorkSpaces, and Amazon AppStream 2.0 are priced based on usage. For more information, see the pricing page for each service.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
