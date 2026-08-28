---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/APISummary.html
---

# API Summary
<a name="APISummary"></a>

The Amazon SimpleDB service consists of a small group of API calls that provide the core functionality you need to build your application. See [Operations](SDB_API_Operations.md) in the API Reference chapter for detailed descriptions of each option.
+ **CreateDomain—**Create domains to contain your data; you can create up to 250 domains. If you require additional domains, go to [https://console.aws.amazon.com/support/home\#/case/create?issueType=service-limit-increase&limitType=service-code-simpledb-domains](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-simpledb-domains).
+ **DeleteDomain—**Delete any of your domains
+ **ListDomains—**List all domains within your account
+ **PutAttributes—**Add, modify, or remove data within your Amazon SimpleDB domains
+ **BatchPutAttributes—**Generate multiple put operations in a single call
+ **DeleteAttributes—**Remove items, attributes, or attribute values from your domain
+ **BatchDeleteAttributes—**Generate multiple delete operations in a single call
+ **GetAttributes—**Retrieve the attributes and values of any item ID that you specify
+ **Select—**Query the specified domain using a SQL SELECT expression
+ **DomainMetadata—**View information about the domain, such as the creation date, number of items and attributes, and the size of attribute names and values
+ **StartDomainExport—**Initiates the export of a Amazon SimpleDB domain to an Amazon S3 bucket
+ **GetExport—**Returns information for an existing domain export
+ **ListExports—**Lists all exports that were created, with paginated results that can be filtered by domain name

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
