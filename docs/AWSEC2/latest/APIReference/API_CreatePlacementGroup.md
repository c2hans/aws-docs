---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreatePlacementGroup.html
---

# CreatePlacementGroup
<a name="API_CreatePlacementGroup"></a>

Creates a placement group in which to launch instances. The strategy of the placement group determines how the instances are organized within the group.

A `cluster` placement group is a logical grouping of instances within a single Availability Zone that benefit from low network latency, high network throughput. A `spread` placement group places instances on distinct hardware. A `partition` placement group places groups of instances in different partitions, where instances in one partition do not share the same hardware with instances in another partition. A `precision-time` placement group places instances on supported hardware with direct access to high-precision time sources in AWS infrastructure.

For more information, see [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreatePlacementGroup_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **GroupName**
A name for the placement group. Must be unique within the scope of your account for the Region.
Constraints: Up to 255 ASCII characters
Type: String
Required: No

 **LinkedGroupId**
Reserved for future use.
Type: String
Required: No

 **Operator**
Reserved for internal use.
Type: [OperatorRequest](API_OperatorRequest.md) object
Required: No

 **ParentGroupId**
The ID of a parent placement group. Valid only when **Strategy** is set to `cluster`.
Type: String
Required: No

 **PartitionCount**
The number of partitions. Valid only when **Strategy** is set to `partition`.
Type: Integer
Required: No

 **SpreadLevel**
Determines how placement groups spread instances.
+ Host – You can use `host` only with Outpost placement groups.
+ Rack – No usage restrictions.
Type: String
Valid Values: `host | rack`
Required: No

 **Strategy**
The placement strategy.
Type: String
Valid Values: `cluster | spread | partition | precision-time`
Required: No

 **TagSpecification.N**
The tags to apply to the new placement group.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreatePlacementGroup_ResponseElements"></a>

The following elements are returned by the service.

 **placementGroup**
Information about the placement group.
Type: [PlacementGroup](API_PlacementGroup.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreatePlacementGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreatePlacementGroup_Examples"></a>

### Example
<a name="API_CreatePlacementGroup_Example_1"></a>

This example creates a cluster placement group named `XYZ-cluster`, and applies a tag with a key of `purpose` and a value of `production`.

#### Sample Request
<a name="API_CreatePlacementGroup_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreatePlacementGroup
&GroupName=XYZ-cluster
&Strategy=cluster
&TagSpecification.1.ResourceType=placement-group
&TagSpecification.1.Tag.1.Key=purpose
&TagSpecification.1.Tag.1.Value=production
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreatePlacementGroup_Example_1_Response"></a>

```
<CreatePlacementGroupResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1bbcaf48-7155-4154-a7ac-c6031EXAMPLE</requestId>
    <return>true</return>
    <placementGroup>
        <groupName>XYZ-cluster</groupName>
        <groupId>pg-0bea00ad0bexample</groupId>
        <strategy>cluster</strategy>
        <state>available</state>
        <tagSet>
            <item>
                <key>purpose</key>
                <value>production</value>
            </item>
        </tagSet>
    </placementGroup>
</CreatePlacementGroupResponse>
```

### Example
<a name="API_CreatePlacementGroup_Example_2"></a>

This example creates a partition placement group named `HDFS-Group-A` with five partitions.

#### Sample Request
<a name="API_CreatePlacementGroup_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreatePlacementGroup
&GroupName=HDFS-Group-A
&Strategy=partition
&PartitionCount=5
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreatePlacementGroup_Example_2_Response"></a>

```
<CreatePlacementGroupResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1bbcaf48-7155-4154-a7ac-c6031EXAMPLE</requestId>
    <return>true</return>
    <placementGroup>
        <groupName>HDFS-Group-A</groupName>
        <groupId>pg-0fc13f6eb3example</groupId>
        <strategy>partition</strategy>
        <state>available</state>
        <partitionCount>5</partitionCount>
    </placementGroup>
</CreatePlacementGroupResponse>
```

## See Also
<a name="API_CreatePlacementGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreatePlacementGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreatePlacementGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreatePlacementGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreatePlacementGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreatePlacementGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreatePlacementGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreatePlacementGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreatePlacementGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreatePlacementGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreatePlacementGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
