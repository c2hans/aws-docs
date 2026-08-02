---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AddStreamGroupLocations.html
---

# AddStreamGroupLocations
<a name="API_AddStreamGroupLocations"></a>

 Add locations that can host stream sessions. To add a location, the stream group must be in `ACTIVE` status. You configure locations and their corresponding capacity for each stream group. Creating a stream group in a location that's nearest to your end users can help minimize latency and improve quality.

 This operation provisions stream capacity at the specified locations. By default, all locations have 1 or 2 capacity, depending on the stream class option: 2 for 'High' and 1 for 'Ultra' and 'Win2022'. This operation also copies the content files of all associated applications to an internal S3 bucket at each location. This allows Amazon GameLift Streams to host performant stream sessions.

## Request Syntax
<a name="API_AddStreamGroupLocations_RequestSyntax"></a>

```
POST /streamgroups/{{Identifier}}/locations HTTP/1.1
Content-type: application/json

{
   "LocationConfigurations": [
      {
         "AlwaysOnCapacity": {{number}},
         "LocationName": "{{string}}",
         "MaximumCapacity": {{number}},
         "OnDemandCapacity": {{number}},
         "TargetIdleCapacity": {{number}},
         "VpcTransitConfiguration": {
            "Ipv4CidrBlocks": [ "{{string}}" ],
            "VpcId": "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_AddStreamGroupLocations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_AddStreamGroupLocations_RequestSyntax) **   <a name="gameliftstreams-AddStreamGroupLocations-request-uri-Identifier"></a>
 A stream group to add the specified locations to.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_AddStreamGroupLocations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LocationConfigurations](#API_AddStreamGroupLocations_RequestSyntax) **   <a name="gameliftstreams-AddStreamGroupLocations-request-LocationConfigurations"></a>
 A set of one or more locations and the streaming capacity for each location.
Type: Array of [LocationConfiguration](API_LocationConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_AddStreamGroupLocations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Identifier": "string",
   "Locations": [
      {
         "AllocatedCapacity": number,
         "AlwaysOnCapacity": number,
         "IdleCapacity": number,
         "InternalVpcIpv4CidrBlock": "string",
         "LocationName": "string",
         "MaximumCapacity": number,
         "OnDemandCapacity": number,
         "RequestedCapacity": number,
         "Status": "string",
         "TargetIdleCapacity": number,
         "VpcTransitConfiguration": {
            "Ipv4CidrBlocks": [ "string" ],
            "TransitGatewayId": "string",
            "TransitGatewayResourceShareArn": "string",
            "VpcId": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_AddStreamGroupLocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Identifier](#API_AddStreamGroupLocations_ResponseSyntax) **   <a name="gameliftstreams-AddStreamGroupLocations-response-Identifier"></a>
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`

 ** [Locations](#API_AddStreamGroupLocations_ResponseSyntax) **   <a name="gameliftstreams-AddStreamGroupLocations-response-Locations"></a>
This value is set of locations, including their name, current status, and capacities.
A location can be in one of the following states:
+  `ACTIVATING`: Amazon GameLift Streams is preparing the location. You cannot stream from, scale the capacity of, or remove this location yet.
+  `ACTIVE`: The location is provisioned with initial capacity. You can now stream from, scale the capacity of, or remove this location.
+  `ERROR`: Amazon GameLift Streams failed to set up this location. The `StatusReason` field describes the error. You can remove this location and try to add it again.
+  `REMOVING`: Amazon GameLift Streams is working to remove this location. This will release all provisioned capacity for this location in this stream group.
Type: Array of [LocationState](API_LocationState.md) objects

## Errors
<a name="API_AddStreamGroupLocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error and is unable to complete the request.
 ** Message **
Description of the error.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The resource specified in the request was not found. Correct the request before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 404

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 402

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling. Retry the request after the suggested wait time.
 ** Message **
Description of the error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.
 ** Message **
Description of the error.
HTTP Status Code: 400

## Examples
<a name="API_AddStreamGroupLocations_Examples"></a>

### CLI Example
<a name="API_AddStreamGroupLocations_Example_1"></a>

The following example shows how to add multiple locations to the stream group.

#### Sample Request
<a name="API_AddStreamGroupLocations_Example_1_Request"></a>

```
aws gameliftstreams add-stream-group-locations \
    --identifier arn:aws:gameliftstreams:us-west-2:123456789012:streamgroup/sg-1AB2C3De4 \
    --location-configurations '[{"LocationName": "us-east-1", "AlwaysOnCapacity": 2, "MaximumCapacity": 4, "TargetIdleCapacity": 1}]'
```

## See Also
<a name="API_AddStreamGroupLocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/AddStreamGroupLocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/AddStreamGroupLocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/AddStreamGroupLocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/AddStreamGroupLocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/AddStreamGroupLocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/AddStreamGroupLocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/AddStreamGroupLocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/AddStreamGroupLocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/AddStreamGroupLocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/AddStreamGroupLocations)
