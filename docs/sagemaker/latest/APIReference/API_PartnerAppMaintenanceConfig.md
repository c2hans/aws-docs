---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PartnerAppMaintenanceConfig.html
---

# PartnerAppMaintenanceConfig
<a name="API_PartnerAppMaintenanceConfig"></a>

Maintenance configuration settings for the SageMaker Partner AI App.

## Contents
<a name="API_PartnerAppMaintenanceConfig_Contents"></a>

 ** MaintenanceWindowStart **   <a name="sagemaker-Type-PartnerAppMaintenanceConfig-MaintenanceWindowStart"></a>
The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time that weekly maintenance updates are scheduled. This value must take the following format: `3-letter-day:24-h-hour:minute`. For example: `TUE:03:30`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):([0-5]\d)`
Required: No

## See Also
<a name="API_PartnerAppMaintenanceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PartnerAppMaintenanceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PartnerAppMaintenanceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PartnerAppMaintenanceConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
