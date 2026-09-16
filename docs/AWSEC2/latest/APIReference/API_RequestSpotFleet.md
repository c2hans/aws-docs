---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html
---

# RequestSpotFleet
<a name="API_RequestSpotFleet"></a>

Creates a Spot Fleet request.

The Spot Fleet request specifies the total target capacity and the On-Demand target capacity. Amazon EC2 calculates the difference between the total capacity and On-Demand capacity, and launches the difference as Spot capacity.

You can submit a single request that includes multiple launch specifications that vary by instance type, AMI, Availability Zone, or subnet.

By default, the Spot Fleet requests Spot Instances in the Spot Instance pool where the price per unit is the lowest. Each launch specification can include its own instance weighting that reflects the value of the instance type to your application workload.

Alternatively, you can specify that the Spot Fleet distribute the target capacity across the Spot pools included in its launch specifications. By ensuring that the Spot Instances in your Spot Fleet are in different Spot pools, you can improve the availability of your fleet.

You can specify tags for the Spot Fleet request and instances launched by the fleet. You cannot tag other resource types in a Spot Fleet request because only the `spot-fleet-request` and `instance` resource types are supported.

For more information, see [Spot Fleet requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-requests.html) in the *Amazon EC2 User Guide*.

**Important**
We strongly discourage using the RequestSpotFleet API because it is a legacy API with no planned investment. For options for requesting Spot Instances, see [Which is the best Spot request method to use?](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html#which-spot-request-method-to-use) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_RequestSpotFleet_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SpotFleetRequestConfig**
The configuration for the Spot Fleet request.
Type: [SpotFleetRequestConfigData](API_SpotFleetRequestConfigData.md) object
Required: Yes

## Response Elements
<a name="API_RequestSpotFleet_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **spotFleetRequestId**
The ID of the Spot Fleet request.
Type: String

## Errors
<a name="API_RequestSpotFleet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RequestSpotFleet_Examples"></a>

### Example
<a name="API_RequestSpotFleet_Example_1"></a>

This example creates a Spot Fleet request with two launch specifications.

#### Sample Request
<a name="API_RequestSpotFleet_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=RequestSpotFleet
&SpotFleetRequestConfig.IamFleetRole=arn:aws:iam::123456789011:role/spot-fleet-role
&SpotFleetRequestConfig.TargetCapacity=5
&SpotFleetRequestConfig.LaunchSpecifications.1.ImageId=ami-1ecae776
&SpotFleetRequestConfig.LaunchSpecifications.1.InstanceType=m4.large
&SpotFleetRequestConfig.LaunchSpecifications.1.SubnetId=subnet-1a2b3c4d
&SpotFleetRequestConfig.LaunchSpecifications.2.ImageId=ami-1ecae776
&SpotFleetRequestConfig.LaunchSpecifications.2.InstanceType=m3.medium
&SpotFleetRequestConfig.LaunchSpecifications.2.SubnetId=subnet-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_RequestSpotFleet_Example_1_Response"></a>

```
<RequestSpotFleetResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>60262cc5-2bd4-4c8d-98ed-example</requestId>
    <spotFleetRequestId>sfr-123f8fc2-cb31-425e-abcd-example2710</spotFleetRequestId>
</RequestSpotFleetResponse>
```

## See Also
<a name="API_RequestSpotFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RequestSpotFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RequestSpotFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RequestSpotFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RequestSpotFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RequestSpotFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RequestSpotFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RequestSpotFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RequestSpotFleet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RequestSpotFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RequestSpotFleet)
