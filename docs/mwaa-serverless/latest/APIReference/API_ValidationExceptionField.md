---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ValidationExceptionField.html
---

# ValidationExceptionField
<a name="API_ValidationExceptionField"></a>

Contains information about a field that failed validation, including the field name and a descriptive error message.

## Contents
<a name="API_ValidationExceptionField_Contents"></a>

 ** Message **   <a name="mwaaserverless-Type-ValidationExceptionField-Message"></a>
A message that describes why the field failed validation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`
Required: Yes

 ** Name **   <a name="mwaaserverless-Type-ValidationExceptionField-Name"></a>
The name of the field that failed validation.
Type: String
Required: Yes

## See Also
<a name="API_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/ValidationExceptionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/ValidationExceptionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/ValidationExceptionField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
