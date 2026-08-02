---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolReplica.html
---

# UpdateUserPoolReplica
<a name="API_UpdateUserPoolReplica"></a>

Updates replica-specific settings for a user pool replica. You can modify the status to activate or deactivate the replica. This request can be made in both primary and secondary regions of the user pool.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_UpdateUserPoolReplica_RequestSyntax"></a>

```
{
   "RegionName": "{{string}}",
   "Status": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateUserPoolReplica_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RegionName](#API_UpdateUserPoolReplica_RequestSyntax) **   <a name="CognitoUserPools-UpdateUserPoolReplica-request-RegionName"></a>
The AWS Region of the replica to update.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 32.
Required: Yes

 ** [Status](#API_UpdateUserPoolReplica_RequestSyntax) **   <a name="CognitoUserPools-UpdateUserPoolReplica-request-Status"></a>
The status to set for the replica. Valid values are ACTIVE and INACTIVE.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** [UserPoolId](#API_UpdateUserPoolReplica_RequestSyntax) **   <a name="CognitoUserPools-UpdateUserPoolReplica-request-UserPoolId"></a>
The ID of the user pool that contains the replica to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_UpdateUserPoolReplica_ResponseSyntax"></a>

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
<a name="API_UpdateUserPoolReplica_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserPoolReplica](#API_UpdateUserPoolReplica_ResponseSyntax) **   <a name="CognitoUserPools-UpdateUserPoolReplica-response-UserPoolReplica"></a>
Information about the updated user pool replica.
Type: [UserPoolReplicaType](API_UserPoolReplicaType.md) object

## Errors
<a name="API_UpdateUserPoolReplica_Errors"></a>

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
<a name="API_UpdateUserPoolReplica_Examples"></a>

### Example
<a name="API_UpdateUserPoolReplica_Example_1"></a>

The following example request activates a secondary replica in the US West (Oregon) Region.

#### Sample Request
<a name="API_UpdateUserPoolReplica_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.UpdateUserPoolReplica
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "UserPoolId": "us-east-1_EXAMPLE",
    "RegionName": "us-west-2",
    "Status": "ACTIVE"
}
```

#### Sample Response
<a name="API_UpdateUserPoolReplica_Example_1_Response"></a>

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
        "Status": "ACTIVE",
        "Role": "SECONDARY"
    }
}
```

## See Also
<a name="API_UpdateUserPoolReplica_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/UpdateUserPoolReplica)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/UpdateUserPoolReplica)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UpdateUserPoolReplica)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/UpdateUserPoolReplica)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UpdateUserPoolReplica)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/UpdateUserPoolReplica)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/UpdateUserPoolReplica)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/UpdateUserPoolReplica)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/UpdateUserPoolReplica)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UpdateUserPoolReplica)
