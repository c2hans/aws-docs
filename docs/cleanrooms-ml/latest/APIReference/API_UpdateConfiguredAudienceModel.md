---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_UpdateConfiguredAudienceModel.html
---

# UpdateConfiguredAudienceModel
<a name="API_UpdateConfiguredAudienceModel"></a>

Provides the information necessary to update a configured audience model. Updates that impact audience generation jobs take effect when a new job starts, but do not impact currently running jobs.

## Request Syntax
<a name="API_UpdateConfiguredAudienceModel_RequestSyntax"></a>

```
PATCH /configured-audience-model/{{configuredAudienceModelArn}} HTTP/1.1
Content-type: application/json

{
   "audienceModelArn": "{{string}}",
   "audienceSizeConfig": {
      "audienceSizeBins": [ {{number}} ],
      "audienceSizeType": "{{string}}"
   },
   "description": "{{string}}",
   "minMatchingSeedSize": {{number}},
   "outputConfig": {
      "destination": {
         "s3Destination": {
            "s3Uri": "{{string}}"
         }
      },
      "roleArn": "{{string}}"
   },
   "sharedAudienceMetrics": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateConfiguredAudienceModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configuredAudienceModelArn](#API_UpdateConfiguredAudienceModel_RequestSyntax) **   <a name="API-UpdateConfiguredAudienceModel-request-uri-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model that you want to update.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_UpdateConfiguredAudienceModel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [audienceModelArn](#API_UpdateConfiguredAudienceModel_RequestSyntax) **   <a name="API-UpdateConfiguredAudienceModel-request-audienceModelArn"></a>
The Amazon Resource Name (ARN) of the new audience model that you want to use.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-model/[-a-zA-Z0-9_/.]+`
Required: No

 ** [audienceSizeConfig](#API_UpdateConfiguredAudienceModel_RequestSyntax) **   <a name="API-UpdateConfiguredAudienceModel-request-audienceSizeConfig"></a>
The new audience size configuration.
Type: [AudienceSizeConfig](API_AudienceSizeConfig.md) object
Required: No

 ** [description](#API_UpdateConfiguredAudienceModel_RequestSyntax) **   <a name="API-UpdateConfiguredAudienceModel-request-description"></a>
The new description of the configured audience model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [minMatchingSeedSize](#API_UpdateConfiguredAudienceModel_RequestSyntax) **   <a name="API-UpdateConfiguredAudienceModel-request-minMatchingSeedSize"></a>
The minimum number of users from the seed audience that must match with users in the training data of the audience model.
Type: Integer
Valid Range: Minimum value of 25. Maximum value of 500000.
Required: No

 ** [outputConfig](#API_UpdateConfiguredAudienceModel_RequestSyntax) **   <a name="API-UpdateConfiguredAudienceModel-request-outputConfig"></a>
The new output configuration.
Type: [ConfiguredAudienceModelOutputConfig](API_ConfiguredAudienceModelOutputConfig.md) object
Required: No

 ** [sharedAudienceMetrics](#API_UpdateConfiguredAudienceModel_RequestSyntax) **   <a name="API-UpdateConfiguredAudienceModel-request-sharedAudienceMetrics"></a>
The new value for whether to share audience metrics.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ALL | NONE`
Required: No

## Response Syntax
<a name="API_UpdateConfiguredAudienceModel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredAudienceModelArn": "string"
}
```

## Response Elements
<a name="API_UpdateConfiguredAudienceModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredAudienceModelArn](#API_UpdateConfiguredAudienceModel_ResponseSyntax) **   <a name="API-UpdateConfiguredAudienceModel-response-configuredAudienceModelArn"></a>
The Amazon Resource Name (ARN) of the configured audience model that was updated.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`

## Errors
<a name="API_UpdateConfiguredAudienceModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
You can't complete this action because another resource depends on this resource.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The resource you are requesting does not exist.
HTTP Status Code: 404

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_UpdateConfiguredAudienceModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/UpdateConfiguredAudienceModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/UpdateConfiguredAudienceModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/UpdateConfiguredAudienceModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/UpdateConfiguredAudienceModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/UpdateConfiguredAudienceModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/UpdateConfiguredAudienceModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/UpdateConfiguredAudienceModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/UpdateConfiguredAudienceModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/UpdateConfiguredAudienceModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/UpdateConfiguredAudienceModel)
