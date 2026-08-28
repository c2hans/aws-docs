---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_PublicKeyList.html
---

# PublicKeyList
<a name="API_PublicKeyList"></a>

A list of public keys that you can use with [signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html), or with [field-level encryption](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html).

## Contents
<a name="API_PublicKeyList_Contents"></a>

 ** MaxItems **   <a name="cloudfront-Type-PublicKeyList-MaxItems"></a>
The maximum number of public keys you want in the response.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-PublicKeyList-Quantity"></a>
The number of public keys in the list.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-PublicKeyList-Items"></a>
A list of public keys.
Type: Array of [PublicKeySummary](API_PublicKeySummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-PublicKeyList-NextMarker"></a>
If there are more elements to be listed, this element is present and contains the value that you can use for the `Marker` request parameter to continue listing your public keys where you left off.
Type: String
Required: No

## See Also
<a name="API_PublicKeyList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublicKeyList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublicKeyList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublicKeyList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
