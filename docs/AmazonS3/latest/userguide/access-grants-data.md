---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-data.html
---

# Getting S3 data using access grants
<a name="access-grants-data"></a>

Grantees who have been given access to S3 data through S3 Access Grants must request temporary credentials from S3 Access Grants, which they use to access the S3 data. For more information, see [Request access to Amazon S3 data through S3 Access Grants](access-grants-credentials.md). Grantees then use the temporary credentials to perform allowable S3 actions on the S3 data. For more information, see [Accessing S3 data using credentials vended by S3 Access Grants](access-grants-get-data.md). Grantees can optionally request a list of their access grants for an AWS account before requesting these credentials. For more information, see [List the caller's access grants](access-grants-list-grants.md).

**Topics**
+ [Request access to Amazon S3 data through S3 Access Grants](access-grants-credentials.md)
+ [Accessing S3 data using credentials vended by S3 Access Grants](access-grants-get-data.md)
+ [List the caller's access grants](access-grants-list-grants.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
