---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/input-output-formats.html
---

# Input and output formats
<a name="input-output-formats"></a>

Jobs require input data in [Apache Parquet](https://parquet.apache.org/docs/overview/) format stored in Amazon S3. Your input files must conform to a specific schema corresponding to the action you want to perform. The service writes results back to Amazon S3 in Parquet format, preserving all original input data and adding results from the processed action.

Input files have a limitation of 10 GB per file, and 1 GB per Parquet row-group within the file.

For more information, see [How to prepare input data](https://docs.aws.amazon.com/location/latest/developerguide/preparing-input-data.html) and [How to retrieve results](https://docs.aws.amazon.com/location/latest/developerguide/retrieving-results.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
