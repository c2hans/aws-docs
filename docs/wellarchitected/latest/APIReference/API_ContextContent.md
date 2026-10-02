---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ContextContent.html
---

# ContextContent
<a name="API_ContextContent"></a>

Typed content structure for a context. Contains application-specific fields that describe the environment used during recommendation generation.

## Contents
<a name="API_ContextContent_Contents"></a>

 ** accountIds **   <a name="wellarchitected-Type-ContextContent-accountIds"></a>
The AWS account IDs associated with this application context.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** additionalContext **   <a name="wellarchitected-Type-ContextContent-additionalContext"></a>
Additional context not captured by other fields.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}\r\n])*`
Required: No

 ** applicationOverview **   <a name="wellarchitected-Type-ContextContent-applicationOverview"></a>
A free-form overview of the application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}\r\n])*`
Required: No

 ** applicationType **   <a name="wellarchitected-Type-ContextContent-applicationType"></a>
The type of the application.
Type: String
Valid Values: `SAS | DESKTOP_APPLICATION | OTHER`
Required: No

 ** architectureOverview **   <a name="wellarchitected-Type-ContextContent-architectureOverview"></a>
A free-form description of the application architecture.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}\r\n])*`
Required: No

 ** awsServices **   <a name="wellarchitected-Type-ContextContent-awsServices"></a>
The AWS services used by this application.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\P{C}]+`
Required: No

 ** criticality **   <a name="wellarchitected-Type-ContextContent-criticality"></a>
The business criticality of the application.
Type: String
Valid Values: `MISSION_CRITICAL | BUSINESS_CRITICAL | NON_CRITICAL | TEST_DEVELOPMENT`
Required: No

 ** industry **   <a name="wellarchitected-Type-ContextContent-industry"></a>
The industry vertical for this application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}\r\n])*`
Required: No

 ** organizationalUnitIds **   <a name="wellarchitected-Type-ContextContent-organizationalUnitIds"></a>
The AWS Organizations organizational unit (OU) IDs associated with this application context. Valid only for organizational profiles; rejected for standard profiles.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2500 items.
Length Constraints: Minimum length of 1. Maximum length of 68.
Pattern: `(ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}|r-[a-z0-9]{4,32})`
Required: No

 ** regions **   <a name="wellarchitected-Type-ContextContent-regions"></a>
The AWS Regions where this application operates.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z]{2}(-gov)?-[a-z]+-\d+`
Required: No

 ** resourceTags **   <a name="wellarchitected-Type-ContextContent-resourceTags"></a>
Resource tags used to scope this application context.
Type: Array of [ContextResourceTag](API_ContextResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** resourceTypes **   <a name="wellarchitected-Type-ContextContent-resourceTypes"></a>
The AWS resource types relevant to this application.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1500 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\P{C}]+`
Required: No

## See Also
<a name="API_ContextContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ContextContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ContextContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ContextContent)
