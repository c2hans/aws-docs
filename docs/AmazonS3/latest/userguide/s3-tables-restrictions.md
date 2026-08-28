---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-restrictions.html
---

# Security considerations and limitations for S3 Tables
<a name="s3-tables-restrictions"></a>

The following list describes which security and access control features and functionality are unsupported or limited for S3 Tables.
+ Public access policies are not supported. Users can't modify bucket or table policies to allow public access.
+ Presigned URLs to access objects associated with a table are not supported.
+ Requests made over HTTP are not supported. Amazon S3 automatically responds with an HTTP redirect for any requests made over HTTP to upgrade the requests to HTTPS.
+ You must use AWS Signature Version 4 when making requests to an access point by using the REST APIs.
+ Requests made over the Internet Protocol version 6 (IPv6) are supported only for object-level actions over table storage endpoints, and not for the table- and bucket-level actions.
+ Table bucket and table access policies are limited to 20 KB in size.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
