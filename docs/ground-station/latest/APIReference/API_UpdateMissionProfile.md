---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateMissionProfile.html
---

# UpdateMissionProfile
<a name="API_UpdateMissionProfile"></a>

Updates a mission profile.

Updating a mission profile will not update the execution parameters for existing future contacts.

## Request Syntax
<a name="API_UpdateMissionProfile_RequestSyntax"></a>

```
PUT /missionprofile/{{missionProfileId}} HTTP/1.1
Content-type: application/json

{
   "contactPostPassDurationSeconds": {{number}},
   "contactPrePassDurationSeconds": {{number}},
   "dataflowEdges": [
      [ "{{string}}" ]
   ],
   "minimumViableContactDurationSeconds": {{number}},
   "name": "{{string}}",
   "streamsKmsKey": { ... },
   "streamsKmsRole": "{{string}}",
   "telemetrySinkConfigArn": "{{string}}",
   "trackingConfigArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateMissionProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [missionProfileId](#API_UpdateMissionProfile_RequestSyntax) **   <a name="groundstation-UpdateMissionProfile-request-uri-missionProfileId"></a>
UUID of a mission profile.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_UpdateMissionProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [contactPostPassDurationSeconds](#API_UpdateMissionProfile_RequestSyntax) **   <a name="groundstation-UpdateMissionProfile-request-contactPostPassDurationSeconds"></a>
Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 21600.
Required: No

 ** [contactPrePassDurationSeconds](#API_UpdateMissionProfile_RequestSyntax) **   <a name="groundstation-UpdateMissionProfile-request-contactPrePassDurationSeconds"></a>
Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 21600.
Required: No

 ** [dataflowEdges](#API_UpdateMissionProfile_RequestSyntax) **   <a name="groundstation-UpdateMissionProfile-request-dataflowEdges"></a>
A list of lists of ARNs. Each list of ARNs is an edge, with a *from* ` Config` and a *to* `Config`.
Type: Array of arrays of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Array Members: Fixed number of 2 items.
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`
Required: No

 ** [minimumViableContactDurationSeconds](#API_UpdateMissionProfile_RequestSyntax) **   <a name="groundstation-UpdateMissionProfile-request-minimumViableContactDurationSeconds"></a>
Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 21600.
Required: No

 ** [name](#API_UpdateMissionProfile_RequestSyntax) **   <a name="groundstation-UpdateMissionProfile-request-name"></a>
Name of a mission profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: No

 ** [streamsKmsKey](#API_UpdateMissionProfile_RequestSyntax) **   <a name="groundstation-UpdateMissionProfile-request-streamsKmsKey"></a>
KMS key to use for encrypting streams.
Type: [KmsKey](API_KmsKey.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [streamsKmsRole](#API_UpdateMissionProfile_RequestSyntax) **   <a name="groundstation-UpdateMissionProfile-request-streamsKmsRole"></a>
Role to use for encrypting streams with KMS key.
Type: String
Length Constraints: Minimum length of 30. Maximum length of 165.
Pattern: `arn:[a-z0-9-.]{1,63}:iam::[0-9]{12}:role/[\w+=,.@-]{1,64}`
Required: No

 ** [telemetrySinkConfigArn](#API_UpdateMissionProfile_RequestSyntax) **   <a name="groundstation-UpdateMissionProfile-request-telemetrySinkConfigArn"></a>
ARN of a telemetry sink `Config`.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`
Required: No

 ** [trackingConfigArn](#API_UpdateMissionProfile_RequestSyntax) **   <a name="groundstation-UpdateMissionProfile-request-trackingConfigArn"></a>
ARN of a tracking `Config`.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`
Required: No

## Response Syntax
<a name="API_UpdateMissionProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "missionProfileId": "string"
}
```

## Response Elements
<a name="API_UpdateMissionProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [missionProfileId](#API_UpdateMissionProfile_ResponseSyntax) **   <a name="groundstation-UpdateMissionProfile-response-missionProfileId"></a>
UUID of a mission profile.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_UpdateMissionProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_UpdateMissionProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/UpdateMissionProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/UpdateMissionProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/UpdateMissionProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/UpdateMissionProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/UpdateMissionProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/UpdateMissionProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/UpdateMissionProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/UpdateMissionProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/UpdateMissionProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/UpdateMissionProfile)
