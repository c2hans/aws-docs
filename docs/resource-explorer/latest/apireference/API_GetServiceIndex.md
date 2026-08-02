---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetServiceIndex.html
---

# GetServiceIndex
<a name="API_GetServiceIndex"></a>

Retrieves information about the Resource Explorer index in the current AWS Region. This operation returns the ARN and type of the index if one exists.

## Request Syntax
<a name="API_GetServiceIndex_RequestSyntax"></a>

```
POST /GetServiceIndex HTTP/1.1
```

## URI Request Parameters
<a name="API_GetServiceIndex_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetServiceIndex_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetServiceIndex_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Type": "string"
}
```

## Response Elements
<a name="API_GetServiceIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetServiceIndex_ResponseSyntax) **   <a name="resourceexplorer-GetServiceIndex-response-Arn"></a>
The Amazon Resource Name (ARN) of the Resource Explorer index in the current Region.
Type: String

 ** [Type](#API_GetServiceIndex_ResponseSyntax) **   <a name="resourceexplorer-GetServiceIndex-response-Type"></a>
The type of the index. Valid values are `LOCAL` (contains resources from the current Region only) or `AGGREGATOR` (contains replicated resource information from all Regions).
Type: String
Valid Values: `LOCAL | AGGREGATOR`

## Errors
<a name="API_GetServiceIndex_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## See Also
<a name="API_GetServiceIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/GetServiceIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/GetServiceIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/GetServiceIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/GetServiceIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/GetServiceIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/GetServiceIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/GetServiceIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/GetServiceIndex)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/GetServiceIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/GetServiceIndex)
