---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListSignalCatalogNodes.html
---

# ListSignalCatalogNodes
<a name="API_ListSignalCatalogNodes"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Lists of information about the signals (nodes) specified in a signal catalog.

**Note**
This API operation uses pagination. Specify the `nextToken` parameter in the request to return more results.

## Request Syntax
<a name="API_ListSignalCatalogNodes_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "name": "{{string}}",
   "nextToken": "{{string}}",
   "signalNodeType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSignalCatalogNodes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListSignalCatalogNodes_RequestSyntax) **   <a name="iotfleetwise-ListSignalCatalogNodes-request-maxResults"></a>
The maximum number of items to return, between 1 and 100, inclusive.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [name](#API_ListSignalCatalogNodes_RequestSyntax) **   <a name="iotfleetwise-ListSignalCatalogNodes-request-name"></a>
 The name of the signal catalog to list information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** [nextToken](#API_ListSignalCatalogNodes_RequestSyntax) **   <a name="iotfleetwise-ListSignalCatalogNodes-request-nextToken"></a>
A pagination token for the next set of results.
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [signalNodeType](#API_ListSignalCatalogNodes_RequestSyntax) **   <a name="iotfleetwise-ListSignalCatalogNodes-request-signalNodeType"></a>
The type of node in the signal catalog.
Type: String
Valid Values: `SENSOR | ACTUATOR | ATTRIBUTE | BRANCH | CUSTOM_STRUCT | CUSTOM_PROPERTY`
Required: No

## Response Syntax
<a name="API_ListSignalCatalogNodes_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "nodes": [
      { ... }
   ]
}
```

## Response Elements
<a name="API_ListSignalCatalogNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSignalCatalogNodes_ResponseSyntax) **   <a name="iotfleetwise-ListSignalCatalogNodes-response-nextToken"></a>
 The token to retrieve the next set of results, or `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [nodes](#API_ListSignalCatalogNodes_ResponseSyntax) **   <a name="iotfleetwise-ListSignalCatalogNodes-response-nodes"></a>
 A list of information about nodes.
Type: Array of [Node](API_Node.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.

## Errors
<a name="API_ListSignalCatalogNodes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

 ** LimitExceededException **
A service quota was exceeded.
 ** resourceId **
The identifier of the resource that was exceeded.
 ** resourceType **
The type of resource that was exceeded.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource wasn't found.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 400

 ** ThrottlingException **
The request couldn't be completed due to throttling.
 ** quotaCode **
The quota identifier of the applied throttling rules for this request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
 ** serviceCode **
The code for the service that couldn't be completed due to throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of fields that fail to satisfy the constraints specified by an AWS service.
 ** reason **
The reason the input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListSignalCatalogNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/ListSignalCatalogNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/ListSignalCatalogNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/ListSignalCatalogNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/ListSignalCatalogNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/ListSignalCatalogNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/ListSignalCatalogNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/ListSignalCatalogNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/ListSignalCatalogNodes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/ListSignalCatalogNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/ListSignalCatalogNodes)
