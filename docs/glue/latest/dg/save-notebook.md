---
source_url: https://docs.aws.amazon.com/glue/latest/dg/save-notebook.html
---

# Saving your notebook and job script
<a name="save-notebook"></a>

 You can save your notebook and the job script you are creating at any time. Simply choose the **Save** button in the upper right corner, the same as if you were using the visual or script editor.

 When you choose **Save**, the notebook file is saved in the default locations:
+  By default, the job script is saved to the Amazon S3 location indicated in the **Job Details** tab, under **Advanced properties**, in the Job details property **Script path**. Job scripts are saved in a subfolder named `Scripts`.
+  By default, the notebook file (`.ipynb`) is saved to the Amazon S3 location indicated in the **Job Details** tab, under **Advanced properties**, in the Job details **Script path**. Notebook files are saved in a subfolder named `Notebooks`.

**Note**
 When you save the job, the job script contains only the code cells from the notebook. The Markdown cells and magics aren't included in the job script. However, the `.ipynb` file will contain any markdown and magics.

 After you save the job, you can then run the job using the script that you created in the notebook.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
