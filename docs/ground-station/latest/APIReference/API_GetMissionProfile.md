---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetMissionProfile.html
---

# GetMissionProfile
<a name="API_GetMissionProfile"></a>

Returns a mission profile.

## Request Syntax
<a name="API_GetMissionProfile_RequestSyntax"></a>

```
GET /missionprofile/{{missionProfileId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMissionProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [missionProfileId](#API_GetMissionProfile_RequestSyntax) **   <a name="groundstation-GetMissionProfile-request-uri-missionProfileId"></a>
UUID of a mission profile.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_GetMissionProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMissionProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "contactPostPassDurationSeconds": number,
   "contactPrePassDurationSeconds": number,
   "dataflowEdges": [
      [ "string" ]
   ],
   "minimumViableContactDurationSeconds": number,
   "missionProfileArn": "string",
   "missionProfileId": "string",
   "name": "string",
   "region": "string",
   "streamsKmsKey": { ... },
   "streamsKmsRole": "string",
   "tags": {
      "string" : "string"
   },
   "telemetrySinkConfigArn": "string",
   "trackingConfigArn": "string"
}
```

## Response Elements
<a name="API_GetMissionProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contactPostPassDurationSeconds](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-contactPostPassDurationSeconds"></a>
Amount of time after a contact ends that you'd like to receive a CloudWatch event indicating the pass has finished.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 21600.

 ** [contactPrePassDurationSeconds](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-contactPrePassDurationSeconds"></a>
Amount of time prior to contact start you'd like to receive a CloudWatch event indicating an upcoming pass.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 21600.

 ** [dataflowEdges](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-dataflowEdges"></a>
A list of lists of ARNs. Each list of ARNs is an edge, with a *from* ` Config` and a *to* `Config`.
Type: Array of arrays of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Array Members: Fixed number of 2 items.
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`

 ** [minimumViableContactDurationSeconds](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-minimumViableContactDurationSeconds"></a>
Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 21600.

 ** [missionProfileArn](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-missionProfileArn"></a>
ARN of a mission profile.
Type: String
Length Constraints: Minimum length of 89. Maximum length of 138.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:mission-profile/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [missionProfileId](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-missionProfileId"></a>
UUID of a mission profile.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-name"></a>
Name of a mission profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`

 ** [region](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-region"></a>
Region of a mission profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w-]+`

 ** [streamsKmsKey](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-streamsKmsKey"></a>
KMS key to use for encrypting streams.
Type: [KmsKey](API_KmsKey.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [streamsKmsRole](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-streamsKmsRole"></a>
Role to use for encrypting streams with KMS key.
Type: String
Length Constraints: Minimum length of 30. Maximum length of 165.
Pattern: `arn:[a-z0-9-.]{1,63}:iam::[0-9]{12}:role/[\w+=,.@-]{1,64}`

 ** [tags](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-tags"></a>
Tags assigned to a mission profile.
Type: String to string map

 ** [telemetrySinkConfigArn](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-telemetrySinkConfigArn"></a>
ARN of a telemetry sink `Config`.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`

 ** [trackingConfigArn](#API_GetMissionProfile_ResponseSyntax) **   <a name="groundstation-GetMissionProfile-response-trackingConfigArn"></a>
ARN of a tracking `Config`.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`

## Errors
<a name="API_GetMissionProfile_Errors"></a>

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
<a name="API_GetMissionProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/GetMissionProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/GetMissionProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/GetMissionProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/GetMissionProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/GetMissionProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/GetMissionProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/GetMissionProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/GetMissionProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/GetMissionProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/GetMissionProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
