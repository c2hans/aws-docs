---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/incremental_file_upload.html
---

# Uploading subsequent files to an existing source
<a name="incremental_file_upload"></a>

There are two ways to upload subsequent datasets to an existing source. You can either upload the dataset on the Amazon S3 path displayed under the **Source Flows** tab, or choose **Upload files** under the **Actions** tab.

If you're using an automated connector, executing scripts, or using a middle ware solution to ingest the dataset into AWS Supply Chain, you must update the Amazon S3 path with the Amazon S3 path displayed under the **Source Flows** tab.

**Note**
If an existing file with the same file name is re uploaded to Amazon S3, AWS Supply Chain will overwrite the file on Amazon S3.

![Data ingestion for subsequent file uploads](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/Data_lake_upload.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
