---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-jl-view.html
---

# View the JupyterLab version of a notebook from the console
<a name="nbi-jl-view"></a>

**Important**
JupyterLab 1 and JupyterLab 3 are no longer supported as of June 30, 2025. You can no longer create new or restart stopped notebook instances using these versions. Existing in-service instances may continue to function but will not receive security updates or bug fixes. Migrate to AL2023 (`notebook-al2023-v1`) for continued support. For more information, see [JupyterLab version maintenance](nbi-jl.md#nbi-jl-version-maintenance).

 You can view the JupyterLab version of a notebook using the following procedure:

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. From the left navigation, select **Notebook**.

1.  From the dropdown menu, select **Notebook instances** to navigate to the **Notebook instances** page.

1.  From the list of notebook instances, select your notebook instance name.

1.  On the **Notebook instance settings** page, view the **Platform Identifier** to see the JupyterLab version of the notebook.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
