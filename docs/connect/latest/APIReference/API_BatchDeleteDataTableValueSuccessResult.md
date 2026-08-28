---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchDeleteDataTableValueSuccessResult.html
---

# BatchDeleteDataTableValueSuccessResult
<a name="API_BatchDeleteDataTableValueSuccessResult"></a>

A batch delete data table value success result.

## Contents
<a name="API_BatchDeleteDataTableValueSuccessResult_Contents"></a>

 ** AttributeName **   <a name="connect-Type-BatchDeleteDataTableValueSuccessResult-AttributeName"></a>
The result's attribute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** LockVersion **   <a name="connect-Type-BatchDeleteDataTableValueSuccessResult-LockVersion"></a>
The result's lock version.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object
Required: Yes

 ** PrimaryValues **   <a name="connect-Type-BatchDeleteDataTableValueSuccessResult-PrimaryValues"></a>
The result's primary values.
Type: Array of [PrimaryValue](API_PrimaryValue.md) objects
Required: Yes

## See Also
<a name="API_BatchDeleteDataTableValueSuccessResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/BatchDeleteDataTableValueSuccessResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/BatchDeleteDataTableValueSuccessResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/BatchDeleteDataTableValueSuccessResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
