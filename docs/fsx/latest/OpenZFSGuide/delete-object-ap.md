---
source_url: https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/delete-object-ap.html
---

# Deleting a file using an S3 access point
<a name="delete-object-ap"></a>

The following `delete-object` example command shows how you can use the AWS CLI to delete a file through an access point.

```
$ aws s3api delete-object --bucket {{my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias --key {{my-image.jpg}}
```

You can also use the REST API to delete an object through an access point. For more information, see [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) in the *Amazon Simple Storage Service API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
