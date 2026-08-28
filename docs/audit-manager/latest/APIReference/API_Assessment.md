---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Assessment.html
---

# Assessment
<a name="API_Assessment"></a>

 An entity that defines the scope of audit evidence collected by AWS Audit Manager. An Audit Manager assessment is an implementation of an Audit Manager framework.

## Contents
<a name="API_Assessment_Contents"></a>

 ** arn **   <a name="auditmanager-Type-Assessment-arn"></a>
 The Amazon Resource Name (ARN) of the assessment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:auditmanager:.*`
Required: No

 ** awsAccount **   <a name="auditmanager-Type-Assessment-awsAccount"></a>
 The AWS account that's associated with the assessment.
Type: [AWSAccount](API_AWSAccount.md) object
Required: No

 ** framework **   <a name="auditmanager-Type-Assessment-framework"></a>
 The framework that the assessment was created from.
Type: [AssessmentFramework](API_AssessmentFramework.md) object
Required: No

 ** metadata **   <a name="auditmanager-Type-Assessment-metadata"></a>
 The metadata for the assessment.
Type: [AssessmentMetadata](API_AssessmentMetadata.md) object
Required: No

 ** tags **   <a name="auditmanager-Type-Assessment-tags"></a>
 The tags that are associated with the assessment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.{0,255}`
Required: No

## See Also
<a name="API_Assessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/Assessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/Assessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/Assessment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
