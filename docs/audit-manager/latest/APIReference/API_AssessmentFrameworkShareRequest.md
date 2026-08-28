---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentFrameworkShareRequest.html
---

# AssessmentFrameworkShareRequest
<a name="API_AssessmentFrameworkShareRequest"></a>

 Represents a share request for a custom framework in AWS Audit Manager.

## Contents
<a name="API_AssessmentFrameworkShareRequest_Contents"></a>

 ** comment **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-comment"></a>
 An optional comment from the sender about the share request.
Type: String
Length Constraints: Maximum length of 500.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** complianceType **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-complianceType"></a>
The compliance type that the shared custom framework supports, such as CIS or HIPAA.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** creationTime **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-creationTime"></a>
 The time when the share request was created.
Type: Timestamp
Required: No

 ** customControlsCount **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-customControlsCount"></a>
The number of custom controls that are part of the shared custom framework.
Type: Integer
Required: No

 ** destinationAccount **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-destinationAccount"></a>
 The AWS account of the recipient.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

 ** destinationRegion **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-destinationRegion"></a>
 The AWS Region of the recipient.
Type: String
Pattern: `^[a-z]{2}-[a-z]+-[0-9]{1}$`
Required: No

 ** expirationTime **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-expirationTime"></a>
 The time when the share request expires.
Type: Timestamp
Required: No

 ** frameworkDescription **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-frameworkDescription"></a>
The description of the shared custom framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** frameworkId **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-frameworkId"></a>
The unique identifier for the shared custom framework.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** frameworkName **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-frameworkName"></a>
 The name of the custom framework that the share request is for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** id **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-id"></a>
 The unique identifier for the share request.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** lastUpdated **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-lastUpdated"></a>
 Specifies when the share request was last updated.
Type: Timestamp
Required: No

 ** sourceAccount **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-sourceAccount"></a>
 The AWS account of the sender.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

 ** standardControlsCount **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-standardControlsCount"></a>
The number of standard controls that are part of the shared custom framework.
Type: Integer
Required: No

 ** status **   <a name="auditmanager-Type-AssessmentFrameworkShareRequest-status"></a>
 The status of the share request.
Type: String
Valid Values: `ACTIVE | REPLICATING | SHARED | EXPIRING | FAILED | EXPIRED | DECLINED | REVOKED`
Required: No

## See Also
<a name="API_AssessmentFrameworkShareRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentFrameworkShareRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentFrameworkShareRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentFrameworkShareRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
