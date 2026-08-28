---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/put-object-ap.html
---

# Uploading a file using an S3 access point
<a name="put-object-ap"></a>

The following `put-object` example command shows how you can use the AWS CLI to upload a file through an access point. You must include an outfile, which is a file name for the uploaded object.

The example uploads the file {{`my-new-image.jpg`}} through the access point {{`my-ontap-ap`}} and saves the uploaded file as {{`my-new-image.jpg`}}.

```
$ aws s3api put-object --bucket {{my-ontap-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias --key {{my-new-image.jpg}} --body  {{my-new-image.jpg}}
```

You can also use the REST API to upload an object through an access point. For more information, see [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) in the *Amazon Simple Storage Service API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
