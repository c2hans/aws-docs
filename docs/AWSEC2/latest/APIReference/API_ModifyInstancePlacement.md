---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstancePlacement.html
---

# ModifyInstancePlacement
<a name="API_ModifyInstancePlacement"></a>

Modifies the placement attributes for a specified instance. You can do the following:
+ Modify the affinity between an instance and a [Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html). When affinity is set to `host` and the instance is not associated with a specific Dedicated Host, the next time the instance is started, it is automatically associated with the host on which it lands. If the instance is restarted or rebooted, this relationship persists.
+ Change the Dedicated Host with which an instance is associated.
+ Change the instance tenancy of an instance.
+ Move an instance to or from a [placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

At least one attribute for affinity, host ID, tenancy, or placement group name must be specified in the request. Affinity and tenancy can be modified in the same request.

To modify the host ID, tenancy, placement group, or partition for an instance, the instance must be in the `stopped` state.

## Request Parameters
<a name="API_ModifyInstancePlacement_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Affinity**
The affinity setting for the instance. For more information, see [Host affinity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html#dedicated-hosts-affinity) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `default | host`
Required: No

 **GroupId**
The Group Id of a placement group. You must specify the Placement Group **Group Id** to launch an instance in a shared placement group.
Type: String
Required: No

 **GroupName**
The name of the placement group in which to place the instance. For spread placement groups, the instance must have a tenancy of `default`. For cluster and partition placement groups, the instance must have a tenancy of `default` or `dedicated`.
To remove an instance from a placement group, specify an empty string ("").
Type: String
Required: No

 **HostId**
The ID of the Dedicated Host with which to associate the instance.
Type: String
Required: No

 **HostResourceGroupArn**
The ARN of the host resource group in which to place the instance. The instance must have a tenancy of `host` to specify this parameter.
Type: String
Required: No

 **InstanceId**
The ID of the instance that you are modifying.
Type: String
Required: Yes

 **PartitionNumber**
The number of the partition in which to place the instance. Valid only if the placement group strategy is set to `partition`.
Type: Integer
Required: No

 **Tenancy**
The tenancy for the instance.
For T3 instances, you must launch the instance on a Dedicated Host to use a tenancy of `host`. You can't change the tenancy from `host` to `dedicated` or `default`. Attempting to make one of these unsupported tenancy changes results in an `InvalidRequest` error code.
Type: String
Valid Values: `default | dedicated | host`
Required: No

## Response Elements
<a name="API_ModifyInstancePlacement_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ModifyInstancePlacement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyInstancePlacement_Examples"></a>

### Example 1
<a name="API_ModifyInstancePlacement_Example_1"></a>

This example modifies the affinity of instance `i-0b33i09` so that it always has affinity with host `h-00548908djdsgfs`.

#### Sample Request
<a name="API_ModifyInstancePlacement_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyInstancePlacement
&Affinity=host
&HostId=h-00548908djdsgfs
&InstanceId=i-0b33i09
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyInstancePlacement_Example_1_Response"></a>

```
<ModifyInstancePlacementResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <return>true</item>
</ModifyInstancePlacementResponse>
```

### Example 2
<a name="API_ModifyInstancePlacement_Example_2"></a>

This example places instance `i-01234567812345678` in the placement group `MyPlacementGroup`.

#### Sample Request
<a name="API_ModifyInstancePlacement_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyInstancePlacement
&InstanceId=i-01234567812345678
&GroupName=MyPlacementGroup
&AUTHPARAMS
```

## See Also
<a name="API_ModifyInstancePlacement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyInstancePlacement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyInstancePlacement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyInstancePlacement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyInstancePlacement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyInstancePlacement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyInstancePlacement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyInstancePlacement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyInstancePlacement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyInstancePlacement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyInstancePlacement)
