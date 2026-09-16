---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeSubscribedWorkteam.html
---

# DescribeSubscribedWorkteam
<a name="API_DescribeSubscribedWorkteam"></a>

Gets information about a work team provided by a vendor. It returns details about the subscription with a vendor in the AWS Marketplace.

## Request Syntax
<a name="API_DescribeSubscribedWorkteam_RequestSyntax"></a>

```
{
   "WorkteamArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSubscribedWorkteam_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WorkteamArn](#API_DescribeSubscribedWorkteam_RequestSyntax) **   <a name="sagemaker-DescribeSubscribedWorkteam-request-WorkteamArn"></a>
The Amazon Resource Name (ARN) of the subscribed work team to describe.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:workteam/.*`
Required: Yes

## Response Syntax
<a name="API_DescribeSubscribedWorkteam_ResponseSyntax"></a>

```
{
   "SubscribedWorkteam": {
      "ListingId": "string",
      "MarketplaceDescription": "string",
      "MarketplaceTitle": "string",
      "SellerName": "string",
      "WorkteamArn": "string"
   }
}
```

## Response Elements
<a name="API_DescribeSubscribedWorkteam_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SubscribedWorkteam](#API_DescribeSubscribedWorkteam_ResponseSyntax) **   <a name="sagemaker-DescribeSubscribedWorkteam-response-SubscribedWorkteam"></a>
A `Workteam` instance that contains information about the work team.
Type: [SubscribedWorkteam](API_SubscribedWorkteam.md) object

## Errors
<a name="API_DescribeSubscribedWorkteam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeSubscribedWorkteam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeSubscribedWorkteam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeSubscribedWorkteam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeSubscribedWorkteam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeSubscribedWorkteam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeSubscribedWorkteam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeSubscribedWorkteam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeSubscribedWorkteam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeSubscribedWorkteam)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeSubscribedWorkteam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeSubscribedWorkteam)
