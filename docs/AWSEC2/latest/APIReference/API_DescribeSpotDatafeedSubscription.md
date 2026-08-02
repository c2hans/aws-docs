---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotDatafeedSubscription.html
---

# DescribeSpotDatafeedSubscription
<a name="API_DescribeSpotDatafeedSubscription"></a>

Describes the data feed for Spot Instances. For more information, see [Spot Instance data feed](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeSpotDatafeedSubscription_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DescribeSpotDatafeedSubscription_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **spotDatafeedSubscription**
The Spot Instance data feed subscription.
Type: [SpotDatafeedSubscription](API_SpotDatafeedSubscription.md) object

## Errors
<a name="API_DescribeSpotDatafeedSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeSpotDatafeedSubscription_Examples"></a>

### Example
<a name="API_DescribeSpotDatafeedSubscription_Example_1"></a>

This example describes the data feed for the account.

#### Sample Request
<a name="API_DescribeSpotDatafeedSubscription_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSpotDatafeedSubscription
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeSpotDatafeedSubscription_Example_1_Response"></a>

```
<DescribeSpotDatafeedSubscriptionResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <spotDatafeedSubscription>
      <ownerId>123456789012</ownerId>
      <bucket>amzn-s3-demo-bucket</bucket>
      <prefix>spotdata_</prefix>
      <state>Active</state>
   </spotDatafeedSubscription>
</DescribeSpotDatafeedSubscriptionResponse>
```

## See Also
<a name="API_DescribeSpotDatafeedSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeSpotDatafeedSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeSpotDatafeedSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeSpotDatafeedSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeSpotDatafeedSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeSpotDatafeedSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeSpotDatafeedSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeSpotDatafeedSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeSpotDatafeedSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeSpotDatafeedSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeSpotDatafeedSubscription)
