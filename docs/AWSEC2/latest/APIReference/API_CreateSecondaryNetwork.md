---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecondaryNetwork.html
---

# CreateSecondaryNetwork
<a name="API_CreateSecondaryNetwork"></a>

Creates a secondary network.

The allowed size for a secondary network CIDR block is between /28 netmask (16 IP addresses) and /12 netmask (1,048,576 IP addresses).

## Request Parameters
<a name="API_CreateSecondaryNetwork_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensure Idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Ipv4CidrBlock**
The IPv4 CIDR block for the secondary network. The CIDR block size must be between /12 and /28.
Type: String
Required: Yes

 **NetworkType**
The type of secondary network.
Type: String
Valid Values: `rdma`
Required: Yes

 **TagSpecification.N**
The tags to assign to the secondary network.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateSecondaryNetwork_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.
Type: String

 **requestId**
The ID of the request.
Type: String

 **secondaryNetwork**
Information about the secondary network.
Type: [SecondaryNetwork](API_SecondaryNetwork.md) object

## Errors
<a name="API_CreateSecondaryNetwork_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateSecondaryNetwork_Examples"></a>

### Example
<a name="API_CreateSecondaryNetwork_Example_1"></a>

This example creates a rdma secondary network with a /16 CIDR block.

#### Sample Request
<a name="API_CreateSecondaryNetwork_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateSecondaryNetwork
   &Ipv4CidrBlock=10.0.0.0/16
   &NetworkType=rdma
   &ClientToken=550e8400-e29b-41d4-a716-446655440000
   &TagSpecification.1.ResourceType=secondary-network
   &TagSpecification.1.Tag.1.Key=Name
   &TagSpecification.1.Tag.1.Value=Prod%20Secondary%20Network
   &AUTHPARAMS
```

#### Sample Response
<a name="API_CreateSecondaryNetwork_Example_1_Response"></a>

```
<CreateSecondaryNetworkResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <secondaryNetwork>
      <secondaryNetworkId>sn-0123456789abcdef0</secondaryNetworkId>
      <secondaryNetworkArn>arn:aws:ec2:us-east-2:123456789012:secondary-network/sn-0123456789abcdef0</secondaryNetworkArn>
      <ownerId>123456789012</ownerId>
      <type>rdma</type>
      <state>create-in-progress</state>
      <ipv4CidrBlockAssociations>
         <item>
            <associationId>sn-cidr-assoc-56789901234abcdef0</associationId>
            <cidrBlock>10.0.0.0/16</cidrBlock>
            <state>associating</state>
         </item>
      </ipv4CidrBlockAssociations>
      <tagSet>
         <item>
            <key>Name</key>
            <value>Prod Secondary Network</value>
         </item>
      </tagSet>
   </secondaryNetwork>
   <clientToken>550e8400-e29b-41d4-a716-446655440000</clientToken>
</CreateSecondaryNetworkResponse>
```

## See Also
<a name="API_CreateSecondaryNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateSecondaryNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateSecondaryNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateSecondaryNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateSecondaryNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateSecondaryNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateSecondaryNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateSecondaryNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateSecondaryNetwork)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateSecondaryNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateSecondaryNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
