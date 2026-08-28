---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_QuickConnect.html
---

# QuickConnect
<a name="API_QuickConnect"></a>

Contains information about a quick connect.

## Contents
<a name="API_QuickConnect_Contents"></a>

 ** Description **   <a name="connect-Type-QuickConnect-Description"></a>
The description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-QuickConnect-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-QuickConnect-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-QuickConnect-Name"></a>
The name of the quick connect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** QuickConnectARN **   <a name="connect-Type-QuickConnect-QuickConnectARN"></a>
The Amazon Resource Name (ARN) of the quick connect.
Type: String
Required: No

 ** QuickConnectConfig **   <a name="connect-Type-QuickConnect-QuickConnectConfig"></a>
Contains information about the quick connect.
Type: [QuickConnectConfig](API_QuickConnectConfig.md) object
Required: No

 ** QuickConnectId **   <a name="connect-Type-QuickConnect-QuickConnectId"></a>
The identifier for the quick connect.
Type: String
Required: No

 ** Tags **   <a name="connect-Type-QuickConnect-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_QuickConnect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/QuickConnect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/QuickConnect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/QuickConnect)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
