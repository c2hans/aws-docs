---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrincipalIdFormat.html
---

# DescribePrincipalIdFormat
<a name="API_DescribePrincipalIdFormat"></a>

Describes the ID format settings for the root user and all IAM roles and IAM users that have explicitly specified a longer ID (17-character ID) preference.

By default, all IAM roles and IAM users default to the same ID settings as the root user, unless they explicitly override the settings. This request is useful for identifying those IAM users and IAM roles that have overridden the default ID settings.

The following resource types support longer IDs: `bundle` \| `conversion-task` \| `customer-gateway` \| `dhcp-options` \| `elastic-ip-allocation` \| `elastic-ip-association` \| `export-task` \| `flow-log` \| `image` \| `import-task` \| `instance` \| `internet-gateway` \| `network-acl` \| `network-acl-association` \| `network-interface` \| `network-interface-attachment` \| `prefix-list` \| `reservation` \| `route-table` \| `route-table-association` \| `security-group` \| `snapshot` \| `subnet` \| `subnet-cidr-block-association` \| `volume` \| `vpc` \| `vpc-cidr-block-association` \| `vpc-endpoint` \| `vpc-peering-connection` \| `vpn-connection` \| `vpn-gateway`.

## Request Parameters
<a name="API_DescribePrincipalIdFormat_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **MaxResults**
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 **NextToken**
The token to request the next page of results.
Type: String
Required: No

 **Resource.N**
The type of resource: `bundle` \| `conversion-task` \| `customer-gateway` \| `dhcp-options` \| `elastic-ip-allocation` \| `elastic-ip-association` \| `export-task` \| `flow-log` \| `image` \| `import-task` \| `instance` \| `internet-gateway` \| `network-acl` \| `network-acl-association` \| `network-interface` \| `network-interface-attachment` \| `prefix-list` \| `reservation` \| `route-table` \| `route-table-association` \| `security-group` \| `snapshot` \| `subnet` \| `subnet-cidr-block-association` \| `volume` \| `vpc` \| `vpc-cidr-block-association` \| `vpc-endpoint` \| `vpc-peering-connection` \| `vpn-connection` \| `vpn-gateway`
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribePrincipalIdFormat_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

 **principalSet**
Information about the ID format settings for the ARN.
Type: Array of [PrincipalIdFormat](API_PrincipalIdFormat.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribePrincipalIdFormat_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribePrincipalIdFormat_Examples"></a>

### Example
<a name="API_DescribePrincipalIdFormat_Example_1"></a>

This example describes the ID format for the root user and all IAM roles and IAM users that have explicitly specified a longer ID preference.

#### Sample Request
<a name="API_DescribePrincipalIdFormat_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribePrincipalIdFormat
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribePrincipalIdFormat_Example_1_Response"></a>

```
<DescribePrincipalIdFormatResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <principalSet>
        <item>
            <arn>arn:aws:iam::123456789012:root</arn>
            <statusSet>
                <item>
                    <deadline>2016-12-15T12:00:00.000Z</deadline>
                    <resource>reservation</resource>
                    <useLongIds>true</useLongIds>
                </item>
                <item>
                    <deadline>2016-12-15T12:00:00.000Z</deadline>
                    <resource>instance</resource>
                    <useLongIds>true</useLongIds>
                </item>
                <item>
                    <deadline>2016-12-15T12:00:00.000Z</deadline>
                    <resource>volume</resource>
                    <useLongIds>true</useLongIds>
                </item>
                <item>
                    <deadline>2016-12-15T12:00:00.000Z</deadline>
                    <resource>snapshot</resource>
                    <useLongIds>true</useLongIds>
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
        </item>
        <item>
            <arn>arn:aws:iam::987654321000:user/user1</arn>
            <statusSet>
                <item>
                    <deadline>2016-12-15T12:00:00.000Z</deadline>
                    <resource>reservation</resource>
                    <useLongIds>true</useLongIds>
                </item>
                <item>
                    <deadline>2016-12-15T12:00:00.000Z</deadline>
                    <resource>instance</resource>
                    <useLongIds>true</useLongIds>
                </item>
                <item>
                    <deadline>2016-12-15T12:00:00.000Z</deadline>
                    <resource>volume</resource>
                    <useLongIds>true</useLongIds>
                </item>
                <item>
                    <deadline>2016-12-15T12:00:00.000Z</deadline>
                    <resource>snapshot</resource>
                    <useLongIds>true</useLongIds>
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
                    <useLongIds>false</useLongIds>
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
        </item>
    </principalSet>
</DescribePrincipalIdFormatResponse>
```

## See Also
<a name="API_DescribePrincipalIdFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribePrincipalIdFormat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribePrincipalIdFormat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribePrincipalIdFormat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribePrincipalIdFormat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribePrincipalIdFormat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribePrincipalIdFormat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribePrincipalIdFormat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribePrincipalIdFormat)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribePrincipalIdFormat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribePrincipalIdFormat)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
