---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AuthenticationProfileSummary.html
---

# AuthenticationProfileSummary
<a name="API_AuthenticationProfileSummary"></a>

This API is in preview release for Connect Customer and is subject to change. To request access to this API, contact Support.

A summary of a given authentication profile.

## Contents
<a name="API_AuthenticationProfileSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-AuthenticationProfileSummary-Arn"></a>
The Amazon Resource Name (ARN) of the authentication profile summary.
Type: String
Required: No

 ** Id **   <a name="connect-Type-AuthenticationProfileSummary-Id"></a>
The unique identifier of the authentication profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IsDefault **   <a name="connect-Type-AuthenticationProfileSummary-IsDefault"></a>
Shows whether the authentication profile is the default authentication profile for the Connect Customer instance. The default authentication profile applies to all agents in an Connect Customer instance, unless overridden by another authentication profile.
Type: Boolean
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-AuthenticationProfileSummary-LastModifiedRegion"></a>
The AWS Region when the authentication profile summary was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-AuthenticationProfileSummary-LastModifiedTime"></a>
The timestamp when the authentication profile summary was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-AuthenticationProfileSummary-Name"></a>
The name of the authentication profile summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_AuthenticationProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AuthenticationProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AuthenticationProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AuthenticationProfileSummary)
