---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-taskrunner-proxy.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Using Task Runner with a Proxy
<a name="dp-taskrunner-proxy"></a>

If you are using a proxy host, you can either specify its [configuration](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-taskrunner-config-options.html) when invoking Task Runner or set the environment variable, HTTPS\_PROXY. The environment variable used with Task Runner accepts the same configuration used for the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-http-proxy.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
