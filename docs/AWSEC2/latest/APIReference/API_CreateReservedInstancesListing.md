---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateReservedInstancesListing.html
---

# CreateReservedInstancesListing
<a name="API_CreateReservedInstancesListing"></a>

Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the Reserved Instance Marketplace. You can submit one Standard Reserved Instance listing at a time. To get a list of your Standard Reserved Instances, you can use the [DescribeReservedInstances](API_DescribeReservedInstances.md) operation.

**Note**
Only Standard Reserved Instances can be sold in the Reserved Instance Marketplace. Convertible Reserved Instances cannot be sold.

The Reserved Instance Marketplace matches sellers who want to resell Standard Reserved Instance capacity that they no longer need with buyers who want to purchase additional capacity. Reserved Instances bought and sold through the Reserved Instance Marketplace work like any other Reserved Instances.

To sell your Standard Reserved Instances, you must first register as a seller in the Reserved Instance Marketplace. After completing the registration process, you can create a Reserved Instance Marketplace listing of some or all of your Standard Reserved Instances, and specify the upfront price to receive for them. Your Standard Reserved Instance listings then become available for purchase. To view the details of your Standard Reserved Instance listing, you can use the [DescribeReservedInstancesListings](API_DescribeReservedInstancesListings.md) operation.

For more information, see [Sell in the Reserved Instance Marketplace](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateReservedInstancesListing_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier you provide to ensure idempotency of your listings. This helps avoid duplicate listings. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: Yes

 **InstanceCount**
The number of instances that are a part of a Reserved Instance account to be listed in the Reserved Instance Marketplace. This number should be less than or equal to the instance count associated with the Reserved Instance ID specified in this call.
Type: Integer
Required: Yes

 **PriceSchedules.N**
A list specifying the price of the Standard Reserved Instance for each month remaining in the Reserved Instance term.
Type: Array of [PriceScheduleSpecification](API_PriceScheduleSpecification.md) objects
Required: Yes

 **ReservedInstancesId**
The ID of the active Standard Reserved Instance.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateReservedInstancesListing_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **reservedInstancesListingsSet**
Information about the Standard Reserved Instance listing.
Type: Array of [ReservedInstancesListing](API_ReservedInstancesListing.md) objects

## Errors
<a name="API_CreateReservedInstancesListing_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateReservedInstancesListing_Examples"></a>

### Example
<a name="API_CreateReservedInstancesListing_Example_1"></a>

This example creates a Reserved Instance Marketplace listing from the specified Standard Reserved Instance, which has 11 months remaining in its term. In this example, we set the upfront price at $2.50, and the price drops over the course of the 11-month term if the instance is still not sold.

#### Sample Request
<a name="API_CreateReservedInstancesListing_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateReservedInstancesListing
&ClientToken=myIdempToken1
&InstanceCount=1
&PriceSchedules.1.Price=2.5
&PriceSchedules.1.Term=11
&PriceSchedules.2.Price=2.0
&PriceSchedules.2.Term=8
&PriceSchedules.3.Price=1.5
&PriceSchedules.3.Term=5
&PriceSchedules.4.Price=0.7
&PriceSchedules.4.Term=3
&PriceSchedules.5.Price=0.1
&PriceSchedules.5.Term=1
&ReservedInstancesId=e5a2ff3b-7d14-494f-90af-0b5d0EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateReservedInstancesListing_Example_1_Response"></a>

```
<CreateReservedInstancesListingResponse>
    <requestId>a42481af-335a-4e9e-b291-bd18dexample</requestId>
    <reservedInstancesListingsSet>
        <item>
            <reservedInstancesListingId>5ec28771-05ff-4b9b-aa31-9e57dEXAMPLE</reservedInstancesListingId>
            <reservedInstancesId>e5a2ff3b-7d14-494f-90af-0b5d0EXAMPLE</reservedInstancesId>
            <createDate>2012-07-17T17:11:09.449Z</createDate>
            <updateDate>2012-07-17T17:11:09.468Z</updateDate>
            <status>active</status>
            <statusMessage>ACTIVE</statusMessage>
            <instanceCounts>
                <item>
                    <state>Available</state>
                    <instanceCount>1</instanceCount>
                </item>
                <item>
                    <state>Sold</state>
                    <instanceCount>0</instanceCount>
                </item>
                <item>
                    <state>Cancelled</state>
                    <instanceCount>0</instanceCount>
                </item>
                <item>
                    <state>Pending</state>
                    <instanceCount>0</instanceCount>
                </item>
            </instanceCounts>
            <priceSchedules>
                <item>
                    <term>11</term>
                    <price>2.5</price>
                    <currencyCode>USD</currencyCode>
                    <active>true</active>
                </item>
                <item>
                    <term>10</term>
                    <price>2.5</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>9</term>
                    <price>2.5</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>8</term>
                    <price>2.0</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>7</term>
                    <price>2.0</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>6</term>
                    <price>2.0</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>5</term>
                    <price>1.5</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>4</term>
                    <price>1.5</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>3</term>
                    <price>0.7</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>2</term>
                    <price>0.7</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>1</term>
                    <price>0.1</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
            </priceSchedules>
            <tagSet/>
            <clientToken>myIdempToken1</clientToken>
        </item>
    </reservedInstancesListingsSet>
</CreateReservedInstancesListingResponse>
```

## See Also
<a name="API_CreateReservedInstancesListing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateReservedInstancesListing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateReservedInstancesListing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateReservedInstancesListing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateReservedInstancesListing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateReservedInstancesListing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateReservedInstancesListing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateReservedInstancesListing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateReservedInstancesListing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateReservedInstancesListing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateReservedInstancesListing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
