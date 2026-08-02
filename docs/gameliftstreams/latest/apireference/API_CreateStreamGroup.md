---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamGroup.html
---

# CreateStreamGroup
<a name="API_CreateStreamGroup"></a>

 Stream groups manage how Amazon GameLift Streams allocates resources and handles concurrent streams, allowing you to effectively manage capacity and costs. Within a stream group, you specify an application to stream, streaming locations and their capacity, and the stream class you want to use when streaming applications to your end-users. A stream class defines the hardware configuration of the compute resources that Amazon GameLift Streams will use when streaming, such as the CPU, GPU, and memory.

 Stream capacity represents the number of concurrent streams that can be active at a time. You set stream capacity per location, per stream group. The following capacity settings are available:
+  **Always-on capacity**: This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle.
+  **Maximum capacity**: This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released.
+  **Target-idle capacity**: This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state.

Values for capacity must be whole number multiples of the tenancy value of the stream group's stream class.

 To adjust the capacity of any `ACTIVE` stream group, call [UpdateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html).

 If the `CreateStreamGroup` request is successful, Amazon GameLift Streams assigns a unique ID to the stream group resource and sets the status to `ACTIVATING`. It can take a few minutes for Amazon GameLift Streams to finish creating the stream group while it searches for unallocated compute resources and provisions them. When complete, the stream group status will be `ACTIVE` and you can start stream sessions by using [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html). To check the stream group's status, call [GetStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamGroup.html).

Stream groups should be recreated every 3-4 weeks to pick up important service updates and fixes. Stream groups that are older than 180 days can no longer be updated with new application associations. Stream groups expire when they are 365 days old, at which point they can no longer stream sessions. The exact expiration date is indicated by the date value in the `ExpiresAt` field.

## Request Syntax
<a name="API_CreateStreamGroup_RequestSyntax"></a>

```
POST /streamgroups HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
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
   ],
   "StreamClass": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateStreamGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateStreamGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateStreamGroup_RequestSyntax) **   <a name="gameliftstreams-CreateStreamGroup-request-Description"></a>
A descriptive label for the stream group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`
Required: Yes

 ** [StreamClass](#API_CreateStreamGroup_RequestSyntax) **   <a name="gameliftstreams-CreateStreamGroup-request-StreamClass"></a>
The target stream quality for sessions that are hosted in this stream group. Set a stream class that is appropriate to the type of content that you're streaming. Stream class determines the type of computing resources Amazon GameLift Streams uses and impacts the cost of streaming. The following options are available:
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
Required: Yes

 ** [ClientToken](#API_CreateStreamGroup_RequestSyntax) **   <a name="gameliftstreams-CreateStreamGroup-request-ClientToken"></a>
 A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [DefaultApplicationIdentifier](#API_CreateStreamGroup_RequestSyntax) **   <a name="gameliftstreams-CreateStreamGroup-request-DefaultApplicationIdentifier"></a>
The unique identifier of the Amazon GameLift Streams application that you want to set as the default application in a stream group. The application that you specify must be in `READY` status. The default application is pre-cached on always-on compute resources, reducing stream startup times. Other applications are automatically cached as needed.
If you do not link an application when you create a stream group, you will need to link one later, before you can start streaming, using [AssociateApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html).
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`. Example ID: `a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: No

 ** [LocationConfigurations](#API_CreateStreamGroup_RequestSyntax) **   <a name="gameliftstreams-CreateStreamGroup-request-LocationConfigurations"></a>
 A set of one or more locations and the streaming capacity for each location.
Type: Array of [LocationConfiguration](API_LocationConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [Tags](#API_CreateStreamGroup_RequestSyntax) **   <a name="gameliftstreams-CreateStreamGroup-request-Tags"></a>
A list of labels to assign to the new stream group resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management and cost allocation. See [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*. You can use [TagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html) to add tags, [UntagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html) to remove tags, and [ListTagsForResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html) to view tags on existing resources.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateStreamGroup_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateStreamGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-Arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that is assigned to the stream group resource and that uniquely identifies the group across all AWS Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamgroup/[resource ID]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`

 ** [AssociatedApplications](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-AssociatedApplications"></a>
 A set of applications that this stream group is associated to. You can stream any of these applications by using this stream group.
This value is a set of [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identify application resources. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [CreatedAt](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-CreatedAt"></a>
A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [DefaultApplication](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-DefaultApplication"></a>
The default Amazon GameLift Streams application that is associated with this stream group.
Type: [DefaultApplication](API_DefaultApplication.md) object

 ** [Description](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-Description"></a>
A descriptive label for the stream group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`

 ** [ExpiresAt](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-ExpiresAt"></a>
The time at which this stream group expires. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC). After this time, you will no longer be able to update this stream group or use it to start stream sessions. Only Get and Delete operations will work on an expired stream group.
Type: Timestamp

 ** [Id](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-Id"></a>
A unique ID value that is assigned to the resource when it's created. Format example: `sg-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`

 ** [LastUpdatedAt](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-LastUpdatedAt"></a>
A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [LocationStates](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-LocationStates"></a>
This value is the set of locations, including their name, current status, and capacities.
A location can be in one of the following states:
+  `ACTIVATING`: Amazon GameLift Streams is preparing the location. You cannot stream from, scale the capacity of, or remove this location yet.
+  `ACTIVE`: The location is provisioned with initial capacity. You can now stream from, scale the capacity of, or remove this location.
+  `ERROR`: Amazon GameLift Streams failed to set up this location. The `StatusReason` field describes the error. You can remove this location and try to add it again.
+  `REMOVING`: Amazon GameLift Streams is working to remove this location. This will release all provisioned capacity for this location in this stream group.
Type: Array of [LocationState](API_LocationState.md) objects

 ** [Status](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-Status"></a>
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

 ** [StatusReason](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-StatusReason"></a>
 A short description of the reason that the stream group is in `ERROR` status. The possible reasons can be one of the following:
+  `internalError`: The request can't process right now because of an issue with the server. Try again later.
+  `noAvailableInstances`: Amazon GameLift Streams does not currently have enough available capacity to fulfill your request. Wait a few minutes and retry the request as capacity can shift frequently. You can also try to make the request using a different stream class or in another region.
Type: String
Valid Values: `internalError | noAvailableInstances`

 ** [StreamClass](#API_CreateStreamGroup_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamGroup-response-StreamClass"></a>
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
<a name="API_CreateStreamGroup_Errors"></a>

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
<a name="API_CreateStreamGroup_Examples"></a>

### CLI Example
<a name="API_CreateStreamGroup_Example_1"></a>

The following example shows how to use the AWS CLI to create a Amazon GameLift Streams stream group with a `gen4n_high` stream class. The application for the stream group is specified with an ARN value. Values for capacity must be whole number multiples of the tenancy value of the stream group's stream class.

#### Sample Request
<a name="API_CreateStreamGroup_Example_1_Request"></a>

```
aws gameliftstreams create-stream-group \
  --description "MyGame JPregion" \
  --stream-class gen4n_high \
  --default-application-identifier arn:aws:gameliftstreams:us-west-2:123456789012:application/a-9ZY8X7Wv6 \
  --location-configurations '[{"LocationName": "us-west-2", "AlwaysOnCapacity": 2, "MaximumCapacity": 4, "TargetIdleCapacity": 1}]'
```

## See Also
<a name="API_CreateStreamGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/CreateStreamGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/CreateStreamGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/CreateStreamGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/CreateStreamGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/CreateStreamGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/CreateStreamGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/CreateStreamGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/CreateStreamGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/CreateStreamGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/CreateStreamGroup)
