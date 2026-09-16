---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolDomain.html
---

# CreateUserPoolDomain
<a name="API_CreateUserPoolDomain"></a>

A user pool domain hosts managed login, an authorization server and web server for authentication in your application. This operation creates a new user pool prefix domain or custom domain and sets the managed login branding version. Set the branding version to `1` for hosted UI (classic) or `2` for managed login. When you choose a custom domain, you must provide an SSL certificate in the US East (N. Virginia) AWS Region in your request.

Your prefix domain might take up to one minute to take effect. Your custom domain is online within five minutes, but it can take up to one hour to distribute your SSL certificate.

For more information about adding a custom domain to your user pool, see [Configuring a user pool domain](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_CreateUserPoolDomain_RequestSyntax"></a>

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
<a name="API_CreateUserPoolDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CustomDomainConfig](#API_CreateUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolDomain-request-CustomDomainConfig"></a>
The configuration for a custom domain. Configures your domain with an AWS Certificate Manager certificate in the `us-east-1` Region.
Provide this parameter only if you want to use a [custom domain](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html) for your user pool. Otherwise, you can omit this parameter and use a [prefix domain](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain-prefix.html) instead.
When you create a custom domain, the passkey RP ID defaults to the custom domain. If you had a prefix domain active, this will cause passkey integration for your prefix domain to stop working due to a mismatch in RP ID. To keep the prefix domain passkey integration working, you can explicitly set RP ID to the prefix domain.
Update the RP ID in a [SetUserPoolMfaConfig](API_SetUserPoolMfaConfig.md) request.
Type: [CustomDomainConfigType](API_CustomDomainConfigType.md) object
Required: No

 ** [Domain](#API_CreateUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolDomain-request-Domain"></a>
The domain string. For custom domains, this is the fully-qualified domain name, such as `auth.example.com`. For prefix domains, this is the prefix alone, such as `myprefix`. A prefix value of `myprefix` for a user pool in the `us-east-1` Region results in a domain of `myprefix.auth.us-east-1.amazoncognito.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?$`
Required: Yes

 ** [ManagedLoginVersion](#API_CreateUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolDomain-request-ManagedLoginVersion"></a>
The version of managed login branding that you want to apply to your domain. A value of `1` indicates hosted UI (classic) and a version of `2` indicates managed login.
Managed login requires that your user pool be configured for any [feature plan](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html) other than `Lite`.
A `ManagedLoginVersion` value of `2` does not activate managed login pages for your app client. When you create an app client programmatically, your app client has no branding style. To use managed login, create a branding style using the [CreateManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateManagedLoginBranding.html) operation. When you use the console, Amazon Cognito assigns a default branding style automatically. When you use the API or an SDK, you must create a branding style yourself.
Type: Integer
Required: No

 ** [Routing](#API_CreateUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolDomain-request-Routing"></a>
The configuration of routing for requests to the domain for replicas of a replicated user pool. The routing configuration is currently only supported for custom domains.
Type: [RoutingType](API_RoutingType.md) object
Required: No

 ** [UserPoolId](#API_CreateUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolDomain-request-UserPoolId"></a>
The ID of the user pool where you want to add a domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_CreateUserPoolDomain_ResponseSyntax"></a>

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
<a name="API_CreateUserPoolDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudFrontDomain](#API_CreateUserPoolDomain_ResponseSyntax) **   <a name="CognitoUserPools-CreateUserPoolDomain-response-CloudFrontDomain"></a>
The fully-qualified domain name (FQDN) of the Amazon CloudFront distribution that hosts your managed login or classic hosted UI pages. Your domain-name authority must have an alias record that points requests for your custom domain to this FQDN. Amazon Cognito returns this value if you set a custom domain with `CustomDomainConfig`. If you set an Amazon Cognito prefix domain, this parameter returns null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?$`

 ** [ManagedLoginVersion](#API_CreateUserPoolDomain_ResponseSyntax) **   <a name="CognitoUserPools-CreateUserPoolDomain-response-ManagedLoginVersion"></a>
The version of managed login branding applied your domain. A value of `1` indicates hosted UI (classic) and a version of `2` indicates managed login.
Type: Integer

 ** [Routing](#API_CreateUserPoolDomain_ResponseSyntax) **   <a name="CognitoUserPools-CreateUserPoolDomain-response-Routing"></a>
The routing configuration that was applied to the user pool domain.
Type: [RoutingType](API_RoutingType.md) object

## Errors
<a name="API_CreateUserPoolDomain_Errors"></a>

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

 ** LimitExceededException **
This exception is thrown when a user exceeds the limit for a requested AWS resource.
 ** message **
The message returned when Amazon Cognito throws a limit exceeded exception.
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

## Examples
<a name="API_CreateUserPoolDomain_Examples"></a>

### Example
<a name="API_CreateUserPoolDomain_Example_1"></a>

The following example creates a user pool custom domain with multi-region failover routing. Amazon Cognito creates resources for the resulting domain `auth.example.com` at the CloudFront distribution `example.cloudfront.net` with failover to the us-west-2 region.

#### Sample Request
<a name="API_CreateUserPoolDomain_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.ca-central-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.CreateUserPoolDomain
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
<a name="API_CreateUserPoolDomain_Example_1_Response"></a>

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
<a name="API_CreateUserPoolDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/CreateUserPoolDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/CreateUserPoolDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CreateUserPoolDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/CreateUserPoolDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CreateUserPoolDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/CreateUserPoolDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/CreateUserPoolDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/CreateUserPoolDomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/CreateUserPoolDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CreateUserPoolDomain)
