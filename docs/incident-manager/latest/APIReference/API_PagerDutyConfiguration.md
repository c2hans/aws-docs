---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_PagerDutyConfiguration.html
---

# PagerDutyConfiguration
<a name="API_PagerDutyConfiguration"></a>

Details about the PagerDuty configuration for a response plan.

## Contents
<a name="API_PagerDutyConfiguration_Contents"></a>

 ** name **   <a name="IncidentManager-Type-PagerDutyConfiguration-name"></a>
The name of the PagerDuty configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** pagerDutyIncidentConfiguration **   <a name="IncidentManager-Type-PagerDutyConfiguration-pagerDutyIncidentConfiguration"></a>
Details about the PagerDuty service associated with the configuration.
Type: [PagerDutyIncidentConfiguration](API_PagerDutyIncidentConfiguration.md) object
Required: Yes

 ** secretId **   <a name="IncidentManager-Type-PagerDutyConfiguration-secretId"></a>
The ID of the AWS Secrets Manager secret that stores your PagerDuty key, either a General Access REST API Key or User Token REST API Key, and other user credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

## See Also
<a name="API_PagerDutyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/PagerDutyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/PagerDutyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/PagerDutyConfiguration)
