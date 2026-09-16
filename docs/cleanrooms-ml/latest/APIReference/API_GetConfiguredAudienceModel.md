---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetConfiguredAudienceModel.html
---

# GetConfiguredAudienceModel
<a name="API_GetConfiguredAudienceModel"></a>

Returns information about a specified configured audience model.

## Request Syntax
<a name="API_GetConfiguredAudienceModel_RequestSyntax"></a>

```
GET /configured-audience-model/{{configuredAudienceModelArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfiguredAudienceModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configuredAudienceModelArn](#API_GetConfiguredAudienceModel_RequestSyntax) **   <a name="API-GetConfiguredAudienceModel-request-uri-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model that you are interested in.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_GetConfiguredAudienceModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfiguredAudienceModel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "audienceModelArn": "string",
   "audienceSizeConfig": {
      "audienceSizeBins": [ number ],
      "audienceSizeType": "string"
   },
   "childResourceTagOnCreatePolicy": "string",
   "configuredAudienceModelArn": "string",
   "createTime": "string",
   "description": "string",
   "minMatchingSeedSize": number,
   "name": "string",
   "outputConfig": {
      "destination": {
         "s3Destination": {
            "s3Uri": "string"
         }
      },
      "roleArn": "string"
   },
   "sharedAudienceMetrics": [ "string" ],
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetConfiguredAudienceModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [audienceModelArn](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-audienceModelArn"></a>
The Amazon Resource Name (ARN) of the audience model used for this configured audience model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-model/[-a-zA-Z0-9_/.]+`

 ** [audienceSizeConfig](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-audienceSizeConfig"></a>
The list of output sizes of audiences that can be created using this configured audience model. A request to [StartAudienceGenerationJob](API_StartAudienceGenerationJob.md) that uses this configured audience model must have an `audienceSize` selected from this list. You can use the `ABSOLUTE` [AudienceSize](API_AudienceSize.md) to configure out audience sizes using the count of identifiers in the output. You can use the `Percentage` [AudienceSize](API_AudienceSize.md) to configure sizes in the range 1-100 percent.
Type: [AudienceSizeConfig](API_AudienceSizeConfig.md) object

 ** [childResourceTagOnCreatePolicy](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-childResourceTagOnCreatePolicy"></a>
Provides the `childResourceTagOnCreatePolicy` that was used for this configured audience model.
Type: String
Valid Values: `FROM_PARENT_RESOURCE | NONE`

 ** [configuredAudienceModelArn](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`

 ** [createTime](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-createTime"></a>
The time at which the configured audience model was created.
Type: Timestamp

 ** [description](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-description"></a>
The description of the configured audience model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`

 ** [minMatchingSeedSize](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-minMatchingSeedSize"></a>
The minimum number of users from the seed audience that must match with users in the training data of the audience model.
Type: Integer
Valid Range: Minimum value of 25. Maximum value of 500000.

 ** [name](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-name"></a>
The name of the configured audience model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`

 ** [outputConfig](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-outputConfig"></a>
The output configuration of the configured audience model
Type: [ConfiguredAudienceModelOutputConfig](API_ConfiguredAudienceModelOutputConfig.md) object

 ** [sharedAudienceMetrics](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-sharedAudienceMetrics"></a>
Whether audience metrics are shared.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ALL | NONE`

 ** [status](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-status"></a>
The status of the configured audience model.
Type: String
Valid Values: `ACTIVE`

 ** [tags](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-tags"></a>
The tags that are associated to this configured audience model.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updateTime](#API_GetConfiguredAudienceModel_ResponseSyntax) **   <a name="API-GetConfiguredAudienceModel-response-updateTime"></a>
The most recent time at which the configured audience model was updated.
Type: Timestamp

## Errors
<a name="API_GetConfiguredAudienceModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The resource you are requesting does not exist.
HTTP Status Code: 404

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_GetConfiguredAudienceModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetConfiguredAudienceModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetConfiguredAudienceModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetConfiguredAudienceModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetConfiguredAudienceModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetConfiguredAudienceModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetConfiguredAudienceModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetConfiguredAudienceModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetConfiguredAudienceModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetConfiguredAudienceModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetConfiguredAudienceModel)
