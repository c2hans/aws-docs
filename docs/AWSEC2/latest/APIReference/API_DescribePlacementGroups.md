---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePlacementGroups.html
---

# DescribePlacementGroups
<a name="API_DescribePlacementGroups"></a>

Describes the specified placement groups or all of your placement groups.

**Note**
To describe a specific placement group that is *shared* with your account, you must specify the ID of the placement group using the `GroupId` parameter. Specifying the name of a *shared* placement group using the `GroupNames` parameter will result in an error.

For more information, see [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribePlacementGroups_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `group-name` - The name of the placement group.
+  `group-arn` - The Amazon Resource Name (ARN) of the placement group.
+  `spread-level` - The spread level for the placement group (`host` \| `rack`).
+  `state` - The state of the placement group (`pending` \| `available` \| `deleting` \| `deleted`).
+  `strategy` - The strategy of the placement group (`cluster` \| `spread` \| `partition` \| `precision-time`).
+  `tag:<key>` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **GroupId.N**
The IDs of the placement groups.
Type: Array of strings
Required: No

 **GroupName.N**
The names of the placement groups.
Constraints:
+ You can specify a name only if the placement group is owned by your account.
+ If a placement group is *shared* with your account, specifying the name results in an error. You must use the `GroupId` parameter instead.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribePlacementGroups_ResponseElements"></a>

The following elements are returned by the service.

 **placementGroupSet**
Information about the placement groups.
Type: Array of [PlacementGroup](API_PlacementGroup.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribePlacementGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribePlacementGroups_Examples"></a>

### Example 1
<a name="API_DescribePlacementGroups_Example_1"></a>

This example describes the placement group named `ABC-spread`.

#### Sample Request
<a name="API_DescribePlacementGroups_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribePlacementGroups
&GroupName.1=ABC-spread
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribePlacementGroups_Example_1_Response"></a>

```
<DescribePlacementGroupsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestID>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestID>
   <placementGroupSet>
      <item>
         <groupName>ABC-spread</groupName>
         <spreadLevel>rack</spreadLevel>
         <strategy>spread</strategy>
         <state>available</state>
      </item>
   </placementGroupSet>
</DescribePlacementGroupsResponse>
```

### Example 2
<a name="API_DescribePlacementGroups_Example_2"></a>

This example filters the response to include only placement groups that include the string `Project` in the name.

#### Sample Request
<a name="API_DescribePlacementGroups_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribePlacementGroups
&Filter.1.Name=group-name
&Filter.1.Value=*Project*
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribePlacementGroups_Example_2_Response"></a>

```
<DescribePlacementGroupsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestID>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestID>
   <placementGroupSet>
      <item>
         <groupName>Project-cluster</groupName>
         <strategy>cluster</strategy>
         <state>available</state>
      </item>
   </placementGroupSet>
</DescribePlacementGroupsResponse>
```

### Example 3
<a name="API_DescribePlacementGroups_Example_3"></a>

This example describes the partition placement group named `HDSF-Group-A` with three partitions.

#### Sample Request
<a name="API_DescribePlacementGroups_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribePlacementGroups
&GroupName.1=HDSF-Group-A
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribePlacementGroups_Example_3_Response"></a>

```
<DescribePlacementGroupsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestID>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestID>
   <placementGroupSet>
      <item>
         <groupName>HDSF-Group-A</groupName>
         <strategy>partition</strategy>
         <partitionCount>3</partitionCount>
         <state>available</state>
      </item>
   </placementGroupSet>
</DescribePlacementGroupsResponse>
```

## See Also
<a name="API_DescribePlacementGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribePlacementGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribePlacementGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribePlacementGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribePlacementGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribePlacementGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribePlacementGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribePlacementGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribePlacementGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribePlacementGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribePlacementGroups)
