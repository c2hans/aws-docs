---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_UserIdentity.html
---

# UserIdentity
<a name="API_UserIdentity"></a>

Information about a user whose activity is recorded in an event for a space.

## Contents
<a name="API_UserIdentity_Contents"></a>

 ** principalId **   <a name="codecatalyst-Type-UserIdentity-principalId"></a>
The ID of the Amazon CodeCatalyst service principal.
Type: String
Required: Yes

 ** userType **   <a name="codecatalyst-Type-UserIdentity-userType"></a>
The role assigned to the user in a Amazon CodeCatalyst space or project when the event occurred.
Type: String
Valid Values: `USER | AWS_ACCOUNT | UNKNOWN`
Required: Yes

 ** awsAccountId **   <a name="codecatalyst-Type-UserIdentity-awsAccountId"></a>
The AWS account number of the user in AWS, if any.
Type: String
Required: No

 ** userName **   <a name="codecatalyst-Type-UserIdentity-userName"></a>
The display name of the user in Amazon CodeCatalyst.
Type: String
Required: No

## See Also
<a name="API_UserIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/UserIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/UserIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/UserIdentity)
