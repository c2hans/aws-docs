---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_WebsiteConfiguration.html
---

# WebsiteConfiguration
<a name="API_WebsiteConfiguration"></a>

Specifies website configuration parameters for an Amazon S3 bucket.

## Contents
<a name="API_WebsiteConfiguration_Contents"></a>

 ** ErrorDocument **   <a name="AmazonS3-Type-WebsiteConfiguration-ErrorDocument"></a>
The name of the error document for the website.
Type: [ErrorDocument](API_ErrorDocument.md) data type
Required: No

 ** IndexDocument **   <a name="AmazonS3-Type-WebsiteConfiguration-IndexDocument"></a>
The name of the index document for the website.
Type: [IndexDocument](API_IndexDocument.md) data type
Required: No

 ** RedirectAllRequestsTo **   <a name="AmazonS3-Type-WebsiteConfiguration-RedirectAllRequestsTo"></a>
The redirect behavior for every request to this bucket's website endpoint.
If you specify this property, you can't specify any other property.
Type: [RedirectAllRequestsTo](API_RedirectAllRequestsTo.md) data type
Required: No

 ** RoutingRules **   <a name="AmazonS3-Type-WebsiteConfiguration-RoutingRules"></a>
Rules that define when a redirect is applied and the redirect behavior.
Type: Array of [RoutingRule](API_RoutingRule.md) data types
Required: No

## See Also
<a name="API_WebsiteConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/WebsiteConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/WebsiteConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/WebsiteConfiguration)
