---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_RecommendationSettings.html
---

# RecommendationSettings
<a name="API_RecommendationSettings"></a>

Provides information about the required target engine settings.

## Contents
<a name="API_RecommendationSettings_Contents"></a>

 ** InstanceSizingType **   <a name="DMS-Type-RecommendationSettings-InstanceSizingType"></a>
The size of your target instance. Fleet Advisor calculates this value based on your data collection type, such as total capacity and resource utilization. Valid values include `"total-capacity"` and `"utilization"`.
Type: String
Required: Yes

 ** WorkloadType **   <a name="DMS-Type-RecommendationSettings-WorkloadType"></a>
The deployment option for your target engine. For production databases, Fleet Advisor chooses Multi-AZ deployment. For development or test databases, Fleet Advisor chooses Single-AZ deployment. Valid values include `"development"` and `"production"`.
Type: String
Required: Yes

## See Also
<a name="API_RecommendationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/RecommendationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/RecommendationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/RecommendationSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
