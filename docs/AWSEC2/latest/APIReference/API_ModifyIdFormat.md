---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIdFormat.html
---

# ModifyIdFormat
<a name="API_ModifyIdFormat"></a>

Modifies the ID format for the specified resource on a per-Region basis. You can specify that resources should receive longer IDs (17-character IDs) when they are created.

This request can only be used to modify longer ID settings for resource types that are within the opt-in period. Resources currently in their opt-in period include: `bundle` \| `conversion-task` \| `customer-gateway` \| `dhcp-options` \| `elastic-ip-allocation` \| `elastic-ip-association` \| `export-task` \| `flow-log` \| `image` \| `import-task` \| `internet-gateway` \| `network-acl` \| `network-acl-association` \| `network-interface` \| `network-interface-attachment` \| `prefix-list` \| `route-table` \| `route-table-association` \| `security-group` \| `subnet` \| `subnet-cidr-block-association` \| `vpc` \| `vpc-cidr-block-association` \| `vpc-endpoint` \| `vpc-peering-connection` \| `vpn-connection` \| `vpn-gateway`.

This setting applies to the IAM user who makes the request; it does not apply to the entire AWS account. By default, an IAM user defaults to the same settings as the root user. If you're using this action as the root user, then these settings apply to the entire account, unless an IAM user explicitly overrides these settings for themselves. For more information, see [Resource IDs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resource-ids.html) in the *Amazon Elastic Compute Cloud User Guide*.

Resources created with longer IDs are visible to all IAM roles and users, regardless of these settings and provided that they have permission to use the relevant `Describe` command for the resource type.

## Request Parameters
<a name="API_ModifyIdFormat_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Resource**
The type of resource: `bundle` \| `conversion-task` \| `customer-gateway` \| `dhcp-options` \| `elastic-ip-allocation` \| `elastic-ip-association` \| `export-task` \| `flow-log` \| `image` \| `import-task` \| `internet-gateway` \| `network-acl` \| `network-acl-association` \| `network-interface` \| `network-interface-attachment` \| `prefix-list` \| `route-table` \| `route-table-association` \| `security-group` \| `subnet` \| `subnet-cidr-block-association` \| `vpc` \| `vpc-cidr-block-association` \| `vpc-endpoint` \| `vpc-peering-connection` \| `vpn-connection` \| `vpn-gateway`.
Alternatively, use the `all-current` option to include all resource types that are currently within their opt-in period for longer IDs.
Type: String
Required: Yes

 **UseLongIds**
Indicate whether the resource should use longer IDs (17-character IDs).
Type: Boolean
Required: Yes

## Response Elements
<a name="API_ModifyIdFormat_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ModifyIdFormat_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyIdFormat_Examples"></a>

### Example
<a name="API_ModifyIdFormat_Example_1"></a>

This example sets the UseLongIds parameter to true for instances, so that instances you launch receive longer IDs.

#### Sample Request
<a name="API_ModifyIdFormat_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyIdFormat
&Resource=instance
&UseLongIds=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyIdFormat_Example_1_Response"></a>

```
<ModifyIdFormatResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>92c1af09-cb4c-410e-8a96-EXAMPLE</requestId>
    <return>true</return>
</ModifyIdFormatResponse>
```

## See Also
<a name="API_ModifyIdFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyIdFormat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyIdFormat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyIdFormat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyIdFormat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyIdFormat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyIdFormat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyIdFormat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyIdFormat)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyIdFormat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyIdFormat)
