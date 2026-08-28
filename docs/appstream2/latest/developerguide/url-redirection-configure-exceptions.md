---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/url-redirection-configure-exceptions.html
---

# Configure the exception list (optional)
<a name="url-redirection-configure-exceptions"></a>

The exception list lets you exclude specific URL patterns from redirection, even if they match the allowlist.

**How URL evaluation works**

URLs are evaluated in the following order:

1. **Check exception list first.** If a URL matches an exception pattern, it opens in the remote session (no redirection).

1. **Check allowlist second.** If a URL matches an allowlist pattern and is not in the exception list, it redirects to the local browser.

1. **Default behavior.** If a URL matches neither list, it opens in the remote session.

**Example scenarios**

*Scenario 1: Allow YouTube except for specific channels*
+ Allowlist: `https://www.youtube.com/*`
+ Exception list: `https://www.youtube.com/channel/UCrestrictedChannel`
+ Result: `https://www.youtube.com/watch?v=abc123` redirects to the local browser. `https://www.youtube.com/channel/UCrestrictedChannel` opens in the remote session.

*Scenario 2: Exclude specific subdomains*
+ Allowlist: `https://*.example.com/*`
+ Exception list: `https://admin.example.com/*`, `https://secure.example.com/*`
+ Result: `https://www.example.com/page` redirects to the local browser. `https://admin.example.com/dashboard` opens in the remote session.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
