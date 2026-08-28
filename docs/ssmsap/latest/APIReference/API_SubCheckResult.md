---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_SubCheckResult.html
---

# SubCheckResult
<a name="API_SubCheckResult"></a>

Represents the result of a sub-check within a configuration check operation.

## Contents
<a name="API_SubCheckResult_Contents"></a>

 ** Description **   <a name="ssmsap-Type-SubCheckResult-Description"></a>
A description of what the sub-check validates.
Type: String
Required: No

 ** Id **   <a name="ssmsap-Type-SubCheckResult-Id"></a>
The unique identifier of the sub-check result.
Type: String
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`
Required: No

 ** Name **   <a name="ssmsap-Type-SubCheckResult-Name"></a>
The name of the sub-check.
Type: String
Required: No

 ** References **   <a name="ssmsap-Type-SubCheckResult-References"></a>
A list of references or documentation links related to the sub-check.
Type: Array of strings
Required: No

## See Also
<a name="API_SubCheckResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/SubCheckResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/SubCheckResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/SubCheckResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
