---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_GetSessionEndpoint.html
---

# GetSessionEndpoint
<a name="API_GetSessionEndpoint"></a>

Returns the Spark Connect endpoint URL and a time-limited authentication token for the specified session. Use the endpoint and token to connect a PySpark client to the session. Call this operation again when the token expires to obtain a new one.

## Request Syntax
<a name="API_GetSessionEndpoint_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "SessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSessionEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_GetSessionEndpoint_RequestSyntax) **   <a name="EMR-GetSessionEndpoint-request-ClusterId"></a>
The ID of the cluster that the session belongs to.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** [SessionId](#API_GetSessionEndpoint_RequestSyntax) **   <a name="EMR-GetSessionEndpoint-request-SessionId"></a>
The ID of the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_GetSessionEndpoint_ResponseSyntax"></a>

```
{
   "AuthToken": "string",
   "AuthTokenExpirationTime": number,
   "Credentials": { ... },
   "Endpoint": "string"
}
```

## Response Elements
<a name="API_GetSessionEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthToken](#API_GetSessionEndpoint_ResponseSyntax) **   <a name="EMR-GetSessionEndpoint-response-AuthToken"></a>
A time-limited authentication token used to connect to the Spark Connect endpoint.
Type: String

 ** [AuthTokenExpirationTime](#API_GetSessionEndpoint_ResponseSyntax) **   <a name="EMR-GetSessionEndpoint-response-AuthTokenExpirationTime"></a>
The time at which the authentication token expires. After this time, call `GetSessionEndpoint` again to obtain a new token.
Type: Timestamp

 ** [Credentials](#API_GetSessionEndpoint_ResponseSyntax) **   <a name="EMR-GetSessionEndpoint-response-Credentials"></a>
Username and password used to authenticate with the Spark Connect server when connecting directly over VPC peering.
Type: [Credentials](API_Credentials.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [Endpoint](#API_GetSessionEndpoint_ResponseSyntax) **   <a name="EMR-GetSessionEndpoint-response-Endpoint"></a>
The Spark Connect endpoint URL to use in the PySpark client.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_GetSessionEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This exception occurs when there is an internal failure in the Amazon EMR service.
 ** Message **
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception occurs when there is something wrong with user input.
 ** ErrorCode **
The error code associated with the exception.
 ** Message **
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetSessionEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/GetSessionEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/GetSessionEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/GetSessionEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/GetSessionEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/GetSessionEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/GetSessionEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/GetSessionEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/GetSessionEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/GetSessionEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/GetSessionEndpoint)
