---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/pstools-s3-bucket-create.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Create an Amazon S3 Bucket, Verify Its Region, and Optionally Remove It
<a name="pstools-s3-bucket-create"></a>

Use the `New-S3Bucket` cmdlet to create a new Amazon S3 bucket. The following examples creates a bucket named `website-example`. The name of the bucket must be unique across all regions. The example creates the bucket in the `us-west-1` region.

```
PS > New-S3Bucket -BucketName {{website-example}} -Region {{us-west-2}}

CreationDate         BucketName
------------         ----------
8/16/19 8:45:38 PM   website-example
```

You can verify the region in which the bucket is located using the `Get-S3BucketLocation` cmdlet.

```
PS > Get-S3BucketLocation -BucketName website-example

Value
-----
us-west-2
```

When you're done with this tutorial, you can use the following line to remove this bucket. We suggest that you leave this bucket in place as we use it in subsequent examples.

```
PS > Remove-S3Bucket -BucketName website-example
```

Note that the bucket removal process can take some time to finish. If you try to re-create a same-named bucket immediately, the `New-S3Bucket` cmdlet can fail until the old one is completely gone.

## See Also
<a name="pstools-seealso-s3-bucket-create"></a>
+  [Calling AWS services in the AWS Tools for PowerShell](pstools-using.md)
+  [Put Bucket (Amazon S3 Service Reference)](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUT.html)
+  [AWS PowerShell Regions for Amazon S3](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
