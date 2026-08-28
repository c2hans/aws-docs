---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/pstools-s3-create-website.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Configure an Amazon S3 Bucket as a Website and Enable Logging
<a name="pstools-s3-create-website"></a>

Use the `Write-S3BucketWebsite` cmdlet to configure an Amazon S3 bucket as a static website. The following example specifies a name of `index.html` for the default content web page and a name of `error.html` for the default error web page. Note that this cmdlet does not create those pages. They need to be [uploaded as Amazon S3 objects](pstools-s3-upload-object.md).

```
PS > Write-S3BucketWebsite -BucketName website-example -WebsiteConfiguration_IndexDocumentSuffix index.html -WebsiteConfiguration_ErrorDocument error.html
RequestId      : A1813E27995FFDDD
AmazonId2      : T7hlDOeLqA5Q2XfTe8j2q3SLoP3/5XwhUU3RyJBGHU/LnC+CIWLeGgP0MY24xAlI
ResponseStream :
Headers        : {x-amz-id-2, x-amz-request-id, Content-Length, Date...}
Metadata       : {}
ResponseXml    :
```

## See Also
<a name="pstools-seealso-s3-create-website"></a>
+  [Calling AWS services in the AWS Tools for PowerShell](pstools-using.md)
+  [Put Bucket Website (Amazon S3 API Reference)](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTwebsite.html)
+  [Put Bucket ACL (Amazon S3 API Reference)](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTacl.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
