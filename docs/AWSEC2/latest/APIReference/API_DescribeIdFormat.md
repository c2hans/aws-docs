---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIdFormat.html
---

# DescribeIdFormat
<a name="API_DescribeIdFormat"></a>

Describes the ID format settings for your resources on a per-Region basis, for example, to view which resource types are enabled for longer IDs. This request only returns information about resource types whose ID formats can be modified; it does not return information about other resource types.

The following resource types support longer IDs: `bundle` \| `conversion-task` \| `customer-gateway` \| `dhcp-options` \| `elastic-ip-allocation` \| `elastic-ip-association` \| `export-task` \| `flow-log` \| `image` \| `import-task` \| `instance` \| `internet-gateway` \| `network-acl` \| `network-acl-association` \| `network-interface` \| `network-interface-attachment` \| `prefix-list` \| `reservation` \| `route-table` \| `route-table-association` \| `security-group` \| `snapshot` \| `subnet` \| `subnet-cidr-block-association` \| `volume` \| `vpc` \| `vpc-cidr-block-association` \| `vpc-endpoint` \| `vpc-peering-connection` \| `vpn-connection` \| `vpn-gateway`.

These settings apply to the IAM user who makes the request; they do not apply to the entire AWS account. By default, an IAM user defaults to the same settings as the root user, unless they explicitly override the settings by running the [ModifyIdFormat](API_ModifyIdFormat.md) command. Resources created with longer IDs are visible to all IAM users, regardless of these settings and provided that they have permission to use the relevant `Describe` command for the resource type.

## Request Parameters
<a name="API_DescribeIdFormat_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Resource**
The type of resource: `bundle` \| `conversion-task` \| `customer-gateway` \| `dhcp-options` \| `elastic-ip-allocation` \| `elastic-ip-association` \| `export-task` \| `flow-log` \| `image` \| `import-task` \| `instance` \| `internet-gateway` \| `network-acl` \| `network-acl-association` \| `network-interface` \| `network-interface-attachment` \| `prefix-list` \| `reservation` \| `route-table` \| `route-table-association` \| `security-group` \| `snapshot` \| `subnet` \| `subnet-cidr-block-association` \| `volume` \| `vpc` \| `vpc-cidr-block-association` \| `vpc-endpoint` \| `vpc-peering-connection` \| `vpn-connection` \| `vpn-gateway`
Type: String
Required: No

## Response Elements
<a name="API_DescribeIdFormat_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **statusSet**
Information about the ID format for the resource.
Type: Array of [IdFormat](API_IdFormat.md) objects

## Errors
<a name="API_DescribeIdFormat_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeIdFormat_Examples"></a>

### Example
<a name="API_DescribeIdFormat_Example_1"></a>

This example describes the ID format for all resources that support longer IDs.

#### Sample Request
<a name="API_DescribeIdFormat_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeIdFormat
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeIdFormat_Example_1_Response"></a>

```
<DescribeIdFormatResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
    <statusSet>
        <item>
            <resource>reservation</resource>
            <useLongIds>true</useLongIds>
            <deadline>2016-12-15T12:00:00.000Z</deadline>
        </item>
        <item>
            <resource>instance</resource>
            <useLongIds>true</useLongIds>
            <deadline>2016-12-15T12:00:00.000Z</deadline>
        </item>
        <item>
            <resource>volume</resource>
            <useLongIds>true</useLongIds>
            <deadline>2016-12-15T12:00:00.000Z</deadline>
        </item>
        <item>
            <resource>snapshot</resource>
            <useLongIds>true</useLongIds>
            <deadline>2016-12-15T12:00:00.000Z</deadline>
        </item>
        <item>
            <resource>network-interface-attachment</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>network-interface</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>elastic-ip-allocation</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>elastic-ip-association</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>vpc</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>subnet</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>route-table</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>route-table-association</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>network-acl</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>network-acl-association</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>dhcp-options</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>internet-gateway</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>vpc-cidr-block-association</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>vpc-ipv6-cidr-block-association</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>subnet-ipv6-cidr-block-association</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>vpc-peering-connection</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>security-group</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>flow-log</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>customer-gateway</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>vpc-endpoint</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>vpn-connection</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>vpn-gateway</resource>
            <useLongIds>true</useLongIds>
        </item>
    </statusSet>
</DescribeIdFormatResponse>
```

## See Also
<a name="API_DescribeIdFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeIdFormat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeIdFormat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeIdFormat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeIdFormat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeIdFormat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeIdFormat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeIdFormat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeIdFormat)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeIdFormat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeIdFormat)
