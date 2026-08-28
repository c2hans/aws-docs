---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/googledrive-v1-field-mappings.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Google Drive data source connector field mappings
<a name="googledrive-v1-field-mappings"></a>

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields in your Amazon Q index.

The Amazon Q Google Drive connector supports the following entities and the associated reserved and custom attributes.

## Files
<a name="googledrive-v1-field-mappings-files"></a>

| Google Drive field name | Index field name | Description | Data type |
| --- | --- | --- | --- |
| authors | \_authors | Default | String list |
| mimeType | gd\_file\_mime\_type | Custom | String |
| size | gd\_size | Custom | Long (numeric) |
| webViewLink | \_source\_uri | Default | String |
| createdAt | \_created\_at | Default | Date |
| modifiedAt | \_last\_updated\_at | Default | Date |

## Comments
<a name="googledrive-v1-field-mappings-comments"></a>

| Google Drive field name | Index field name | Description | Data type |
| --- | --- | --- | --- |
| authors | \_authors | Default | String list |
| commentType | gd\_type | Custom | String |
| createdAt | \_created\_at | Default | Date |
| modifiedAt | \_last\_updated\_at | Default | Date |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
