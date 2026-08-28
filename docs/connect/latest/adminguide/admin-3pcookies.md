---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/admin-3pcookies.html
---

# Using Connect Customer with third-party cookies
<a name="admin-3pcookies"></a>

## Google Chrome
<a name="admin-3pcookies-google"></a>

On Jul 22, 2024, Google [announced](https://privacysandbox.com/news/privacy-sandbox-update/) that they no longer plan to deprecate third-party cookies and instead will provide an opt-in mechanism for deprecating third-party cookies. Amazon Connect uses third-party cookies for authentication. With this announcement, Amazon Connect customers using Google Chrome no longer need to upgrade to StreamsJS or CTI Adapter versions that address third-party cookie deprecation, which were planned for release in Q3 2024. No customer action is needed at this time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
