---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolReplica.html
---

# CreateUserPoolReplica
<a name="API_CreateUserPoolReplica"></a>

Creates a replica of an existing user pool in a specified AWS Region. The replica enables multi-region replication for high availability and disaster recovery. To create a replica, you must have permissions to create user pools in the target Region.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_CreateUserPoolReplica_RequestSyntax"></a>

```
{
   "RegionName": "{{string}}",
   "UserPoolId": "{{string}}",
   "UserPoolTags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateUserPoolReplica_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RegionName](#API_CreateUserPoolReplica_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolReplica-request-RegionName"></a>
The AWS Region where you want to create the replica user pool.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 32.
Required: Yes

 ** [UserPoolId](#API_CreateUserPoolReplica_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolReplica-request-UserPoolId"></a>
The ID of the user pool to replicate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

 ** [UserPoolTags](#API_CreateUserPoolReplica_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolReplica-request-UserPoolTags"></a>
A map of tags to assign to the replica user pool. Each tag consists of a key and an optional value, both of which you define. You can maintain tags independently on replica user pools.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateUserPoolReplica_ResponseSyntax"></a>

```
{
   "UserPoolReplica": {
      "RegionName": "string",
      "Role": "string",
      "Status": "string",
      "UserPoolArn": "string"
   }
}
```

## Response Elements
<a name="API_CreateUserPoolReplica_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserPoolReplica](#API_CreateUserPoolReplica_ResponseSyntax) **   <a name="CognitoUserPools-CreateUserPoolReplica-response-UserPoolReplica"></a>
Information about the created user pool replica, including its status and role.
Type: [UserPoolReplicaType](API_UserPoolReplicaType.md) object

## Errors
<a name="API_CreateUserPoolReplica_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FeatureUnavailableInTierException **
This exception is thrown when a feature that you attempted to use or configure isn't included in your user pool's current feature plan. This can occur when:
+ You configure a feature that your feature plan doesn't support.
+ You make a request that uses a feature that requires a higher feature plan.
To resolve this issue, upgrade your user pool to a feature plan that includes the feature.
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

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

 ** UserPoolTaggingException **
This exception is thrown when a user pool tag can't be set or updated.
HTTP Status Code: 400

## Examples
<a name="API_CreateUserPoolReplica_Examples"></a>

### Example
<a name="API_CreateUserPoolReplica_Example_1"></a>

The following example request creates a replica of user pool us-east-1\_EXAMPLE in the US West (Oregon) Region.

#### Sample Request
<a name="API_CreateUserPoolReplica_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.CreateUserPoolReplica
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "UserPoolId": "us-east-1_EXAMPLE",
    "RegionName": "us-west-2",
    "UserPoolTags": {
        "Environment": "Production",
        "Team": "Backend"
    }
}
```

#### Sample Response
<a name="API_CreateUserPoolReplica_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
    "UserPoolReplica": {
        "RegionName": "us-west-2",
        "UserPoolArn": "arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-east-1_EXAMPLE",
        "Status": "PENDING_CREATE",
        "Role": "SECONDARY"
    }
}
```

## See Also
<a name="API_CreateUserPoolReplica_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/CreateUserPoolReplica)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/CreateUserPoolReplica)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CreateUserPoolReplica)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/CreateUserPoolReplica)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CreateUserPoolReplica)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/CreateUserPoolReplica)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/CreateUserPoolReplica)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/CreateUserPoolReplica)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/CreateUserPoolReplica)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CreateUserPoolReplica)
