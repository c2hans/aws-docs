---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentFrameworkMetadata.html
---

# AssessmentFrameworkMetadata
<a name="API_AssessmentFrameworkMetadata"></a>

 The metadata that's associated with a standard framework or a custom framework.

## Contents
<a name="API_AssessmentFrameworkMetadata_Contents"></a>

 ** arn **   <a name="auditmanager-Type-AssessmentFrameworkMetadata-arn"></a>
 The Amazon Resource Name (ARN) of the framework.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:auditmanager:.*`
Required: No

 ** complianceType **   <a name="auditmanager-Type-AssessmentFrameworkMetadata-complianceType"></a>
 The compliance type that the new custom framework supports, such as CIS or HIPAA.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** controlsCount **   <a name="auditmanager-Type-AssessmentFrameworkMetadata-controlsCount"></a>
 The number of controls that are associated with the framework.
Type: Integer
Required: No

 ** controlSetsCount **   <a name="auditmanager-Type-AssessmentFrameworkMetadata-controlSetsCount"></a>
 The number of control sets that are associated with the framework.
Type: Integer
Required: No

 ** createdAt **   <a name="auditmanager-Type-AssessmentFrameworkMetadata-createdAt"></a>
 The time when the framework was created.
Type: Timestamp
Required: No

 ** description **   <a name="auditmanager-Type-AssessmentFrameworkMetadata-description"></a>
 The description of the framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** id **   <a name="auditmanager-Type-AssessmentFrameworkMetadata-id"></a>
 The unique identifier for the framework.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** lastUpdatedAt **   <a name="auditmanager-Type-AssessmentFrameworkMetadata-lastUpdatedAt"></a>
 The time when the framework was most recently updated.
Type: Timestamp
Required: No

 ** logo **   <a name="auditmanager-Type-AssessmentFrameworkMetadata-logo"></a>
 The logo that's associated with the framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w,\s-]+\.[A-Za-z]+$`
Required: No

 ** name **   <a name="auditmanager-Type-AssessmentFrameworkMetadata-name"></a>
 The name of the framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** type **   <a name="auditmanager-Type-AssessmentFrameworkMetadata-type"></a>
 The framework type, such as a standard framework or a custom framework.
Type: String
Valid Values: `Standard | Custom`
Required: No

## See Also
<a name="API_AssessmentFrameworkMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AssessmentFrameworkMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AssessmentFrameworkMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AssessmentFrameworkMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
