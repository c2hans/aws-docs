---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDomainsExport.html
---

# Exporting a Domain to Amazon Simple Storage Service
<a name="WorkingWithDomainsExport"></a>

 Amazon SimpleDB allows you to export domain data to Amazon S3 for migration and archival. The export process runs asynchronously in the background and does not affect the performance of your active database operations. Exported data is stored in standard JSON format.

The new Amazon SimpleDB export operations are only available through the SimpleDBv2 service in newer versions of the AWS SDKs and AWS CLI.

**Important**
 Exported data cannot be restored back to Amazon SimpleDB. The export feature is designed for one-way data migration and archival. After you have exported your Amazon SimpleDB data to Amazon S3, you can't import the data again.

 This section covers the following topics:

**Topics**
+ [Prerequisites and Permissions](ExportPrerequisites.md)
+ [Export a domain to Amazon S3](HowToExportDomainToS3.md)
+ [Export Considerations](ExportConsiderations.md)
+ [Track Export Status](TrackingExportStatus.md)
+ [List Exports in an Account](ListingExports.md)
+ [Log Amazon SimpleDB export calls with AWS CloudTrail](LoggingExportsCloudTrail.md)
+ [Best Practices for Domain Exports](ExportBestPractices.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
