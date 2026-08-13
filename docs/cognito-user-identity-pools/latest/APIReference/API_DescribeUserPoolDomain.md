---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolDomain.html
---

# DescribeUserPoolDomain
<a name="API_DescribeUserPoolDomain"></a>

Given a user pool domain name, returns information about the domain configuration.

**Note**
This operation doesn't return results when you query a prefix domain in a secondary Region. Prefix domains are Region-specific and can only be described in the Region where they were created. To describe a prefix domain for a replica user pool, make the request to the primary Region's endpoint.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_DescribeUserPoolDomain_RequestSyntax"></a>

```
{
   "Domain": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeUserPoolDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Domain](#API_DescribeUserPoolDomain_RequestSyntax) **   <a name="CognitoUserPools-DescribeUserPoolDomain-request-Domain"></a>
The domain that you want to describe. For custom domains, this is the fully-qualified domain name, such as `auth.example.com`. For Amazon Cognito prefix domains, this is the prefix alone, such as `auth`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?$`
Required: Yes

## Response Syntax
<a name="API_DescribeUserPoolDomain_ResponseSyntax"></a>

```
{
   "DomainDescription": {
      "AWSAccountId": "string",
      "CloudFrontDistribution": "string",
      "CustomDomainConfig": {
         "CertificateArn": "string",
         "SecurityPolicy": "string"
      },
      "Domain": "string",
      "ManagedLoginVersion": number,
      "Routing": {
         "Failover": {
            "PrimaryRoute53HealthCheckId": "string",
            "SecondaryRegion": "string"
         }
      },
      "S3Bucket": "string",
      "Status": "string",
      "UserPoolId": "string",
      "Version": "string"
   }
}
```

## Response Elements
<a name="API_DescribeUserPoolDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainDescription](#API_DescribeUserPoolDomain_ResponseSyntax) **   <a name="CognitoUserPools-DescribeUserPoolDomain-response-DomainDescription"></a>
The details of the requested user pool domain.
Type: [DomainDescriptionType](API_DomainDescriptionType.md) object

## Errors
<a name="API_DescribeUserPoolDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## Examples
<a name="API_DescribeUserPoolDomain_Examples"></a>

### Example
<a name="API_DescribeUserPoolDomain_Example_1"></a>

The following example request describes the custom domain `auth.example.com` for the user pool `us-west-2_EXAMPLE`.

#### Sample Request
<a name="API_DescribeUserPoolDomain_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.DescribeUserPoolDomain
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "Domain": "auth.example.com"
}
```

#### Sample Response
<a name="API_DescribeUserPoolDomain_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "DomainDescription": {
        "AWSAccountId": "123456789012",
        "CloudFrontDistribution": "example.cloudfront.net",
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
        "S3Bucket": "aws-cognito-prod-pdx-assets",
        "Status": "ACTIVE",
        "UserPoolId": "us-west-2_EXAMPLE",
        "Version": "20241127003837"
    }
}
```

## See Also
<a name="API_DescribeUserPoolDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/DescribeUserPoolDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/DescribeUserPoolDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DescribeUserPoolDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/DescribeUserPoolDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DescribeUserPoolDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/DescribeUserPoolDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/DescribeUserPoolDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/DescribeUserPoolDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/DescribeUserPoolDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DescribeUserPoolDomain)
