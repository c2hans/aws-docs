---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/http-validation-redirect-issues.html
---

# HTTP redirect issues
<a name="http-validation-redirect-issues"></a>

If you're using a redirect instead of serving the content directly, follow these steps to verify your configuration.

**To verify redirect configuration**

1. Copy the `RedirectFrom` URL and paste it into your browser's address bar.

1. In a new browser tab, paste the `RedirectTo` URL.

1. Compare the content at both URLs to ensure they match exactly.

1. Verify that the redirect returns a 302 status code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
