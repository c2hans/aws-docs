---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-media-connect.html
---

# Requirements for AWS Elemental MediaConnect
<a name="requirements-for-media-connect"></a>

Your deployment might include using a flow from AWS Elemental MediaConnect as an input to AWS Elemental MediaLive.

Users need permissions to perform actions in MediaConnect when they use the MediaLive workflow wizard. Users don't need special permissions when they use the regular MediaLive console to specify a MediaConnect flow in an input or channel.

| Permissions | Service name in IAM | Actions |
| --- | --- | --- |
| Use the workflow wizard to create a MediaConnect flow, if your organization supports sources from MediaConnect.Use the workflow wizard to delete a workflow that includes a source from MediaConnect. | MediaConnect | List\*`Describe*`<br />`Create*`<br />`Delete*` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
