---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AppComponentCompliance.html
---

# AppComponentCompliance
<a name="API_AppComponentCompliance"></a>

Defines the compliance of an AppComponent against the resiliency policy.

## Contents
<a name="API_AppComponentCompliance_Contents"></a>

 ** appComponentName **   <a name="resiliencehub-Type-AppComponentCompliance-appComponentName"></a>
Name of the AppComponent.
Type: String
Pattern: `\S{1,255}`
Required: No

 ** compliance **   <a name="resiliencehub-Type-AppComponentCompliance-compliance"></a>
The compliance of the AppComponent against the resiliency policy.
Type: String to [DisruptionCompliance](API_DisruptionCompliance.md) object map
Valid Keys: `Software | Hardware | AZ | Region`
Required: No

 ** cost **   <a name="resiliencehub-Type-AppComponentCompliance-cost"></a>
The cost for the application.
Type: [Cost](API_Cost.md) object
Required: No

 ** message **   <a name="resiliencehub-Type-AppComponentCompliance-message"></a>
The compliance message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** resiliencyScore **   <a name="resiliencehub-Type-AppComponentCompliance-resiliencyScore"></a>
The current resiliency score for the application.
Type: [ResiliencyScore](API_ResiliencyScore.md) object
Required: No

 ** status **   <a name="resiliencehub-Type-AppComponentCompliance-status"></a>
Status of the action.
Type: String
Valid Values: `PolicyBreached | PolicyMet | NotApplicable | MissingPolicy`
Required: No

## See Also
<a name="API_AppComponentCompliance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/AppComponentCompliance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/AppComponentCompliance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/AppComponentCompliance)
