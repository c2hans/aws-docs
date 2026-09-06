---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetConnection.html
---

# GetConnection
<a name="API_GetConnection"></a>

Returns the connection ARN and details such as status, owner, and provider type.

## Request Syntax
<a name="API_GetConnection_RequestSyntax"></a>

```
{
   "ConnectionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionArn](#API_GetConnection_RequestSyntax) **   <a name="codeconnections-GetConnection-request-ConnectionArn"></a>
The Amazon Resource Name (ARN) of a connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
Required: Yes

## Response Syntax
<a name="API_GetConnection_ResponseSyntax"></a>

```
{
   "Connection": {
      "ConnectionArn": "string",
      "ConnectionName": "string",
      "ConnectionStatus": "string",
      "HostArn": "string",
      "OwnerAccountId": "string",
      "ProviderType": "string"
   }
}
```

## Response Elements
<a name="API_GetConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connection](#API_GetConnection_ResponseSyntax) **   <a name="codeconnections-GetConnection-response-Connection"></a>
The connection details, such as status, owner, and provider type.
Type: [Connection](API_Connection.md) object

## Errors
<a name="API_GetConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found. Verify the connection resource ARN and try again.
HTTP Status Code: 400

 ** ResourceUnavailableException **
Resource not found. Verify the ARN for the host resource and try again.
HTTP Status Code: 400

## See Also
<a name="API_GetConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/GetConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/GetConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/GetConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/GetConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/GetConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/GetConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/GetConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/GetConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/GetConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/GetConnection)
