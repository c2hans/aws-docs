---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchDescribeDataTableValueSuccessResult.html
---

# BatchDescribeDataTableValueSuccessResult
<a name="API_BatchDescribeDataTableValueSuccessResult"></a>

A batch describe data table value success result.

## Contents
<a name="API_BatchDescribeDataTableValueSuccessResult_Contents"></a>

 ** AttributeId **   <a name="connect-Type-BatchDescribeDataTableValueSuccessResult-AttributeId"></a>
The result's attribute ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** AttributeName **   <a name="connect-Type-BatchDescribeDataTableValueSuccessResult-AttributeName"></a>
The result's attribute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** LockVersion **   <a name="connect-Type-BatchDescribeDataTableValueSuccessResult-LockVersion"></a>
The result's lock version.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object
Required: Yes

 ** PrimaryValues **   <a name="connect-Type-BatchDescribeDataTableValueSuccessResult-PrimaryValues"></a>
The result's primary values.
Type: Array of [PrimaryValueResponse](API_PrimaryValueResponse.md) objects
Required: Yes

 ** RecordId **   <a name="connect-Type-BatchDescribeDataTableValueSuccessResult-RecordId"></a>
The result's record ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** LastModifiedRegion **   <a name="connect-Type-BatchDescribeDataTableValueSuccessResult-LastModifiedRegion"></a>
The result's last modified region.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-BatchDescribeDataTableValueSuccessResult-LastModifiedTime"></a>
The result's last modified time.
Type: Timestamp
Required: No

 ** Value **   <a name="connect-Type-BatchDescribeDataTableValueSuccessResult-Value"></a>
The result's value.
Type: String
Required: No

## See Also
<a name="API_BatchDescribeDataTableValueSuccessResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/BatchDescribeDataTableValueSuccessResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/BatchDescribeDataTableValueSuccessResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/BatchDescribeDataTableValueSuccessResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
