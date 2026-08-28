---
source_url: https://docs.aws.amazon.com/filegateway/latest/files3/edit-nfs-client.html
---

# Limit client access for your NFS file share
<a name="edit-nfs-client"></a>

We recommend editing the NFS client access settings to to define a list of specific client IP addresses or CIDR block ranges for NFS clients that are allowed to connect to your NFS file share. If you choose not to limit access, any client on your network can mount to your file share.

**To limit client access for your NFS file share**

1. Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/).

1. Choose **File shares** from the navigation pane on the left side of the console page, and then choose the **File share ID** of the NFS file share that you want to edit.

1. From the **Actions** drop down menu, choose **Edit file share access settings**.

   The **Access object** section displays a list of IP addresses and CIDR blocks that are currently allowed to connect to the NFS file share. If access is not currently limited, you will see an entry under **Allowed clients** for the 0.0.0.0/0 CIDR block, which indicates that all possible IPv4 addresses are allowed to connect.

1. Under **Allowed clients**, to the right of the 0.0.0.0/0 CIDR block, choose **Remove**.

1. Choose **Add client**, and then provide an IP address or address range in CIDR notation for the clients that you want to allow.

1. Repeat the previous step to add more IP addresses or ranges as necessary. If make a mistake or need to revoke access, you can choose **Remove** to the right of the IP address or range that you want to delete from the list.

1. Choose **Save changes** when finished.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query filegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
