---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/change-type.html
---

# Changing the identity provider type for Amazon WorkSpaces Secure Browser
<a name="change-type"></a>

You can change the authentication type of your portal at any time. To do this, follow these steps.
+ To change from **IAM Identity Center** to **Standard**, follow the steps at [Configuring the standard authentication type for Amazon WorkSpaces Secure Browser](configure-standard.md).
+ To change from **Standard** to **IAM Identity Center**, follow the steps at [Configuring the IAM Identity Center authentication type for Amazon WorkSpaces Secure Browser](configure-iam.md).

Changes to the identity provider type may take up to 15 minutes to deploy, and will not automatically terminate in-progress sessions.

You can view identity provider type changes to your portal through AWS CloudTrail by inspecting `UpdatePortal` events. The type is visible in the request and response payloads of the event.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
