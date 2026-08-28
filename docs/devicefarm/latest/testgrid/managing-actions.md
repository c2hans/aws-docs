---
source_url: https://docs.aws.amazon.com/devicefarm/latest/testgrid/managing-actions.html
---

# Actions in Device Farm desktop browser testing
<a name="managing-actions"></a>

 When you interact with the W3C WebDriver protocol, Device Farm logs the calls made as actions.

An `action` represents the WebDriver endpoint requested by your test's `RemoteWebDriver`. Actions consist of:
+ The HTTP `requestType` (method) used for the call.
+ The HTTP `statusCode` returned by the WebDriver API.
+ The time that the call was made.
+ The number, in milliseconds, it took to make the call.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
