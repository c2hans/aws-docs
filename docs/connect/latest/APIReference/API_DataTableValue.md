---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DataTableValue.html
---

# DataTableValue
<a name="API_DataTableValue"></a>

A data table value.

## Contents
<a name="API_DataTableValue_Contents"></a>

 ** AttributeName **   <a name="connect-Type-DataTableValue-AttributeName"></a>
The value's attribute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** Value **   <a name="connect-Type-DataTableValue-Value"></a>
The value's value.
Type: String
Required: Yes

 ** LastModifiedRegion **   <a name="connect-Type-DataTableValue-LastModifiedRegion"></a>
The value's last modified region.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-DataTableValue-LastModifiedTime"></a>
The value's last modified time.
Type: Timestamp
Required: No

 ** LockVersion **   <a name="connect-Type-DataTableValue-LockVersion"></a>
The value's lock version.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object
Required: No

 ** PrimaryValues **   <a name="connect-Type-DataTableValue-PrimaryValues"></a>
The value's primary values.
Type: Array of [PrimaryValue](API_PrimaryValue.md) objects
Required: No

## See Also
<a name="API_DataTableValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DataTableValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DataTableValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DataTableValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
