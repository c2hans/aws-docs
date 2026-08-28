---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/fine-grained-access-control.html
---

# Fine-grained access control to data in Amazon DataZone
<a name="fine-grained-access-control"></a>

In the current release of Amazon DataZone, fine-grained access control of your data is supported, enabling you to have granular access control over your sensitive data. You can control which project can access specific records of data within your data assets published to the Amazon DataZone business data catalog. Amazon DataZone supports row and column filters to implement fine-grained access control.

**Row filters** enable you to restrict access to specific rows based on the criteria you define. For example, if your table contains data for two regions (America and Europe) and you want to ensure that employees in Europe can only access data relevant to their region, you can create a row filter that includes rows where the region is Europe (e.g., region = 'Europe'). This way, employees in Europe won't have access to America’s data.

**Column filters** enable you to limit access to specific columns within your data assets. For example, if your table includes sensitive information such as Personally Identifiable Information (PII), you can create a column filter to exclude PII columns. This ensures that subscribers can only access non-sensitive data.

To utilize fine-grained access control, you can create row and column filters for your AWS Glue and Amazon Redshift assets in Amazon DataZone. When a subscription request to access your data assets is received, you can approve it by applying the appropriate row and column filters. Amazon DataZone ensures that the subscriber can only access the rows and columns permitted by the filters you applied at the time of subscription approval.

**Topics**
+ [Create row filters in Amazon DataZone](create-row-filter.md)
+ [Create column filters in Amazon DataZone](create-column-filter.md)
+ [Delete row or column filters in Amazon DataZone](delete-row-column-filter.md)
+ [Edit row or column filters in Amazon DataZone](edit-row-column-filter.md)
+ [Grant access with filters in Amazon DataZone](grant-access-with-filters.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
