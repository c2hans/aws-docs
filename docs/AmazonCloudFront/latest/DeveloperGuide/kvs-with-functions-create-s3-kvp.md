---
source_url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions-create-s3-kvp.html
---

# File format for key-value pairs
<a name="kvs-with-functions-create-s3-kvp"></a>

When you create a UTF-8 encoded file, use the following JSON format:

```
{
  "data":[
    {
      "key":"{{key1}}",
      "value":"{{value}}"
    },
    {
      "key":"{{key2}}",
      "value":"{{value}}"
    }
  ]
}
```

Your file can't include duplicate keys. If you specified an invalid file in your Amazon S3 bucket, you can update the file to remove any duplicates and then try creating your key value store again.

For more information, see [Create a key value store](kvs-with-functions-create.md).

**Note**
The file for your data source and its key-value pairs have the following limits:
File size – 5 MB
Key size – 512 characters
Value size – 1024 characters

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudFront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
