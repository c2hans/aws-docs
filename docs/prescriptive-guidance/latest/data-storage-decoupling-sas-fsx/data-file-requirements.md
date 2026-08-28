---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-storage-decoupling-sas-fsx/data-file-requirements.html
---

# Data file requirements
<a name="data-file-requirements"></a>

Before you deploy your SAS server on AWS, we recommend that you prepare your data files to meet important requirements. We recommend that your data files are:
+ Permanently and consistently referenceable by the same path/location
+ Securely available
+ Easily to share
+ Easy to access for end users
+ Recoverable through self-service
+ Able to integrate with existing Microsoft Active Directory environments

Amazon FSx for Windows File Server can help you meet all these requirements. FSx for Windows File Server provides fully managed shared storage that's built on Windows Server. FSx for Windows File Server has native support for Windows file system features and for the industry-standard Server Message Block (SMB) protocol that's used to access file storage over a network. Your SAS server can map to FSx for Windows File Server by using the SMB protocol.

A key standard feature of FSx for Windows File Server is encryption at rest. This is important if your organization must handle data that contains highly-sensitive information. Data in FSx for Windows File Server is always encrypted at rest, and you can use your own customer managed keys for encryption. For more information, see [Encryption at Rest](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption-at-rest.html) in the Amazon for FSx Windows User Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
