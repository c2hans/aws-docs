---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_RecommendationTemplate.html
---

# RecommendationTemplate
<a name="API_RecommendationTemplate"></a>

Defines a recommendation template created with the [CreateRecommendationTemplate](API_CreateRecommendationTemplate.md) action.

## Contents
<a name="API_RecommendationTemplate_Contents"></a>

 ** assessmentArn **   <a name="resiliencehub-Type-RecommendationTemplate-assessmentArn"></a>
Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app-assessment/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** format **   <a name="resiliencehub-Type-RecommendationTemplate-format"></a>
Format of the recommendation template.
CfnJson
The template is CloudFormation JSON.
CfnYaml
The template is CloudFormation YAML.
Type: String
Valid Values: `CfnYaml | CfnJson`
Required: Yes

 ** name **   <a name="resiliencehub-Type-RecommendationTemplate-name"></a>
Name for the recommendation template.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** recommendationTemplateArn **   <a name="resiliencehub-Type-RecommendationTemplate-recommendationTemplateArn"></a>
Amazon Resource Name (ARN) for the recommendation template.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** recommendationTypes **   <a name="resiliencehub-Type-RecommendationTemplate-recommendationTypes"></a>
An array of strings that specify the recommendation template type or types.
Alarm
The template is an [AlarmRecommendation](API_AlarmRecommendation.md) template.
Sop
The template is a [SopRecommendation](API_SopRecommendation.md) template.
Test
The template is a [TestRecommendation](API_TestRecommendation.md) template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `Alarm | Sop | Test`
Required: Yes

 ** status **   <a name="resiliencehub-Type-RecommendationTemplate-status"></a>
Status of the action.
Type: String
Valid Values: `Pending | InProgress | Failed | Success`
Required: Yes

 ** appArn **   <a name="resiliencehub-Type-RecommendationTemplate-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** endTime **   <a name="resiliencehub-Type-RecommendationTemplate-endTime"></a>
The end time for the action.
Type: Timestamp
Required: No

 ** message **   <a name="resiliencehub-Type-RecommendationTemplate-message"></a>
Message for the recommendation template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** needsReplacements **   <a name="resiliencehub-Type-RecommendationTemplate-needsReplacements"></a>
Indicates if replacements are needed.
Type: Boolean
Required: No

 ** recommendationIds **   <a name="resiliencehub-Type-RecommendationTemplate-recommendationIds"></a>
Identifiers for the recommendations used in the recommendation template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: No

 ** startTime **   <a name="resiliencehub-Type-RecommendationTemplate-startTime"></a>
The start time for the action.
Type: Timestamp
Required: No

 ** tags **   <a name="resiliencehub-Type-RecommendationTemplate-tags"></a>
Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

 ** templatesLocation **   <a name="resiliencehub-Type-RecommendationTemplate-templatesLocation"></a>
The file location of the template.
Type: [S3Location](API_S3Location.md) object
Required: No

## See Also
<a name="API_RecommendationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/RecommendationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/RecommendationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/RecommendationTemplate)
