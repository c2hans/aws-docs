---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_FailoverRouterInputStreamDetails.html
---

# FailoverRouterInputStreamDetails
<a name="API_FailoverRouterInputStreamDetails"></a>

Configuration details for a failover router input that can automatically switch between two sources.

## Contents
<a name="API_FailoverRouterInputStreamDetails_Contents"></a>

 ** sourceIndexOneStreamDetails **   <a name="mediaconnect-Type-FailoverRouterInputStreamDetails-sourceIndexOneStreamDetails"></a>
Configuration details for the secondary source (index 1) in the failover setup.
Type: [FailoverRouterInputIndexedStreamDetails](API_FailoverRouterInputIndexedStreamDetails.md) object
Required: Yes

 ** sourceIndexZeroStreamDetails **   <a name="mediaconnect-Type-FailoverRouterInputStreamDetails-sourceIndexZeroStreamDetails"></a>
Configuration details for the primary source (index 0) in the failover setup.
Type: [FailoverRouterInputIndexedStreamDetails](API_FailoverRouterInputIndexedStreamDetails.md) object
Required: Yes

## See Also
<a name="API_FailoverRouterInputStreamDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/FailoverRouterInputStreamDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/FailoverRouterInputStreamDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/FailoverRouterInputStreamDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
