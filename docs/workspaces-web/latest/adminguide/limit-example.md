---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/limit-example.html
---

# Limit example for Amazon WorkSpaces Secure Browser
<a name="limit-example"></a>

As an example, assume an administrator is configuring two web portals in US East (N. Virginia) for 125 total users. Before creating the web portal, the administrator identifies the first web portal (Portal A) will support 100 users. When testing the workflow for these users, the administrator determines they will need the XL instance type to support streaming of audio and video during the session. The second web portal (Portal B) needs to be available for up to 25 users to support access to a single static webpage hosted in the customers VPC. When testing this use case, the administrator determines that the standard instance type can support this use case.

For portal A, the administrator must submit a service quota increase request to raise the limit for XL instances from the regions default (i.e., 5) to 100. Once fulfilled, the administrator can allocate the capacity by editing the web portal. For portal B, the administrator can move forward without requesting a quota increase (i.e., since the region has a default quota of 25 for standard instance type).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
