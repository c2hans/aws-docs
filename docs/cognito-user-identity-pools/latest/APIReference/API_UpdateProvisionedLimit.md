---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateProvisionedLimit.html
---

# UpdateProvisionedLimit
<a name="API_UpdateProvisionedLimit"></a>

Sets the provisioned limit for a specific API category. The value must be between the default limit and your account-level maximum limit in Service Quotas.

For more information about adjustable API rate limits, see [Managing provisioned limits](https://docs.aws.amazon.com/cognito/latest/developerguide/quotas.html#provisioned-quotas).

Managed login user pools don't support adjustments to the `UserAuthentication` or `UserFederation` categories. To increase these limits, submit a Service Quotas increase request.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_UpdateProvisionedLimit_RequestSyntax"></a>

```
{
   "LimitDefinition": {
      "Attributes": {
         "{{string}}" : "{{string}}"
      },
      "LimitClass": "{{string}}"
   },
   "RequestedLimitValue": {{number}}
}
```

## Request Parameters
<a name="API_UpdateProvisionedLimit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LimitDefinition](#API_UpdateProvisionedLimit_RequestSyntax) **   <a name="CognitoUserPools-UpdateProvisionedLimit-request-LimitDefinition"></a>
The limit to update. Specify the limit class and the attributes that identify the limit.
Type: [LimitDefinitionType](API_LimitDefinitionType.md) object
Required: Yes

 ** [RequestedLimitValue](#API_UpdateProvisionedLimit_RequestSyntax) **   <a name="CognitoUserPools-UpdateProvisionedLimit-request-RequestedLimitValue"></a>
The provisioned rate to set, in requests per second (RPS).
Type: Integer
Required: Yes

## Response Syntax
<a name="API_UpdateProvisionedLimit_ResponseSyntax"></a>

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
<a name="API_UpdateProvisionedLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Limit](#API_UpdateProvisionedLimit_ResponseSyntax) **   <a name="CognitoUserPools-UpdateProvisionedLimit-response-Limit"></a>
The updated provisioned and default limit values.
Type: [LimitType](API_LimitType.md) object

## Errors
<a name="API_UpdateProvisionedLimit_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request exceeded your account's service quota. To increase your limit, use [UpdateProvisionedLimit](#API_UpdateProvisionedLimit) or submit a Service Quotas increase request.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateProvisionedLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/UpdateProvisionedLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/UpdateProvisionedLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UpdateProvisionedLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/UpdateProvisionedLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UpdateProvisionedLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/UpdateProvisionedLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/UpdateProvisionedLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/UpdateProvisionedLimit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/UpdateProvisionedLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UpdateProvisionedLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
