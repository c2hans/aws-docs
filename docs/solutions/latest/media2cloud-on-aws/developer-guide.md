---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/developer-guide.html
---

# Developer guide
<a name="developer-guide"></a>

 This section provides the source code for the solution and additional customizations.

## Source code
<a name="source-code"></a>

 Visit our [GitHub repository](https://github.com/aws-solutions/media2cloud) to download the templates and scripts for this solution, and to share your customizations with others.

## Considerations for customizing the solution
<a name="considerations-for-customizing-the-solution"></a>

### Bucket Region
<a name="bucket-region"></a>

 If you specify your own S3 ingestion (and/or proxy) buckets, ensure the bucket(s) are in the same AWS Region as the Region where the solution is deployed to avoid cross-Region data transfer costs.

### Bucket CORS settings
<a name="bucket-cors-settings"></a>

 If you decide to use your own Amazon S3 ingest (and/or proxy) bucket, the solution updates your bucket's CORS settings to allow the web interface to perform cross origin GET/POST requests. The following example shows the CORS settings:

```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>https://<cf-id>.cloudfront.net</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <AllowedMethod>DELETE</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <ExposeHeader>Content-Length</ExposeHeader>
    <ExposeHeader>ETag</ExposeHeader>
    <ExposeHeader>x-amz-meta-uuid</ExposeHeader>
    <ExposeHeader>x-amz-meta-md5</ExposeHeader>
    <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
