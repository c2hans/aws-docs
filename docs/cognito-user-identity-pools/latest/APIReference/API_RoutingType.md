---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RoutingType.html
---

# RoutingType
<a name="API_RoutingType"></a>

Specifies routing configuration for user pool domains. Contains failover settings for multi-region deployments.

This data type is a request parameter of [CreateUserPoolDomain](API_CreateUserPoolDomain.md) and [UpdateUserPoolDomain](API_UpdateUserPoolDomain.md), and a response parameter of [DescribeUserPoolDomain](API_DescribeUserPoolDomain.md).

## Contents
<a name="API_RoutingType_Contents"></a>

 ** Failover **   <a name="CognitoUserPools-Type-RoutingType-Failover"></a>
The failover configuration that specifies the secondary region and health check settings.
Type: [FailoverType](API_FailoverType.md) object
Required: No

## See Also
<a name="API_RoutingType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/RoutingType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/RoutingType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/RoutingType)
