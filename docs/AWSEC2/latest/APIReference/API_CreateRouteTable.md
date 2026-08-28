---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRouteTable.html
---

# CreateRouteTable
<a name="API_CreateRouteTable"></a>

Creates a route table for the specified VPC. After you create a route table, you can add routes and associate the table with a subnet.

For more information, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateRouteTable_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TagSpecification.N**
The tags to assign to the route table.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VpcId**
The ID of the VPC.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateRouteTable_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.
Type: String

 **requestId**
The ID of the request.
Type: String

 **routeTable**
Information about the route table.
Type: [RouteTable](API_RouteTable.md) object

## Errors
<a name="API_CreateRouteTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateRouteTable_Examples"></a>

### Example 1
<a name="API_CreateRouteTable_Example_1"></a>

This example creates a route table for the VPC with the ID `vpc-1122334455667788a`. By default, every route table includes a local route that enables traffic to flow within the VPC. The following response shows that route.

#### Sample Request
<a name="API_CreateRouteTable_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateRouteTable
&VpcId=vpc-1122334455667788a
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateRouteTable_Example_1_Response"></a>

```
<CreateRouteTableResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <routeTable>
      <routeTableId>rtb-029e01e661a8fffd9</routeTableId>
      <vpcId>vpc-11ad4878</vpcId>
      <routeSet>
         <item>
            <destinationCidrBlock>10.0.0.0/22</destinationCidrBlock>
            <gatewayId>local</gatewayId>
            <state>active</state>
         </item>
      </routeSet>
      <associationSet/>
      <tagSet/>
   </routeTable>
</CreateRouteTableResponse>
```

### Example 2
<a name="API_CreateRouteTable_Example_2"></a>

This example creates a route table for a VPC that has an associated IPv6 CIDR block. The route table includes a local route that enables IPv6 traffic to flow within the VPC.

#### Sample Request
<a name="API_CreateRouteTable_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateRouteTable
&VpcId=vpc-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateRouteTable_Example_2_Response"></a>

```
<CreateRouteTableResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <routeTable>
        <routeTableId>rtb-8bda6cef</routeTableId>
        <vpcId>vpc-1a2b3c4d</vpcId>
        <routeSet>
            <item>
                <destinationCidrBlock>10.0.0.0/16</destinationCidrBlock>
                <gatewayId>local</gatewayId>
                <state>active</state>
                <origin>CreateRouteTable</origin>
            </item>
            <item>
                <destinationIpv6CidrBlock>2001:db8:1234:1a00::/56</destinationIpv6CidrBlock>
                <gatewayId>local</gatewayId>
                <state>active</state>
                <origin>CreateRouteTable</origin>
            </item>
        </routeSet>
        <associationSet/>
        <propagatingVgwSet/>
        <tagSet/>
    </routeTable>
</CreateRouteTableResponse>
```

## See Also
<a name="API_CreateRouteTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateRouteTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateRouteTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateRouteTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateRouteTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateRouteTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateRouteTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateRouteTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateRouteTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateRouteTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateRouteTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
