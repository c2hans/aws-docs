---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateDataflowEndpointGroupV2.html
---

# CreateDataflowEndpointGroupV2
<a name="API_CreateDataflowEndpointGroupV2"></a>

Creates a `DataflowEndpoint` group containing the specified list of Ground Station Agent based endpoints.

The `name` field in each endpoint is used in your mission profile ` DataflowEndpointConfig` to specify which endpoints to use during a contact.

When a contact uses multiple `DataflowEndpointConfig` objects, each ` Config` must match a `DataflowEndpoint` in the same group.

## Request Syntax
<a name="API_CreateDataflowEndpointGroupV2_RequestSyntax"></a>

```
POST /dataflowEndpointGroupV2 HTTP/1.1
Content-type: application/json

{
   "contactPostPassDurationSeconds": {{number}},
   "contactPrePassDurationSeconds": {{number}},
   "endpoints": [
      { ... }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDataflowEndpointGroupV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDataflowEndpointGroupV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [contactPostPassDurationSeconds](#API_CreateDataflowEndpointGroupV2_RequestSyntax) **   <a name="groundstation-CreateDataflowEndpointGroupV2-request-contactPostPassDurationSeconds"></a>
 Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a `POSTPASS` state. A [Ground Station Dataflow Endpoint Group State Change event](https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html) will be emitted when the Dataflow Endpoint Group enters and exits the `POSTPASS` state.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 480.
Required: No

 ** [contactPrePassDurationSeconds](#API_CreateDataflowEndpointGroupV2_RequestSyntax) **   <a name="groundstation-CreateDataflowEndpointGroupV2-request-contactPrePassDurationSeconds"></a>
 Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a `PREPASS` state. A [Ground Station Dataflow Endpoint Group State Change event](https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html) will be emitted when the Dataflow Endpoint Group enters and exits the `PREPASS` state.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 480.
Required: No

 ** [endpoints](#API_CreateDataflowEndpointGroupV2_RequestSyntax) **   <a name="groundstation-CreateDataflowEndpointGroupV2-request-endpoints"></a>
Dataflow endpoint group's endpoint definitions
Type: Array of [CreateEndpointDetails](API_CreateEndpointDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 12 items.
Required: Yes

 ** [tags](#API_CreateDataflowEndpointGroupV2_RequestSyntax) **   <a name="groundstation-CreateDataflowEndpointGroupV2-request-tags"></a>
Tags of a V2 dataflow endpoint group.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateDataflowEndpointGroupV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataflowEndpointGroupId": "string"
}
```

## Response Elements
<a name="API_CreateDataflowEndpointGroupV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataflowEndpointGroupId](#API_CreateDataflowEndpointGroupV2_ResponseSyntax) **   <a name="groundstation-CreateDataflowEndpointGroupV2-response-dataflowEndpointGroupId"></a>
Dataflow endpoint group ID
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_CreateDataflowEndpointGroupV2_Errors"></a>

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

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
 ** parameterName **
Parameter name that caused the exception
HTTP Status Code: 402

## See Also
<a name="API_CreateDataflowEndpointGroupV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/CreateDataflowEndpointGroupV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/CreateDataflowEndpointGroupV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/CreateDataflowEndpointGroupV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/CreateDataflowEndpointGroupV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/CreateDataflowEndpointGroupV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/CreateDataflowEndpointGroupV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/CreateDataflowEndpointGroupV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/CreateDataflowEndpointGroupV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/CreateDataflowEndpointGroupV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/CreateDataflowEndpointGroupV2)
