---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy-delete.html
---

# Deleting the Amazon S3 Bucket for Home Folders and Application Settings Persistence
<a name="s3-iam-policy-delete"></a>

WorkSpaces Applications adds an Amazon S3 bucket policy to the buckets that it creates to prevent them from being accidentally deleted. To delete an S3 bucket, you must first delete the S3 bucket policy. Following are the bucket policies that you must delete for home folders and application settings persistence.

**Home folders policy**

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "PreventAccidentalDeletionOfBucket",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:DeleteBucket",
      "Resource": "arn:aws:s3:::appstream2-36fb080bb8-{{region-code}}-{{123456789012-without-hyphens}}"
    }
  ]
}
```

------

**Application settings persistence policy**

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "PreventAccidentalDeletionOfBucket",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:DeleteBucket",
      "Resource": "arn:aws:s3:::appstream-app-settings-{{region-code}}-{{123456789012-without-hyphens}}-{{unique-identifier}}"
     }
   ]
}
```

------

 For more information, see [Deleting or Emptying a Bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-or-empty-bucket.html) in the *Amazon Simple Storage Service User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
