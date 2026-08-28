---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_NewGeolocationDetail.html
---

# NewGeolocationDetail
<a name="API_NewGeolocationDetail"></a>

Details new geolocations used either at the resource or account level. For example, lists an observed geolocation that is an infrequent or unused location based on previous user activity.

## Contents
<a name="API_NewGeolocationDetail_Contents"></a>

 ** IpAddress **   <a name="detective-Type-NewGeolocationDetail-IpAddress"></a>
IP address using which the resource was accessed.
Type: String
Required: No

 ** IsNewForEntireAccount **   <a name="detective-Type-NewGeolocationDetail-IsNewForEntireAccount"></a>
Checks if the geolocation is new for the entire account.
Type: Boolean
Required: No

 ** Location **   <a name="detective-Type-NewGeolocationDetail-Location"></a>
Location where the resource was accessed.
Type: String
Required: No

## See Also
<a name="API_NewGeolocationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/NewGeolocationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/NewGeolocationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/NewGeolocationDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
