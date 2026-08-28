---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/url-redirection-troubleshooting.html
---

# Troubleshooting
<a name="url-redirection-troubleshooting"></a>

**URLs not redirecting when expected**
+ Verify that the URL pattern includes the protocol (`https://`).
+ Check for typos in the pattern.
+ Verify that wildcards are used correctly.
+ Confirm that the feature is enabled on the stack.

**URLs redirecting when they are not expected to**
+ Add the URL pattern to the exception list.
+ Verify that exception list patterns are more specific than allowlist patterns.

**Local browser not launching**
+ Verify that the local device has a default browser configured.
+ Verify that the WorkSpaces Applications client is up to date.
+ Verify network connectivity on the local device.
+ On the web client, verify that popups are allowed on the streaming URL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
