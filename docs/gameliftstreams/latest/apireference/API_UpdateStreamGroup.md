---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html
---

# UpdateStreamGroup
<a name="API_UpdateStreamGroup"></a>

 Updates the configuration settings for an Amazon GameLift Streams stream group resource. To update a stream group, it must be in `ACTIVE` status. You can change the description, the set of locations, and the requested capacity of a stream group per location. If you want to change the stream class, create a new stream group.

 Stream capacity represents the number of concurrent streams that can be active at a time. You set stream capacity per location, per stream group. The following capacity settings are available:
+  **Always-on capacity**: This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle.
+  **Maximum capacity**: This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released.
+  **Target-idle capacity**: This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state.

Values for capacity must be whole number multiples of the tenancy value of the stream group's stream class.

To update a stream group, specify the stream group's Amazon Resource Name (ARN) and provide the new values. If the request is successful, Amazon GameLift Streams returns the complete updated metadata for the stream group. Expired stream groups cannot be updated.

## Request Syntax
<a name="API_UpdateStreamGroup_RequestSyntax"></a>

```
PATCH /streamgroups/{{Identifier}} HTTP/1.1
Content-type: application/json

{
   "DefaultApplicationIdentifier": "{{string}}",
   "Description": "{{string}}",
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
<a name="API_UpdateStreamGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_UpdateStreamGroup_RequestSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-request-uri-Identifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_UpdateStreamGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DefaultApplicationIdentifier](#API_UpdateStreamGroup_RequestSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-request-DefaultApplicationIdentifier"></a>
The unique identifier of the Amazon GameLift Streams application that you want to set as the default application in a stream group. The application that you specify must be in `READY` status. The default application is pre-cached on always-on compute resources, reducing stream startup times. Other applications are automatically cached as needed.
Note that this parameter only sets the default application in a stream group. To associate a new application to an existing stream group, you must use [AssociateApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html).
When you switch default applications in a stream group, it can take up to a few hours for the new default application to be pre-cached.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`. Example ID: `a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: No

 ** [Description](#API_UpdateStreamGroup_RequestSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-request-Description"></a>
A descriptive label for the stream group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`
Required: No

 ** [LocationConfigurations](#API_UpdateStreamGroup_RequestSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-request-LocationConfigurations"></a>
 A set of one or more locations and the streaming capacity for each location.
Type: Array of [LocationConfiguration](API_LocationConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_UpdateStreamGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "AssociatedApplications": [ "string" ],
   "CreatedAt": number,
   "DefaultApplication": {
      "Arn": "string",
      "Id": "string"
   },
   "Description": "string",
   "ExpiresAt": number,
   "Id": "string",
   "LastUpdatedAt": number,
   "LocationStates": [
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
   ],
   "Status": "string",
   "StatusReason": "string",
   "StreamClass": "string"
}
```

## Response Elements
<a name="API_UpdateStreamGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-Arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that is assigned to the stream group resource and that uniquely identifies the group across all AWS Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamgroup/[resource ID]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`

 ** [AssociatedApplications](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-AssociatedApplications"></a>
 A set of applications that this stream group is associated with. You can stream any of these applications with the stream group.
This value is a set of [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identify application resources. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [CreatedAt](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-CreatedAt"></a>
A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [DefaultApplication](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-DefaultApplication"></a>
The default Amazon GameLift Streams application that is associated with this stream group.
Type: [DefaultApplication](API_DefaultApplication.md) object

 ** [Description](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-Description"></a>
A descriptive label for the stream group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`

 ** [ExpiresAt](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-ExpiresAt"></a>
The time at which this stream group expires. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC). After this time, you will no longer be able to update this stream group or use it to start stream sessions. Only Get and Delete operations will work on an expired stream group.
Type: Timestamp

 ** [Id](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-Id"></a>
A unique ID value that is assigned to the resource when it's created. Format example: `sg-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`

 ** [LastUpdatedAt](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-LastUpdatedAt"></a>
A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [LocationStates](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-LocationStates"></a>
This value is set of locations, including their name, current status, and capacities.
A location can be in one of the following states:
+  `ACTIVATING`: Amazon GameLift Streams is preparing the location. You cannot stream from, scale the capacity of, or remove this location yet.
+  `ACTIVE`: The location is provisioned with initial capacity. You can now stream from, scale the capacity of, or remove this location.
+  `ERROR`: Amazon GameLift Streams failed to set up this location. The `StatusReason` field describes the error. You can remove this location and try to add it again.
+  `REMOVING`: Amazon GameLift Streams is working to remove this location. This will release all provisioned capacity for this location in this stream group.
Type: Array of [LocationState](API_LocationState.md) objects

 ** [Status](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-Status"></a>
The current status of the stream group resource. Possible statuses include the following:
+  `ACTIVATING`: The stream group is deploying and isn't ready to host streams.
+  `ACTIVE`: The stream group is ready to host streams.
+  `ACTIVE_WITH_ERRORS`: One or more locations in the stream group are in an error state. Verify the details of individual locations and remove any locations which are in error.
+  `DELETING`: Amazon GameLift Streams is in the process of deleting the stream group.
+  `ERROR`: An error occurred when the stream group deployed. See `StatusReason` (returned by `CreateStreamGroup`, `GetStreamGroup`, and `UpdateStreamGroup`) for more information.
+  `EXPIRED`: The stream group is expired and can no longer host streams. This typically occurs when a stream group is 365 days old, as indicated by the value of `ExpiresAt`. Create a new stream group to resume streaming capabilities.
+  `UPDATING_LOCATIONS`: One or more locations in the stream group are in the process of updating (either activating or deleting).
Type: String
Valid Values: `ACTIVATING | UPDATING_LOCATIONS | ACTIVE | ACTIVE_WITH_ERRORS | ERROR | DELETING | EXPIRED`

 ** [StatusReason](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-StatusReason"></a>
 A short description of the reason that the stream group is in `ERROR` status. The possible reasons can be one of the following:
+  `internalError`: The request can't process right now because of an issue with the server. Try again later.
+  `noAvailableInstances`: Amazon GameLift Streams does not currently have enough available capacity to fulfill your request. Wait a few minutes and retry the request as capacity can shift frequently. You can also try to make the request using a different stream class or in another region.
Type: String
Valid Values: `internalError | noAvailableInstances`

 ** [StreamClass](#API_UpdateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-UpdateStreamGroup-response-StreamClass"></a>
The target stream quality for the stream group.
A stream class can be one of the following:
+  ** `gen6n_pro_win2022` (NVIDIA, pro)** Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
+  ** `gen6n_pro` (NVIDIA, pro)** Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
+  ** `gen6n_ultra_win2022` (NVIDIA, ultra)** Supports applications with high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
+  ** `gen6n_ultra` (NVIDIA, ultra)** Supports applications with high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
+  ** `gen6n_high` (NVIDIA, high)** Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM
  + Tenancy: Supports up to 2 concurrent stream sessions
+  ** `gen6n_medium` (NVIDIA, medium)** Supports applications with moderate 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 2 vCPUs, 8 GB RAM, 6 GB VRAM
  + Tenancy: Supports up to 4 concurrent stream sessions
+  ** `gen6n_small` (NVIDIA, small)** Supports applications with lightweight 3D scene complexity and low CPU usage. Powered by NVIDIA L4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 1 vCPUs, 4 GB RAM, 2 GB VRAM
  + Tenancy: Supports up to 12 concurrent stream sessions
+  ** `gen6n_medium_win2022` (NVIDIA, medium)** Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 8 vCPUs, 32 GB RAM, 6 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
+  ** `gen6n_small_win2022` (NVIDIA, small)** Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 2 vCPUs, 8 GB RAM, 3 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
+  ** `gen6e_pro_win2022` (NVIDIA, pro)** Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L40S Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
+  ** `gen6e_pro` (NVIDIA, pro)** Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L40S Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
+  ** `gen5n_win2022` (NVIDIA, ultra)** Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA A10G Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
+  ** `gen5n_high` (NVIDIA, high)** Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM
  + Tenancy: Supports up to 2 concurrent stream sessions
+  ** `gen5n_ultra` (NVIDIA, ultra)** Supports applications with extremely high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
+  ** `gen4n_win2022` (NVIDIA, ultra)** Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA T4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
+  ** `gen4n_high` (NVIDIA, high)** Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 4 vCPUs, 16 GB RAM, 8 GB VRAM
  + Tenancy: Supports up to 2 concurrent stream sessions
+  ** `gen4n_ultra` (NVIDIA, ultra)** Supports applications with high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.
  + Reference resolution: 1080p
  + Reference frame rate: 60 fps
  + Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM
  + Tenancy: Supports 1 concurrent stream session
Type: String
Valid Values: `gen4n_high | gen4n_ultra | gen4n_win2022 | gen5n_high | gen5n_ultra | gen5n_win2022 | gen6n_small | gen6n_medium | gen6n_high | gen6n_ultra | gen6n_ultra_win2022 | gen6n_pro | gen6n_pro_win2022 | gen6n_small_win2022 | gen6n_medium_win2022 | gen6e_pro | gen6e_pro_win2022`

## Errors
<a name="API_UpdateStreamGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

 [ConflictException](API_ConflictException.md)
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
 ** Message **
Description of the error.
HTTP Status Code: 409

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
<a name="API_UpdateStreamGroup_Examples"></a>

### CLI Example
<a name="API_UpdateStreamGroup_Example_1"></a>

The following example shows how to update stream capacity in the primary location. In response, Amazon GameLift Streams attempts to provision additional resources until the stream group's allocated, always-on capacity reaches the new requested capacity of 4.

#### Sample Request
<a name="API_UpdateStreamGroup_Example_1_Request"></a>

```
aws gameliftstreams update-stream-group \
  --identifier arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4 \
  --location-configurations '[{"LocationName": "us-west-2", "AlwaysOnCapacity": 4}]'
```

### CLI Example
<a name="API_UpdateStreamGroup_Example_2"></a>

The following example shows how to update both always-on capacity and maximum capacity with target-idle capacity. In response, Amazon GameLift Streams attempts to provision resources to maintain a baseline of 4 capacity. With a target-idle capacity of 2, the service keeps 2 capacity available and ready beyond what's actively streaming, up to the maximum capacity of 10. If stream requests exceed the rate at which the service can replenish the buffer, or if you don't specify a target-idle capacity, new sessions may take several minutes to start while the service provisions additional capacity as needed.

#### Sample Request
<a name="API_UpdateStreamGroup_Example_2_Request"></a>

```
aws gameliftstreams update-stream-group \
  --identifier arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4 \
  --location-configurations '[{"LocationName": "us-west-2", "AlwaysOnCapacity": 4, "MaximumCapacity": 10, "TargetIdleCapacity": 2}]'
```

### CLI Example
<a name="API_UpdateStreamGroup_Example_3"></a>

The following example shows how to update stream capacity in two locations.

#### Sample Request
<a name="API_UpdateStreamGroup_Example_3_Request"></a>

```
aws gameliftstreams update-stream-group \
    --identifier arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4 \
    --location-configurations '[{"LocationName": "us-west-2", "AlwaysOnCapacity": 4}, \
      {"LocationName": "ap-northeast-1", "AlwaysOnCapacity": 4}]'
```

## See Also
<a name="API_UpdateStreamGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/UpdateStreamGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/UpdateStreamGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/UpdateStreamGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/UpdateStreamGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/UpdateStreamGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/UpdateStreamGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/UpdateStreamGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/UpdateStreamGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/UpdateStreamGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/UpdateStreamGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
