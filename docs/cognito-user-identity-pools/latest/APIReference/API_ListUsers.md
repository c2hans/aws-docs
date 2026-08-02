---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsers.html
---

# ListUsers
<a name="API_ListUsers"></a>

Given a user pool ID, returns a list of users and their basic details in a user pool.

This operation is eventually consistent. You might experience a delay before results are up-to-date. To validate the existence or configuration of an individual user, use `AdminGetUser`.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_ListUsers_RequestSyntax"></a>

```
{
   "AttributesToGet": [ "{{string}}" ],
   "Filter": "{{string}}",
   "Limit": {{number}},
   "PaginationToken": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUsers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributesToGet](#API_ListUsers_RequestSyntax) **   <a name="CognitoUserPools-ListUsers-request-AttributesToGet"></a>
A JSON array of user attribute names, for example `given_name`, that you want Amazon Cognito to include in the response for each user. When you don't provide an `AttributesToGet` parameter, Amazon Cognito returns all attributes for each user.
Use `AttributesToGet` with required attributes in your user pool, or in conjunction with `Filter`. Amazon Cognito returns an error if not all users in the results have set a value for the attribute you request. Attributes that you can't filter on, including custom attributes, must have a value set in every user profile before an `AttributesToGet` parameter returns results.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r ]+`
Required: No

 ** [Filter](#API_ListUsers_RequestSyntax) **   <a name="CognitoUserPools-ListUsers-request-Filter"></a>
A filter string of the form `"AttributeName Filter-Type "AttributeValue"`. Quotation marks within the filter string must be escaped using the backslash (`\`) character. For example, `"family_name = \"Reddy\""`.
+  *AttributeName*: The name of the attribute to search for. You can only search for one attribute at a time.
+  *Filter-Type*: For an exact match, use `=`, for example, "`given_name = \"Jon\"`". For a prefix ("starts with") match, use `^=`, for example, "`given_name ^= \"Jon\"`".
+  *AttributeValue*: The attribute value that must be matched for each user.
If the filter string is empty, `ListUsers` returns all users in the user pool.
You can only search for the following standard attributes:
+  `username` (case-sensitive)
+  `email`
+  `phone_number`
+  `name`
+  `given_name`
+  `family_name`
+  `preferred_username`
+  `cognito:user_status` (called **Status** in the Console) (case-insensitive)
+  `status (called Enabled in the Console) (case-sensitive)`
+  `sub`
Custom attributes aren't searchable.
You can also list users with a client-side filter. The server-side filter matches no more than one attribute. For an advanced search, use a client-side filter with the `--query` parameter of the `list-users` action in the AWS CLI. When you use a client-side filter, ListUsers returns a paginated list of zero or more users. You can receive multiple pages in a row with zero results. Repeat the query with each pagination token that is returned until you receive a null pagination token value, and then review the combined result.
For more information about server-side and client-side filtering, see [FilteringAWS CLI output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html) in the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html).
For more information, see [Searching for Users Using the ListUsers API](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html#cognito-user-pools-searching-for-users-using-listusers-api) and [Examples of Using the ListUsers API](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html#cognito-user-pools-searching-for-users-listusers-api-examples) in the *Amazon Cognito Developer Guide*.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Limit](#API_ListUsers_RequestSyntax) **   <a name="CognitoUserPools-ListUsers-request-Limit"></a>
The maximum number of users that you want Amazon Cognito to return in the response. In some SDK contexts, this operation might return fewer items than you specify in the `Limit` parameter without having reached the end of the full list. If the response contains a `PaginationToken`, then there are more results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 60.
Required: No

 ** [PaginationToken](#API_ListUsers_RequestSyntax) **   <a name="CognitoUserPools-ListUsers-request-PaginationToken"></a>
This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\S]+`
Required: No

 ** [UserPoolId](#API_ListUsers_RequestSyntax) **   <a name="CognitoUserPools-ListUsers-request-UserPoolId"></a>
The ID of the user pool where you want to display or search for users.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_ListUsers_ResponseSyntax"></a>

```
{
   "PaginationToken": "string",
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
<a name="API_ListUsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PaginationToken](#API_ListUsers_ResponseSyntax) **   <a name="CognitoUserPools-ListUsers-response-PaginationToken"></a>
The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\S]+`

 ** [Users](#API_ListUsers_ResponseSyntax) **   <a name="CognitoUserPools-ListUsers-response-Users"></a>
An array of user pool users who match your query, and their attributes. Between different requests, you might observe variations in the sequence that users in this response object are sorted into. The sort order of users isn't guaranteed to follow a single pattern, but the paginated list from a single chain of requests won't return duplicates.
Amazon Cognito creates a profile in your user pool for each local user in your user pool and for each unique user ID from your third-party identity providers (IdPs). When you link users with the [AdminLinkProviderForUser](API_AdminLinkProviderForUser.md) API operation, the output of `ListUsers` displays both the IdP user and the local user that you linked. You can identify IdP users in the `Users` object of this API response by the IdP prefix that Amazon Cognito appends to `Username`.
Type: Array of [UserType](API_UserType.md) objects

## Errors
<a name="API_ListUsers_Errors"></a>

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
<a name="API_ListUsers_Examples"></a>

### Example
<a name="API_ListUsers_Example_1"></a>

This request submits a value for all possible parameters for ListUsers. By iterating the PaginationToken, you can page through and collect all users in a user pool.

#### Sample Request
<a name="API_ListUsers_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.ListUsers
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "AttributesToGet": [
        "email",
        "sub"
    ],
    "Filter": "\"email\"^=\"testuser\"",
    "Limit": 3,
    "PaginationToken": "abcd1234EXAMPLE",
    "UserPoolId": "us-east-1_EXAMPLE"
}
```

#### Sample Response
<a name="API_ListUsers_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
    "PaginationToken": "efgh5678EXAMPLE",
    "Users": [
        {
            "Attributes": [
                {
                    "Name": "sub",
                    "Value": "eaad0219-2117-439f-8d46-4db20e59268f"
                },
                {
                    "Name": "email",
                    "Value": "testuser@example.com"
                }
            ],
            "Enabled": true,
            "UserCreateDate": 1682955829.578,
            "UserLastModifiedDate": 1689030181.63,
            "UserStatus": "CONFIRMED",
            "Username": "testuser"
        },
        {
            "Attributes": [
                {
                    "Name": "sub",
                    "Value": "3b994cfd-0b07-4581-be46-3c82f9a70c90"
                },
                {
                    "Name": "email",
                    "Value": "testuser2@example.com"
                }
            ],
            "Enabled": true,
            "UserCreateDate": 1684427979.201,
            "UserLastModifiedDate": 1684427979.201,
            "UserStatus": "UNCONFIRMED",
            "Username": "testuser2"
        },
        {
            "Attributes": [
                {
                    "Name": "sub",
                    "Value": "5929e0d1-4c34-42d1-9b79-a5ecacfe66f7"
                },
                {
                    "Name": "email",
                    "Value": "testuser3@example.com"
                }
            ],
            "Enabled": true,
            "UserCreateDate": 1684427823.641,
            "UserLastModifiedDate": 1684427823.641,
            "UserStatus": "UNCONFIRMED",
            "Username": "testuser3@example.com"
        }
    ]
}
```

## See Also
<a name="API_ListUsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/ListUsers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/ListUsers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ListUsers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/ListUsers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ListUsers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/ListUsers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/ListUsers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/ListUsers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/ListUsers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ListUsers)
