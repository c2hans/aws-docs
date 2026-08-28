---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/add-tag-set-ap.html
---

# Tagging a file using an S3 access point
<a name="add-tag-set-ap"></a>

The following `put-object-tagging` example command shows how you can use the AWS CLI to add a tag-set through an access point. Each tag is a key-value pair. For more information, see [Categorizing your storage using tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html) in the *Amazon Simple Storage Service User Guide*.

The example adds a tag-set to the existing file `my-image.jpg` using the access point {{`my-ontap-ap`}}.

```
$ aws s3api put-object-tagging --bucket {{my-ontap-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias --key {{my-image.jpg}} --tagging TagSet=[{Key="{{finance}}",Value="{{true}}"}]
```

You can also use the REST API to add a tag-set to an object through an access point. For more information, see [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html) in the *Amazon Simple Storage Service API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
