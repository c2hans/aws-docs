---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/update-app-block.html
---

# Update the App Block, VHD, and Setup Script
<a name="update-app-block"></a>

App block resources are immutable and do not allow you to change them once created. If you need to make backwards compatible updates to the VHD or setup script, it is recommended that you upload a new version of the file to the Amazon S3 bucket, overwriting the current version. New Elastic fleet streaming sessions will download the latest version of the objects, and use them.

If you need to make backwards incompatible updates to the VHD or setup script, it is recommended that you upload them as new objects to the Amazon S3 bucket, and create a new app block and application resource. You can then manage the deployment to your users as part of a change window or other outage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
