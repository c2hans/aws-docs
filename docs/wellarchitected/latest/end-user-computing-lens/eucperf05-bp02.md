---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp02.html
---

# EUCPERF05-BP02 Understand integrated storage capabilities (AppStream)
<a name="eucperf05-bp02"></a>

 For persistent, per-user storage, WorkSpaces Applications offers built-in connectors to Amazon S3 home folders, Google Drive for Google Workspace, and OneDrive for Business. For more information on these connectors, see [Enable and Administer Persistent Storage for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/persistent-storage.html).

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance-11"></a>

 Use Amazon S3 home folders when you need a simple, fully-managed solution for persisting user files between sessions and users don't need to access their files from outside their WorkSpaces Applications sessions. Use Google Drive for Google Workspaces or OneDrive for Business when you use Windows fleets and your users have a license for one of the services.

 If the integrated storage features of Amazon WorkSpaces Applications do not offer the capabilities you require, consider Amazon FSx for Windows File Server, Amazon FSx for NetApp ONTAP, or Amazon EC2 hosted file sharing. You can use these fully or partly-managed solutions to store user data or user profiles, such as FSLogix, close to your AWS EUC control plane.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
