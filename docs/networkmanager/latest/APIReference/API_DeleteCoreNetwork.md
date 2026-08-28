---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteCoreNetwork.html
---

# DeleteCoreNetwork
<a name="API_DeleteCoreNetwork"></a>

Deletes a core network along with all core network policies. This can only be done if there are no attachments on a core network.

## Request Syntax
<a name="API_DeleteCoreNetwork_RequestSyntax"></a>

```
DELETE /core-networks/{{coreNetworkId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCoreNetwork_RequestParameters"></a>

The request uses the following URI parameters.

 ** [coreNetworkId](#API_DeleteCoreNetwork_RequestSyntax) **   <a name="networkmanager-DeleteCoreNetwork-request-uri-CoreNetworkId"></a>
The network ID of the deleted core network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: Yes

## Request Body
<a name="API_DeleteCoreNetwork_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCoreNetwork_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CoreNetwork": {
      "CoreNetworkArn": "string",
      "CoreNetworkId": "string",
      "CreatedAt": number,
      "Description": "string",
      "Edges": [
         {
            "Asn": number,
            "EdgeLocation": "string",
            "InsideCidrBlocks": [ "string" ]
         }
      ],
      "GlobalNetworkId": "string",
      "NetworkFunctionGroups": [
         {
            "EdgeLocations": [ "string" ],
            "Name": "string",
            "Segments": {
               "SendTo": [ "string" ],
               "SendVia": [ "string" ]
            }
         }
      ],
      "Segments": [
         {
            "EdgeLocations": [ "string" ],
            "Name": "string",
            "SharedSegments": [ "string" ]
         }
      ],
      "State": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DeleteCoreNetwork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CoreNetwork](#API_DeleteCoreNetwork_ResponseSyntax) **   <a name="networkmanager-DeleteCoreNetwork-response-CoreNetwork"></a>
Information about the deleted core network.
Type: [CoreNetwork](API_CoreNetwork.md) object

## Errors
<a name="API_DeleteCoreNetwork_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed due to an internal error.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** Context **
The specified resource could not be found.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason for the error.
HTTP Status Code: 400

## See Also
<a name="API_DeleteCoreNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/DeleteCoreNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/DeleteCoreNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/DeleteCoreNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/DeleteCoreNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/DeleteCoreNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/DeleteCoreNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/DeleteCoreNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/DeleteCoreNetwork)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/DeleteCoreNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/DeleteCoreNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
