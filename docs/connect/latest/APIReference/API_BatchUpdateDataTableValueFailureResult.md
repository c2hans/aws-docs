---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchUpdateDataTableValueFailureResult.html
---

# BatchUpdateDataTableValueFailureResult
<a name="API_BatchUpdateDataTableValueFailureResult"></a>

A batch update data table value failure result.

## Contents
<a name="API_BatchUpdateDataTableValueFailureResult_Contents"></a>

 ** AttributeName **   <a name="connect-Type-BatchUpdateDataTableValueFailureResult-AttributeName"></a>
The result's attribute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** Message **   <a name="connect-Type-BatchUpdateDataTableValueFailureResult-Message"></a>
The result's message.
Type: String
Required: Yes

 ** PrimaryValues **   <a name="connect-Type-BatchUpdateDataTableValueFailureResult-PrimaryValues"></a>
The result's primary values.
Type: Array of [PrimaryValue](API_PrimaryValue.md) objects
Required: Yes

## See Also
<a name="API_BatchUpdateDataTableValueFailureResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/BatchUpdateDataTableValueFailureResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/BatchUpdateDataTableValueFailureResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/BatchUpdateDataTableValueFailureResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
