---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetAudienceModel.html
---

# GetAudienceModel
<a name="API_GetAudienceModel"></a>

Returns information about an audience model

## Request Syntax
<a name="API_GetAudienceModel_RequestSyntax"></a>

```
GET /audience-model/{{audienceModelArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAudienceModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [audienceModelArn](#API_GetAudienceModel_RequestSyntax) **   <a name="API-GetAudienceModel-request-uri-audienceModelArn"></a>
The Amazon Resource Name (ARN) of the audience model that you are interested in.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_GetAudienceModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAudienceModel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "audienceModelArn": "string",
   "createTime": "string",
   "description": "string",
   "kmsKeyArn": "string",
   "name": "string",
   "status": "string",
   "statusDetails": {
      "message": "string",
      "statusCode": "string"
   },
   "tags": {
      "string" : "string"
   },
   "trainingDataEndTime": "string",
   "trainingDatasetArn": "string",
   "trainingDataStartTime": "string",
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetAudienceModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [audienceModelArn](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-audienceModelArn"></a>
The Amazon Resource Name (ARN) of the audience model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-model/[-a-zA-Z0-9_/.]+`

 ** [createTime](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-createTime"></a>
The time at which the audience model was created.
Type: Timestamp

 ** [description](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-description"></a>
The description of the audience model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`

 ** [kmsKeyArn](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-kmsKeyArn"></a>
The KMS key ARN used for the audience model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/.+`

 ** [name](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-name"></a>
The name of the audience model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`

 ** [status](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-status"></a>
The status of the audience model.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_FAILED`

 ** [statusDetails](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-statusDetails"></a>
Details about the status of the audience model.
Type: [StatusDetails](API_StatusDetails.md) object

 ** [tags](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-tags"></a>
The tags that are assigned to the audience model.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [trainingDataEndTime](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-trainingDataEndTime"></a>
The end date specified for the training window.
Type: Timestamp

 ** [trainingDatasetArn](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-trainingDatasetArn"></a>
The Amazon Resource Name (ARN) of the training dataset that was used for this audience model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:training-dataset/[-a-zA-Z0-9_/.]+`

 ** [trainingDataStartTime](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-trainingDataStartTime"></a>
The start date specified for the training window.
Type: Timestamp

 ** [updateTime](#API_GetAudienceModel_ResponseSyntax) **   <a name="API-GetAudienceModel-response-updateTime"></a>
The most recent time at which the audience model was updated.
Type: Timestamp

## Errors
<a name="API_GetAudienceModel_Errors"></a>

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
<a name="API_GetAudienceModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetAudienceModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetAudienceModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetAudienceModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetAudienceModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetAudienceModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetAudienceModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetAudienceModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetAudienceModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetAudienceModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetAudienceModel)
