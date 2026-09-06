---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_QuickConnectSummary.html
---

# QuickConnectSummary
<a name="API_QuickConnectSummary"></a>

Contains summary information about a quick connect.

## Contents
<a name="API_QuickConnectSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-QuickConnectSummary-Arn"></a>
The Amazon Resource Name (ARN) of the quick connect.
Type: String
Required: No

 ** Id **   <a name="connect-Type-QuickConnectSummary-Id"></a>
The identifier for the quick connect.
Type: String
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-QuickConnectSummary-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-QuickConnectSummary-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-QuickConnectSummary-Name"></a>
The name of the quick connect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** QuickConnectType **   <a name="connect-Type-QuickConnectSummary-QuickConnectType"></a>
The type of quick connect. In the Connect Customer admin website, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE\_NUMBER), or Queue (QUEUE).
Type: String
Valid Values: `USER | QUEUE | PHONE_NUMBER | FLOW`
Required: No

## See Also
<a name="API_QuickConnectSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/QuickConnectSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/QuickConnectSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/QuickConnectSummary)
