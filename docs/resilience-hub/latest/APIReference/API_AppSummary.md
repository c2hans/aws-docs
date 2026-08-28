---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AppSummary.html
---

# AppSummary
<a name="API_AppSummary"></a>

Defines an application summary.

## Contents
<a name="API_AppSummary_Contents"></a>

 ** appArn **   <a name="resiliencehub-Type-AppSummary-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** creationTime **   <a name="resiliencehub-Type-AppSummary-creationTime"></a>
Date and time when the app was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="resiliencehub-Type-AppSummary-name"></a>
The name of the application.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** assessmentSchedule **   <a name="resiliencehub-Type-AppSummary-assessmentSchedule"></a>
 Assessment execution schedule with 'Daily' or 'Disabled' values.
Type: String
Valid Values: `Disabled | Daily`
Required: No

 ** awsApplicationArn **   <a name="resiliencehub-Type-AppSummary-awsApplicationArn"></a>
Amazon Resource Name (ARN) of AWS Resource Groups group that is integrated with an AppRegistry application. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** complianceStatus **   <a name="resiliencehub-Type-AppSummary-complianceStatus"></a>
The current status of compliance for the resiliency policy.
Type: String
Valid Values: `PolicyBreached | PolicyMet | NotAssessed | ChangesDetected | NotApplicable | MissingPolicy`
Required: No

 ** description **   <a name="resiliencehub-Type-AppSummary-description"></a>
The optional description for an app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** driftStatus **   <a name="resiliencehub-Type-AppSummary-driftStatus"></a>
Indicates if compliance drifts (deviations) were detected while running an assessment for your application.
Type: String
Valid Values: `NotChecked | NotDetected | Detected`
Required: No

 ** lastAppComplianceEvaluationTime **   <a name="resiliencehub-Type-AppSummary-lastAppComplianceEvaluationTime"></a>
Date and time of the most recent compliance evaluation.
Type: Timestamp
Required: No

 ** resiliencyScore **   <a name="resiliencehub-Type-AppSummary-resiliencyScore"></a>
The current resiliency score for the application.
Type: Double
Required: No

 ** rpoInSecs **   <a name="resiliencehub-Type-AppSummary-rpoInSecs"></a>
Recovery Point Objective (RPO) in seconds.
Type: Integer
Required: No

 ** rtoInSecs **   <a name="resiliencehub-Type-AppSummary-rtoInSecs"></a>
Recovery Time Objective (RTO) in seconds.
Type: Integer
Required: No

 ** status **   <a name="resiliencehub-Type-AppSummary-status"></a>
Status of the application.
Type: String
Valid Values: `Active | Deleting`
Required: No

## See Also
<a name="API_AppSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/AppSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/AppSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/AppSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
