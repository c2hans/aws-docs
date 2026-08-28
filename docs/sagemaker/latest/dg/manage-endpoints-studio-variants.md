---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-studio-variants.html
---

# View Variants (or Models)
<a name="manage-endpoints-studio-variants"></a>

The **Variants** tab (also called the **Models** tab if your endpoint has multiple models deployed) shows you the list of [model variants](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html) or models currently deployed to your endpoint. The following screenshot shows you what the overview and **Models** section looks like for an endpoint with multiple models deployed.

![Screenshot of an endpoint's main page showing multiple models deployed.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/studio-goldfinch-multi-model-endpoint.png)

You can add or edit the settings for each variant or model. You can also select a variant and enable a default auto-scaling policy, which you can edit later in the **Auto-scaling** tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
