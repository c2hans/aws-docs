---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_ApplicationSummary"></a>

The summary of the SAP application registered with AWS Systems Manager for SAP.

## Contents
<a name="API_ApplicationSummary_Contents"></a>

 ** Arn **   <a name="ssmsap-Type-ApplicationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** DiscoveryStatus **   <a name="ssmsap-Type-ApplicationSummary-DiscoveryStatus"></a>
The status of the latest discovery.
Type: String
Valid Values: `SUCCESS | REGISTRATION_FAILED | REFRESH_FAILED | REGISTERING | DELETING`
Required: No

 ** Id **   <a name="ssmsap-Type-ApplicationSummary-Id"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: No

 ** Tags **   <a name="ssmsap-Type-ApplicationSummary-Tags"></a>
The tags on the application.
Type: String to string map
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Type **   <a name="ssmsap-Type-ApplicationSummary-Type"></a>
The type of the application.
Type: String
Valid Values: `HANA | SAP_ABAP`
Required: No

## See Also
<a name="API_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/ApplicationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
