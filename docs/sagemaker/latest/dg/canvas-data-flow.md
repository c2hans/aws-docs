---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-flow.html
---

# Create a data flow
<a name="canvas-data-flow"></a>

Use a Data Wrangler flow in SageMaker Canvas, or *data flow*, to create and modify a data preparation pipeline. We recommend that you use Data Wrangler for datasets larger than 5 GB.

To get started, use the following procedure to import your data into a data flow.

1. Open SageMaker Canvas.

1. In the left-hand navigation, choose **Data Wrangler**.

1. Choose **Import and prepare**.

1. From the dropdown menu, choose either **Tabular** or **Image**.

1. For **Select a data source**, choose your data source and select the data that you want to import. You have the option to select up to 30 files or one folder. If you have a dataset already imported into Canvas, choose **Canvas dataset** as your source. Otherwise, connect to a data source such as Amazon S3 or Snowflake and browse through your data. For information about connecting to a data source or importing data, see the following pages:
   + [Data import](canvas-importing-data.md)
   + [Connect to data sources](canvas-connecting-external.md)

1. After selecting the data that you want to import, choose **Next**.

1. (Optional) For the **Import settings** section when importing a tabular dataset, expand the **Advanced** dropdown menu. You can specify the following advanced settings for data flow imports:
   + **Sampling method** – Select the sampling method and sample size you'd like to use. For more information about how to change your sample, see the section [Edit the data flow sampling configuration](canvas-data-flow-edit-sampling.md).
   + **File encoding (CSV)** – Select your dataset file’s encoding. `UTF-8` is the default.
   + **Skip first rows** – Enter the number of rows you’d like to skip importing if you have redundant rows at the beginning of your dataset.
   + **Delimiter** – Select the delimiter that separates each item in your data. You can also specify a custom delimiter.
   + **Multi-line detection** – Select this option if you’d like Canvas to manually parse your entire dataset for multi-line cells. Canvas determines whether or not to use multi-line support by taking a sample of your data, but Canvas might not detect any multi-line cells in the sample. In this case, we recommend that you select the **Multi-line detection** option to force Canvas to check your entire dataset for multi-line cells.

1. Choose **Import**.

You should now have a new data flow, and you can begin adding transform steps and analyses.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
