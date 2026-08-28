---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-tutorial-enable-discovery.html
---

# Step 5: Enable dependency discovery (optional)
<a name="next-gen-tutorial-enable-discovery"></a>

Dependency discovery automatically identifies the AWS services, internal endpoints, and third-party endpoints that your service calls. It uses DNS query log analysis with a 35-day look-back window and continuous polling to identify dependencies you may not know about, including unexpected cross-Region calls or critical third-party dependencies.

Dependency discovery is an optional add-on. To enable it, navigate to your service in the console and choose **Enable dependency discovery**. Once enabled, the next generation of Resilience Hub begins discovering dependencies and surfaces them on the **Dependencies** tab of your service.

For more information, see [Dependency discovery](next-gen-dependency-discovery.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
