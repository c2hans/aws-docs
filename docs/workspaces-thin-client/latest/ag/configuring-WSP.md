---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/configuring-WSP.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Configuring WorkSpaces Personal for WorkSpaces Thin Client
<a name="configuring-WSP"></a>

For WorkSpaces Thin Client to be used with Amazon WorkSpaces Personal, your service will need to be configured to access the WorkSpaces directories. Amazon WorkSpaces Personal directories are listed based on their directory names on the WorkSpaces Thin Client **Create environment** page within AWS console.

**Note**
Configurations must be made before using the console for the first time. It is not recommended that you modify any prerequisite features after you start using the console.

## Before you begin
<a name="configuring-WSP-before-begin"></a>

Make sure that you have an AWS account to create or administer a WorkSpace. Device users, however, don't need an AWS account to connect to and use their WorkSpaces.

Review and understand the following concepts before you proceed with your configuration:
+ When you launch a WorkSpace, select a WorkSpace bundle. For more information, see [Amazon WorkSpaces Bundles](https://aws.amazon.com/workspaces/features/#Amazon_WorkSpaces_Bundles).
+ When you launch a WorkSpace, select which protocol that you want to use with your bundle. For more information, see [ Protocols for Amazon WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-protocols.html).
+ When you launch a WorkSpace, specify the profile information for each user, including username and email address. Users complete their profiles by creating a password. Information about WorkSpaces and users is stored in a directory. For more information, see [Manage directories for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html).
+ When you launch a WorkSpace, enable and configure the WorkSpaces Thin Client web access. For more information, see [Configure WorkSpaces Thin Client](https://docs.aws.amazon.com/workspaces/latest/adminguide/access-control-awstc.html)

## Step 1: Verify that your system meets WorkSpaces Personal required features
<a name="workspaces-features"></a>

For WorkSpaces Thin Client administrator console to work properly with Amazon WorkSpaces Personal, your system must meet the following specific requirements. This table lists all of these supported features and their requirements.

| Feature | Requirement |
| --- | --- |
| Web access | Enabled |
| Supported operating system |  + Windows 10<br />+ Windows 10 (Bring Your Own License)<br />+ Windows 11<br />+ Windows 11 (Bring Your Own License)  |
| Supported bundles |  + Microsoft Power with Windows 10 (Server 2016, 2019, and 2022 based)<br />+ Microsoft Power with Windows 10 (Server 2016, 2019, and 2022 based) w Office<br />+ Microsoft PowerPro with Windows 10 (Server 2016, 2019, and 2022 based)<br />+ Microsoft PowerPro with Windows 10 (Server 2016, 2019, and 2022 based) w Office<br />+ Microsoft Performance with Windows 10 (Server 2016, 2019, and 2022 based)<br />+ Microsoft Performance with Windows 10 (Server 2016, 2019, and 2022 based) w Office  |
| Supported protocol | DCV only |

## Step 2: Use advanced setup to launch your WorkSpace
<a name="configuring-wsp-advanced-setup"></a>

**To use advanced setup to launch your WorkSpace**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home/](https://console.aws.amazon.com/workspaces/v2/home/).

1. Choose one of the following directory types, and then choose **Next**:
   + AWS Managed Microsoft AD
   + Simple AD
   + AD Connector

1. Enter the directory information.

1. Choose two subnets in a VPC from two different Availability Zones. For more information, see [Configure a VPC with public subnets](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html#configure-vpc-public-subnets).

1. Review your directory information and choose **Create directory**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
