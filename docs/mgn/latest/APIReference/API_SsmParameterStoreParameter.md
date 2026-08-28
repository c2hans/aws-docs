---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_SsmParameterStoreParameter.html
---

# SsmParameterStoreParameter
<a name="API_SsmParameterStoreParameter"></a>

AWS Systems Manager Parameter Store parameter.

## Contents
<a name="API_SsmParameterStoreParameter_Contents"></a>

 ** parameterName **   <a name="mgn-Type-SsmParameterStoreParameter-parameterName"></a>
AWS Systems Manager Parameter Store parameter name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `([A-Za-z0-9_\.-])+`
Required: Yes

 ** parameterType **   <a name="mgn-Type-SsmParameterStoreParameter-parameterType"></a>
AWS Systems Manager Parameter Store parameter type.
Type: String
Valid Values: `STRING | SECURE_STRING`
Required: Yes

## See Also
<a name="API_SsmParameterStoreParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/SsmParameterStoreParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/SsmParameterStoreParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/SsmParameterStoreParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
