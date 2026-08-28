---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_DatabaseSummary.html
---

# DatabaseSummary
<a name="API_DatabaseSummary"></a>

The summary of the database.

## Contents
<a name="API_DatabaseSummary_Contents"></a>

 ** ApplicationId **   <a name="ssmsap-Type-DatabaseSummary-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: No

 ** Arn **   <a name="ssmsap-Type-DatabaseSummary-Arn"></a>
The Amazon Resource Name (ARN) of the database.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** ComponentId **   <a name="ssmsap-Type-DatabaseSummary-ComponentId"></a>
The ID of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\d-]+`
Required: No

 ** DatabaseId **   <a name="ssmsap-Type-DatabaseSummary-DatabaseId"></a>
The ID of the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `.*[\w\d]+`
Required: No

 ** DatabaseType **   <a name="ssmsap-Type-DatabaseSummary-DatabaseType"></a>
The type of the database.
Type: String
Valid Values: `SYSTEM | TENANT`
Required: No

 ** Tags **   <a name="ssmsap-Type-DatabaseSummary-Tags"></a>
The tags of the database.
Type: String to string map
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_DatabaseSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/DatabaseSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/DatabaseSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/DatabaseSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
