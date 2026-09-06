---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IdentitySourceDetails.html
---

# IdentitySourceDetails
<a name="API_IdentitySourceDetails"></a>

 *This data type has been deprecated.*

A structure that contains configuration of the identity source.

This data type was a response parameter for the [GetIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html) operation. Replaced by [ConfigurationDetail](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ConfigurationDetail.html).

## Contents
<a name="API_IdentitySourceDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** clientIds **   <a name="verifiedpermissions-Type-IdentitySourceDetails-clientIds"></a>
 *This member has been deprecated.*
The application client IDs associated with the specified Amazon Cognito user pool that are enabled for this identity source.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** discoveryUrl **   <a name="verifiedpermissions-Type-IdentitySourceDetails-discoveryUrl"></a>
 *This member has been deprecated.*
The well-known URL that points to this user pool's OIDC discovery endpoint. This is a URL string in the following format. This URL replaces the placeholders for both the AWS Region and the user pool identifier with those appropriate for this user pool.
 `https://cognito-idp.<region>.amazonaws.com/<user-pool-id>/.well-known/openid-configuration`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://.*`
Required: No

 ** openIdIssuer **   <a name="verifiedpermissions-Type-IdentitySourceDetails-openIdIssuer"></a>
 *This member has been deprecated.*
A string that identifies the type of OIDC service represented by this identity source.
At this time, the only valid value is `cognito`.
Type: String
Valid Values: `COGNITO`
Required: No

 ** userPoolArn **   <a name="verifiedpermissions-Type-IdentitySourceDetails-userPoolArn"></a>
 *This member has been deprecated.*
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Amazon Cognito user pool whose identities are accessible to this Verified Permissions policy store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:[a-zA-Z0-9-]+:cognito-idp:(([a-zA-Z0-9-]+:\d{12}:userpool/[\w-]+_[0-9a-zA-Z]+))`
Required: No

## See Also
<a name="API_IdentitySourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/IdentitySourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/IdentitySourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/IdentitySourceDetails)
