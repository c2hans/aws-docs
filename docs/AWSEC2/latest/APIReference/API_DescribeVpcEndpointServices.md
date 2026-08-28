---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServices.html
---

# DescribeVpcEndpointServices
<a name="API_DescribeVpcEndpointServices"></a>

Describes available services to which you can create a VPC endpoint.

When the service provider and the consumer have different accounts in multiple Availability Zones, and the consumer views the VPC endpoint service information, the response only includes the common Availability Zones. For example, when the service provider account uses `us-east-1a` and `us-east-1c` and the consumer uses `us-east-1a` and `us-east-1b`, the response includes the VPC endpoint services in the common Availability Zone, `us-east-1a`.

## Request Parameters
<a name="API_DescribeVpcEndpointServices_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `owner` - The ID or alias of the AWS account that owns the service.
+  `service-name` - The name of the service.
+  `service-region` - The Region of the service.
+  `service-type` - The type of service (`Interface` \| `Gateway` \| `GatewayLoadBalancer`).
+  `supported-ip-address-types` - The IP address type (`ipv4` \| `ipv6`).
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
Constraint: If the value is greater than 1,000, we return only 1,000 items.
Type: Integer
Required: No

 **NextToken**
The token for the next set of items to return. (You received this token from a prior call.)
Type: String
Required: No

 **ServiceName.N**
The service names.
Type: Array of strings
Required: No

 **ServiceRegion.N**
The service Regions.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeVpcEndpointServices_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 **requestId**
The ID of the request.
Type: String

 **serviceDetailSet**
Information about the service.
Type: Array of [ServiceDetail](API_ServiceDetail.md) objects

 **serviceNameSet**
The supported services.
Type: Array of strings

## Errors
<a name="API_DescribeVpcEndpointServices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeVpcEndpointServices_Examples"></a>

### Example 1
<a name="API_DescribeVpcEndpointServices_Example_1"></a>

This example describes all available endpoint services.

#### Sample Request
<a name="API_DescribeVpcEndpointServices_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVpcEndpointServices
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVpcEndpointServices_Example_1_Response"></a>

