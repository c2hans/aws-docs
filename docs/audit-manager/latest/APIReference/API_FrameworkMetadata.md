---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_FrameworkMetadata.html
---

# FrameworkMetadata
<a name="API_FrameworkMetadata"></a>

 The metadata of a framework, such as the name, ID, or description.

## Contents
<a name="API_FrameworkMetadata_Contents"></a>

 ** complianceType **   <a name="auditmanager-Type-FrameworkMetadata-complianceType"></a>
 The compliance standard that's associated with the framework. For example, this could be PCI DSS or HIPAA.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** description **   <a name="auditmanager-Type-FrameworkMetadata-description"></a>
 The description of the framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** logo **   <a name="auditmanager-Type-FrameworkMetadata-logo"></a>
 The logo that's associated with the framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w,\s-]+\.[A-Za-z]+$`
Required: No

 ** name **   <a name="auditmanager-Type-FrameworkMetadata-name"></a>
 The name of the framework.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

## See Also
<a name="API_FrameworkMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/FrameworkMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/FrameworkMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/FrameworkMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
