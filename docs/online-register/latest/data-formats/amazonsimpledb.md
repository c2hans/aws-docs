---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonsimpledb.html
---

# Data retrieval APIs for Amazon SimpleDB
<a name="amazonsimpledb"></a>

Amazon SimpleDB provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="sdb-DomainMetadata"></a>[DomainMetadata](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DomainMetadata.html) | Return information about the domain, including when the domain was created, the number of items and attributes, and the size of attribute names and values | Read |
| <a name="sdb-GetAttributes"></a>[GetAttributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_GetAttributes.html) | Return all of the attributes associated with the item | Read |
| <a name="sdb-GetExport"></a>[GetExport](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_GetExport.html) | Return information for an existing domain export arn | Read |
| <a name="sdb-ListDomains"></a>[ListDomains](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_ListDomains.html) | List all domains | List |
| <a name="sdb-ListExports"></a>[ListExports](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_ListExports.html) | List all exports that were created. The results are paginated and can be filtered by domain name | List |
| <a name="sdb-Select"></a>[Select](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_Select.html) | Execute a query against the items in a domain | Read |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
