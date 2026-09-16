---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_GetManagedEndpointSessionCredentials.html
---

# GetManagedEndpointSessionCredentials
<a name="API_GetManagedEndpointSessionCredentials"></a>

Generate a session token to connect to a managed endpoint.

## Request Syntax
<a name="API_GetManagedEndpointSessionCredentials_RequestSyntax"></a>

```
POST /virtualclusters/{{virtualClusterId}}/endpoints/{{endpointId}}/credentials HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "credentialType": "{{string}}",
   "durationInSeconds": {{number}},
   "executionRoleArn": "{{string}}",
   "logContext": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetManagedEndpointSessionCredentials_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endpointId](#API_GetManagedEndpointSessionCredentials_RequestSyntax) **   <a name="emroneks-GetManagedEndpointSessionCredentials-request-uri-endpointIdentifier"></a>
The ARN of the managed endpoint for which the request is submitted.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

 ** [virtualClusterId](#API_GetManagedEndpointSessionCredentials_RequestSyntax) **   <a name="emroneks-GetManagedEndpointSessionCredentials-request-uri-virtualClusterIdentifier"></a>
The ARN of the Virtual Cluster which the Managed Endpoint belongs to.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetManagedEndpointSessionCredentials_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_GetManagedEndpointSessionCredentials_RequestSyntax) **   <a name="emroneks-GetManagedEndpointSessionCredentials-request-clientToken"></a>
The client idempotency token of the job run request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: No

 ** [credentialType](#API_GetManagedEndpointSessionCredentials_RequestSyntax) **   <a name="emroneks-GetManagedEndpointSessionCredentials-request-credentialType"></a>
Type of the token requested. Currently supported and default value of this field is “TOKEN.”
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^.*\S.*$`
Required: Yes

 ** [durationInSeconds](#API_GetManagedEndpointSessionCredentials_RequestSyntax) **   <a name="emroneks-GetManagedEndpointSessionCredentials-request-durationInSeconds"></a>
Duration in seconds for which the session token is valid. The default duration is 15 minutes and the maximum is 12 hours.
Type: Integer
Required: No

 ** [executionRoleArn](#API_GetManagedEndpointSessionCredentials_RequestSyntax) **   <a name="emroneks-GetManagedEndpointSessionCredentials-request-executionRoleArn"></a>
The IAM Execution Role ARN that will be used by the job run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
Required: Yes

 ** [logContext](#API_GetManagedEndpointSessionCredentials_RequestSyntax) **   <a name="emroneks-GetManagedEndpointSessionCredentials-request-logContext"></a>
String identifier used to separate sections of the execution logs uploaded to S3.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^((?!.*-s3alias)(?!xn--.*)[a-z0-9][-a-z0-9.]*)?[a-z0-9]$`
Required: No

## Response Syntax
<a name="API_GetManagedEndpointSessionCredentials_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "credentials": { ... },
   "endpointCredentials": { ... },
   "expiresAt": "string",
   "id": "string"
}
```

## Response Elements
<a name="API_GetManagedEndpointSessionCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [credentials](#API_GetManagedEndpointSessionCredentials_ResponseSyntax) **   <a name="emroneks-GetManagedEndpointSessionCredentials-response-credentials"></a>
The structure containing the session credentials.
Type: [Credentials](API_Credentials.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [endpointCredentials](#API_GetManagedEndpointSessionCredentials_ResponseSyntax) **   <a name="emroneks-GetManagedEndpointSessionCredentials-response-endpointCredentials"></a>
The session credentials that the operation returns.
Type: [Credentials](API_Credentials.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [expiresAt](#API_GetManagedEndpointSessionCredentials_ResponseSyntax) **   <a name="emroneks-GetManagedEndpointSessionCredentials-response-expiresAt"></a>
The date and time when the session token will expire.
Type: Timestamp

 ** [id](#API_GetManagedEndpointSessionCredentials_ResponseSyntax) **   <a name="emroneks-GetManagedEndpointSessionCredentials-response-id"></a>
The identifier of the session token returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

## Errors
<a name="API_GetManagedEndpointSessionCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** RequestThrottledException **
The request throttled.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_GetManagedEndpointSessionCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/GetManagedEndpointSessionCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/GetManagedEndpointSessionCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/GetManagedEndpointSessionCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/GetManagedEndpointSessionCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/GetManagedEndpointSessionCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/GetManagedEndpointSessionCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/GetManagedEndpointSessionCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/GetManagedEndpointSessionCredentials)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/GetManagedEndpointSessionCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/GetManagedEndpointSessionCredentials)
