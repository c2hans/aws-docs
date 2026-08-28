---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAggregateIdFormat.html
---

# DescribeAggregateIdFormat
<a name="API_DescribeAggregateIdFormat"></a>

Describes the longer ID format settings for all resource types in a specific Region. This request is useful for performing a quick audit to determine whether a specific Region is fully opted in for longer IDs (17-character IDs).

This request only returns information about resource types that support longer IDs.

The following resource types support longer IDs: `bundle` \| `conversion-task` \| `customer-gateway` \| `dhcp-options` \| `elastic-ip-allocation` \| `elastic-ip-association` \| `export-task` \| `flow-log` \| `image` \| `import-task` \| `instance` \| `internet-gateway` \| `network-acl` \| `network-acl-association` \| `network-interface` \| `network-interface-attachment` \| `prefix-list` \| `reservation` \| `route-table` \| `route-table-association` \| `security-group` \| `snapshot` \| `subnet` \| `subnet-cidr-block-association` \| `volume` \| `vpc` \| `vpc-cidr-block-association` \| `vpc-endpoint` \| `vpc-peering-connection` \| `vpn-connection` \| `vpn-gateway`.

## Request Parameters
<a name="API_DescribeAggregateIdFormat_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DescribeAggregateIdFormat_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **statusSet**
Information about each resource's ID format.
Type: Array of [IdFormat](API_IdFormat.md) objects

 **useLongIdsAggregated**
Indicates whether all resource types in the Region are configured to use longer IDs. This value is only `true` if all users are configured to use longer IDs for all resources types in the Region.
Type: Boolean

## Errors
<a name="API_DescribeAggregateIdFormat_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeAggregateIdFormat_Examples"></a>

### Example
<a name="API_DescribeAggregateIdFormat_Example_1"></a>

This example describes the overall ID format settings for the default Region.

#### Sample Request
<a name="API_DescribeAggregateIdFormat_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeAggregateIdFormat
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeAggregateIdFormat_Example_1_Response"></a>

```
<DescribeAggregateIdFormatResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <useLongIdsAggregated>true</useLongIdsAggregated>
    <statusSet>
        <item>
            <resource>security-group</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>route-table-association</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>vpc</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>flow-log</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>vpc-peering-connection</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>elastic-ip-association</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>vpc-cidr-block-association</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>network-interface</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>subnet</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <deadline>2016-12-15T14:00:00.000Z</deadline>
            <resource>volume</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>vpc-ipv6-cidr-block-association</resource>
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
            <deadline>2016-12-15T14:00:00.000Z</deadline>
            <resource>snapshot</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>subnet-ipv6-cidr-block-association</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>network-interface-attachment</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>elastic-ip-allocation</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>internet-gateway</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <deadline>2016-12-15T14:00:00.000Z</deadline>
            <resource>reservation</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <deadline>2016-12-15T14:00:00.000Z</deadline>
            <resource>instance</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>route-table</resource>
            <useLongIds>true</useLongIds>
        </item>
        <item>
            <resource>network-acl</resource>
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
</DescribeAggregateIdFormatResponse>
```

## See Also
<a name="API_DescribeAggregateIdFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeAggregateIdFormat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeAggregateIdFormat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeAggregateIdFormat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeAggregateIdFormat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeAggregateIdFormat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeAggregateIdFormat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeAggregateIdFormat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeAggregateIdFormat)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeAggregateIdFormat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeAggregateIdFormat)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
