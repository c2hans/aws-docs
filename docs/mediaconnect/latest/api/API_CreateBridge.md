---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateBridge.html
---

# CreateBridge
<a name="API_CreateBridge"></a>

 Creates a new bridge. The request must include one source.

## Request Syntax
<a name="API_CreateBridge_RequestSyntax"></a>

```
POST /v1/bridges HTTP/1.1
Content-type: application/json

{
   "egressGatewayBridge": {
      "maxBitrate": {{number}}
   },
   "ingressGatewayBridge": {
      "maxBitrate": {{number}},
      "maxOutputs": {{number}}
   },
   "name": "{{string}}",
   "outputs": [
      {
         "networkOutput": {
            "ipAddress": "{{string}}",
            "name": "{{string}}",
            "networkName": "{{string}}",
            "port": {{number}},
            "protocol": "{{string}}",
            "ttl": {{number}}
         }
      }
   ],
   "placementArn": "{{string}}",
   "sourceFailoverConfig": {
      "failoverMode": "{{string}}",
      "recoveryWindow": {{number}},
      "sourcePriority": {
         "primarySource": "{{string}}"
      },
      "state": "{{string}}"
   },
   "sources": [
      {
         "flowSource": {
            "flowArn": "{{string}}",
            "flowVpcInterfaceAttachment": {
               "vpcInterfaceName": "{{string}}"
            },
            "name": "{{string}}"
         },
         "networkSource": {
            "multicastIp": "{{string}}",
            "multicastSourceSettings": {
               "multicastSourceIp": "{{string}}"
            },
            "name": "{{string}}",
            "networkName": "{{string}}",
            "port": {{number}},
            "protocol": "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateBridge_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateBridge_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [egressGatewayBridge](#API_CreateBridge_RequestSyntax) **   <a name="mediaconnect-CreateBridge-request-egressGatewayBridge"></a>
An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.
Type: [AddEgressGatewayBridgeRequest](API_AddEgressGatewayBridgeRequest.md) object
Required: No

 ** [ingressGatewayBridge](#API_CreateBridge_RequestSyntax) **   <a name="mediaconnect-CreateBridge-request-ingressGatewayBridge"></a>
An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.
Type: [AddIngressGatewayBridgeRequest](API_AddIngressGatewayBridgeRequest.md) object
Required: No

 ** [name](#API_CreateBridge_RequestSyntax) **   <a name="mediaconnect-CreateBridge-request-name"></a>
 The name of the bridge. This name can not be modified after the bridge is created.
Type: String
Required: Yes

 ** [outputs](#API_CreateBridge_RequestSyntax) **   <a name="mediaconnect-CreateBridge-request-outputs"></a>
 The outputs that you want to add to this bridge.
Type: Array of [AddBridgeOutputRequest](API_AddBridgeOutputRequest.md) objects
Required: No

 ** [placementArn](#API_CreateBridge_RequestSyntax) **   <a name="mediaconnect-CreateBridge-request-placementArn"></a>
 The bridge placement Amazon Resource Number (ARN).
Type: String
Required: Yes

 ** [sourceFailoverConfig](#API_CreateBridge_RequestSyntax) **   <a name="mediaconnect-CreateBridge-request-sourceFailoverConfig"></a>
 The settings for source failover.
Type: [FailoverConfig](API_FailoverConfig.md) object
Required: No

 ** [sources](#API_CreateBridge_RequestSyntax) **   <a name="mediaconnect-CreateBridge-request-sources"></a>
 The sources that you want to add to this bridge.
Type: Array of [AddBridgeSourceRequest](API_AddBridgeSourceRequest.md) objects
Required: Yes

## Response Syntax
<a name="API_CreateBridge_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "bridge": {
      "bridgeArn": "string",
      "bridgeMessages": [
         {
            "code": "string",
            "message": "string",
            "resourceName": "string"
         }
      ],
      "bridgeState": "string",
      "egressGatewayBridge": {
         "instanceId": "string",
         "maxBitrate": number
      },
      "ingressGatewayBridge": {
         "instanceId": "string",
         "maxBitrate": number,
         "maxOutputs": number
      },
      "name": "string",
      "outputs": [
         {
            "flowOutput": {
               "flowArn": "string",
               "flowSourceArn": "string",
               "name": "string"
            },
            "networkOutput": {
               "ipAddress": "string",
               "name": "string",
               "networkName": "string",
               "port": number,
               "protocol": "string",
               "ttl": number
            }
         }
      ],
      "placementArn": "string",
      "sourceFailoverConfig": {
         "failoverMode": "string",
         "recoveryWindow": number,
         "sourcePriority": {
            "primarySource": "string"
         },
         "state": "string"
      },
      "sources": [
         {
            "flowSource": {
               "flowArn": "string",
               "flowVpcInterfaceAttachment": {
                  "vpcInterfaceName": "string"
               },
               "name": "string",
               "outputArn": "string"
            },
            "networkSource": {
               "multicastIp": "string",
               "multicastSourceSettings": {
                  "multicastSourceIp": "string"
               },
               "name": "string",
               "networkName": "string",
               "port": number,
               "protocol": "string"
            }
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateBridge_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [bridge](#API_CreateBridge_ResponseSyntax) **   <a name="mediaconnect-CreateBridge-response-bridge"></a>
 The name of the bridge that was created.
Type: [Bridge](API_Bridge.md) object

## Errors
<a name="API_CreateBridge_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** CreateBridge420Exception **
Exception raised by AWS Elemental MediaConnect when creating the bridge. See the error message for the operation for more information on the cause of this exception.
HTTP Status Code: 420

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_CreateBridge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/CreateBridge)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/CreateBridge)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/CreateBridge)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/CreateBridge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/CreateBridge)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/CreateBridge)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/CreateBridge)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/CreateBridge)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/CreateBridge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/CreateBridge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
