---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Framework.html
---

# Framework
<a name="API_Framework"></a>

 The file that's used to structure and automate AWS Audit Manager assessments for a given compliance standard.

## Contents
<a name="API_Framework_Contents"></a>

 ** arn **   <a name="auditmanager-Type-Framework-arn"></a>
 The Amazon Resource Name (ARN) of the framework.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:auditmanager:.*`
Required: No

 ** complianceType **   <a name="auditmanager-Type-Framework-complianceType"></a>
 The compliance type that the framework supports, such as CIS or HIPAA.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** controlSets **   <a name="auditmanager-Type-Framework-controlSets"></a>
 The control sets that are associated with the framework.
The `Controls` object returns a partial response when called through Framework APIs. For a complete `Controls` object, use `GetControl`.
Type: Array of [ControlSet](API_ControlSet.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** controlSources **   <a name="auditmanager-Type-Framework-controlSources"></a>
 *This member has been deprecated.*
 The control data sources where Audit Manager collects evidence from.
This API parameter is no longer supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z_0-9-\s.,]+$`
Required: No

 ** createdAt **   <a name="auditmanager-Type-Framework-createdAt"></a>
 The time when the framework was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="auditmanager-Type-Framework-createdBy"></a>
 The user or role that created the framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9\s-_()\[\]]+$`
Required: No

 ** description **   <a name="auditmanager-Type-Framework-description"></a>
 The description of the framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** id **   <a name="auditmanager-Type-Framework-id"></a>
 The unique identifier for the framework.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** lastUpdatedAt **   <a name="auditmanager-Type-Framework-lastUpdatedAt"></a>
 The time when the framework was most recently updated.
Type: Timestamp
Required: No

 ** lastUpdatedBy **   <a name="auditmanager-Type-Framework-lastUpdatedBy"></a>
 The user or role that most recently updated the framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9\s-_()\[\]]+$`
Required: No

 ** logo **   <a name="auditmanager-Type-Framework-logo"></a>
 The logo that's associated with the framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w,\s-]+\.[A-Za-z]+$`
Required: No

 ** name **   <a name="auditmanager-Type-Framework-name"></a>
 The name of the framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

 ** tags **   <a name="auditmanager-Type-Framework-tags"></a>
 The tags that are associated with the framework.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.{0,255}`
Required: No

 ** type **   <a name="auditmanager-Type-Framework-type"></a>
 Specifies whether the framework is a standard framework or a custom framework.
Type: String
Valid Values: `Standard | Custom`
Required: No

## See Also
<a name="API_Framework_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/Framework)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/Framework)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/Framework)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
