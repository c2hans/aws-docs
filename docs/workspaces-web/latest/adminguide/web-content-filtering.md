---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/web-content-filtering.html
---

# Web content filtering in Amazon WorkSpaces Secure Browser
<a name="web-content-filtering"></a>

Web Content Filtering is a security and compliance feature that enables your organization to define policies and regulate content access within WorkSpaces Secure Browser. With Web Content Filtering, you can specify which URLs end users are allowed to access or block specific URLs or domain categories to restrict access, addressing critical security and regulatory compliance requirements.

**Note**
Although you can set up URL filtering policies via Chrome policies to block or allow specific domains, we don't recommend this approach because actions from Chrome policies will not be captured as part of the service logging capabilities. For comprehensive monitoring and compliance reporting, use the Web Content Filtering policies described on this page.

**Topics**
+ [Restricting browsing to specific URLs](restricting-browsing.md)
+ [Blocking specific URLs](blocking-specific-urls.md)
+ [Blocking categories](blocking-categories.md)
+ [Example of URLs](example-urls.md)
+ [Transferring Chrome policies](transferring-chrome-policies.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
