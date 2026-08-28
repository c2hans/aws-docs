---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateRouterNetworkInterface.html
---

# CreateRouterNetworkInterface
<a name="API_CreateRouterNetworkInterface"></a>

Creates a new router network interface in AWS Elemental MediaConnect.

## Request Syntax
<a name="API_CreateRouterNetworkInterface_RequestSyntax"></a>

```
POST /v1/routerNetworkInterface HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "configuration": { ... },
   "name": "{{string}}",
   "regionName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRouterNetworkInterface_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRouterNetworkInterface_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateRouterNetworkInterface_RequestSyntax) **   <a name="mediaconnect-CreateRouterNetworkInterface-request-clientToken"></a>
A unique identifier for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[!-~]+`
Required: No

 ** [configuration](#API_CreateRouterNetworkInterface_RequestSyntax) **   <a name="mediaconnect-CreateRouterNetworkInterface-request-configuration"></a>
The configuration settings for the router network interface.
Type: [RouterNetworkInterfaceConfiguration](API_RouterNetworkInterfaceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [name](#API_CreateRouterNetworkInterface_RequestSyntax) **   <a name="mediaconnect-CreateRouterNetworkInterface-request-name"></a>
The name of the router network interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-_]*[a-zA-Z0-9])?`
Required: Yes

 ** [regionName](#API_CreateRouterNetworkInterface_RequestSyntax) **   <a name="mediaconnect-CreateRouterNetworkInterface-request-regionName"></a>
The AWS Region for the router network interface. Defaults to the current region if not specified.
Type: String
Required: No

 ** [tags](#API_CreateRouterNetworkInterface_RequestSyntax) **   <a name="mediaconnect-CreateRouterNetworkInterface-request-tags"></a>
Key-value pairs that can be used to tag and organize this router network interface.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateRouterNetworkInterface_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "routerNetworkInterface": {
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
}
```

## Response Elements
<a name="API_CreateRouterNetworkInterface_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [routerNetworkInterface](#API_CreateRouterNetworkInterface_ResponseSyntax) **   <a name="mediaconnect-CreateRouterNetworkInterface-response-routerNetworkInterface"></a>
The newly-created router network interface.
Type: [RouterNetworkInterface](API_RouterNetworkInterface.md) object

## Errors
<a name="API_CreateRouterNetworkInterface_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** RouterNetworkInterfaceServiceQuotaExceededException **
The request to create a new router network interface would exceed the service quotas (limits) set for the account.
HTTP Status Code: 420

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_CreateRouterNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/CreateRouterNetworkInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/CreateRouterNetworkInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/CreateRouterNetworkInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/CreateRouterNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/CreateRouterNetworkInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/CreateRouterNetworkInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/CreateRouterNetworkInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/CreateRouterNetworkInterface)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/CreateRouterNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/CreateRouterNetworkInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
