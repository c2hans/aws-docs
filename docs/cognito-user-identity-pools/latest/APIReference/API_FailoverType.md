---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_FailoverType.html
---

# FailoverType
<a name="API_FailoverType"></a>

Specifies failover configuration for multi-region user pool domains. Contains settings for the secondary region and health check configuration.

This data type is a request parameter of [CreateUserPoolDomain](API_CreateUserPoolDomain.md) and [UpdateUserPoolDomain](API_UpdateUserPoolDomain.md), and a response parameter of [DescribeUserPoolDomain](API_DescribeUserPoolDomain.md).

## Contents
<a name="API_FailoverType_Contents"></a>

 ** PrimaryRoute53HealthCheckId **   <a name="CognitoUserPools-Type-FailoverType-PrimaryRoute53HealthCheckId"></a>
The ID of the AWS Route53 healthcheck that controls routing. If the healthcheck is healthy, traffic will be routed to the primary replica, and if the healthcheck is unhealthy, traffic will be routed to the secondary region.
Type: String
Length Constraints: Maximum length of 64.
Required: Yes

 ** SecondaryRegion **   <a name="CognitoUserPools-Type-FailoverType-SecondaryRegion"></a>
The secondary AWS Region to use for failover when the primary region becomes unavailable.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 32.
Required: Yes

## See Also
<a name="API_FailoverType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/FailoverType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/FailoverType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/FailoverType)
