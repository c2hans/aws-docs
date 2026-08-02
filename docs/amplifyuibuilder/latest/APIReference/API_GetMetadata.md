---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_GetMetadata.html
---

# GetMetadata
<a name="API_GetMetadata"></a>

Returns existing metadata for an Amplify app.

## Request Syntax
<a name="API_GetMetadata_RequestSyntax"></a>

```
GET /app/{{appId}}/environment/{{environmentName}}/metadata HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_GetMetadata_RequestSyntax) **   <a name="amplifyuibuilder-GetMetadata-request-uri-appId"></a>
The unique ID of the Amplify app.
Required: Yes

 ** [environmentName](#API_GetMetadata_RequestSyntax) **   <a name="amplifyuibuilder-GetMetadata-request-uri-environmentName"></a>
The name of the backend environment that is part of the Amplify app.
Required: Yes

## Request Body
<a name="API_GetMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "features": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [features](#API_GetMetadata_ResponseSyntax) **   <a name="amplifyuibuilder-GetMetadata-response-features"></a>
Represents the configuration settings for the features metadata.
Type: String to string map

## Errors
<a name="API_GetMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

 ** UnauthorizedException **
You don't have permission to perform this operation.
HTTP Status Code: 401

## See Also
<a name="API_GetMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/GetMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/GetMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/GetMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/GetMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/GetMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/GetMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/GetMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/GetMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/GetMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/GetMetadata)
