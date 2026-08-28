---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/add-deep-links.html
---

# Setting up deep links in Amazon WorkSpaces Secure Browser
<a name="add-deep-links"></a>

To allow permission for deep links, choose **Allowed** when creating user settings. The site you want to deep link to must be URL-encoded. For example, to link a user to “https://www.example.com/?query=true”, update the link to https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue.

A deeplink can contain up to 10 URLs, delineated by comma. For example:

https://<uuid>.workspaces-web.com/?deepLinks=https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue,https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue2,https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue3,https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue4.

For more information about allowing deep links, see [Configuring user settings for Amazon WorkSpaces Secure Browser](user-settings.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
