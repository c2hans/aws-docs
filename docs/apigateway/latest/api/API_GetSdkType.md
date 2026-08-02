---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetSdkType.html
---

# GetSdkType
<a name="API_GetSdkType"></a>

Gets an SDK type.

## Request Syntax
<a name="API_GetSdkType_RequestSyntax"></a>

```
GET /sdktypes/{{sdktype_id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSdkType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sdktype\_id](#API_GetSdkType_RequestSyntax) **   <a name="apigw-GetSdkType-request-uri-id"></a>
The identifier of the queried SdkType instance.
Required: Yes

## Request Body
<a name="API_GetSdkType_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSdkType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configurationProperties": [
      {
         "defaultValue": "string",
         "description": "string",
         "friendlyName": "string",
         "name": "string",
         "required": boolean
      }
   ],
   "description": "string",
   "friendlyName": "string",
   "id": "string"
}
```

## Response Elements
<a name="API_GetSdkType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurationProperties](#API_GetSdkType_ResponseSyntax) **   <a name="apigw-GetSdkType-response-configurationProperties"></a>
A list of configuration properties of an SdkType.
Type: Array of [SdkConfigurationProperty](API_SdkConfigurationProperty.md) objects

 ** [description](#API_GetSdkType_ResponseSyntax) **   <a name="apigw-GetSdkType-response-description"></a>
The description of an SdkType.
Type: String

 ** [friendlyName](#API_GetSdkType_ResponseSyntax) **   <a name="apigw-GetSdkType-response-friendlyName"></a>
The user-friendly name of an SdkType instance.
Type: String

 ** [id](#API_GetSdkType_ResponseSyntax) **   <a name="apigw-GetSdkType-response-id"></a>
The identifier of an SdkType instance.
Type: String

## Errors
<a name="API_GetSdkType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource is not found. Make sure that the request URI is correct.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## See Also
<a name="API_GetSdkType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetSdkType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetSdkType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetSdkType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetSdkType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetSdkType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetSdkType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetSdkType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetSdkType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetSdkType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetSdkType)
