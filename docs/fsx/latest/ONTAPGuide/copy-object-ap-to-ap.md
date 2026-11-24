---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/copy-object-ap-to-ap.html
---

# Copying a file between S3 access points

The following `copy-object` example command shows how you can use the AWS CLI to copy a file between two access points attached to Amazon FSx volumes.

The example copies the file {{`my-image.jpg`}} through the access point {{`my-ontap-ap`}}, which is attached to an FSx for ONTAP volume, to the access point {{`my-openzfs-ap`}}, which is attached to an FSx for OpenZFS volume, and saves the file as {{`my-image.jpg`}}.

```
$ aws s3api copy-object --copy-source {{my-ontap-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias/{{my-image.jpg}} --bucket {{my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias --key {{my-image.jpg}}
```

You can also use the AWS CLI `s3 cp` command. For large files, `s3 cp` copies the file in parts with `UploadPartCopy`, so it can copy files larger than 5 GB. For more information, see [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) in the *AWS CLI Command Reference*.

```
$ aws s3 cp s3://{{my-ontap-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias/{{my-image.jpg}} s3://{{my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias/{{my-image.jpg}}
```

To move the file instead of copying it, use the AWS CLI `s3 mv` command, which copies the file to the destination volume and then deletes it from the source volume. For more information, see [mv](https://docs.aws.amazon.com/cli/latest/reference/s3/mv.html) in the *AWS CLI Command Reference*.

```
$ aws s3 mv s3://{{my-ontap-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias/{{my-image.jpg}} s3://{{my-openzfs-ap-hrzrlukc5m36ft7okagglf3gmwluquse1b}}-ext-s3alias/{{my-image.jpg}}
```

To copy a file larger than 5 GB, use `UploadPartCopy`. For more information, see [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html) in the *Amazon Simple Storage Service API Reference*.
