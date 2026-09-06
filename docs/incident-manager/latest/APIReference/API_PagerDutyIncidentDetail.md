---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_PagerDutyIncidentDetail.html
---

# PagerDutyIncidentDetail
<a name="API_PagerDutyIncidentDetail"></a>

Details about the PagerDuty incident associated with an incident created by an Incident Manager response plan.

## Contents
<a name="API_PagerDutyIncidentDetail_Contents"></a>

 ** id **   <a name="IncidentManager-Type-PagerDutyIncidentDetail-id"></a>
The ID of the incident associated with the PagerDuty service for the response plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** autoResolve **   <a name="IncidentManager-Type-PagerDutyIncidentDetail-autoResolve"></a>
Indicates whether to resolve the PagerDuty incident when you resolve the associated Incident Manager incident.
Type: Boolean
Required: No

 ** secretId **   <a name="IncidentManager-Type-PagerDutyIncidentDetail-secretId"></a>
The ID of the AWS Secrets Manager secret that stores your PagerDuty key, either a General Access REST API Key or User Token REST API Key, and other user credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_PagerDutyIncidentDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/PagerDutyIncidentDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/PagerDutyIncidentDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/PagerDutyIncidentDetail)
