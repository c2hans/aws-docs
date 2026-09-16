---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeApplication.html
---

# DescribeApplication
<a name="API_DescribeApplication"></a>

Describes the application.

## Request Syntax
<a name="API_DescribeApplication_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "ResourceGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_DescribeApplication_RequestSyntax) **   <a name="appinsights-DescribeApplication-request-AccountId"></a>
The AWS account ID for the resource group owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [ResourceGroupName](#API_DescribeApplication_RequestSyntax) **   <a name="appinsights-DescribeApplication-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

## Response Syntax
<a name="API_DescribeApplication_ResponseSyntax"></a>

```
{
   "ApplicationInfo": {
      "AccountId": "string",
      "AttachMissingPermission": boolean,
      "AutoConfigEnabled": boolean,
      "CWEMonitorEnabled": boolean,
      "DiscoveryType": "string",
      "LifeCycle": "string",
      "OpsCenterEnabled": boolean,
      "OpsItemSNSTopicArn": "string",
      "Remarks": "string",
      "ResourceGroupName": "string",
      "SNSNotificationArn": "string"
   }
}
```

## Response Elements
<a name="API_DescribeApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationInfo](#API_DescribeApplication_ResponseSyntax) **   <a name="appinsights-DescribeApplication-response-ApplicationInfo"></a>
Information about the application.
Type: [ApplicationInfo](API_ApplicationInfo.md) object

## Errors
<a name="API_DescribeApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist in the customer account.
HTTP Status Code: 400

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/DescribeApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/DescribeApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/DescribeApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/DescribeApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/DescribeApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/DescribeApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/DescribeApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/DescribeApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/DescribeApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/DescribeApplication)
