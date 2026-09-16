---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet.html
---

# CreateFleet
<a name="API_CreateFleet"></a>

Creates an EC2 Fleet that contains the configuration information for On-Demand Instances and Spot Instances. Instances are launched immediately if there is available capacity.

A single EC2 Fleet can include multiple launch specifications that vary by instance type, AMI, Availability Zone, or subnet.

For more information, see [EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateFleet_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.
For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **Context**
Reserved.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ExcessCapacityTerminationPolicy**
Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.
Supported only for fleets of type `maintain`.
Type: String
Valid Values: `no-termination | termination`
Required: No

 **LaunchTemplateConfigs.N**
The configuration for the EC2 Fleet.
Type: Array of [FleetLaunchTemplateConfigRequest](API_FleetLaunchTemplateConfigRequest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 **OnDemandOptions**
Describes the configuration of On-Demand Instances in an EC2 Fleet.
Type: [OnDemandOptionsRequest](API_OnDemandOptionsRequest.md) object
Required: No

 **ReplaceUnhealthyInstances**
Indicates whether EC2 Fleet should replace unhealthy Spot Instances. Supported only for fleets of type `maintain`. For more information, see [EC2 Fleet health checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#ec2-fleet-health-checks) in the *Amazon EC2 User Guide*.
Type: Boolean
Required: No

 **ReservedCapacityOptions**
Defines EC2 Fleet preferences for utilizing reserved capacity when DefaultTargetCapacityType is set to `reserved-capacity`.
Supported only for fleets of type `instant`.
Type: [ReservedCapacityOptionsRequest](API_ReservedCapacityOptionsRequest.md) object
Required: No

 **SpotOptions**
Describes the configuration of Spot Instances in an EC2 Fleet.
Type: [SpotOptionsRequest](API_SpotOptionsRequest.md) object
Required: No

 **TagSpecification.N**
The key-value pair for tagging the EC2 Fleet request on creation. For more information, see [Tag your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-resources).
If the fleet type is `instant`, specify a resource type of `fleet` to tag the fleet, `instance` to tag the instances at launch, `volume` to tag the volumes at launch, or `network-interface` to tag the network interfaces at launch.
If the fleet type is `maintain` or `request`, specify a resource type of `fleet` to tag the fleet. You cannot specify a resource type of `instance`, `volume`, or `network-interface`. To tag instances at launch, specify the tags in a [launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template).
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TargetCapacitySpecification**
The number of units to request.
Type: [TargetCapacitySpecificationRequest](API_TargetCapacitySpecificationRequest.md) object
Required: Yes

 **TerminateInstancesWithExpiration**
Indicates whether running instances should be terminated when the EC2 Fleet expires.
Type: Boolean
Required: No

 **Type**
The fleet type. The default value is `maintain`.
+  `maintain` - The EC2 Fleet places an asynchronous request for your desired capacity, and continues to maintain your desired Spot capacity by replenishing interrupted Spot Instances.
+  `request` - The EC2 Fleet places an asynchronous one-time request for your desired capacity, but does submit Spot requests in alternative capacity pools if Spot capacity is unavailable, and does not maintain Spot capacity if Spot Instances are interrupted.
+  `instant` - The EC2 Fleet places a synchronous one-time request for your desired capacity, and returns errors for any instances that could not be launched.
For more information, see [EC2 Fleet request types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-request-type.html) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `request | maintain | instant`
Required: No

 **ValidFrom**
The start date and time of the request, in UTC format (for example, *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z). The default is to start fulfilling the request immediately.
Type: Timestamp
Required: No

 **ValidUntil**
The end date and time of the request, in UTC format (for example, *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z). At this point, no new EC2 Fleet requests are placed or able to fulfill the request. If no value is specified, the request remains until you cancel it.
Type: Timestamp
Required: No

## Response Elements
<a name="API_CreateFleet_ResponseElements"></a>

The following elements are returned by the service.

 **errorSet**
Information about the instances that could not be launched by the fleet. Supported only for fleets of type `instant`.
Type: Array of [CreateFleetError](API_CreateFleetError.md) objects

 **fleetId**
The ID of the EC2 Fleet.
Type: String

 **fleetInstanceSet**
Information about the instances that were launched by the fleet. Supported only for fleets of type `instant`.
Type: Array of [CreateFleetInstance](API_CreateFleetInstance.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateFleet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateFleet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateFleet)
