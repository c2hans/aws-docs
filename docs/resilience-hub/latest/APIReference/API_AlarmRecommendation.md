---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AlarmRecommendation.html
---

# AlarmRecommendation
<a name="API_AlarmRecommendation"></a>

Defines a recommendation for a CloudWatch alarm.

## Contents
<a name="API_AlarmRecommendation_Contents"></a>

 ** name **   <a name="resiliencehub-Type-AlarmRecommendation-name"></a>
Name of the alarm recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** recommendationId **   <a name="resiliencehub-Type-AlarmRecommendation-recommendationId"></a>
Identifier of the alarm recommendation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: Yes

 ** referenceId **   <a name="resiliencehub-Type-AlarmRecommendation-referenceId"></a>
Reference identifier of the alarm recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** type **   <a name="resiliencehub-Type-AlarmRecommendation-type"></a>
Type of alarm recommendation.
Type: String
Valid Values: `Metric | Composite | Canary | Logs | Event`
Required: Yes

 ** appComponentName **   <a name="resiliencehub-Type-AlarmRecommendation-appComponentName"></a>
 *This member has been deprecated.*
AppComponent name for the CloudWatch alarm recommendation. This name is saved as the first item in the `appComponentNames` list.
Type: String
Pattern: `\S{1,255}`
Required: No

 ** appComponentNames **   <a name="resiliencehub-Type-AlarmRecommendation-appComponentNames"></a>
List of AppComponent names for the CloudWatch alarm recommendation.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** description **   <a name="resiliencehub-Type-AlarmRecommendation-description"></a>
Description of the alarm recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** items **   <a name="resiliencehub-Type-AlarmRecommendation-items"></a>
List of CloudWatch alarm recommendations.
Type: Array of [RecommendationItem](API_RecommendationItem.md) objects
Required: No

 ** prerequisite **   <a name="resiliencehub-Type-AlarmRecommendation-prerequisite"></a>
The prerequisite for the alarm recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** recommendationStatus **   <a name="resiliencehub-Type-AlarmRecommendation-recommendationStatus"></a>
Status of the recommended Amazon CloudWatch alarm.
Type: String
Valid Values: `Implemented | Inactive | NotImplemented | Excluded`
Required: No

## See Also
<a name="API_AlarmRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/AlarmRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/AlarmRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/AlarmRecommendation)
