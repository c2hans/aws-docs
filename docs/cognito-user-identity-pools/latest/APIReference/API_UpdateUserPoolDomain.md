---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolDomain.html
---

# UpdateUserPoolDomain
<a name="API_UpdateUserPoolDomain"></a>

A user pool domain hosts managed login, an authorization server and web server for authentication in your application. This operation updates the branding version for user pool domains between `1` for hosted UI (classic) and `2` for managed login. It also updates the SSL certificate for user pool custom domains.

Changes to the domain branding version take up to one minute to take effect for a prefix domain and up to five minutes for a custom domain.

This operation doesn't change the name of your user pool domain. To change your domain, delete it with `DeleteUserPoolDomain` and create a new domain with `CreateUserPoolDomain`.

You can pass the ARN of a new AWS Certificate Manager certificate in this request. Typically, ACM certificates automatically renew and you user pool can continue to use the same ARN. But if you generate a new certificate for your custom domain name, replace the original configuration with the new ARN in this request.

ACM certificates for custom domains must be in the US East (N. Virginia) AWS Region. After you submit your request, Amazon Cognito requires up to 1 hour to distribute your new certificate to your custom domain.

For more information about adding a custom domain to your user pool, see [Configuring a user pool domain](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_UpdateUserPoolDomain_RequestSyntax"></a>

```
{
   "CustomDomainConfig": {
      "CertificateArn": "{{string}}",
      "SecurityPolicy": "{{string}}"
   },
   "Domain": "{{string}}",
   "ManagedLoginVersion": {{number}},
   "Routing": {
      "Failover": {
         "PrimaryRoute53HealthCheckId": "{{string}}",
         "SecondaryRegion": "{{string}}"
      }
   },
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateUserPoolDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CustomDomainConfig](#API_UpdateUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-UpdateUserPoolDomain-request-CustomDomainConfig"></a>
The configuration for a custom domain that hosts managed login for your application. In an `UpdateUserPoolDomain` request, this parameter specifies an SSL certificate for the managed login hosted webserver. The certificate must be an ACM ARN in `us-east-1`.
When you create a custom domain, the passkey RP ID defaults to the custom domain. If you had a prefix domain active, this will cause passkey integration for your prefix domain to stop working due to a mismatch in RP ID. To keep the prefix domain passkey integration working, you can explicitly set RP ID to the prefix domain.
Update the RP ID in a [SetUserPoolMfaConfig](API_SetUserPoolMfaConfig.md) request.
Type: [CustomDomainConfigType](API_CustomDomainConfigType.md) object
Required: No

 ** [Domain](#API_UpdateUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-UpdateUserPoolDomain-request-Domain"></a>
The name of the domain that you want to update. For custom domains, this is the fully-qualified domain name, for example `auth.example.com`. For prefix domains, this is the prefix alone, such as `myprefix`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?$`
Required: Yes

 ** [ManagedLoginVersion](#API_UpdateUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-UpdateUserPoolDomain-request-ManagedLoginVersion"></a>
A version number that indicates the state of managed login for your domain. Version `1` is hosted UI (classic). Version `2` is the newer managed login with the branding editor. For more information, see [Managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html).
Type: Integer
Required: No

 ** [Routing](#API_UpdateUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-UpdateUserPoolDomain-request-Routing"></a>
The routing configuration for the user pool domain. Specifies failover settings for multi-region deployments.
Type: [RoutingType](API_RoutingType.md) object
Required: No

 ** [UserPoolId](#API_UpdateUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-UpdateUserPoolDomain-request-UserPoolId"></a>
The ID of the user pool that is associated with the domain you're updating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_UpdateUserPoolDomain_ResponseSyntax"></a>

```
{
   "CloudFrontDomain": "string",
   "ManagedLoginVersion": number,
   "Routing": {
      "Failover": {
         "PrimaryRoute53HealthCheckId": "string",
         "SecondaryRegion": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateUserPoolDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudFrontDomain](#API_UpdateUserPoolDomain_ResponseSyntax) **   <a name="CognitoUserPools-UpdateUserPoolDomain-response-CloudFrontDomain"></a>
The fully-qualified domain name (FQDN) of the Amazon CloudFront distribution that hosts your managed login or classic hosted UI pages. You domain-name authority must have an alias record that points requests for your custom domain to this FQDN. Amazon Cognito returns this value if you set a custom domain with `CustomDomainConfig`. If you set an Amazon Cognito prefix domain, this operation returns a blank response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?$`

 ** [ManagedLoginVersion](#API_UpdateUserPoolDomain_ResponseSyntax) **   <a name="CognitoUserPools-UpdateUserPoolDomain-response-ManagedLoginVersion"></a>
A version number that indicates the state of managed login for your domain. Version `1` is hosted UI (classic). Version `2` is the newer managed login with the branding editor. For more information, see [Managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html).
Type: Integer

 ** [Routing](#API_UpdateUserPoolDomain_ResponseSyntax) **   <a name="CognitoUserPools-UpdateUserPoolDomain-response-Routing"></a>
The updated routing configuration for the user pool domain.
Type: [RoutingType](API_RoutingType.md) object

## Errors
<a name="API_UpdateUserPoolDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
This exception is thrown if two or more modifications are happening concurrently.
 ** message **
The message provided when the concurrent exception is thrown.
HTTP Status Code: 400

 ** FeatureUnavailableInTierException **
This exception is thrown when a feature you attempted to configure isn't available in your current feature plan.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## Examples
<a name="API_UpdateUserPoolDomain_Examples"></a>

### Example
<a name="API_UpdateUserPoolDomain_Example_1"></a>

The following example request configures an ACM certificate, sets the managed login branding version to 2, and configures multi-region failover routing for a custom domain.

#### Sample Request
<a name="API_UpdateUserPoolDomain_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.ca-central-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.UpdateUserPoolDomain
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "CustomDomainConfig": {
      "CertificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
      "SecurityPolicy": "TLS_V1_2_2021"
   },
   "Domain": "auth.example.com",
   "ManagedLoginVersion": 2,
   "Routing": {
      "Failover": {
         "SecondaryRegion": "us-west-2",
         "PrimaryRoute53HealthCheckId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
      }
   },
   "UserPoolId": "ca-central-1_EXAMPLE"
}
```

#### Sample Response
<a name="API_UpdateUserPoolDomain_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "CloudFrontDomain": "example.cloudfront.net",
    "ManagedLoginVersion": 2,
    "Routing": {
        "Failover": {
            "SecondaryRegion": "us-west-2",
            "PrimaryRoute53HealthCheckId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        }
    }
}
```

## See Also
<a name="API_UpdateUserPoolDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/UpdateUserPoolDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/UpdateUserPoolDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UpdateUserPoolDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/UpdateUserPoolDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UpdateUserPoolDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/UpdateUserPoolDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/UpdateUserPoolDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/UpdateUserPoolDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/UpdateUserPoolDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UpdateUserPoolDomain)
