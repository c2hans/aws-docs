---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSpotDatafeedSubscription.html
---

# CreateSpotDatafeedSubscription
<a name="API_CreateSpotDatafeedSubscription"></a>

Creates a data feed for Spot Instances, enabling you to view Spot Instance usage logs. You can create one data feed per AWS account. For more information, see [Spot Instance data feed](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateSpotDatafeedSubscription_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Bucket**
The name of the Amazon S3 bucket in which to store the Spot Instance data feed. For more information about bucket names, see [Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) in the *Amazon S3 User Guide*.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Prefix**
The prefix for the data feed file names.
Type: String
Required: No

## Response Elements
<a name="API_CreateSpotDatafeedSubscription_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **spotDatafeedSubscription**
The Spot Instance data feed subscription.
Type: [SpotDatafeedSubscription](API_SpotDatafeedSubscription.md) object

## Errors
<a name="API_CreateSpotDatafeedSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateSpotDatafeedSubscription_Examples"></a>

### Example
<a name="API_CreateSpotDatafeedSubscription_Example_1"></a>

This example creates a Spot Instance data feed for the account.

#### Sample Request
<a name="API_CreateSpotDatafeedSubscription_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateSpotDatafeedSubscription
&Bucket=amzn-s3-demo-bucket
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateSpotDatafeedSubscription_Example_1_Response"></a>

```
<CreateSpotDatafeedSubscriptionResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <spotDatafeedSubscription>
    <ownerId>123456789012</ownerId>
    <bucket>amzn-s3-demo-bucket</bucket>
    <prefix>spotdata_</prefix>
    <state>Active</state>
  </spotDatafeedSubscription>
</CreateSpotDatafeedSubscriptionResponse>
```

## See Also
<a name="API_CreateSpotDatafeedSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateSpotDatafeedSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateSpotDatafeedSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateSpotDatafeedSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateSpotDatafeedSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateSpotDatafeedSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateSpotDatafeedSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateSpotDatafeedSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateSpotDatafeedSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateSpotDatafeedSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateSpotDatafeedSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
