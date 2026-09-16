---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeDhcpOptions.html
---

# DescribeDhcpOptions
<a name="API_DescribeDhcpOptions"></a>

Describes your DHCP option sets. The default is to describe all your DHCP option sets. Alternatively, you can specify specific DHCP option set IDs or filter the results to include only the DHCP option sets that match specific criteria.

For more information, see [DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_DescribeDhcpOptions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DhcpOptionsId.N**
The IDs of DHCP option sets.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `dhcp-options-id` - The ID of a DHCP options set.
+  `key` - The key for one of the options (for example, `domain-name`).
+  `value` - The value for one of the options.
+  `owner-id` - The ID of the AWS account that owns the DHCP options set.
+  `tag` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeDhcpOptions_ResponseElements"></a>

The following elements are returned by the service.

 **dhcpOptionsSet**
Information about the DHCP options sets.
Type: Array of [DhcpOptions](API_DhcpOptions.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeDhcpOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeDhcpOptions_Examples"></a>

### Example 1
<a name="API_DescribeDhcpOptions_Example_1"></a>

This example describes all of your DHCP option sets.

#### Sample Request
<a name="API_DescribeDhcpOptions_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeDhcpOptions
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeDhcpOptions_Example_1_Response"></a>

```
<DescribeDhcpOptionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>a0d78ea6-7bc7-4cb8-b827-c5ff0aff0140</requestId>
    <dhcpOptionsSet>
        <item>
            <dhcpOptionsId>dopt-1EXAMPLE</dhcpOptionsId>
            <ownerId>111122223333</ownerId>
            <dhcpConfigurationSet>
                <item>
                    <key>domain-name</key>
                    <valueSet>
                        <item>
                            <value>us-east-2.compute.internal</value>
                        </item>
                    </valueSet>
                </item>
                <item>
                    <key>domain-name-servers</key>
                    <valueSet>
                        <item>
                            <value>AmazonProvidedDNS</value>
                        </item>
                    </valueSet>
                </item>
            </dhcpConfigurationSet>
        </item>
        <item>
            <dhcpOptionsId>dopt-fEXAMPLE</dhcpOptionsId>
            <ownerId>111122223333</ownerId>
            <dhcpConfigurationSet>
                <item>
                    <key>domain-name</key>
                    <valueSet>
                        <item>
                            <value>us-east-2.compute.internal</value>
                        </item>
                    </valueSet>
                </item>
                <item>
                    <key>domain-name-servers</key>
                    <valueSet>
                        <item>
                            <value>AmazonProvidedDNS</value>
                        </item>
                    </valueSet>
                </item>
            </dhcpConfigurationSet>
        </item>
    </dhcpOptionsSet>
</DescribeDhcpOptionsResponse>
```

### Example 2
<a name="API_DescribeDhcpOptions_Example_2"></a>

This example uses filters to describe any DHCP option sets that include a `domain-name` option whose value includes the string `example`.

#### Sample Request
<a name="API_DescribeDhcpOptions_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeDhcpOptions
&Filter.1.Name=key
&Filter.1.Value.1=domain-name
&Filter.2.Name=value
&Filter.2.Value.1=*example*
&AUTHPARAMS
```

## See Also
<a name="API_DescribeDhcpOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeDhcpOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeDhcpOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeDhcpOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeDhcpOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeDhcpOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeDhcpOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeDhcpOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeDhcpOptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeDhcpOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeDhcpOptions)
