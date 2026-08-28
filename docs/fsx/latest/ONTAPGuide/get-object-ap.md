---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/get-object-ap.html
---

# Downloading a file using an S3 access point
<a name="get-object-ap"></a>

The following `get-object` example command shows how you can use the AWS CLI to download a file through an access point. You must include an outfile, which is a file name for the downloaded object.

The example requests the file {{`my-image.jpg`}} through the access point {{`my-ontap-ap`}} and saves the downloaded file as {{`download.jpg`}}.

```
$ aws s3api get-object --key {{my-image.jpg}} --bucket {{my-ontap-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias {{download.jpg}}
{
    "AcceptRanges": "bytes",
    "LastModified": "Mon, 14 Oct 2024 17:01:48 GMT",
    "ContentLength": 141756,
    "ETag": "\"00751974dc146b76404bb7290f8f51bb-1\"",
    "ContentType": "binary/octet-stream",
    "ServerSideEncryption": "SSE_FSX",
    "Metadata": {},
    "StorageClass": "FSX_ONTAP"
}
```

You can also use the REST API to download an object through an access point. For more information, see [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) in the *Amazon Simple Storage Service API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
