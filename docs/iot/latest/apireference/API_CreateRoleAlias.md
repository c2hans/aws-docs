---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateRoleAlias.html
---

# CreateRoleAlias
<a name="API_CreateRoleAlias"></a>

Creates a role alias.

Requires permission to access the [CreateRoleAlias](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

**Important**
The value of [https://docs.aws.amazon.com/iot/latest/apireference/API_CreateRoleAlias.html#iot-CreateRoleAlias-request-credentialDurationSeconds](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateRoleAlias.html#iot-CreateRoleAlias-request-credentialDurationSeconds) must be less than or equal to the maximum session duration of the IAM role that the role alias references. For more information, see [ Modifying a role maximum session duration (AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-api.html#roles-modify_max-session-duration-api) from the AWS Identity and Access Management User Guide.

## Request Syntax
<a name="API_CreateRoleAlias_RequestSyntax"></a>

```
POST /role-aliases/{{roleAlias}} HTTP/1.1
Content-type: application/json

{
   "credentialDurationSeconds": {{number}},
   "roleArn": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateRoleAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [roleAlias](#API_CreateRoleAlias_RequestSyntax) **   <a name="iot-CreateRoleAlias-request-uri-roleAlias"></a>
The role alias that points to a role ARN. This allows you to change the role without having to update the device.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`
Required: Yes

## Request Body
<a name="API_CreateRoleAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [credentialDurationSeconds](#API_CreateRoleAlias_RequestSyntax) **   <a name="iot-CreateRoleAlias-request-credentialDurationSeconds"></a>
How long (in seconds) the credentials will be valid. The default value is 3,600 seconds.
This value must be less than or equal to the maximum session duration of the IAM role that the role alias references.
Type: Integer
Valid Range: Minimum value of 900. Maximum value of 43200.
Required: No

 ** [roleArn](#API_CreateRoleAlias_RequestSyntax) **   <a name="iot-CreateRoleAlias-request-roleArn"></a>
The role ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [tags](#API_CreateRoleAlias_RequestSyntax) **   <a name="iot-CreateRoleAlias-request-tags"></a>
Metadata which can be used to manage the role alias.
For URI Request parameters use format: ...key1=value1&key2=value2...
For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."
For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateRoleAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "roleAlias": "string",
   "roleAliasArn": "string"
}
```

## Response Elements
<a name="API_CreateRoleAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [roleAlias](#API_CreateRoleAlias_ResponseSyntax) **   <a name="iot-CreateRoleAlias-response-roleAlias"></a>
The role alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`

 ** [roleAliasArn](#API_CreateRoleAlias_ResponseSyntax) **   <a name="iot-CreateRoleAlias-response-roleAliasArn"></a>
The role alias ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_CreateRoleAlias_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_CreateRoleAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateRoleAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateRoleAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateRoleAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateRoleAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateRoleAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateRoleAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateRoleAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateRoleAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateRoleAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateRoleAlias)
