---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_RedirectAllRequestsTo.html
---

# RedirectAllRequestsTo
<a name="API_RedirectAllRequestsTo"></a>

Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket.

## Contents
<a name="API_RedirectAllRequestsTo_Contents"></a>

 ** HostName **   <a name="AmazonS3-Type-RedirectAllRequestsTo-HostName"></a>
Name of the host where requests are redirected.
Type: String
Required: Yes

 ** Protocol **   <a name="AmazonS3-Type-RedirectAllRequestsTo-Protocol"></a>
Protocol to use when redirecting requests. The default is the protocol that is used in the original request.
Type: String
Valid Values: `http | https`
Required: No

## See Also
<a name="API_RedirectAllRequestsTo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RedirectAllRequestsTo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RedirectAllRequestsTo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RedirectAllRequestsTo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