```
<DescribeVpcEndpointServicesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>19a9ff46-7df6-49b8-9726-3df27527089d</requestId>
    <serviceNameSet>
        <item>com.amazonaws.us-east-1.dynamodb</item>
        <item>com.amazonaws.us-east-1.ec2</item>
        <item>com.amazonaws.us-east-1.ec2messages</item>
        <item>com.amazonaws.us-east-1.elasticloadbalancing</item>
        <item>com.amazonaws.us-east-1.kinesis-streams</item>
        <item>com.amazonaws.us-east-1.s3</item>
        <item>com.amazonaws.us-east-1.ssm</item>
    </serviceNameSet>
    <serviceDetailSet>
        <item>
            <owner>amazon</owner>
            <serviceType>
                <item>
                    <serviceType>Gateway</serviceType>
                </item>
            </serviceType>
            <baseEndpointDnsNameSet>
                <item>dynamodb.us-east-1.amazonaws.com</item>
            </baseEndpointDnsNameSet>
            <acceptanceRequired>false</acceptanceRequired>
            <availabilityZoneSet>
                <item>us-east-1a</item>
                <item>us-east-1b</item>
                <item>us-east-1c</item>
                <item>us-east-1d</item>
                <item>us-east-1e</item>
                <item>us-east-1f</item>
            </availabilityZoneSet>
            <serviceName>com.amazonaws.us-east-1.dynamodb</serviceName>
            <vpcEndpointPolicySupported>true</vpcEndpointPolicySupported>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>TeamA</value>
                </item>
            </tagSet>
        </item>
        <item>
            <owner>amazon</owner>
            <serviceType>
                <item>
                    <serviceType>Interface</serviceType>
                </item>
            </serviceType>
            <baseEndpointDnsNameSet>
                <item>ec2.us-east-1.vpce.amazonaws.com</item>
            </baseEndpointDnsNameSet>
            <acceptanceRequired>false</acceptanceRequired>
            <privateDnsName>ec2.us-east-1.amazonaws.com</privateDnsName>
            <availabilityZoneSet>
                <item>us-east-1a</item>
                <item>us-east-1b</item>
                <item>us-east-1c</item>
                <item>us-east-1d</item>
                <item>us-east-1e</item>
                <item>us-east-1f</item>
            </availabilityZoneSet>
            <serviceName>com.amazonaws.us-east-1.ec2</serviceName>
            <vpcEndpointPolicySupported>false</vpcEndpointPolicySupported>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>TeamA</value>
                </item>
            </tagSet>
        </item>
        <item>
            <owner>amazon</owner>
            <serviceType>
                <item>
                    <serviceType>Interface</serviceType>
                </item>
            </serviceType>
            <baseEndpointDnsNameSet>
                <item>ec2messages.us-east-1.vpce.amazonaws.com</item>
            </baseEndpointDnsNameSet>
            <acceptanceRequired>false</acceptanceRequired>
            <privateDnsName>ec2messages.us-east-1.amazonaws.com</privateDnsName>
            <availabilityZoneSet>
                <item>us-east-1a</item>
                <item>us-east-1b</item>
                <item>us-east-1c</item>
                <item>us-east-1d</item>
                <item>us-east-1e</item>
                <item>us-east-1f</item>
            </availabilityZoneSet>
            <serviceName>com.amazonaws.us-east-1.ec2messages</serviceName>
            <vpcEndpointPolicySupported>false</vpcEndpointPolicySupported>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>TeamA</value>
                </item>
            </tagSet>
        </item>
        <item>
            <owner>amazon</owner>
            <serviceType>
                <item>
                    <serviceType>Interface</serviceType>
                </item>
            </serviceType>
            <baseEndpointDnsNameSet>
                <item>elasticloadbalancing.us-east-1.vpce.amazonaws.com</item>
            </baseEndpointDnsNameSet>
            <acceptanceRequired>false</acceptanceRequired>
            <privateDnsName>elasticloadbalancing.us-east-1.amazonaws.com</privateDnsName>
            <availabilityZoneSet>
                <item>us-east-1a</item>
                <item>us-east-1b</item>
                <item>us-east-1c</item>
                <item>us-east-1d</item>
                <item>us-east-1e</item>
                <item>us-east-1f</item>
            </availabilityZoneSet>
            <serviceName>com.amazonaws.us-east-1.elasticloadbalancing</serviceName>
            <vpcEndpointPolicySupported>false</vpcEndpointPolicySupported>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>TeamA</value>
                </item>
            </tagSet>
        </item>
        <item>
            <owner>amazon</owner>
            <serviceType>
                <item>
                    <serviceType>Interface</serviceType>
                </item>
            </serviceType>
            <baseEndpointDnsNameSet>
                <item>kinesis.us-east-1.vpce.amazonaws.com</item>
            </baseEndpointDnsNameSet>
            <acceptanceRequired>false</acceptanceRequired>
            <privateDnsName>kinesis.us-east-1.amazonaws.com</privateDnsName>
            <availabilityZoneSet>
                <item>us-east-1a</item>
                <item>us-east-1b</item>
                <item>us-east-1c</item>
                <item>us-east-1d</item>
                <item>us-east-1e</item>
                <item>us-east-1f</item>
            </availabilityZoneSet>
            <serviceName>com.amazonaws.us-east-1.kinesis-streams</serviceName>
            <vpcEndpointPolicySupported>false</vpcEndpointPolicySupported>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>TeamA</value>
                </item>
            </tagSet>
        </item>
        <item>
            <owner>amazon</owner>
            <serviceType>
                <item>
                    <serviceType>Gateway</serviceType>
                </item>
            </serviceType>
            <baseEndpointDnsNameSet>
                <item>s3.us-east-1.amazonaws.com</item>
            </baseEndpointDnsNameSet>
            <acceptanceRequired>false</acceptanceRequired>
            <availabilityZoneSet>
                <item>us-east-1a</item>
                <item>us-east-1b</item>
                <item>us-east-1c</item>
                <item>us-east-1d</item>
                <item>us-east-1e</item>
                <item>us-east-1f</item>
            </availabilityZoneSet>
            <serviceName>com.amazonaws.us-east-1.s3</serviceName>
            <vpcEndpointPolicySupported>true</vpcEndpointPolicySupported>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>TeamA</value>
                </item>
            </tagSet>
        </item>
        <item>
            <owner>amazon</owner>
            <serviceType>
                <item>
                    <serviceType>Interface</serviceType>
                </item>
            </serviceType>
            <baseEndpointDnsNameSet>
                <item>ssm.us-east-1.vpce.amazonaws.com</item>
            </baseEndpointDnsNameSet>
            <acceptanceRequired>false</acceptanceRequired>
            <privateDnsName>ssm.us-east-1.amazonaws.com</privateDnsName>
            <availabilityZoneSet>
                <item>us-east-1a</item>
                <item>us-east-1b</item>
                <item>us-east-1c</item>
                <item>us-east-1d</item>
                <item>us-east-1e</item>
            </availabilityZoneSet>
            <serviceName>com.amazonaws.us-east-1.ssm</serviceName>
            <vpcEndpointPolicySupported>true</vpcEndpointPolicySupported>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>TeamA</value>
                </item>
            </tagSet>
        </item>
    </serviceDetailSet>
</DescribeVpcEndpointServicesResponse>
```

## See Also
<a name="API_DescribeVpcEndpointServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVpcEndpointServices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVpcEndpointServices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVpcEndpointServices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVpcEndpointServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVpcEndpointServices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVpcEndpointServices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVpcEndpointServices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVpcEndpointServices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVpcEndpointServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVpcEndpointServices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
