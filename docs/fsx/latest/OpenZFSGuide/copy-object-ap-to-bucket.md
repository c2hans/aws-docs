---
source_url: https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/copy-object-ap-to-bucket.html
---

# Copying a file to an Amazon S3 bucket using an S3 access point

The following `copy-object` example command shows how you can use the AWS CLI to copy a file from an FSx for OpenZFS volume to an Amazon S3 bucket through an access point.

The example copies the file {{`my-image.jpg`}} through the access point {{`my-openzfs-ap`}} to the bucket {{`amzn-s3-demo-bucket`}} and saves the object as {{`my-image.jpg`}}.

```
$ aws s3api copy-object --copy-source {{my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias/{{my-image.jpg}} --bucket {{amzn-s3-demo-bucket}} --key {{my-image.jpg}}
```

You can also use the AWS CLI `s3 cp` command. For large files, `s3 cp` copies the file in parts with `UploadPartCopy`, so it can copy files larger than 5 GB. For more information, see [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) in the *AWS CLI Command Reference*.

```
$ aws s3 cp s3://{{my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias/{{my-image.jpg}} s3://{{amzn-s3-demo-bucket}}/{{my-image.jpg}}
```

To move the file instead of copying it, use the AWS CLI `s3 mv` command, which copies the file to the bucket and then deletes it from the FSx for OpenZFS volume. For more information, see [mv](https://docs.aws.amazon.com/cli/latest/reference/s3/mv.html) in the *AWS CLI Command Reference*.

```
$ aws s3 mv s3://{{my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias/{{my-image.jpg}} s3://{{amzn-s3-demo-bucket}}/{{my-image.jpg}}
```

You can also use the REST API to copy an object through an access point. For more information, see [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) in the *Amazon Simple Storage Service API Reference*.
