---
source_url: https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-convert.html
---

# Converting a script or notebook into an AWS Glue job
<a name="interactive-sessions-convert"></a>

 There are two ways you can convert a script or notebook into an AWS Glue job:
+  Use **nbconvert** to convert your Jupyter `.ipynb` notebook document file into a `.py` file. For more information, see [nbconvert: Convert Notebooks to other formats](https://nbconvert.readthedocs.io/en/latest/).
+  Upload the file to AWS Glue Studio Notebooks.
  +  In the AWS Glue Studio console, choose **Jobs** from the navigation menu.
  +  In the **Create job** section, choose **Jupyter Notebook**.
  +  In the **Options** section, choose **Upload and edit an existing notebook**.
  +  Select **Choose file** to upload an `.ipynb` file.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
