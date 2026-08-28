---
source_url: https://docs.aws.amazon.com/filegateway/latest/files3/guest-access.html
---

# Provide guest access to your file share
<a name="guest-access"></a>

You can configure your S3 File Gateway to allow guest access for any user that is able to provide the correct guest account username and password. If you want this to be the only method by which users can access your file gateway, then you do not need to join the gateway to a Microsoft Active Directory domain. You can also use this guest access method to create file shares on an S3 File Gateway that is a member of an Active Directory domain.

When you configure a file share to use the **Guest Access** authentication method, the guest access username is `smbguest`. Before you can create a file share using guest access, you need to change the default password for the `smbguest` user.

You can use the following procedure to change the password for the guest user `smbguest`.

**To change the guest access password**

1. Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/).

1. Choose **Gateways** from the navigation pane on the left side of the console page, and then choose the **Name** of the gateway for which you want to provide guest access.

1. From the **Actions** drop down menu, choose **Edit SMB settings**, and then choose **Guest access settings**.

1. For **Guest password**, enter the guest access password you want to set, and then choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query filegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
