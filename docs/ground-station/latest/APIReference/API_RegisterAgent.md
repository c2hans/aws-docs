---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_RegisterAgent.html
---

# RegisterAgent
<a name="API_RegisterAgent"></a>

**Note**
 For use by AWS Ground Station Agent and shouldn't be called directly.

 Registers a new agent with AWS Ground Station.

## Request Syntax
<a name="API_RegisterAgent_RequestSyntax"></a>

```
POST /agent HTTP/1.1
Content-type: application/json

{
   "agentDetails": {
      "agentCpuCores": [ {{number}} ],
      "agentVersion": "{{string}}",
      "componentVersions": [
         {
            "componentType": "{{string}}",
            "versions": [ "{{string}}" ]
         }
      ],
      "instanceId": "{{string}}",
      "instanceType": "{{string}}",
      "reservedCpuCores": [ {{number}} ]
   },
   "discoveryData": {
      "capabilityArns": [ "{{string}}" ],
      "privateIpAddresses": [ "{{string}}" ],
      "publicIpAddresses": [ "{{string}}" ]
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_RegisterAgent_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterAgent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentDetails](#API_RegisterAgent_RequestSyntax) **   <a name="groundstation-RegisterAgent-request-agentDetails"></a>
Detailed information about the agent being registered.
Type: [AgentDetails](API_AgentDetails.md) object
Required: Yes

 ** [discoveryData](#API_RegisterAgent_RequestSyntax) **   <a name="groundstation-RegisterAgent-request-discoveryData"></a>
Data for associating an agent with the capabilities it is managing.
Type: [DiscoveryData](API_DiscoveryData.md) object
Required: Yes

 ** [tags](#API_RegisterAgent_RequestSyntax) **   <a name="groundstation-RegisterAgent-request-tags"></a>
Tags assigned to an `Agent`.
Type: String to string map
Required: No

## Response Syntax
<a name="API_RegisterAgent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentId": "string"
}
```

## Response Elements
<a name="API_RegisterAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentId](#API_RegisterAgent_ResponseSyntax) **   <a name="groundstation-RegisterAgent-response-agentId"></a>
UUID of registered agent.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_RegisterAgent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_RegisterAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/RegisterAgent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/RegisterAgent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/RegisterAgent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/RegisterAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/RegisterAgent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/RegisterAgent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/RegisterAgent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/RegisterAgent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/RegisterAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/RegisterAgent)
