---
source_url: https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref.html
---

# Technical reference
<a name="techref"></a>

In the W3C WebDriver model, the feature operates as an intermediary node. It provides a means to start, end, and manage sessions.

 Here is the functional flow for using the feature:

1. Use the `createTestGridProject` API to create a project.

1. Use the `createTestGridUrl` API to create a signed WebDriver hub URL.

1. Pass the WebDriver URL to your Selenium `RemoteWebDriver` configuration.

1. Run your tests.

1. Use the `listTestGridSessions` API to retrieve the sessions created in the running of your tests.

1. Use the `listTestGridSessionArtifacts` API to collect any artifacts such as Selenium logs or video.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
