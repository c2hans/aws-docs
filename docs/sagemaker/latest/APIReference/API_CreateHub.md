---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHub.html
---

# CreateHub
<a name="API_CreateHub"></a>

Create a hub.

## Request Syntax
<a name="API_CreateHub_RequestSyntax"></a>

```
{
   "HubDescription": "{{string}}",
   "HubDisplayName": "{{string}}",
   "HubName": "{{string}}",
   "HubSearchKeywords": [ "{{string}}" ],
   "S3StorageConfig": {
      "S3OutputPath": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateHub_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HubDescription](#API_CreateHub_RequestSyntax) **   <a name="sagemaker-CreateHub-request-HubDescription"></a>
A description of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `.*`
Required: Yes

 ** [HubDisplayName](#API_CreateHub_RequestSyntax) **   <a name="sagemaker-CreateHub-request-HubDisplayName"></a>
The display name of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [HubName](#API_CreateHub_RequestSyntax) **   <a name="sagemaker-CreateHub-request-HubName"></a>
The name of the hub to create.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [HubSearchKeywords](#API_CreateHub_RequestSyntax) **   <a name="sagemaker-CreateHub-request-HubSearchKeywords"></a>
The searchable keywords for the hub.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[^A-Z]*`
Required: No

 ** [S3StorageConfig](#API_CreateHub_RequestSyntax) **   <a name="sagemaker-CreateHub-request-S3StorageConfig"></a>
The Amazon S3 storage configuration for the hub.
Type: [HubS3StorageConfig](API_HubS3StorageConfig.md) object
Required: No

 ** [Tags](#API_CreateHub_RequestSyntax) **   <a name="sagemaker-CreateHub-request-Tags"></a>
Any tags to associate with the hub.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateHub_ResponseSyntax"></a>

```
{
   "HubArn": "string"
}
```

## Response Elements
<a name="API_CreateHub_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HubArn](#API_CreateHub_ResponseSyntax) **   <a name="sagemaker-CreateHub-response-HubArn"></a>
The Amazon Resource Name (ARN) of the hub.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

## Errors
<a name="API_CreateHub_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateHub_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateHub)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateHub)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateHub)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateHub)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateHub)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateHub)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateHub)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateHub)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateHub)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateHub)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
