---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UserUnion.html
---

# UserUnion
<a name="API_connect-cases_UserUnion"></a>

Represents the entity that performed the action.

## Contents
<a name="API_connect-cases_UserUnion_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customEntity **   <a name="connect-Type-connect-cases_UserUnion-customEntity"></a>
Any provided entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[a-zA-Z0-9_\-\.@:/ ]*[a-zA-Z0-9_\-\.@:/]`
Required: No

 ** userArn **   <a name="connect-Type-connect-cases_UserUnion-userArn"></a>
Represents the Connect Customer ARN of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_connect-cases_UserUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/UserUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/UserUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/UserUnion)
