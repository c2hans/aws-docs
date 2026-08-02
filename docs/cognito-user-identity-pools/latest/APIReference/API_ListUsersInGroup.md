---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsersInGroup.html
---

# ListUsersInGroup
<a name="API_ListUsersInGroup"></a>

Given a user pool ID and a group name, returns a list of users in the group. For more information about user pool groups, see [Adding groups to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_ListUsersInGroup_RequestSyntax"></a>

```
{
   "GroupName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUsersInGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GroupName](#API_ListUsersInGroup_RequestSyntax) **   <a name="CognitoUserPools-ListUsersInGroup-request-GroupName"></a>
The name of the group that you want to query for user membership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [Limit](#API_ListUsersInGroup_RequestSyntax) **   <a name="CognitoUserPools-ListUsersInGroup-request-Limit"></a>
The maximum number of groups that you want Amazon Cognito to return in the response. In some SDK contexts, this operation might return fewer items than you specify in the `Limit` parameter without having reached the end of the full list. If the response contains a `PaginationToken`, then there are more results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 60.
Required: No

 ** [NextToken](#API_ListUsersInGroup_RequestSyntax) **   <a name="CognitoUserPools-ListUsersInGroup-request-NextToken"></a>
This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\S]+`
Required: No

 ** [UserPoolId](#API_ListUsersInGroup_RequestSyntax) **   <a name="CognitoUserPools-ListUsersInGroup-request-UserPoolId"></a>
The ID of the user pool where you want to view the membership of the requested group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_ListUsersInGroup_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Users": [
      {
         "Attributes": [
            {
               "Name": "string",
               "Value": "string"
            }
         ],
         "Enabled": boolean,
         "MFAOptions": [
            {
               "AttributeName": "string",
               "DeliveryMedium": "string"
            }
         ],
         "UserCreateDate": number,
         "UserLastModifiedDate": number,
         "Username": "string",
         "UserStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUsersInGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListUsersInGroup_ResponseSyntax) **   <a name="CognitoUserPools-ListUsersInGroup-response-NextToken"></a>
The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\S]+`

 ** [Users](#API_ListUsersInGroup_ResponseSyntax) **   <a name="CognitoUserPools-ListUsersInGroup-response-Users"></a>
An array of users who are members in the group, and their attributes.
Type: Array of [UserType](API_UserType.md) objects

## Errors
<a name="API_ListUsersInGroup_Errors"></a>

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

## Examples
<a name="API_ListUsersInGroup_Examples"></a>

### Example
<a name="API_ListUsersInGroup_Example_1"></a>

The following example request lists the two users of the requested group.

#### Sample Request
<a name="API_ListUsersInGroup_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.ListUsersInGroup
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
    "GroupName": "testgroup",
    "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_ListUsersInGroup_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "Users": [
        {
            "Attributes": [
                {
                    "Name": "sub",
                    "Value": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
                },
                {
                    "Name": "identities",
                    "Value": "[{\"userId\":\"a1b2c3d4-5678-90ab-cdef-EXAMPLE22222\",\"providerName\":\"SignInWithApple\",\"providerType\":\"SignInWithApple\",\"issuer\":null,\"primary\":false,\"dateCreated\":1701125599632}]"
                },
                {
                    "Name": "email_verified",
                    "Value": "true"
                },
                {
                    "Name": "custom:state",
                    "Value": "Maine"
                },
                {
                    "Name": "name",
                    "Value": "John Doe"
                },
                {
                    "Name": "phone_number_verified",
                    "Value": "true"
                },
                {
                    "Name": "phone_number",
                    "Value": "+12065551212"
                },
                {
                    "Name": "preferred_username",
                    "Value": "jamesdoe"
                },
                {
                    "Name": "locale",
                    "Value": "EMEA"
                },
                {
                    "Name": "email",
                    "Value": "jamesdoe@example.com"
                }
            ],
            "Enabled": true,
            "UserCreateDate": 1682955829.578,
            "UserLastModifiedDate": 1736292876.446,
            "Username": "johndoe",
            "UserStatus": "CONFIRMED"
        },
        {
            "Attributes": [
                {
                    "Name": "sub",
                    "Value": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
                },
                {
                    "Name": "website",
                    "Value": "https://example.com"
                },
                {
                    "Name": "email_verified",
                    "Value": "true"
                },
                {
                    "Name": "custom:state",
                    "Value": "New York"
                },
                {
                    "Name": "phone_number_verified",
                    "Value": "true"
                },
                {
                    "Name": "given_name",
                    "Value": "Carlos"
                },
                {
                    "Name": "name",
                    "Value": "Carlos Salazar"
                },
                {
                    "Name": "phone_number",
                    "Value": "+12065551212"
                },
                {
                    "Name": "family_name",
                    "Value": "Salazar"
                },
                {
                    "Name": "email",
                    "Value": "carlos.salazar@example.com"
                }
            ],
            "Enabled": true,
            "UserCreateDate": 1701124862.116,
            "UserLastModifiedDate": 1726695472.107,
            "Username": "salazarc",
            "UserStatus": "CONFIRMED"
        }
    ]
}
```

## See Also
<a name="API_ListUsersInGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/ListUsersInGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/ListUsersInGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ListUsersInGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/ListUsersInGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ListUsersInGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/ListUsersInGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/ListUsersInGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/ListUsersInGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/ListUsersInGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ListUsersInGroup)
