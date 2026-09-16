---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html
---

# RequestSpotInstances
<a name="API_RequestSpotInstances"></a>

Creates a Spot Instance request.

For more information, see [Work with Spot Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html) in the *Amazon EC2 User Guide*.

**Important**
We strongly discourage using the RequestSpotInstances API because it is a legacy API with no planned investment. For options for requesting Spot Instances, see [Which is the best Spot request method to use?](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html#which-spot-request-method-to-use) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_RequestSpotInstances_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AvailabilityZoneGroup**
The user-specified name for a logical grouping of requests.
When you specify an Availability Zone group in a Spot Instance request, all Spot Instances in the request are launched in the same Availability Zone. Instance proximity is maintained with this parameter, but the choice of Availability Zone is not. The group applies only to requests for Spot Instances of the same instance type. Any additional Spot Instance requests that are specified with the same Availability Zone group name are launched in that same Availability Zone, as long as at least one instance from the group is still active.
If there is no active instance running in the Availability Zone group that you specify for a new Spot Instance request (all instances are terminated, the request is expired, or the maximum price you specified falls below current Spot price), then Amazon EC2 launches the instance in any Availability Zone where the constraint can be met. Consequently, the subsequent set of Spot Instances could be placed in a different zone from the original request, even if you specified the same Availability Zone group.
Default: Instances are launched in any available Availability Zone.
Type: String
Required: No

 **BlockDurationMinutes**
Deprecated.
Type: Integer
Required: No

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceCount**
The maximum number of Spot Instances to launch.
Default: 1
Type: Integer
Required: No

 **InstanceInterruptionBehavior**
The behavior when a Spot Instance is interrupted. The default is `terminate`.
Type: String
Valid Values: `hibernate | stop | terminate`
Required: No

 **LaunchGroup**
The instance launch group. Launch groups are Spot Instances that launch together and terminate together.
Default: Instances are launched and terminated individually
Type: String
Required: No

 **LaunchSpecification**
The launch specification.
Type: [RequestSpotLaunchSpecification](API_RequestSpotLaunchSpecification.md) object
Required: No

 **SpotPrice**
The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.
If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.
Type: String
Required: No

 **TagSpecification.N**
The key-value pair for tagging the Spot Instance request on creation. The value for `ResourceType` must be `spot-instances-request`, otherwise the Spot Instance request fails. To tag the Spot Instance request after it has been created, see [CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html).
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **Type**
The Spot Instance request type.
Default: `one-time`
Type: String
Valid Values: `one-time | persistent`
Required: No

 **ValidFrom**
The start date of the request. If this is a one-time request, the request becomes active at this date and time and remains active until all instances launch, the request expires, or the request is canceled. If the request is persistent, the request becomes active at this date and time and remains active until it expires or is canceled.
The specified start date and time cannot be equal to the current date and time. You must specify a start date and time that occurs after the current date and time.
Type: Timestamp
Required: No

 **ValidUntil**
The end date of the request, in UTC format (*YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z).
+ For a persistent request, the request remains active until the `ValidUntil` date and time is reached. Otherwise, the request remains active until you cancel it.
+ For a one-time request, the request remains active until all instances launch, the request is canceled, or the `ValidUntil` date and time is reached. By default, the request is valid for 7 days from the date the request was created.
Type: Timestamp
Required: No

## Response Elements
<a name="API_RequestSpotInstances_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **spotInstanceRequestSet**
The Spot Instance requests.
Type: Array of [SpotInstanceRequest](API_SpotInstanceRequest.md) objects

## Errors
<a name="API_RequestSpotInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RequestSpotInstances_Examples"></a>

### Example 1
<a name="API_RequestSpotInstances_Example_1"></a>

This example creates a one-time Spot Instance request for two instances. It does not include an Availability Zone or subnet, so Amazon EC2 selects an Availability Zone for you and launches the instances in the default subnet of the selected Availability Zone.

#### Sample Request
<a name="API_RequestSpotInstances_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=RequestSpotInstances
&InstanceCount=2
&Type=one-time
&LaunchSpecification.ImageId=ami-1a2b3c4d
&LaunchSpecification.KeyName=my-key-pair
&LaunchSpecification.SecurityGroupId.1=sg-1a2b3c4d
&LaunchSpecification.InstanceType=m3.medium
&LaunchSpecification.IamInstanceProfile.Name=s3access
&AUTHPARAMS
```

### Example 2
<a name="API_RequestSpotInstances_Example_2"></a>

The following example includes an Availability Zone. Amazon EC2 launches the instances in the default subnet of the specified Availability Zone.

#### Sample Request
<a name="API_RequestSpotInstances_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=RequestSpotInstances
&InstanceCount=2
&Type=one-time
&LaunchSpecification.ImageId=ami-1a2b3c4d
&LaunchSpecification.KeyName=my-key-pair
&LaunchSpecification.SecurityGroupId.1=sg-1a2b3c4d
&LaunchSpecification.InstanceType=m3.medium
&LaunchSpecification.Placement.AvailabilityZone=us-west-2a
&LaunchSpecification.IamInstanceProfile.Name=s3access
&AUTHPARAMS
```

### Example 3
<a name="API_RequestSpotInstances_Example_3"></a>

The following example includes a subnet. Amazon EC2 launches the instances in the specified subnet.

#### Sample Request
<a name="API_RequestSpotInstances_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=RequestSpotInstances
&InstanceCount=2
&Type=one-time
&LaunchSpecification.ImageId=ami-1a2b3c4d
&LaunchSpecification.KeyName=my-key-pair
&LaunchSpecification.SecurityGroupId.1=sg-1a2b3c4d
&LaunchSpecification.InstanceType=m3.medium
&LaunchSpecification.SubnetId=subnet-1a2b3c4d
&LaunchSpecification.IamInstanceProfile.Name=s3access
&AUTHPARAMS
```

## See Also
<a name="API_RequestSpotInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RequestSpotInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RequestSpotInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RequestSpotInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RequestSpotInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RequestSpotInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RequestSpotInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RequestSpotInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RequestSpotInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RequestSpotInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RequestSpotInstances)
