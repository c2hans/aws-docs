---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateDataflowEndpointGroup.html
---

# CreateDataflowEndpointGroup
<a name="API_CreateDataflowEndpointGroup"></a>

Creates a `DataflowEndpoint` group containing the specified list of ` DataflowEndpoint` objects.

The `name` field in each endpoint is used in your mission profile ` DataflowEndpointConfig` to specify which endpoints to use during a contact.

When a contact uses multiple `DataflowEndpointConfig` objects, each ` Config` must match a `DataflowEndpoint` in the same group.

## Request Syntax
<a name="API_CreateDataflowEndpointGroup_RequestSyntax"></a>

```
POST /dataflowEndpointGroup HTTP/1.1
Content-type: application/json

{
   "contactPostPassDurationSeconds": {{number}},
   "contactPrePassDurationSeconds": {{number}},
   "endpointDetails": [
      {
         "awsGroundStationAgentEndpoint": {
            "agentStatus": "{{string}}",
            "auditResults": "{{string}}",
            "egressAddress": {
               "mtu": {{number}},
               "socketAddress": {
                  "name": "{{string}}",
                  "port": {{number}}
               }
            },
            "ingressAddress": {
               "mtu": {{number}},
               "socketAddress": {
                  "name": "{{string}}",
                  "portRange": {
                     "maximum": {{number}},
                     "minimum": {{number}}
                  }
               }
            },
            "name": "{{string}}"
         },
         "downlinkAwsGroundStationAgentEndpoint": {
            "agentStatus": "{{string}}",
            "auditResults": "{{string}}",
            "dataflowDetails": { ... },
            "name": "{{string}}"
         },
         "endpoint": {
            "address": {
               "name": "{{string}}",
               "port": {{number}}
            },
            "mtu": {{number}},
            "name": "{{string}}",
            "status": "{{string}}"
         },
         "healthReasons": [ "{{string}}" ],
         "healthStatus": "{{string}}",
         "securityDetails": {
            "roleArn": "{{string}}",
            "securityGroupIds": [ "{{string}}" ],
            "subnetIds": [ "{{string}}" ]
         },
         "uplinkAwsGroundStationAgentEndpoint": {
            "agentStatus": "{{string}}",
            "auditResults": "{{string}}",
            "dataflowDetails": { ... },
            "name": "{{string}}"
         }
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDataflowEndpointGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDataflowEndpointGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [contactPostPassDurationSeconds](#API_CreateDataflowEndpointGroup_RequestSyntax) **   <a name="groundstation-CreateDataflowEndpointGroup-request-contactPostPassDurationSeconds"></a>
 Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a `POSTPASS` state. A [Ground Station Dataflow Endpoint Group State Change event](https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html) will be emitted when the Dataflow Endpoint Group enters and exits the `POSTPASS` state.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 480.
Required: No

 ** [contactPrePassDurationSeconds](#API_CreateDataflowEndpointGroup_RequestSyntax) **   <a name="groundstation-CreateDataflowEndpointGroup-request-contactPrePassDurationSeconds"></a>
 Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a `PREPASS` state. A [Ground Station Dataflow Endpoint Group State Change event](https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html) will be emitted when the Dataflow Endpoint Group enters and exits the `PREPASS` state.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 480.
Required: No

 ** [endpointDetails](#API_CreateDataflowEndpointGroup_RequestSyntax) **   <a name="groundstation-CreateDataflowEndpointGroup-request-endpointDetails"></a>
Endpoint details of each endpoint in the dataflow endpoint group. All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix [ AWS Ground Station Agent endpoints](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AwsGroundStationAgentEndpoint.html) with [Dataflow endpoints](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpoint.html) in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint groups for each type.
Type: Array of [EndpointDetails](API_EndpointDetails.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Required: Yes

 ** [tags](#API_CreateDataflowEndpointGroup_RequestSyntax) **   <a name="groundstation-CreateDataflowEndpointGroup-request-tags"></a>
Tags of a dataflow endpoint group.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateDataflowEndpointGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataflowEndpointGroupId": "string"
}
```

## Response Elements
<a name="API_CreateDataflowEndpointGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataflowEndpointGroupId](#API_CreateDataflowEndpointGroup_ResponseSyntax) **   <a name="groundstation-CreateDataflowEndpointGroup-response-dataflowEndpointGroupId"></a>
UUID of a dataflow endpoint group.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_CreateDataflowEndpointGroup_Errors"></a>

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
<a name="API_CreateDataflowEndpointGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/CreateDataflowEndpointGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/CreateDataflowEndpointGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/CreateDataflowEndpointGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/CreateDataflowEndpointGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/CreateDataflowEndpointGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/CreateDataflowEndpointGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/CreateDataflowEndpointGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/CreateDataflowEndpointGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/CreateDataflowEndpointGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/CreateDataflowEndpointGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
