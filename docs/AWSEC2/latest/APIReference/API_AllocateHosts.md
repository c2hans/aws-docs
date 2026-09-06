---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AllocateHosts.html
---

# AllocateHosts
<a name="API_AllocateHosts"></a>

Allocates a Dedicated Host to your account. At a minimum, specify the supported instance type or instance family, the Availability Zone in which to allocate the host, and the number of hosts to allocate.

## Request Parameters
<a name="API_AllocateHosts_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssetId.N**
The IDs of the Outpost hardware assets on which to allocate the Dedicated Hosts. Targeting specific hardware assets on an Outpost can help to minimize latency between your workloads. This parameter is supported only if you specify **OutpostArn**. If you are allocating the Dedicated Hosts in a Region, omit this parameter.
+ If you specify this parameter, you can omit **Quantity**. In this case, Amazon EC2 allocates a Dedicated Host on each specified hardware asset.
+ If you specify both **AssetIds** and **Quantity**, then the value for **Quantity** must be equal to the number of asset IDs specified.
Type: Array of strings
Required: No

 **AutoPlacement**
Indicates whether the host accepts any untargeted instance launches that match its instance type configuration, or if it only accepts Host tenancy instance launches that specify its unique host ID. For more information, see [ Understanding auto-placement and affinity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html#dedicated-hosts-understanding) in the *Amazon EC2 User Guide*.
Default: `off`
Type: String
Valid Values: `on | off`
Required: No

 **AvailabilityZone**
The Availability Zone in which to allocate the Dedicated Host.
Type: String
Required: No

 **AvailabilityZoneId**
The ID of the Availability Zone.
Type: String
Required: No

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **CpuOptions**
The CPU configuration options to apply to the Dedicated Host.
Type: [HostCpuOptionsRequest](API_HostCpuOptionsRequest.md) object
Required: No

 **HostMaintenance**
Indicates whether to enable or disable host maintenance for the Dedicated Host. For more information, see [Host maintenance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance.html) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `on | off`
Required: No

 **HostRecovery**
Indicates whether to enable or disable host recovery for the Dedicated Host. Host recovery is disabled by default. For more information, see [ Host recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-recovery.html) in the *Amazon EC2 User Guide*.
Default: `off`
Type: String
Valid Values: `on | off`
Required: No

 **InstanceFamily**
Specifies the instance family to be supported by the Dedicated Hosts. If you specify an instance family, the Dedicated Hosts support multiple instance types within that instance family.
If you want the Dedicated Hosts to support a specific instance type only, omit this parameter and specify **InstanceType** instead. You cannot specify **InstanceFamily** and **InstanceType** in the same request.
Type: String
Required: No

 **InstanceType**
Specifies the instance type to be supported by the Dedicated Hosts. If you specify an instance type, the Dedicated Hosts support instances of the specified instance type only.
If you want the Dedicated Hosts to support multiple instance types in a specific instance family, omit this parameter and specify **InstanceFamily** instead. You cannot specify **InstanceType** and **InstanceFamily** in the same request.
Type: String
Required: No

 **OutpostArn**
The Amazon Resource Name (ARN) of the AWS Outpost on which to allocate the Dedicated Host. If you specify **OutpostArn**, you can optionally specify **AssetIds**.
If you are allocating the Dedicated Host in a Region, omit this parameter.
Type: String
Required: No

 **Quantity**
The number of Dedicated Hosts to allocate to your account with these parameters. If you are allocating the Dedicated Hosts on an Outpost, and you specify **AssetIds**, you can omit this parameter. In this case, Amazon EC2 allocates a Dedicated Host on each specified hardware asset. If you specify both **AssetIds** and **Quantity**, then the value that you specify for **Quantity** must be equal to the number of asset IDs specified.
Type: Integer
Required: No

 **TagSpecification.N**
The tags to apply to the Dedicated Host during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_AllocateHosts_ResponseElements"></a>

The following elements are returned by the service.

 **hostIdSet**
The ID of the allocated Dedicated Host. This is used to launch an instance onto a specific host.
Type: Array of strings

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AllocateHosts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AllocateHosts_Examples"></a>

### Example 1
<a name="API_AllocateHosts_Example_1"></a>

This example allocates a Dedicated Host to your account, on to which you can launch only `m5.large` instances.

#### Sample Request
<a name="API_AllocateHosts_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AllocateHosts
&AvailabilityZone=us-east-1b
&InstanceType=m5.large
&Quantity=1
&AUTHPARAMS
```

#### Sample Response
<a name="API_AllocateHosts_Example_1_Response"></a>

```
<AllocateHostsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <hostIdSet>
        <item>h-00548908djdsgfs</item>
    </hostIdSet>
</AllocateHostsResponse>
```

### Example 2
<a name="API_AllocateHosts_Example_2"></a>

This example allocates a Dedicated Host to your account, on to which you can launch multiple instance types in the `m5` instance family.

#### Sample Request
<a name="API_AllocateHosts_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=AllocateHosts
&AvailabilityZone=us-east-1b
&InstanceFamily=m5
&Quantity=1
&AUTHPARAMS
```

#### Sample Response
<a name="API_AllocateHosts_Example_2_Response"></a>

```
<AllocateHostsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <hostIdSet>
        <item>h-00548908djdsgfs</item>
    </hostIdSet>
</AllocateHostsResponse>
```

### Example 3
<a name="API_AllocateHosts_Example_3"></a>

This example allocates a Dedicated Host to your account with host recovery `on`.

#### Sample Request
<a name="API_AllocateHosts_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=AllocateHosts
&AvailabilityZone=us-east-1b
&InstanceType=m5.large
&Quantity=1
&HostRecovery=on
&AUTHPARAMS
```

#### Sample Response
<a name="API_AllocateHosts_Example_3_Response"></a>

```
<AllocateHostsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <hostIdSet>
        <item>h-00548908djdsgfs</item>
    </hostIdSet>
</AllocateHostsResponse>
```

### Example 4
<a name="API_AllocateHosts_Example_4"></a>

This example allocates a Dedicated Host to your account with auto-placement `off`.

#### Sample Request
<a name="API_AllocateHosts_Example_4_Request"></a>

```
https://ec2.amazonaws.com/?Action=AllocateHosts
&AvailabilityZone=us-east-1b
&InstanceFamily=m5
&Quantity=1
&AutoPlacement=off
&AUTHPARAMS
```

#### Sample Response
<a name="API_AllocateHosts_Example_4_Response"></a>

```
<AllocateHostsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <hostIdSet>
        <item>h-00548908djdsgfs</item>
    </hostIdSet>
</AllocateHostsResponse>
```

### Example 5
<a name="API_AllocateHosts_Example_5"></a>

This example allocates a Dedicated Host to your account, on to which you can launch only m5.2xlarge instances, and applies a tag with a key of `purpose` and a value of `production`.

#### Sample Request
<a name="API_AllocateHosts_Example_5_Request"></a>

```
https://ec2.amazonaws.com/?Action=AllocateHosts
&AvailabilityZone=us-east-1b
&InstanceType=m5.2xlarge
&Quantity=1
&TagSpecification.1.ResourceType=dedicated-host
&TagSpecification.1.Tag.1.Key=purpose
&TagSpecification.1.Tag.1.Value=production
&AUTHPARAMS
```

## See Also
<a name="API_AllocateHosts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AllocateHosts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AllocateHosts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AllocateHosts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AllocateHosts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AllocateHosts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AllocateHosts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AllocateHosts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AllocateHosts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AllocateHosts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AllocateHosts)
