---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-cost.html
---

# Amazon SageMaker Studio pricing
<a name="studio-updated-cost"></a>

**Important**
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md).

There is no additional charge for using the Amazon SageMaker Studio UI.

The following do incur costs:
+ Amazon Elastic Block Store or Amazon Elastic File System volumes that are mounted with your applications.
+ Any jobs and resources that users launch from Studio applications.
+ Launching a JupyterLab application, even if no resources or jobs launched in the application.

For information about how Amazon SageMaker Studio Classic is billed, see [Amazon SageMaker Studio Classic Pricing](studio-pricing.md).

For more information about billing along with pricing examples, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
