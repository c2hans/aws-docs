---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartOutpostDecommission.html
---

# StartOutpostDecommission
<a name="API_StartOutpostDecommission"></a>

Starts the decommission process to return the Outposts racks or servers.

## Request Syntax
<a name="API_StartOutpostDecommission_RequestSyntax"></a>

```
POST /outposts/{{OutpostId}}/decommission HTTP/1.1
Content-type: application/json

{
   "ValidateOnly": {{boolean}}
}
```

## URI Request Parameters
<a name="API_StartOutpostDecommission_RequestParameters"></a>

The request uses the following URI parameters.

 ** [OutpostId](#API_StartOutpostDecommission_RequestSyntax) **   <a name="outposts-StartOutpostDecommission-request-uri-OutpostIdentifier"></a>
The ID or ARN of the Outpost that you want to decommission.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_StartOutpostDecommission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ValidateOnly](#API_StartOutpostDecommission_RequestSyntax) **   <a name="outposts-StartOutpostDecommission-request-ValidateOnly"></a>
Validates the request without starting the decommission process.
Type: Boolean
Required: No

## Response Syntax
<a name="API_StartOutpostDecommission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BlockingResourceTypes": [ "string" ],
   "Status": "string"
}
```

## Response Elements
<a name="API_StartOutpostDecommission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BlockingResourceTypes](#API_StartOutpostDecommission_ResponseSyntax) **   <a name="outposts-StartOutpostDecommission-response-BlockingResourceTypes"></a>
The resources still associated with the Outpost that you are decommissioning.
Type: Array of strings
Valid Values: `EC2_INSTANCE | OUTPOST_RAM_SHARE | LGW_ROUTING_DOMAIN | LGW_ROUTE_TABLE | LGW_VIRTUAL_INTERFACE_GROUP | OUTPOST_ORDER_CANCELLABLE | OUTPOST_ORDER_INTERVENTION_REQUIRED`

 ** [Status](#API_StartOutpostDecommission_ResponseSyntax) **   <a name="outposts-StartOutpostDecommission-response-Status"></a>
The status of the decommission request.
Type: String
Valid Values: `SKIPPED | BLOCKED | REQUESTED`

## Errors
<a name="API_StartOutpostDecommission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource causing the conflict.
 ** ResourceType **
The type of the resource causing the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_StartOutpostDecommission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/StartOutpostDecommission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/StartOutpostDecommission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/StartOutpostDecommission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/StartOutpostDecommission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/StartOutpostDecommission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/StartOutpostDecommission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/StartOutpostDecommission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/StartOutpostDecommission)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/StartOutpostDecommission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/StartOutpostDecommission)
