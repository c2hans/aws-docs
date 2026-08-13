---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDlpSetting.html
---

# DescribeDlpSetting
<a name="API_DescribeDlpSetting"></a>

Describes the full configuration of a DLP setting in an AWS account.

## Request Syntax
<a name="API_DescribeDlpSetting_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/data-loss-prevention/settings/{{DlpSettingId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDlpSetting_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeDlpSetting_RequestSyntax) **   <a name="QS-DescribeDlpSetting-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the DLP setting that you want to describe.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DlpSettingId](#API_DescribeDlpSetting_RequestSyntax) **   <a name="QS-DescribeDlpSetting-request-uri-DlpSettingId"></a>
The ID of the DLP setting that you want to describe.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\-_]+`
Required: Yes

## Request Body
<a name="API_DescribeDlpSetting_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDlpSetting_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DlpSetting": {
      "Arn": "string",
      "CreatedAt": number,
      "DlpSettingId": "string",
      "Name": "string",
      "ProviderConfig": { ... },
      "ProviderOutageAction": "string",
      "ProviderType": "string",
      "Status": "string",
      "UpdatedAt": number
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeDlpSetting_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DlpSetting](#API_DescribeDlpSetting_ResponseSyntax) **   <a name="QS-DescribeDlpSetting-response-DlpSetting"></a>
The full configuration of the requested DLP setting, returned as a `DlpSettingDetails` object.
Type: [DlpSettingDetails](API_DlpSettingDetails.md) object

 ** [RequestId](#API_DescribeDlpSetting_ResponseSyntax) **   <a name="QS-DescribeDlpSetting-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_DescribeDlpSetting_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidRequestException **
You don't have this feature activated for your account. To fix this issue, contact AWS support.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_DescribeDlpSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeDlpSetting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeDlpSetting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeDlpSetting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeDlpSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeDlpSetting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeDlpSetting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeDlpSetting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeDlpSetting)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeDlpSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeDlpSetting)
