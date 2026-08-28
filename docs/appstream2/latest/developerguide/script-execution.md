---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/script-execution.html
---

# App block setup script execution in Amazon WorkSpaces Applications
<a name="script-execution"></a>

The following diagrams indicate where in the process the setup script runs. The run order is dependent upon whether Application Settings Persistence is enabled on the stack associated with the elastic fleet.

**Note**
WorkSpaces Applications uses your VPC details to download the VHD and setup script from the Amazon S3 bucket. Your VPC must provide access to the Amazon S3 bucket. For more information, see [Using Amazon S3 VPC Endpoints for WorkSpaces Applications Features](managing-network-vpce-iam-policy.md).

Application Settings Persistence is enabled:

![Application Settings Persistence is enabled.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/app-settings-enabled.png)

Application Settings Persistence is disabled:

![Application Settings Persistence is disabled.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/app-settings-disabled.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
