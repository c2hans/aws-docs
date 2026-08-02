---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfacePermissions.html
---

# DescribeNetworkInterfacePermissions
<a name="API_DescribeNetworkInterfacePermissions"></a>

Describes the permissions for your network interfaces.

## Request Parameters
<a name="API_DescribeNetworkInterfacePermissions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Filter.N**
One or more filters.
+  `network-interface-permission.network-interface-permission-id` - The ID of the permission.
+  `network-interface-permission.network-interface-id` - The ID of the network interface.
+  `network-interface-permission.aws-account-id` - The AWS account ID.
+  `network-interface-permission.aws-service` - The AWS service.
+  `network-interface-permission.permission` - The type of permission (`INSTANCE-ATTACH` \| `EIP-ASSOCIATE`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. If this parameter is not specified, up to 50 results are returned by default. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 255.
Required: No

 **NetworkInterfacePermissionId.N**
The network interface permission IDs.
Type: Array of strings
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeNetworkInterfacePermissions_ResponseElements"></a>

The following elements are returned by the service.

 **networkInterfacePermissions**
The network interface permissions.
Type: Array of [NetworkInterfacePermission](API_NetworkInterfacePermission.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeNetworkInterfacePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeNetworkInterfacePermissions_Examples"></a>

### Example
<a name="API_DescribeNetworkInterfacePermissions_Example_1"></a>

This example describes all of your network interface permissions.

#### Sample Request
<a name="API_DescribeNetworkInterfacePermissions_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeNetworkInterfacePermissions
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeNetworkInterfacePermissions_Example_1_Response"></a>

```
<DescribeNetworkInterfacePermissionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>6d4fe5e1-4bd2-4e76-8980-04cexample</requestId>
    <networkInterfacePermissions>
        <item>
            <awsAccountId>123456789012</awsAccountId>
            <networkInterfaceId>eni-b909511a</networkInterfaceId>
            <networkInterfacePermissionId>eni-perm-06fd19020ede149ea</networkInterfacePermissionId>
            <permission>INSTANCE-ATTACH</permission>
            <permissionState>
                <state>GRANTED</state>
            </permissionState>
        </item>
    </networkInterfacePermissions>
</DescribeNetworkInterfacePermissionsResponse>
```

## See Also
<a name="API_DescribeNetworkInterfacePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeNetworkInterfacePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeNetworkInterfacePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeNetworkInterfacePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeNetworkInterfacePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeNetworkInterfacePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeNetworkInterfacePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeNetworkInterfacePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeNetworkInterfacePermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeNetworkInterfacePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeNetworkInterfacePermissions)
