---
source_url: https://docs.aws.amazon.com/filegateway/latest/files3/create-smb-file-share.html
---

# Create an SMB file share
<a name="create-smb-file-share"></a>

The Server Message Block (SMB) protocol is deeply integrated into the Microsoft Windows product suite, and remains the default file sharing protocol for Windows operating systems. The process of client-server communication is similar to NFS at a high level, but there are differences in some details and operational mechanisms. For example, in SMB, file systems are not mounted on the local SMB client. Instead, a network share hosted on the SMB server is accessed via a network path.

The topics in this section explain various methods for creating an SMB file share for your File Gateway.

**Contents**
+ [Create an SMB file share using the default configuration](smb-fileshare-quickstart-settings.md)
  + [Default configuration settings for SMB file shares](smb-fileshare-quickstart-settings.md#quickstart-default-settings)
+ [Create an SMB file share with a custom configuration](CreatingAnSMBFileShare.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query filegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
