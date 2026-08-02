---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreatedByInfo.html
---

# CreatedByInfo
<a name="API_CreatedByInfo"></a>

Information on the identity that created the file.

## Contents
<a name="API_CreatedByInfo_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AWSIdentityArn **   <a name="connect-Type-CreatedByInfo-AWSIdentityArn"></a>
STS or IAM ARN representing the identity of API Caller. SDK users cannot populate this and this value is calculated automatically if `ConnectUserArn` is not provided.
Type: String
Required: No

 ** ConnectUserArn **   <a name="connect-Type-CreatedByInfo-ConnectUserArn"></a>
An agent ARN representing a [connect user](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html#amazonconnect-resources-for-iam-policies).
Type: String
Required: No

## See Also
<a name="API_CreatedByInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreatedByInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreatedByInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreatedByInfo)
