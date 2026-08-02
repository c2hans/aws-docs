---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminListUserAuthEvents.html
---

# AdminListUserAuthEvents
<a name="API_AdminListUserAuthEvents"></a>

Requests a history of user activity and any risks detected as part of Amazon Cognito threat protection. For more information, see [Viewing user event history](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-event-user-history).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_AdminListUserAuthEvents_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Username": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AdminListUserAuthEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_AdminListUserAuthEvents_RequestSyntax) **   <a name="CognitoUserPools-AdminListUserAuthEvents-request-MaxResults"></a>
The maximum number of authentication events to return. Returns 60 events if you set `MaxResults` to 0, or if you don't include a `MaxResults` parameter.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 60.
Required: No

 ** [NextToken](#API_AdminListUserAuthEvents_RequestSyntax) **   <a name="CognitoUserPools-AdminListUserAuthEvents-request-NextToken"></a>
This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\S]+`
Required: No

 ** [Username](#API_AdminListUserAuthEvents_RequestSyntax) **   <a name="CognitoUserPools-AdminListUserAuthEvents-request-Username"></a>
The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If `username` isn't an alias attribute in your user pool, this value must be the `sub` of a local user or the username of a user from a third-party IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [UserPoolId](#API_AdminListUserAuthEvents_RequestSyntax) **   <a name="CognitoUserPools-AdminListUserAuthEvents-request-UserPoolId"></a>
The Id of the user pool that contains the user profile with the logged events.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_AdminListUserAuthEvents_ResponseSyntax"></a>

```
{
   "AuthEvents": [
      {
         "ChallengeResponses": [
            {
               "ChallengeName": "string",
               "ChallengeResponse": "string"
            }
         ],
         "CreationDate": number,
         "EventContextData": {
            "City": "string",
            "Country": "string",
            "DeviceName": "string",
            "IpAddress": "string",
            "Timezone": "string"
         },
         "EventFeedback": {
            "FeedbackDate": number,
            "FeedbackValue": "string",
            "Provider": "string"
         },
         "EventId": "string",
         "EventResponse": "string",
         "EventRisk": {
            "CompromisedCredentialsDetected": boolean,
            "RiskDecision": "string",
            "RiskLevel": "string"
         },
         "EventType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_AdminListUserAuthEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthEvents](#API_AdminListUserAuthEvents_ResponseSyntax) **   <a name="CognitoUserPools-AdminListUserAuthEvents-response-AuthEvents"></a>
The response object. It includes the `EventID`, `EventType`, `CreationDate`, `EventRisk`, and `EventResponse`.
Type: Array of [AuthEventType](API_AuthEventType.md) objects

 ** [NextToken](#API_AdminListUserAuthEvents_ResponseSyntax) **   <a name="CognitoUserPools-AdminListUserAuthEvents-response-NextToken"></a>
The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\S]+`

## Errors
<a name="API_AdminListUserAuthEvents_Errors"></a>

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

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

 ** UserNotFoundException **
This exception is thrown when a user isn't found.
 ** message **
The message returned when a user isn't found.
HTTP Status Code: 400

 ** UserPoolAddOnNotEnabledException **
This exception is thrown when user pool add-ons aren't enabled.
HTTP Status Code: 400

## Examples
<a name="API_AdminListUserAuthEvents_Examples"></a>

### Example
<a name="API_AdminListUserAuthEvents_Example_1"></a>

The following example returns the two most recent advanced security features events for the user "testuser."

#### Sample Request
<a name="API_AdminListUserAuthEvents_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminListUserAuthEvents
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
  "UserPoolId": "us-west-2_EXAMPLE",
  "Username": "testuser",
  "MaxResults": 2
}
```

#### Sample Response
<a name="API_AdminListUserAuthEvents_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "AuthEvents": [
        {
            "ChallengeResponses": [
                {
                    "ChallengeName": "Password",
                    "ChallengeResponse": "Success"
                }
            ],
            "CreationDate": 1.7232229982E9,
            "EventContextData": {
                "City": "null",
                "Country": "United States",
                "IpAddress": "192.0.2.1"
            },
            "EventId": "7875548a-bd00-490a-93b8-fa36fe42a3e0",
            "EventResponse": "Pass",
            "EventRisk": {
                "CompromisedCredentialsDetected": false,
                "RiskDecision": "AccountTakeover",
                "RiskLevel": "Medium"
            },
            "EventType": "SignIn"
        },
        {
            "ChallengeResponses": [
                {
                    "ChallengeName": "Password",
                    "ChallengeResponse": "Success"
                }
            ],
            "CreationDate": 1.723136049929E9,
            "EventContextData": {
                "City": "Loughborough",
                "Country": "United Kingdom",
                "DeviceName": "Other, Other",
                "IpAddress": "192.0.2.99"
            },
            "EventId": "768d375c-ee6c-435e-a005-25c4981565c3",
            "EventResponse": "Pass",
            "EventRisk": {
                "CompromisedCredentialsDetected": false,
                "RiskDecision": "AccountTakeover",
                "RiskLevel": "Low"
            },
            "EventType": "SignIn"
        }
    ],
    "NextToken": "768d375c-ee6c-435e-a005-25c4981565c3#2024-08-08T16:54:09.929Z"
}
```

## See Also
<a name="API_AdminListUserAuthEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminListUserAuthEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminListUserAuthEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminListUserAuthEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminListUserAuthEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminListUserAuthEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminListUserAuthEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminListUserAuthEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminListUserAuthEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminListUserAuthEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminListUserAuthEvents)
