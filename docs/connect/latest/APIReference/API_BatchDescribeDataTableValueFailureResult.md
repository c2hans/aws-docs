---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchDescribeDataTableValueFailureResult.html
---

# BatchDescribeDataTableValueFailureResult
<a name="API_BatchDescribeDataTableValueFailureResult"></a>

A batch describe data table value failure result.

## Contents
<a name="API_BatchDescribeDataTableValueFailureResult_Contents"></a>

 ** AttributeName **   <a name="connect-Type-BatchDescribeDataTableValueFailureResult-AttributeName"></a>
The result's attribute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** Message **   <a name="connect-Type-BatchDescribeDataTableValueFailureResult-Message"></a>
The result's message.
Type: String
Required: Yes

 ** PrimaryValues **   <a name="connect-Type-BatchDescribeDataTableValueFailureResult-PrimaryValues"></a>
The result's primary values.
Type: Array of [PrimaryValue](API_PrimaryValue.md) objects
Required: Yes

## See Also
<a name="API_BatchDescribeDataTableValueFailureResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/BatchDescribeDataTableValueFailureResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/BatchDescribeDataTableValueFailureResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/BatchDescribeDataTableValueFailureResult)
