---
source_url: https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections-how-it-works-github-organizations.html
---

# How connections in AWS CodeConnections work with organizations
<a name="welcome-connections-how-it-works-github-organizations"></a>

For organizations with a provider, such as GitHub Organizations, you cannot install a GitHub app into multiple GitHub Organizations. A connection has a 1:1 mapping with an organization through the use of the Github connector app. The connector app should be separate for every organization in GitHub or GitHub Enterprise Server and should have a connection associated with it.

For example, to work with multiple organizations on the same GitHub server, you must create separate connections for each organization and install separate GitHub apps for these organizations. The target account on the Github side, however, can be the same.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Developer Tools Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dtconsole` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
