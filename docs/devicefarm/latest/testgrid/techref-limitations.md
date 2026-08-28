---
source_url: https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref-limitations.html
---

# Limitations of Device Farm desktop browser testing
<a name="techref-limitations"></a>

 Keep these limitations in mind when you use the desktop browser testing feature:
+ The feature is only available in the `us-west-2` (Oregon) region.
+  Not all Selenium interfaces are supported. The `pytest-selenium` package, for example, does not allow a command execution URL to be specified.
+ Each session you create is isolated from other sessions. Testing that involves multi-window or multi-session interaction is not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
