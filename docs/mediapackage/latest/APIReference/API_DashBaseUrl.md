---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashBaseUrl.html
---

# DashBaseUrl
<a name="API_DashBaseUrl"></a>

The base URLs to use for retrieving segments. You can specify multiple locations and indicate the priority and weight for when each should be used, for use in mutli-CDN workflows.

## Contents
<a name="API_DashBaseUrl_Contents"></a>

 ** Url **   <a name="mediapackage-Type-DashBaseUrl-Url"></a>
A source location for segments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** DvbPriority **   <a name="mediapackage-Type-DashBaseUrl-DvbPriority"></a>
For use with DVB-DASH profiles only. The priority of this location for servings segments. The lower the number, the higher the priority.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 15000.
Required: No

 ** DvbWeight **   <a name="mediapackage-Type-DashBaseUrl-DvbWeight"></a>
For use with DVB-DASH profiles only. The weighting for source locations that have the same priority.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 15000.
Required: No

 ** ServiceLocation **   <a name="mediapackage-Type-DashBaseUrl-ServiceLocation"></a>
The name of the source location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_DashBaseUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/DashBaseUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/DashBaseUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/DashBaseUrl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
