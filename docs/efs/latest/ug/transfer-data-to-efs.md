---
source_url: https://docs.aws.amazon.com/efs/latest/ug/transfer-data-to-efs.html
---

# Transferring data in and out of Amazon EFS
<a name="transfer-data-to-efs"></a>

You can use AWS DataSync and AWS Transfer Family to transfer data in and out of your Amazon EFS file systems. AWS DataSync is an online data transfer service that can copy data between Network File System (NFS), Server Message Block (SMB) file servers, self-managed object storage, and also between AWS services. For more information about using DataSync with Amazon EFS, see [Using AWS DataSync to transfer data](trnsfr-data-using-datasync.md).

AWS Transfer Family is a fully managed AWS service that you can use to transfer files into and out of Amazon EFS file systems over the Secure File Transfer Protocol (SFTP), File Transfer Protocol (FTP), and FTP over Secure Sockets Layer (FTPS) protocol. Using Transfer Family, you can provide your business partners access to files stored in your Amazon EFS file systems for use cases such as data distribution, supply chain, content management, and web serving applications. For more information about using Transfer Family with Amazon EFS, see [Using AWS Transfer Family to transfer data](using-aws-transfer-integration.md).

**Topics**
+ [Using AWS DataSync to transfer data](trnsfr-data-using-datasync.md)
+ [Using AWS Transfer Family to transfer data](using-aws-transfer-integration.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
