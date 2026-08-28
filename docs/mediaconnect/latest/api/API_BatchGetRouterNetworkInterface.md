---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_BatchGetRouterNetworkInterface.html
---

# BatchGetRouterNetworkInterface
<a name="API_BatchGetRouterNetworkInterface"></a>

Retrieves information about multiple router network interfaces in AWS Elemental MediaConnect.

## Request Syntax
<a name="API_BatchGetRouterNetworkInterface_RequestSyntax"></a>

```
GET /v1/routerNetworkInterfaces?arns={{arns}} HTTP/1.1
```

## URI Request Parameters
<a name="API_BatchGetRouterNetworkInterface_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arns](#API_BatchGetRouterNetworkInterface_RequestSyntax) **   <a name="mediaconnect-BatchGetRouterNetworkInterface-request-uri-arns"></a>
The Amazon Resource Names (ARNs) of the router network interfaces you want to retrieve information about.
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: Yes

## Request Body
<a name="API_BatchGetRouterNetworkInterface_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BatchGetRouterNetworkInterface_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "arn": "string",
         "code": "string",
         "message": "string"
      }
   ],
   "routerNetworkInterfaces": [
      {
         "arn": "string",
         "associatedInputCount": number,
         "associatedOutputCount": number,
         "configuration": { ... },
         "createdAt": "string",
         "id": "string",
         "name": "string",
         "networkInterfaceType": "string",
         "regionName": "string",
         "state": "string",
         "tags": {
            "string" : "string"
         },
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetRouterNetworkInterface_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetRouterNetworkInterface_ResponseSyntax) **   <a name="mediaconnect-BatchGetRouterNetworkInterface-response-errors"></a>
An array of errors that occurred when retrieving the requested router network interfaces.
Type: Array of [BatchGetRouterNetworkInterfaceError](API_BatchGetRouterNetworkInterfaceError.md) objects

 ** [routerNetworkInterfaces](#API_BatchGetRouterNetworkInterface_ResponseSyntax) **   <a name="mediaconnect-BatchGetRouterNetworkInterface-response-routerNetworkInterfaces"></a>
An array of router network interfaces that were successfully retrieved.
Type: Array of [RouterNetworkInterface](API_RouterNetworkInterface.md) objects

## Errors
<a name="API_BatchGetRouterNetworkInterface_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_BatchGetRouterNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/BatchGetRouterNetworkInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/BatchGetRouterNetworkInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/BatchGetRouterNetworkInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/BatchGetRouterNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/BatchGetRouterNetworkInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/BatchGetRouterNetworkInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/BatchGetRouterNetworkInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/BatchGetRouterNetworkInterface)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/BatchGetRouterNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/BatchGetRouterNetworkInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
