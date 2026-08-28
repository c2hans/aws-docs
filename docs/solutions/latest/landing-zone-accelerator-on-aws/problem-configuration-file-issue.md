---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-configuration-file-issue.html
---

# Problem: Configuration file issue
<a name="problem-configuration-file-issue"></a>

## Resolution
<a name="resolution"></a>

It is critical that the configuration files follow the property conventions defined. For more details, refer to the [configuration reference](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/user-guide/config/) in our [GitHub Pages website](https://awslabs.github.io/landing-zone-accelerator-on-aws/). Deviations cause an error during the **Build** stage of the pipeline. During this stage, type validation of the configuration files occurs, and variances cause the pipeline to fail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
