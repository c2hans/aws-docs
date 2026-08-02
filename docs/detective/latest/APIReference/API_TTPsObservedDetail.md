---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_TTPsObservedDetail.html
---

# TTPsObservedDetail
<a name="API_TTPsObservedDetail"></a>

Details tactics, techniques, and procedures (TTPs) used in a potential security event. Tactics are based on [MITRE ATT&CK Matrix for Enterprise](https://attack.mitre.org/matrices/enterprise/).

## Contents
<a name="API_TTPsObservedDetail_Contents"></a>

 ** APIFailureCount **   <a name="detective-Type-TTPsObservedDetail-APIFailureCount"></a>
The total number of failed API requests.
Type: Long
Required: No

 ** APIName **   <a name="detective-Type-TTPsObservedDetail-APIName"></a>
The name of the API where the tactics, techniques, and procedure (TTP) was observed.
Type: String
Required: No

 ** APISuccessCount **   <a name="detective-Type-TTPsObservedDetail-APISuccessCount"></a>
The total number of successful API requests.
Type: Long
Required: No

 ** IpAddress **   <a name="detective-Type-TTPsObservedDetail-IpAddress"></a>
The IP address where the tactics, techniques, and procedure (TTP) was observed.
Type: String
Required: No

 ** Procedure **   <a name="detective-Type-TTPsObservedDetail-Procedure"></a>
The procedure used, identified by the investigation.
Type: String
Required: No

 ** Tactic **   <a name="detective-Type-TTPsObservedDetail-Tactic"></a>
The tactic used, identified by the investigation.
Type: String
Required: No

 ** Technique **   <a name="detective-Type-TTPsObservedDetail-Technique"></a>
The technique used, identified by the investigation.
Type: String
Required: No

## See Also
<a name="API_TTPsObservedDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/TTPsObservedDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/TTPsObservedDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/TTPsObservedDetail)
