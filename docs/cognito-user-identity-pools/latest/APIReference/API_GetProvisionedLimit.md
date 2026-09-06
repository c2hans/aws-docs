---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GetProvisionedLimit.html
---

# GetProvisionedLimit
<a name="API_GetProvisionedLimit"></a>

Returns the current provisioned limit for a specific API category.

For more information about adjustable API rate limits, see [Managing provisioned limits](https://docs.aws.amazon.com/cognito/latest/developerguide/quotas.html#provisioned-quotas).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_GetProvisionedLimit_RequestSyntax"></a>

```
{
   "LimitDefinition": {
      "Attributes": {
         "{{string}}" : "{{string}}"
      },
      "LimitClass": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetProvisionedLimit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LimitDefinition](#API_GetProvisionedLimit_RequestSyntax) **   <a name="CognitoUserPools-GetProvisionedLimit-request-LimitDefinition"></a>
The limit to retrieve. Specify the limit class and the attributes that identify the limit.
Type: [LimitDefinitionType](API_LimitDefinitionType.md) object
Required: Yes

## Response Syntax
<a name="API_GetProvisionedLimit_ResponseSyntax"></a>

```
{
   "Limit": {
      "FreeLimitValue": number,
      "LimitDefinition": {
         "Attributes": {
            "string" : "string"
         },
         "LimitClass": "string"
      },
      "ProvisionedLimitValue": number
   }
}
```

## Response Elements
<a name="API_GetProvisionedLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Limit](#API_GetProvisionedLimit_ResponseSyntax) **   <a name="CognitoUserPools-GetProvisionedLimit-response-Limit"></a>
The provisioned and default limit values for the requested limit.
Type: [LimitType](API_LimitType.md) object

## Errors
<a name="API_GetProvisionedLimit_Errors"></a>

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

## See Also
<a name="API_GetProvisionedLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/GetProvisionedLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/GetProvisionedLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/GetProvisionedLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/GetProvisionedLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/GetProvisionedLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/GetProvisionedLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/GetProvisionedLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/GetProvisionedLimit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/GetProvisionedLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/GetProvisionedLimit)
