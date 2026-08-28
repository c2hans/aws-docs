---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateMissionProfile.html
---

# CreateMissionProfile
<a name="API_CreateMissionProfile"></a>

Creates a mission profile.

 `dataflowEdges` is a list of lists of strings. Each lower level list of strings has two elements: a *from* ARN and a *to* ARN.

## Request Syntax
<a name="API_CreateMissionProfile_RequestSyntax"></a>

```
POST /missionprofile HTTP/1.1
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
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "telemetrySinkConfigArn": "{{string}}",
   "trackingConfigArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateMissionProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMissionProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [contactPostPassDurationSeconds](#API_CreateMissionProfile_RequestSyntax) **   <a name="groundstation-CreateMissionProfile-request-contactPostPassDurationSeconds"></a>
Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 21600.
Required: No

 ** [contactPrePassDurationSeconds](#API_CreateMissionProfile_RequestSyntax) **   <a name="groundstation-CreateMissionProfile-request-contactPrePassDurationSeconds"></a>
Amount of time prior to contact start you'd like to receive a Ground Station Contact State Change event indicating an upcoming pass.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 21600.
Required: No

 ** [dataflowEdges](#API_CreateMissionProfile_RequestSyntax) **   <a name="groundstation-CreateMissionProfile-request-dataflowEdges"></a>
A list of lists of ARNs. Each list of ARNs is an edge, with a *from* ` Config` and a *to* `Config`.
Type: Array of arrays of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Array Members: Fixed number of 2 items.
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`
Required: Yes

 ** [minimumViableContactDurationSeconds](#API_CreateMissionProfile_RequestSyntax) **   <a name="groundstation-CreateMissionProfile-request-minimumViableContactDurationSeconds"></a>
Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 21600.
Required: Yes

 ** [name](#API_CreateMissionProfile_RequestSyntax) **   <a name="groundstation-CreateMissionProfile-request-name"></a>
Name of a mission profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: Yes

 ** [streamsKmsKey](#API_CreateMissionProfile_RequestSyntax) **   <a name="groundstation-CreateMissionProfile-request-streamsKmsKey"></a>
KMS key to use for encrypting streams.
Type: [KmsKey](API_KmsKey.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [streamsKmsRole](#API_CreateMissionProfile_RequestSyntax) **   <a name="groundstation-CreateMissionProfile-request-streamsKmsRole"></a>
Role to use for encrypting streams with KMS key.
Type: String
Length Constraints: Minimum length of 30. Maximum length of 165.
Pattern: `arn:[a-z0-9-.]{1,63}:iam::[0-9]{12}:role/[\w+=,.@-]{1,64}`
Required: No

 ** [tags](#API_CreateMissionProfile_RequestSyntax) **   <a name="groundstation-CreateMissionProfile-request-tags"></a>
Tags assigned to a mission profile.
Type: String to string map
Required: No

 ** [telemetrySinkConfigArn](#API_CreateMissionProfile_RequestSyntax) **   <a name="groundstation-CreateMissionProfile-request-telemetrySinkConfigArn"></a>
ARN of a telemetry sink `Config`.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`
Required: No

 ** [trackingConfigArn](#API_CreateMissionProfile_RequestSyntax) **   <a name="groundstation-CreateMissionProfile-request-trackingConfigArn"></a>
ARN of a tracking `Config`.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`
Required: Yes

## Response Syntax
<a name="API_CreateMissionProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "missionProfileId": "string"
}
```

## Response Elements
<a name="API_CreateMissionProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [missionProfileId](#API_CreateMissionProfile_ResponseSyntax) **   <a name="groundstation-CreateMissionProfile-response-missionProfileId"></a>
UUID of a mission profile.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_CreateMissionProfile_Errors"></a>

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
<a name="API_CreateMissionProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/CreateMissionProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/CreateMissionProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/CreateMissionProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/CreateMissionProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/CreateMissionProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/CreateMissionProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/CreateMissionProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/CreateMissionProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/CreateMissionProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/CreateMissionProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
