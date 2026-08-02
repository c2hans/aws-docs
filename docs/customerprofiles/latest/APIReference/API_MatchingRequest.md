---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_MatchingRequest.html
---

# MatchingRequest
<a name="API_connect-customer-profiles_MatchingRequest"></a>

The flag that enables the matching process of duplicate profiles.

## Contents
<a name="API_connect-customer-profiles_MatchingRequest_Contents"></a>

 ** Enabled **   <a name="connect-Type-connect-customer-profiles_MatchingRequest-Enabled"></a>
The flag that enables the matching process of duplicate profiles.
Type: Boolean
Required: Yes

 ** AutoMerging **   <a name="connect-Type-connect-customer-profiles_MatchingRequest-AutoMerging"></a>
Configuration information about the auto-merging process.
Type: [AutoMerging](API_connect-customer-profiles_AutoMerging.md) object
Required: No

 ** ExportingConfig **   <a name="connect-Type-connect-customer-profiles_MatchingRequest-ExportingConfig"></a>
Configuration information for exporting Identity Resolution results, for example, to an S3 bucket.
Type: [ExportingConfig](API_connect-customer-profiles_ExportingConfig.md) object
Required: No

 ** JobSchedule **   <a name="connect-Type-connect-customer-profiles_MatchingRequest-JobSchedule"></a>
The day and time when do you want to start the Identity Resolution Job every week.
Type: [JobSchedule](API_connect-customer-profiles_JobSchedule.md) object
Required: No

## See Also
<a name="API_connect-customer-profiles_MatchingRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/MatchingRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/MatchingRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/MatchingRequest)
