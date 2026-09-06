---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPoolReplicas.html
---

# ListUserPoolReplicas
<a name="API_ListUserPoolReplicas"></a>

Lists all replicas for a user pool, including both primary and secondary replicas. We recommend using pagination to ensure that the operation returns quickly and successfully.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_ListUserPoolReplicas_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUserPoolReplicas_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListUserPoolReplicas_RequestSyntax) **   <a name="CognitoUserPools-ListUserPoolReplicas-request-NextToken"></a>
A pagination token for retrieving the next page of results. If this parameter is omitted, the operation returns the first page of results.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\S]+`
Required: No

 ** [UserPoolId](#API_ListUserPoolReplicas_RequestSyntax) **   <a name="CognitoUserPools-ListUserPoolReplicas-request-UserPoolId"></a>
The ID of the user pool for which to list replicas.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_ListUserPoolReplicas_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "UserPoolReplicas": [
      {
         "RegionName": "string",
         "Role": "string",
         "Status": "string",
         "UserPoolArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUserPoolReplicas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListUserPoolReplicas_ResponseSyntax) **   <a name="CognitoUserPools-ListUserPoolReplicas-response-NextToken"></a>
A pagination token for retrieving the next page of results. If this value is null, there are no more results to retrieve.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\S]+`

 ** [UserPoolReplicas](#API_ListUserPoolReplicas_ResponseSyntax) **   <a name="CognitoUserPools-ListUserPoolReplicas-response-UserPoolReplicas"></a>
A list of user pool replicas, including information about their status, role, and Region.
Type: Array of [UserPoolReplicaType](API_UserPoolReplicaType.md) objects

## Errors
<a name="API_ListUserPoolReplicas_Errors"></a>

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
<a name="API_ListUserPoolReplicas_Examples"></a>

### Example
<a name="API_ListUserPoolReplicas_Example_1"></a>

The following example request lists all replicas for user pool us-east-1\_EXAMPLE.

#### Sample Request
<a name="API_ListUserPoolReplicas_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.ListUserPoolReplicas
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "UserPoolId": "us-east-1_EXAMPLE"
}
```

#### Sample Response
<a name="API_ListUserPoolReplicas_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
    "UserPoolReplicas": [
        {
            "RegionName": "us-east-1",
            "UserPoolArn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_EXAMPLE",
            "Status": "ACTIVE",
            "Role": "PRIMARY"
        },
        {
            "RegionName": "us-west-2",
            "UserPoolArn": "arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-east-1_EXAMPLE",
            "Status": "INACTIVE",
            "Role": "SECONDARY"
        }
    ]
}
```

## See Also
<a name="API_ListUserPoolReplicas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/ListUserPoolReplicas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/ListUserPoolReplicas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ListUserPoolReplicas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/ListUserPoolReplicas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ListUserPoolReplicas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/ListUserPoolReplicas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/ListUserPoolReplicas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/ListUserPoolReplicas)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/ListUserPoolReplicas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ListUserPoolReplicas)
