---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UserSummary.html
---

# UserSummary
<a name="API_UserSummary"></a>

Contains summary information about a user.

## Contents
<a name="API_UserSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-UserSummary-Arn"></a>
The Amazon Resource Name (ARN) of the user account.
Type: String
Required: No

 ** Id **   <a name="connect-Type-UserSummary-Id"></a>
The identifier of the user account.
Type: String
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-UserSummary-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-UserSummary-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** Username **   <a name="connect-Type-UserSummary-Username"></a>
The Connect Customer user name of the user account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_UserSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UserSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UserSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UserSummary)
