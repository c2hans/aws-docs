---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_SendApiAsset.html
---

# SendApiAsset
<a name="API_SendApiAsset"></a>

This operation invokes an API Gateway API asset. The request is proxied to the provider’s API Gateway API.

## Request Syntax
<a name="API_SendApiAsset_RequestSyntax"></a>

```
POST /v1?{{QueryStringParameters}} HTTP/1.1
x-amzn-dataexchange-asset-id: {{AssetId}}
x-amzn-dataexchange-data-set-id: {{DataSetId}}
x-amzn-dataexchange-http-method: {{Method}}
x-amzn-dataexchange-path: {{Path}}
x-amzn-dataexchange-revision-id: {{RevisionId}}

{{Body}}
```

## URI Request Parameters
<a name="API_SendApiAsset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssetId](#API_SendApiAsset_RequestSyntax) **   <a name="dataexchange-SendApiAsset-request-AssetId"></a>
Asset ID value for the API request.
Required: Yes

 ** [DataSetId](#API_SendApiAsset_RequestSyntax) **   <a name="dataexchange-SendApiAsset-request-DataSetId"></a>
Data set ID value for the API request.
Required: Yes

 ** [Method](#API_SendApiAsset_RequestSyntax) **   <a name="dataexchange-SendApiAsset-request-Method"></a>
HTTP method value for the API request. Alternatively, you can use the appropriate verb in your request.

 ** [Path](#API_SendApiAsset_RequestSyntax) **   <a name="dataexchange-SendApiAsset-request-Path"></a>
URI path value for the API request. Alternatively, you can set the URI path directly by invoking /v1/{pathValue}.

 ** [QueryStringParameters](#API_SendApiAsset_RequestSyntax) **   <a name="dataexchange-SendApiAsset-request-uri-QueryStringParameters"></a>
Attach query string parameters to the end of the URI (for example, /v1/examplePath?exampleParam=exampleValue).

 ** [RevisionId](#API_SendApiAsset_RequestSyntax) **   <a name="dataexchange-SendApiAsset-request-RevisionId"></a>
Revision ID value for the API request.
Required: Yes

## Request Body
<a name="API_SendApiAsset_RequestBody"></a>

The request accepts the following string data.

 ** [Body](#API_SendApiAsset_RequestSyntax) **   <a name="dataexchange-SendApiAsset-request-Body"></a>
The request body.

## Response Syntax
<a name="API_SendApiAsset_ResponseSyntax"></a>

```
HTTP/1.1 200

{{Body}}
```

## Response Elements
<a name="API_SendApiAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [Body](#API_SendApiAsset_ResponseSyntax) **   <a name="dataexchange-SendApiAsset-response-Body"></a>
The response body from the underlying API tracked by the API asset.

## Errors
<a name="API_SendApiAsset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the resource is denied.
 ** Message **
Access to the resource is denied.
HTTP Status Code: 403

 ** InternalServerException **
An exception occurred with the service.
 ** Message **
The message identifying the service exception that occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
 ** Message **
The resource couldn't be found.
 ** ResourceId **
The unique identifier for the resource that couldn't be found.
 ** ResourceType **
The type of resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** Message **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request was invalid.
 ** ExceptionCause **
The unique identifier for the resource that couldn't be found.
 ** Message **
The message that informs you about what was invalid about the request.
HTTP Status Code: 400

## See Also
<a name="API_SendApiAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/SendApiAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/SendApiAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/SendApiAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/SendApiAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/SendApiAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/SendApiAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/SendApiAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/SendApiAsset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/SendApiAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/SendApiAsset)
