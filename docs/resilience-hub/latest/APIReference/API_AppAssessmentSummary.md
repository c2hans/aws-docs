---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AppAssessmentSummary.html
---

# AppAssessmentSummary
<a name="API_AppAssessmentSummary"></a>

Defines an application assessment summary.

## Contents
<a name="API_AppAssessmentSummary_Contents"></a>

 ** assessmentArn **   <a name="resiliencehub-Type-AppAssessmentSummary-assessmentArn"></a>
Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app-assessment/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** assessmentStatus **   <a name="resiliencehub-Type-AppAssessmentSummary-assessmentStatus"></a>
Current status of the assessment for the resiliency policy.
Type: String
Valid Values: `Pending | InProgress | Failed | Success`
Required: Yes

 ** appArn **   <a name="resiliencehub-Type-AppAssessmentSummary-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** appVersion **   <a name="resiliencehub-Type-AppAssessmentSummary-appVersion"></a>
Version of an application.
Type: String
Pattern: `\S{1,50}`
Required: No

 ** assessmentName **   <a name="resiliencehub-Type-AppAssessmentSummary-assessmentName"></a>
Name of the assessment.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** complianceStatus **   <a name="resiliencehub-Type-AppAssessmentSummary-complianceStatus"></a>
Current status of compliance for the resiliency policy.
Type: String
Valid Values: `PolicyBreached | PolicyMet | NotApplicable | MissingPolicy`
Required: No

 ** cost **   <a name="resiliencehub-Type-AppAssessmentSummary-cost"></a>
Cost for an application.
Type: [Cost](API_Cost.md) object
Required: No

 ** driftStatus **   <a name="resiliencehub-Type-AppAssessmentSummary-driftStatus"></a>
Indicates if compliance drifts (deviations) were detected while running an assessment for your application.
Type: String
Valid Values: `NotChecked | NotDetected | Detected`
Required: No

 ** endTime **   <a name="resiliencehub-Type-AppAssessmentSummary-endTime"></a>
End time for the action.
Type: Timestamp
Required: No

 ** invoker **   <a name="resiliencehub-Type-AppAssessmentSummary-invoker"></a>
Entity that invoked the assessment.
Type: String
Valid Values: `User | System`
Required: No

 ** message **   <a name="resiliencehub-Type-AppAssessmentSummary-message"></a>
Message from the assessment run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** resiliencyScore **   <a name="resiliencehub-Type-AppAssessmentSummary-resiliencyScore"></a>
Current resiliency score for the application.
Type: Double
Required: No

 ** startTime **   <a name="resiliencehub-Type-AppAssessmentSummary-startTime"></a>
Starting time for the action.
Type: Timestamp
Required: No

 ** versionName **   <a name="resiliencehub-Type-AppAssessmentSummary-versionName"></a>
Name of an application version.
Type: String
Pattern: `\S{1,50}`
Required: No

## See Also
<a name="API_AppAssessmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/AppAssessmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/AppAssessmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/AppAssessmentSummary)
