---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_S3Origin.html
---

# S3Origin
<a name="API_S3Origin"></a>

A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.

## Contents
<a name="API_S3Origin_Contents"></a>

 ** DomainName **   <a name="cloudfront-Type-S3Origin-DomainName"></a>
The DNS name of the Amazon S3 origin.
Type: String
Required: Yes

 ** OriginAccessIdentity **   <a name="cloudfront-Type-S3Origin-OriginAccessIdentity"></a>
The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.
If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty `OriginAccessIdentity` element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty `OriginAccessIdentity` element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information, see [Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the * Amazon CloudFront Developer Guide*.
Type: String
Required: Yes

## See Also
<a name="API_S3Origin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/S3Origin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/S3Origin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/S3Origin)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
