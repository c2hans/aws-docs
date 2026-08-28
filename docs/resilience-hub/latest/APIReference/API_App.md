---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_App.html
---

# App
<a name="API_App"></a>

Defines an AWS Resilience Hub application.

## Contents
<a name="API_App_Contents"></a>

 ** appArn **   <a name="resiliencehub-Type-App-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** creationTime **   <a name="resiliencehub-Type-App-creationTime"></a>
Date and time when the application was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="resiliencehub-Type-App-name"></a>
Name for the application.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** assessmentSchedule **   <a name="resiliencehub-Type-App-assessmentSchedule"></a>
Assessment execution schedule with 'Daily' or 'Disabled' values.
Type: String
Valid Values: `Disabled | Daily`
Required: No

 ** awsApplicationArn **   <a name="resiliencehub-Type-App-awsApplicationArn"></a>
Amazon Resource Name (ARN) of AWS Resource Groups group that is integrated with an AppRegistry application. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** complianceStatus **   <a name="resiliencehub-Type-App-complianceStatus"></a>
Current status of compliance for the resiliency policy.
Type: String
Valid Values: `PolicyBreached | PolicyMet | NotAssessed | ChangesDetected | NotApplicable | MissingPolicy`
Required: No

 ** description **   <a name="resiliencehub-Type-App-description"></a>
Optional description for an application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** driftStatus **   <a name="resiliencehub-Type-App-driftStatus"></a>
Indicates if compliance drifts (deviations) were detected while running an assessment for your application.
Type: String
Valid Values: `NotChecked | NotDetected | Detected`
Required: No

 ** eventSubscriptions **   <a name="resiliencehub-Type-App-eventSubscriptions"></a>
The list of events you would like to subscribe and get notification for. Currently, AWS Resilience Hub supports notifications only for **Drift detected** and **Scheduled assessment failure** events.
Type: Array of [EventSubscription](API_EventSubscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** lastAppComplianceEvaluationTime **   <a name="resiliencehub-Type-App-lastAppComplianceEvaluationTime"></a>
Date and time the most recent compliance evaluation.
Type: Timestamp
Required: No

 ** lastDriftEvaluationTime **   <a name="resiliencehub-Type-App-lastDriftEvaluationTime"></a>
Indicates the last time that a drift was evaluated.
Type: Timestamp
Required: No

 ** lastResiliencyScoreEvaluationTime **   <a name="resiliencehub-Type-App-lastResiliencyScoreEvaluationTime"></a>
Date and time the most recent resiliency score evaluation.
Type: Timestamp
Required: No

 ** permissionModel **   <a name="resiliencehub-Type-App-permissionModel"></a>
Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.
Type: [PermissionModel](API_PermissionModel.md) object
Required: No

 ** policyArn **   <a name="resiliencehub-Type-App-policyArn"></a>
Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:resiliency-policy/`policy-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** resiliencyScore **   <a name="resiliencehub-Type-App-resiliencyScore"></a>
Current resiliency score for the application.
Type: Double
Required: No

 ** rpoInSecs **   <a name="resiliencehub-Type-App-rpoInSecs"></a>
Recovery Point Objective (RPO) in seconds.
Type: Integer
Required: No

 ** rtoInSecs **   <a name="resiliencehub-Type-App-rtoInSecs"></a>
Recovery Time Objective (RTO) in seconds.
Type: Integer
Required: No

 ** status **   <a name="resiliencehub-Type-App-status"></a>
Status of the application.
Type: String
Valid Values: `Active | Deleting`
Required: No

 ** tags **   <a name="resiliencehub-Type-App-tags"></a>
Tags assigned to the resource. A tag is a label that you assign to an AWS resource. Each tag consists of a key/value pair.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

## See Also
<a name="API_App_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/App)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/App)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/App)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
