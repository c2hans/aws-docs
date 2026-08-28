---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-sql-execution.html
---

# SQL execution features of the JupyterLab SQL extension
<a name="sagemaker-sql-extension-features-sql-execution"></a>

You can execute SQL queries against your connected data sources in the SQL extension of JupyterLab. The following sections explain the most common parameters for running SQL queries inside JupyterLab notebooks:
+ Create a simple connection in [Create a simple magic command connection string](sagemaker-sql-extension-features-sql-execution-create-connection.md).
+ Save your query results in a pandas DataFrame in [Save SQL query results in a pandas DataFrame](sagemaker-sql-extension-features-sql-execution-save-dataframe.md).
+ Override or add to connection properties defined by your administrator in [Override connection properties](sagemaker-sql-extension-features-sql-execution-override-connection.md).
+ [Use query parameters to provide dynamic values in SQL queries](sagemaker-sql-extension-features-sql-execution-query-parameters.md).

When you run a cell with the `%%sm_sql` magic command, the SQL extension engine executes the SQL query in the cell against the data source specified in the magic command parameters.

To see the details of the magic command parameters and supported formats, run `%%sm_sql?`.

**Important**
To use Snowflake, users of the SageMaker distribution image version 1.6 must install the Snowflake Python dependency by running the following `micromamba install snowflake-connector-python -c conda-forge` command in a terminal of their JupyterLab application. Restart the JupyterLab server by running `restart-jupyter-server` in the terminal after the installation is complete.
For SageMaker distribution image versions 1.7 and later, the Snowflake dependency is pre-installed. No action is needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
