---
source_url: https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/copy-object-bucket-to-ap.html
---

# Copying a file from an Amazon S3 bucket using an S3 access point

The following `copy-object` example command shows how you can use the AWS CLI to copy an object from an Amazon S3 bucket to an FSx for OpenZFS volume through an access point.

The example copies the object {{`my-image.jpg`}} from the bucket {{`amzn-s3-demo-bucket`}} through the access point {{`my-openzfs-ap`}} and saves the file as {{`my-image.jpg`}}.

```
$ aws s3api copy-object --copy-source {{amzn-s3-demo-bucket}}/{{my-image.jpg}} --bucket {{my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias --key {{my-image.jpg}}
```

You can also use the AWS CLI `s3 cp` command. For large files, `s3 cp` copies the file in parts with `UploadPartCopy`, so it can copy files larger than 5 GB. For more information, see [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) in the *AWS CLI Command Reference*.

```
$ aws s3 cp s3://{{amzn-s3-demo-bucket}}/{{my-image.jpg}} s3://{{my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias/{{my-image.jpg}}
```

To move the file instead of copying it, use the AWS CLI `s3 mv` command, which copies the file to the FSx for OpenZFS volume and then deletes it from the bucket. For more information, see [mv](https://docs.aws.amazon.com/cli/latest/reference/s3/mv.html) in the *AWS CLI Command Reference*.

```
$ aws s3 mv s3://{{amzn-s3-demo-bucket}}/{{my-image.jpg}} s3://{{my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias/{{my-image.jpg}}
```

You can also use the REST API to copy an object through an access point. For more information, see [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) in the *Amazon Simple Storage Service API Reference*.
