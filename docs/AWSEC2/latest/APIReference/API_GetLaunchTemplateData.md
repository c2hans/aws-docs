---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetLaunchTemplateData.html
---

# GetLaunchTemplateData
<a name="API_GetLaunchTemplateData"></a>

Retrieves the configuration data of the specified instance. You can use this data to create a launch template.

This action calls on other describe actions to get instance information. Depending on your instance configuration, you may need to allow the following actions in your IAM policy: `DescribeSpotInstanceRequests`, `DescribeInstanceCreditSpecifications`, `DescribeVolumes`, and `DescribeInstanceAttribute`. Or, you can allow `describe*` depending on your instance requirements.

## Request Parameters
<a name="API_GetLaunchTemplateData_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

## Response Elements
<a name="API_GetLaunchTemplateData_ResponseElements"></a>

The following elements are returned by the service.

 **launchTemplateData**
The instance data.
Type: [ResponseLaunchTemplateData](API_ResponseLaunchTemplateData.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetLaunchTemplateData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetLaunchTemplateData_Examples"></a>

### Example
<a name="API_GetLaunchTemplateData_Example_1"></a>

This example gets the data for instance `i-123456abcabc123ab`.

#### Sample Request
<a name="API_GetLaunchTemplateData_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetLaunchTemplateData
&InstanceId=i-123456abcabc123ab
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetLaunchTemplateData_Example_1_Response"></a>

```
<GetLaunchTemplateDataResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>57372b95-c320-409e-b268-1e4example</requestId>
    <launchTemplateData>
        <blockDeviceMappingSet>
            <item>
                <deviceName>/dev/xvda</deviceName>
                <ebs>
                    <deleteOnTermination>true</deleteOnTermination>
                </ebs>
            </item>
        </blockDeviceMappingSet>
        <ebsOptimized>false</ebsOptimized>
        <iamInstanceProfile>
            <arn>arn:aws:iam::123456789012:instance-profile/AdminRole</arn>
        </iamInstanceProfile>
        <imageId>ami-1a2b3c4d</imageId>
        <instanceType>t2.micro</instanceType>
        <keyName>kp-us-east</keyName>
        <monitoring/>
        <networkInterfaceSet>
            <item>
                <description>Primary network interface</description>
                <groupSet>
                    <groupId>sg-7c227abc</groupId>
                </groupSet>
                <ipv6AddressesSet/>
                <networkInterfaceId>eni-d26c8f36</networkInterfaceId>
                <privateIpAddress>10.0.0.197</privateIpAddress>
                <privateIpAddressesSet>
                    <item>
                        <primary>true</primary>
                        <privateIpAddress>10.0.0.197</privateIpAddress>
                    </item>
                </privateIpAddressesSet>
                <subnetId>subnet-7b16dabc</subnetId>
            </item>
            <item>
                <description>my network interface</description>
                <groupSet>
                    <groupId>sg-54e8b123</groupId>
                </groupSet>
                <ipv6AddressesSet/>
                <networkInterfaceId>eni-714bc4a5</networkInterfaceId>
                <privateIpAddress>10.0.0.190</privateIpAddress>
                <privateIpAddressesSet>
                    <item>
                        <primary>true</primary>
                        <privateIpAddress>10.0.0.190</privateIpAddress>
                    </item>
                </privateIpAddressesSet>
                <subnetId>subnet-7b16de0c</subnetId>
            </item>
        </networkInterfaceSet>
        <placement>
            <availabilityZone>us-east-1a</availabilityZone>
            <groupName/>
            <tenancy>default</tenancy>
        </placement>
    </launchTemplateData>
</GetLaunchTemplateDataResponse>
```

## See Also
<a name="API_GetLaunchTemplateData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetLaunchTemplateData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetLaunchTemplateData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetLaunchTemplateData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetLaunchTemplateData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetLaunchTemplateData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetLaunchTemplateData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetLaunchTemplateData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetLaunchTemplateData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetLaunchTemplateData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetLaunchTemplateData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
