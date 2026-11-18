---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-scheduling_ActorInfo.html
---

# ActorInfo
<a name="API_connect-scheduling_ActorInfo"></a>

Information about the identity that performed an action on a time off request: a Connect Customer user or an IAM or AWS STS identity. Exactly one member is set.

## Contents
<a name="API_connect-scheduling_ActorInfo_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AWSIdentityArn **   <a name="connect-Type-connect-scheduling_ActorInfo-AWSIdentityArn"></a>
The IAM or AWS STS ARN of the identity that performed the action. Present when that identity is not a Connect Customer user.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** ConnectUserArn **   <a name="connect-Type-connect-scheduling_ActorInfo-ConnectUserArn"></a>
The ARN of the Connect Customer user who performed the action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_connect-scheduling_ActorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectscheduling-2026-07-16/ActorInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectscheduling-2026-07-16/ActorInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectscheduling-2026-07-16/ActorInfo)
