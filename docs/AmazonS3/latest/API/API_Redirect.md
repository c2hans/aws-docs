---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Redirect.html
---

# Redirect
<a name="API_Redirect"></a>

Specifies how requests are redirected. In the event of an error, you can specify a different error code to return.

## Contents
<a name="API_Redirect_Contents"></a>

 ** HostName **   <a name="AmazonS3-Type-Redirect-HostName"></a>
The host name to use in the redirect request.
Type: String
Required: No

 ** HttpRedirectCode **   <a name="AmazonS3-Type-Redirect-HttpRedirectCode"></a>
The HTTP redirect code to use on the response. Not required if one of the siblings is present.
Type: String
Required: No

 ** Protocol **   <a name="AmazonS3-Type-Redirect-Protocol"></a>
Protocol to use when redirecting requests. The default is the protocol that is used in the original request.
Type: String
Valid Values: `http | https`
Required: No

 ** ReplaceKeyPrefixWith **   <a name="AmazonS3-Type-Redirect-ReplaceKeyPrefixWith"></a>
The object key prefix to use in the redirect request. For example, to redirect requests for all pages with prefix `docs/` (objects in the `docs/` folder) to `documents/`, you can set a condition block with `KeyPrefixEquals` set to `docs/` and in the Redirect set `ReplaceKeyPrefixWith` to `/documents`. Not required if one of the siblings is present. Can be present only if `ReplaceKeyWith` is not provided.
Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [ XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).
Type: String
Required: No

 ** ReplaceKeyWith **   <a name="AmazonS3-Type-Redirect-ReplaceKeyWith"></a>
The specific object key to use in the redirect request. For example, redirect request to `error.html`. Not required if one of the siblings is present. Can be present only if `ReplaceKeyPrefixWith` is not provided.
Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [ XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).
Type: String
Required: No

## See Also
<a name="API_Redirect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Redirect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Redirect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Redirect)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
