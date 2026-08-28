---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AppAssessment.html
---

# AppAssessment
<a name="API_AppAssessment"></a>

Defines an application assessment.

## Contents
<a name="API_AppAssessment_Contents"></a>

 ** assessmentArn **   <a name="resiliencehub-Type-AppAssessment-assessmentArn"></a>
Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app-assessment/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** assessmentStatus **   <a name="resiliencehub-Type-AppAssessment-assessmentStatus"></a>
Current status of the assessment for the resiliency policy.
Type: String
Valid Values: `Pending | InProgress | Failed | Success`
Required: Yes

 ** invoker **   <a name="resiliencehub-Type-AppAssessment-invoker"></a>
The entity that invoked the assessment.
Type: String
Valid Values: `User | System`
Required: Yes

 ** appArn **   <a name="resiliencehub-Type-AppAssessment-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** appVersion **   <a name="resiliencehub-Type-AppAssessment-appVersion"></a>
Version of an application.
Type: String
Pattern: `\S{1,50}`
Required: No

 ** assessmentName **   <a name="resiliencehub-Type-AppAssessment-assessmentName"></a>
Name of the assessment.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** compliance **   <a name="resiliencehub-Type-AppAssessment-compliance"></a>
Application compliance against the resiliency policy.
Type: String to [DisruptionCompliance](API_DisruptionCompliance.md) object map
Valid Keys: `Software | Hardware | AZ | Region`
Required: No

 ** complianceStatus **   <a name="resiliencehub-Type-AppAssessment-complianceStatus"></a>
Current status of the compliance for the resiliency policy.
Type: String
Valid Values: `PolicyBreached | PolicyMet | NotApplicable | MissingPolicy`
Required: No

 ** cost **   <a name="resiliencehub-Type-AppAssessment-cost"></a>
Cost for the application.
Type: [Cost](API_Cost.md) object
Required: No

 ** driftStatus **   <a name="resiliencehub-Type-AppAssessment-driftStatus"></a>
Indicates if compliance drifts (deviations) were detected while running an assessment for your application.
Type: String
Valid Values: `NotChecked | NotDetected | Detected`
Required: No

 ** endTime **   <a name="resiliencehub-Type-AppAssessment-endTime"></a>
End time for the action.
Type: Timestamp
Required: No

 ** message **   <a name="resiliencehub-Type-AppAssessment-message"></a>
Error or warning message from the assessment execution
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** policy **   <a name="resiliencehub-Type-AppAssessment-policy"></a>
Resiliency policy of an application.
Type: [ResiliencyPolicy](API_ResiliencyPolicy.md) object
Required: No

 ** resiliencyScore **   <a name="resiliencehub-Type-AppAssessment-resiliencyScore"></a>
Current resiliency score for an application.
Type: [ResiliencyScore](API_ResiliencyScore.md) object
Required: No

 ** resourceErrorsDetails **   <a name="resiliencehub-Type-AppAssessment-resourceErrorsDetails"></a>
 A resource error object containing a list of errors retrieving an application's resources.
Type: [ResourceErrorsDetails](API_ResourceErrorsDetails.md) object
Required: No

 ** startTime **   <a name="resiliencehub-Type-AppAssessment-startTime"></a>
Starting time for the action.
Type: Timestamp
Required: No

 ** summary **   <a name="resiliencehub-Type-AppAssessment-summary"></a>
Indicates the AI-generated summary for the AWS Resilience Hub assessment, providing a concise overview that highlights the top risks and recommendations.
This property is available only in the US East (N. Virginia) Region.
Type: [AssessmentSummary](API_AssessmentSummary.md) object
Required: No

 ** tags **   <a name="resiliencehub-Type-AppAssessment-tags"></a>
Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

 ** versionName **   <a name="resiliencehub-Type-AppAssessment-versionName"></a>
Version name of the published application.
Type: String
Pattern: `\S{1,50}`
Required: No

## See Also
<a name="API_AppAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/AppAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/AppAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/AppAssessment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
