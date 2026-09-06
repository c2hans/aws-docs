---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MembershipProtectedQueryResultConfiguration.html
---

# MembershipProtectedQueryResultConfiguration
<a name="API_MembershipProtectedQueryResultConfiguration"></a>

Contains configurations for protected query results.

## Contents
<a name="API_MembershipProtectedQueryResultConfiguration_Contents"></a>

 ** outputConfiguration **   <a name="API-Type-MembershipProtectedQueryResultConfiguration-outputConfiguration"></a>
Configuration for protected query results.
Type: [MembershipProtectedQueryOutputConfiguration](API_MembershipProtectedQueryOutputConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** roleArn **   <a name="API-Type-MembershipProtectedQueryResultConfiguration-roleArn"></a>
The unique ARN for an IAM role that is used by AWS Clean Rooms to write protected query results to the result location, given by the member who can receive results.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 512.
Pattern: `arn:aws:iam::[\w]+:role/[\w+=./@-]+`
Required: No

## See Also
<a name="API_MembershipProtectedQueryResultConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MembershipProtectedQueryResultConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MembershipProtectedQueryResultConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MembershipProtectedQueryResultConfiguration)
