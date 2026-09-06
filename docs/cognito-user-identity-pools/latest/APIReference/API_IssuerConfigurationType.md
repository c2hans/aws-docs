---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_IssuerConfigurationType.html
---

# IssuerConfigurationType
<a name="API_IssuerConfigurationType"></a>

Specifies the issuer configuration for a user pool. Contains settings that determine how tokens are issued and validated.

This data type is a request parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_IssuerConfigurationType_Contents"></a>

 ** Type **   <a name="CognitoUserPools-Type-IssuerConfigurationType-Type"></a>
The type of issuer configuration. Determines the token issuing behavior for the user pool.
ORIGINAL
The original issuer configuration for user pools. The issuer URL is hosted in the user pool’s region and provides OIDC endpoints specific to that region.
Original issuers have the format of `https://cognito-idp.[region].amazonaws.com/[userPoolId]`
UPDATED
Recommended for all user pools, including for multi-Region replication. Updated issuers host the same JWKS content in multiple regions, resulting in improved resilience and efficiency.
Updated issuers have the format of `https://issuer-cognito-idp.[region].amazonaws.com/[userPoolId]`, where region is the primary AWS Region of your user pool.
Type: String
Valid Values: `ORIGINAL | UPDATED`
Required: No

## See Also
<a name="API_IssuerConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/IssuerConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/IssuerConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/IssuerConfigurationType)
