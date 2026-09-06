---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeHub.html
---

# DescribeHub
<a name="API_DescribeHub"></a>

Describes a hub.

## Request Syntax
<a name="API_DescribeHub_RequestSyntax"></a>

```
{
   "HubName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeHub_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HubName](#API_DescribeHub_RequestSyntax) **   <a name="sagemaker-DescribeHub-request-HubName"></a>
The name of the hub to describe.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeHub_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "FailureReason": "string",
   "HubArn": "string",
   "HubDescription": "string",
   "HubDisplayName": "string",
   "HubName": "string",
   "HubSearchKeywords": [ "string" ],
   "HubStatus": "string",
   "LastModifiedTime": number,
   "S3StorageConfig": {
      "S3OutputPath": "string"
   }
}
```

## Response Elements
<a name="API_DescribeHub_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeHub_ResponseSyntax) **   <a name="sagemaker-DescribeHub-response-CreationTime"></a>
The date and time that the hub was created.
Type: Timestamp

 ** [FailureReason](#API_DescribeHub_ResponseSyntax) **   <a name="sagemaker-DescribeHub-response-FailureReason"></a>
The failure reason if importing hub content failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [HubArn](#API_DescribeHub_ResponseSyntax) **   <a name="sagemaker-DescribeHub-response-HubArn"></a>
The Amazon Resource Name (ARN) of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [HubDescription](#API_DescribeHub_ResponseSyntax) **   <a name="sagemaker-DescribeHub-response-HubDescription"></a>
A description of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `.*`

 ** [HubDisplayName](#API_DescribeHub_ResponseSyntax) **   <a name="sagemaker-DescribeHub-response-HubDisplayName"></a>
The display name of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [HubName](#API_DescribeHub_ResponseSyntax) **   <a name="sagemaker-DescribeHub-response-HubName"></a>
The name of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [HubSearchKeywords](#API_DescribeHub_ResponseSyntax) **   <a name="sagemaker-DescribeHub-response-HubSearchKeywords"></a>
The searchable keywords for the hub.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[^A-Z]*`

 ** [HubStatus](#API_DescribeHub_ResponseSyntax) **   <a name="sagemaker-DescribeHub-response-HubStatus"></a>
The status of the hub.
Type: String
Valid Values: `InService | Creating | Updating | Deleting | CreateFailed | UpdateFailed | DeleteFailed`

 ** [LastModifiedTime](#API_DescribeHub_ResponseSyntax) **   <a name="sagemaker-DescribeHub-response-LastModifiedTime"></a>
The date and time that the hub was last modified.
Type: Timestamp

 ** [S3StorageConfig](#API_DescribeHub_ResponseSyntax) **   <a name="sagemaker-DescribeHub-response-S3StorageConfig"></a>
The Amazon S3 storage configuration for the hub.
Type: [HubS3StorageConfig](API_HubS3StorageConfig.md) object

## Errors
<a name="API_DescribeHub_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeHub_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeHub)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeHub)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeHub)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeHub)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeHub)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeHub)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeHub)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeHub)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeHub)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeHub)
