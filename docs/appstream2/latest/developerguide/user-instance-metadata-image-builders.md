---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/user-instance-metadata-image-builders.html
---

# Instance Metadata for WorkSpaces Applications Image Builders
<a name="user-instance-metadata-image-builders"></a>

WorkSpaces Applications image builder instances have instance metadata available through Windows environment variables. You can use the following environment variables in your applications and scripts to modify your environment based on the image builder instance details.

| Environment Variable | Context | Description |
| --- | --- | --- |
| AppStream\_Image\_Arn | Machine | The ARN of the image that was used to create the streaming instance. |
| AppStream\_Instance\_Type | Machine | The instance type of the streaming instance. For example, stream.standard.medium. |
| AppStream\_Resource\_Type | Machine | The type of WorkSpaces Applications resource. The value is either fleet or imagebuilder. |
| AppStream\_Resource\_Name | Machine | The name of the image builder. |

On Linux image builders, environment variables are exported through the script at **/etc/profile.d/appstream\_system\_vars.sh**. To access the environment variables, you can explicitly source this file in your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
