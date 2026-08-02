---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetDataflowEndpointGroup.html
---

# GetDataflowEndpointGroup
<a name="API_GetDataflowEndpointGroup"></a>

Returns the dataflow endpoint group.

## Request Syntax
<a name="API_GetDataflowEndpointGroup_RequestSyntax"></a>

```
GET /dataflowEndpointGroup/{{dataflowEndpointGroupId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataflowEndpointGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataflowEndpointGroupId](#API_GetDataflowEndpointGroup_RequestSyntax) **   <a name="groundstation-GetDataflowEndpointGroup-request-uri-dataflowEndpointGroupId"></a>
UUID of a dataflow endpoint group.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_GetDataflowEndpointGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataflowEndpointGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "contactPostPassDurationSeconds": number,
   "contactPrePassDurationSeconds": number,
   "dataflowEndpointGroupArn": "string",
   "dataflowEndpointGroupId": "string",
   "endpointsDetails": [
      {
         "awsGroundStationAgentEndpoint": {
            "agentStatus": "string",
            "auditResults": "string",
            "egressAddress": {
               "mtu": number,
               "socketAddress": {
                  "name": "string",
                  "port": number
               }
            },
            "ingressAddress": {
               "mtu": number,
               "socketAddress": {
                  "name": "string",
                  "portRange": {
                     "maximum": number,
                     "minimum": number
                  }
               }
            },
            "name": "string"
         },
         "downlinkAwsGroundStationAgentEndpoint": {
            "agentStatus": "string",
            "auditResults": "string",
            "dataflowDetails": { ... },
            "name": "string"
         },
         "endpoint": {
            "address": {
               "name": "string",
               "port": number
            },
            "mtu": number,
            "name": "string",
            "status": "string"
         },
         "healthReasons": [ "string" ],
         "healthStatus": "string",
         "securityDetails": {
            "roleArn": "string",
            "securityGroupIds": [ "string" ],
            "subnetIds": [ "string" ]
         },
         "uplinkAwsGroundStationAgentEndpoint": {
            "agentStatus": "string",
            "auditResults": "string",
            "dataflowDetails": { ... },
            "name": "string"
         }
      }
   ],
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetDataflowEndpointGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contactPostPassDurationSeconds](#API_GetDataflowEndpointGroup_ResponseSyntax) **   <a name="groundstation-GetDataflowEndpointGroup-response-contactPostPassDurationSeconds"></a>
Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a `POSTPASS` state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the `POSTPASS` state.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 480.

 ** [contactPrePassDurationSeconds](#API_GetDataflowEndpointGroup_ResponseSyntax) **   <a name="groundstation-GetDataflowEndpointGroup-response-contactPrePassDurationSeconds"></a>
Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a `PREPASS` state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the `PREPASS` state.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 480.

 ** [dataflowEndpointGroupArn](#API_GetDataflowEndpointGroup_ResponseSyntax) **   <a name="groundstation-GetDataflowEndpointGroup-response-dataflowEndpointGroupArn"></a>
ARN of a dataflow endpoint group.
Type: String
Length Constraints: Minimum length of 97. Maximum length of 146.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:dataflow-endpoint-group/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [dataflowEndpointGroupId](#API_GetDataflowEndpointGroup_ResponseSyntax) **   <a name="groundstation-GetDataflowEndpointGroup-response-dataflowEndpointGroupId"></a>
UUID of a dataflow endpoint group.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [endpointsDetails](#API_GetDataflowEndpointGroup_ResponseSyntax) **   <a name="groundstation-GetDataflowEndpointGroup-response-endpointsDetails"></a>
Details of a dataflow endpoint.
Type: Array of [EndpointDetails](API_EndpointDetails.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.

 ** [tags](#API_GetDataflowEndpointGroup_ResponseSyntax) **   <a name="groundstation-GetDataflowEndpointGroup-response-tags"></a>
Tags assigned to a dataflow endpoint group.
Type: String to string map

## Errors
<a name="API_GetDataflowEndpointGroup_Errors"></a>

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
<a name="API_GetDataflowEndpointGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/GetDataflowEndpointGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/GetDataflowEndpointGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/GetDataflowEndpointGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/GetDataflowEndpointGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/GetDataflowEndpointGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/GetDataflowEndpointGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/GetDataflowEndpointGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/GetDataflowEndpointGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/GetDataflowEndpointGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/GetDataflowEndpointGroup)
