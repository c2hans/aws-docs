---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/restricting-browsing.html
---

# Restricting browsing to specific URLs
<a name="restricting-browsing"></a>

You can implement a "default deny" policy where only explicitly approved websites and URLs are accessible. It's ideal for high-security environments where internet access must be tightly controlled and every permitted site has been vetted for business necessity and security compliance.

In the AWS console, under URL filtering:
+ Navigate to Block list and select the toggle **Block all URLs**
+ Under Allow list, click **Add URL** to add a URL that will be allow listed for your end user. Add one entry per URL.
+ Click **Save**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
