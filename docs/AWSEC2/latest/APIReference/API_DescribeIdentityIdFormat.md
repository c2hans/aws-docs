---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIdentityIdFormat.html
---

# DescribeIdentityIdFormat
<a name="API_DescribeIdentityIdFormat"></a>

Describes the ID format settings for resources for the specified IAM user, IAM role, or root user. For example, you can view the resource types that are enabled for longer IDs. This request only returns information about resource types whose ID formats can be modified; it does not return information about other resource types. For more information, see [Resource IDs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resource-ids.html) in the *Amazon Elastic Compute Cloud User Guide*.

The following resource types support longer IDs: `bundle` \| `conversion-task` \| `customer-gateway` \| `dhcp-options` \| `elastic-ip-allocation` \| `elastic-ip-association` \| `export-task` \| `flow-log` \| `image` \| `import-task` \| `instance` \| `internet-gateway` \| `network-acl` \| `network-acl-association` \| `network-interface` \| `network-interface-attachment` \| `prefix-list` \| `reservation` \| `route-table` \| `route-table-association` \| `security-group` \| `snapshot` \| `subnet` \| `subnet-cidr-block-association` \| `volume` \| `vpc` \| `vpc-cidr-block-association` \| `vpc-endpoint` \| `vpc-peering-connection` \| `vpn-connection` \| `vpn-gateway`.

These settings apply to the principal specified in the request. They do not apply to the principal that makes the request.

## Request Parameters
<a name="API_DescribeIdentityIdFormat_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **PrincipalArn**
The ARN of the principal, which can be an IAM role, IAM user, or the root user.
Type: String
Required: Yes

 **Resource**
The type of resource: `bundle` \| `conversion-task` \| `customer-gateway` \| `dhcp-options` \| `elastic-ip-allocation` \| `elastic-ip-association` \| `export-task` \| `flow-log` \| `image` \| `import-task` \| `instance` \| `internet-gateway` \| `network-acl` \| `network-acl-association` \| `network-interface` \| `network-interface-attachment` \| `prefix-list` \| `reservation` \| `route-table` \| `route-table-association` \| `security-group` \| `snapshot` \| `subnet` \| `subnet-cidr-block-association` \| `volume` \| `vpc` \| `vpc-cidr-block-association` \| `vpc-endpoint` \| `vpc-peering-connection` \| `vpn-connection` \| `vpn-gateway`
Type: String
Required: No

## Response Elements
<a name="API_DescribeIdentityIdFormat_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **statusSet**
Information about the ID format for the resources.
Type: Array of [IdFormat](API_IdFormat.md) objects

## Errors
<a name="API_DescribeIdentityIdFormat_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeIdentityIdFormat_Examples"></a>

### Example
<a name="API_DescribeIdentityIdFormat_Example_1"></a>

This example describes the ID format for the IAM role 'EC2Role'.

#### Sample Request
<a name="API_DescribeIdentityIdFormat_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeIdentityIdFormat
&PrincipalArn=arn:aws:iam::123456789012:role/EC2Role
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeIdentityIdFormat_Example_1_Response"></a>

```
<DescribeIdentityIdFormatResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
    <statusSet>
        <item>
            <useLongIds>true</useLongIds>
            <deadline>2016-12-15T12:00:00Z</deadline>
            <resource>reservation</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <deadline>2016-12-15T12:00:00Z</deadline>
            <resource>instance</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <deadline>2016-12-15T12:00:00Z</deadline>
            <resource>volume</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <deadline>2016-12-15T12:00:00Z</deadline>
            <resource>snapshot</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>network-interface-attachment</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>network-interface</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>elastic-ip-allocation</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>elastic-ip-association</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>vpc</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>subnet</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>route-table</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>route-table-association</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>network-acl</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>network-acl-association</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>dhcp-options</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>internet-gateway</resource>
        </item>
        <item>
            <useLongIds>false</useLongIds>
            <resource>vpc-cidr-block-association</resource>
        </item>
        <item>
            <useLongIds>false</useLongIds>
            <resource>vpc-ipv6-cidr-block-association</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>subnet-ipv6-cidr-block-association</resource>
        </item>
        <item>
            <useLongIds>false</useLongIds>
            <resource>vpc-peering-connection</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>security-group</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>flow-log</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>customer-gateway</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>vpc-endpoint</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>vpn-connection</resource>
        </item>
        <item>
            <useLongIds>true</useLongIds>
            <resource>vpn-gateway</resource>
        </item>
    </statusSet>
</DescribeIdentityIdFormatResponse>
```

## See Also
<a name="API_DescribeIdentityIdFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeIdentityIdFormat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeIdentityIdFormat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeIdentityIdFormat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeIdentityIdFormat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeIdentityIdFormat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeIdentityIdFormat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeIdentityIdFormat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeIdentityIdFormat)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeIdentityIdFormat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeIdentityIdFormat)
