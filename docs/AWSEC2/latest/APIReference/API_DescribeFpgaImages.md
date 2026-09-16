---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFpgaImages.html
---

# DescribeFpgaImages
<a name="API_DescribeFpgaImages"></a>

Describes the Amazon FPGA Images (AFIs) available to you. These include public AFIs, private AFIs that you own, and AFIs owned by other AWS accounts for which you have load permissions.

## Request Parameters
<a name="API_DescribeFpgaImages_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `create-time` - The creation time of the AFI.
+  `fpga-image-id` - The FPGA image identifier (AFI ID).
+  `fpga-image-global-id` - The global FPGA image identifier (AGFI ID).
+  `name` - The name of the AFI.
+  `owner-id` - The AWS account ID of the AFI owner.
+  `product-code` - The product code.
+  `shell-version` - The version of the AWS Shell that was used to create the bitstream.
+  `state` - The state of the AFI (`pending` \| `failed` \| `available` \| `unavailable`).
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `update-time` - The time of the most recent update.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **FpgaImageId.N**
The AFI IDs.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token to retrieve the next page of results.
Type: String
Required: No

 **Owner.N**
Filters the AFI by owner. Specify an AWS account ID, `self` (owner is the sender of the request), or an AWS owner alias (valid values are `amazon` \| `aws-marketplace`).
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeFpgaImages_ResponseElements"></a>

The following elements are returned by the service.

 **fpgaImageSet**
Information about the FPGA images.
Type: Array of [FpgaImage](API_FpgaImage.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeFpgaImages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeFpgaImages_Examples"></a>

### Example
<a name="API_DescribeFpgaImages_Example_1"></a>

This example describes AFIs that are owned by account `123456789012`.

#### Sample Request
<a name="API_DescribeFpgaImages_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeFpgaImages
&Filter.1.Name=owner-id
&Filter.1.Value.1=123456789012
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeFpgaImages_Example_1_Response"></a>

```
<DescribeFpgaImagesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>c984bf72-784e-43b0-be87-d7903example</requestId>
    <fpgaImageSet>
        <item>
            <createTime>2017-12-22T11:43:33.000Z</createTime>
            <description>my-afi</description>
            <fpgaImageGlobalId>agfi-05fabc8e7fcca8abc</fpgaImageGlobalId>
            <fpgaImageId>afi-0feabc187988f4abc</fpgaImageId>
            <public>false</public>
            <name>my-afi</name>
            <ownerId>123456789012</ownerId>
            <pciId>
                <DeviceId>0xf000</DeviceId>
                <SubsystemId>0x1d51</SubsystemId>
                <SubsystemVendorId>0xfedd</SubsystemVendorId>
                <VendorId>0x1d0f</VendorId>
            </pciId>
            <shellVersion>0x071417d3</shellVersion>
            <state>
                <code>available</code>
            </state>
            <updateTime>2017-12-22T12:09:14.000Z</updateTime>
        </item>
        <item>
            <createTime>2017-12-22T11:44:54.000Z</createTime>
            <description>my-afi-2</description>
            <fpgaImageGlobalId>agfi-0312327b5e84a0123</fpgaImageGlobalId>
            <fpgaImageId>afi-0d0123214bfc85123</fpgaImageId>
            <public>false</public>
            <name>my-afi-2</name>
            <ownerId>123456789012</ownerId>
            <pciId>
                <DeviceId>0xf000</DeviceId>
                <SubsystemId>0x1d51</SubsystemId>
                <SubsystemVendorId>0xfedd</SubsystemVendorId>
                <VendorId>0x1d0f</VendorId>
            </pciId>
            <shellVersion>0x071417d3</shellVersion>
            <state>
                <code>available</code>
            </state>
            <updateTime>2017-12-22T12:10:24.000Z</updateTime>
        </item>
    </fpgaImageSet>
</DescribeFpgaImagesResponse>
```

## See Also
<a name="API_DescribeFpgaImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeFpgaImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeFpgaImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeFpgaImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeFpgaImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeFpgaImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeFpgaImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeFpgaImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeFpgaImages)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeFpgaImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeFpgaImages)
