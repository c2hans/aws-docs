---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets-naming.html
---

# Referencing access points for directory buckets
<a name="access-points-directory-buckets-naming"></a>

After you create an access point, you can use it as an endpoint to preform object operations. For access points for directory buckets, the access point alias is the same as the access point name. You can use the access point name instead of a bucket name for all data operations. For a list of these supported operations, see [Object operations for access points for directory buckets](access-points-directory-buckets-service-api-support.md).

## Referring to access points by virtual-hosted-style URIs
<a name="accessing-directory-bucket-through-s3-access-point"></a>

Access points only support virtual-host-style addressing. Access points use the same format as directory bucket endpoints. For more information, see [Regional and Zonal endpoints for directory buckets](s3-express-Regions-and-Zones.md).

S3 access points don't support access through HTTP. Access points support only secure access through HTTPS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
