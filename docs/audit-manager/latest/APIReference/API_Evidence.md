---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Evidence.html
---

# Evidence
<a name="API_Evidence"></a>

 A record that contains the information needed to demonstrate compliance with the requirements specified by a control. Examples of evidence include change activity invoked by a user, or a system configuration snapshot.

## Contents
<a name="API_Evidence_Contents"></a>

 ** assessmentReportSelection **   <a name="auditmanager-Type-Evidence-assessmentReportSelection"></a>
 Specifies whether the evidence is included in the assessment report.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** attributes **   <a name="auditmanager-Type-Evidence-attributes"></a>
 The names and values that are used by the evidence event. This includes an attribute name (such as `allowUsersToChangePassword`) and value (such as `true` or `false`).
Type: String to string map
Key Length Constraints: Maximum length of 100.
Key Pattern: `^[\w\W\s\S]*$`
Value Length Constraints: Maximum length of 200.
Value Pattern: `^[\w\W\s\S]*$`
Required: No

 ** awsAccountId **   <a name="auditmanager-Type-Evidence-awsAccountId"></a>
 The identifier for the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

 ** awsOrganization **   <a name="auditmanager-Type-Evidence-awsOrganization"></a>
 The AWS account that the evidence is collected from, and its organization path.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** complianceCheck **   <a name="auditmanager-Type-Evidence-complianceCheck"></a>
The evaluation status for automated evidence that falls under the compliance check category.
+ Audit Manager classes evidence as non-compliant if Security Hub CSPM reports a *Fail* result, or if AWS Config reports a *Non-compliant* result.
+ Audit Manager classes evidence as compliant if Security Hub CSPM reports a *Pass* result, or if AWS Config reports a *Compliant* result.
+ If a compliance check isn't available or applicable, then no compliance evaluation can be made for that evidence. This is the case if the evidence uses AWS Config or Security Hub CSPM as the underlying data source type, but those services aren't enabled. This is also the case if the evidence uses an underlying data source type that doesn't support compliance checks (such as manual evidence, AWS API calls, or CloudTrail).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** dataSource **   <a name="auditmanager-Type-Evidence-dataSource"></a>
 The data source where the evidence was collected from.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** eventName **   <a name="auditmanager-Type-Evidence-eventName"></a>
 The name of the evidence event.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** eventSource **   <a name="auditmanager-Type-Evidence-eventSource"></a>
 The AWS service that the evidence is collected from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `^[a-zA-Z0-9-\s().]+$`
Required: No

 ** evidenceAwsAccountId **   <a name="auditmanager-Type-Evidence-evidenceAwsAccountId"></a>
 The identifier for the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

 ** evidenceByType **   <a name="auditmanager-Type-Evidence-evidenceByType"></a>
 The type of automated evidence.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** evidenceFolderId **   <a name="auditmanager-Type-Evidence-evidenceFolderId"></a>
 The identifier for the folder that the evidence is stored in.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** iamId **   <a name="auditmanager-Type-Evidence-iamId"></a>
 The unique identifier for the user or role that's associated with the evidence.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:iam:.*`
Required: No

 ** id **   <a name="auditmanager-Type-Evidence-id"></a>
 The identifier for the evidence.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** resourcesIncluded **   <a name="auditmanager-Type-Evidence-resourcesIncluded"></a>
 The list of resources that are assessed to generate the evidence.
Type: Array of [Resource](API_Resource.md) objects
Required: No

 ** time **   <a name="auditmanager-Type-Evidence-time"></a>
 The timestamp that represents when the evidence was collected.
Type: Timestamp
Required: No

## See Also
<a name="API_Evidence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/Evidence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/Evidence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/Evidence)
