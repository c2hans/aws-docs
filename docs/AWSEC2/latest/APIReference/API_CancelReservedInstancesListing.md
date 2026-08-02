---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelReservedInstancesListing.html
---

# CancelReservedInstancesListing
<a name="API_CancelReservedInstancesListing"></a>

Cancels the specified Reserved Instance listing in the Reserved Instance Marketplace.

For more information, see [Sell in the Reserved Instance Marketplace](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CancelReservedInstancesListing_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ReservedInstancesListingId**
The ID of the Reserved Instance listing.
Type: String
Required: Yes

## Response Elements
<a name="API_CancelReservedInstancesListing_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **reservedInstancesListingsSet**
The Reserved Instance listing.
Type: Array of [ReservedInstancesListing](API_ReservedInstancesListing.md) objects

## Errors
<a name="API_CancelReservedInstancesListing_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CancelReservedInstancesListing_Examples"></a>

### Example
<a name="API_CancelReservedInstancesListing_Example_1"></a>

This example request cancels a Reserved Instance listing in the Reserved Instance Marketplace. The response shows that the status is cancelled.

#### Sample Request
<a name="API_CancelReservedInstancesListing_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CancelReservedInstancesListing
&ReservedInstancesListingId=3ebe97b5-f273-43b6-a204-7a18cEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_CancelReservedInstancesListing_Example_1_Response"></a>

```
<CancelReservedInstancesListingResponse>
    <requestId>bec2cf62-98ef-434a-8a15-886fcexample</requestId>
    <reservedInstancesListingsSet>
        <item>
            <reservedInstancesListingId>3ebe97b5-f273-43b6-a204-7a18cEXAMPLE</reservedInstancesListingId>
            <reservedInstancesId>e5a2ff3b-7d14-494f-90af-0b5d0EXAMPLE</reservedInstancesId>
            <createDate>2012-07-12T16:55:28.000Z</createDate>
            <updateDate>2012-07-12T16:55:28.000Z</updateDate>
            <status>cancelled</status>
            <statusMessage>CANCELLED</statusMessage>
            <instanceCounts>
                <item>
                    <state>Available</state>
                    <instanceCount>0</instanceCount>
                </item>
                <item>
                    <state>Sold</state>
                    <instanceCount>0</instanceCount>
                </item>
                <item>
                    <state>Cancelled</state>
                    <instanceCount>1</instanceCount>
                </item>
                <item>
                    <state>Pending</state>
                    <instanceCount>0</instanceCount>
                </item>
            </instanceCounts>
            <priceSchedules>
                <item>
                    <term>5</term>
                    <price>166.64</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>4</term>
                    <price>133.32</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>3</term>
                    <price>99.99</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>2</term>
                    <price>66.66</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
                <item>
                    <term>1</term>
                    <price>33.33</price>
                    <currencyCode>USD</currencyCode>
                    <active>false</active>
                </item>
            </priceSchedules>
            <tagSet/>
            <clientToken>XqJIt1342112125076</clientToken>
        </item>
    </reservedInstancesListingsSet>
</CancelReservedInstancesListingResponse>
```

## See Also
<a name="API_CancelReservedInstancesListing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CancelReservedInstancesListing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CancelReservedInstancesListing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CancelReservedInstancesListing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CancelReservedInstancesListing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CancelReservedInstancesListing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CancelReservedInstancesListing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CancelReservedInstancesListing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CancelReservedInstancesListing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CancelReservedInstancesListing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CancelReservedInstancesListing)
