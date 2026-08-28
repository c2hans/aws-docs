---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_MobileSdkRelease.html
---

# MobileSdkRelease
<a name="API_MobileSdkRelease"></a>

Information for a release of the mobile SDK, including release notes and tags.

The mobile SDK is not generally available. Customers who have access to the mobile SDK can use it to establish and manage AWS WAF tokens for use in HTTP(S) requests from a mobile device to AWS WAF. For more information, see [AWS WAF client application integration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_MobileSdkRelease_Contents"></a>

 ** ReleaseNotes **   <a name="WAF-Type-MobileSdkRelease-ReleaseNotes"></a>
Notes describing the release.
Type: String
Required: No

 ** ReleaseVersion **   <a name="WAF-Type-MobileSdkRelease-ReleaseVersion"></a>
The release version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[\w#:\.\-/]+$`
Required: No

 ** Tags **   <a name="WAF-Type-MobileSdkRelease-Tags"></a>
Tags that are associated with the release.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** Timestamp **   <a name="WAF-Type-MobileSdkRelease-Timestamp"></a>
The timestamp of the release.
Type: Timestamp
Required: No

## See Also
<a name="API_MobileSdkRelease_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/MobileSdkRelease)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/MobileSdkRelease)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/MobileSdkRelease)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
