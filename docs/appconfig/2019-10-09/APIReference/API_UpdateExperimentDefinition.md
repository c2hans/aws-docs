---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateExperimentDefinition.html
---

# UpdateExperimentDefinition
<a name="API_UpdateExperimentDefinition"></a>

Updates an experiment definition. You can update treatments, the control, audience rules, and other properties. You cannot update an experiment definition while an experiment run is active.

## Request Syntax
<a name="API_UpdateExperimentDefinition_RequestSyntax"></a>

```
PATCH /applications/{{ApplicationIdentifier}}/experimentdefinitions/{{ExperimentDefinitionIdentifier}} HTTP/1.1
Content-type: application/json

{
   "AudienceDescription": "{{string}}",
   "AudienceRule": "{{string}}",
   "Control": {
      "Description": "{{string}}",
      "FlagValue": {
         "AttributeValues": {
            "{{string}}" : { ... }
         },
         "Enabled": {{boolean}}
      },
      "Weight": {{number}}
   },
   "Hypothesis": "{{string}}",
   "LaunchCriteria": "{{string}}",
   "Treatments": [
      {
         "Description": "{{string}}",
         "FlagValue": {
            "AttributeValues": {
               "{{string}}" : { ... }
            },
            "Enabled": {{boolean}}
         },
         "Weight": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateExperimentDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_UpdateExperimentDefinition_RequestSyntax) **   <a name="appconfig-UpdateExperimentDefinition-request-uri-ApplicationIdentifier"></a>
The application ID or name.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [ExperimentDefinitionIdentifier](#API_UpdateExperimentDefinition_RequestSyntax) **   <a name="appconfig-UpdateExperimentDefinition-request-uri-ExperimentDefinitionIdentifier"></a>
The experiment definition ID or name.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_UpdateExperimentDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AudienceDescription](#API_UpdateExperimentDefinition_RequestSyntax) **   <a name="appconfig-UpdateExperimentDefinition-request-AudienceDescription"></a>
An updated audience description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [AudienceRule](#API_UpdateExperimentDefinition_RequestSyntax) **   <a name="appconfig-UpdateExperimentDefinition-request-AudienceRule"></a>
An updated audience rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

 ** [Control](#API_UpdateExperimentDefinition_RequestSyntax) **   <a name="appconfig-UpdateExperimentDefinition-request-Control"></a>
An updated control treatment.
Type: [TreatmentInput](API_TreatmentInput.md) object
Required: No

 ** [Hypothesis](#API_UpdateExperimentDefinition_RequestSyntax) **   <a name="appconfig-UpdateExperimentDefinition-request-Hypothesis"></a>
An updated hypothesis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [LaunchCriteria](#API_UpdateExperimentDefinition_RequestSyntax) **   <a name="appconfig-UpdateExperimentDefinition-request-LaunchCriteria"></a>
Updated launch criteria.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Treatments](#API_UpdateExperimentDefinition_RequestSyntax) **   <a name="appconfig-UpdateExperimentDefinition-request-Treatments"></a>
The updated list of treatments to evaluate during the experiment. Each treatment defines a distinct variation compared to the control.
Type: Array of [TreatmentInput](API_TreatmentInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## Response Syntax
<a name="API_UpdateExperimentDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationId": "string",
   "AudienceDescription": "string",
   "AudienceRule": "string",
   "ConfigurationProfileId": "string",
   "Control": {
      "Description": "string",
      "FlagValue": {
         "AttributeValues": {
            "string" : { ... }
         },
         "Enabled": boolean
      },
      "Key": "string",
      "Weight": number
   },
   "CreatedAt": "string",
   "EnvironmentId": "string",
   "FlagKey": "string",
   "Hypothesis": "string",
   "Id": "string",
   "KmsKeyIdentifier": "string",
   "LaunchCriteria": "string",
   "Name": "string",
   "Status": "string",
   "Treatments": [
      {
         "Description": "string",
         "FlagValue": {
            "AttributeValues": {
               "string" : { ... }
            },
            "Enabled": boolean
         },
         "Key": "string",
         "Weight": number
      }
   ],
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateExperimentDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [AudienceDescription](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-AudienceDescription"></a>
A description of the intended audience for the experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [AudienceRule](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-AudienceRule"></a>
The rule that defines which users are eligible to be assigned to treatments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.

 ** [ConfigurationProfileId](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-ConfigurationProfileId"></a>
The configuration profile ID associated with the experiment.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Control](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-Control"></a>
The control treatment used as the baseline for comparison.
Type: [Treatment](API_Treatment.md) object

 ** [CreatedAt](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-CreatedAt"></a>
The date and time the experiment definition was created, in ISO 8601 format.
Type: Timestamp

 ** [EnvironmentId](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-EnvironmentId"></a>
The environment ID where the experiment runs.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [FlagKey](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-FlagKey"></a>
The key of the feature flag used by the experiment.
Type: String
Pattern: `^[a-z][a-zA-Z0-9_-]{1,64}`

 ** [Hypothesis](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-Hypothesis"></a>
The hypothesis that the experiment is designed to validate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Id](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-Id"></a>
The experiment definition ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [KmsKeyIdentifier](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-KmsKeyIdentifier"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt experiment data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [LaunchCriteria](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-LaunchCriteria"></a>
The conditions under which the winning treatment should be launched.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Name](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-Name"></a>
The name of the experiment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [Status](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-Status"></a>
The current status of the experiment definition. Valid values: `ACTIVE`, `IDLE`, `ARCHIVED`.
Type: String
Valid Values: `ACTIVE | IDLE | ARCHIVED`

 ** [Treatments](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-Treatments"></a>
The list of treatments defined for the experiment.
Type: Array of [Treatment](API_Treatment.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [UpdatedAt](#API_UpdateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-UpdateExperimentDefinition-response-UpdatedAt"></a>
The date and time the experiment definition was last updated, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_UpdateExperimentDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_UpdateExperimentDefinition_Examples"></a>

### Example
<a name="API_UpdateExperimentDefinition_Example_1"></a>

This example illustrates one usage of UpdateExperimentDefinition.

#### Sample Request
<a name="API_UpdateExperimentDefinition_Example_1_Request"></a>

```
PATCH /applications/abc1234/experimentdefinitions/bsxyd7k HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Content-Type: application/json
User-Agent: aws-cli
X-Amz-Date: 20210916T175455Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210916/us-east-1/appconfig/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 82

{
	"Hypothesis": "Enabling the feature will increase conversion by 10%",
	"AudienceRule": "(eq $country \"US\")"
}
```

#### Sample Response
<a name="API_UpdateExperimentDefinition_Example_1_Response"></a>

```
{
	"ApplicationId": "abc1234",
	"AudienceRule": "(eq $country \"US\")",
	"ConfigurationProfileId": "ur8hx2f",
	"Control": {
		"FlagValue": {
			"Enabled": false
		},
		"Key": "c",
		"Weight": 50.0
	},
	"CreatedAt": "2026-06-16T17:54:55.847Z",
	"EnvironmentId": "env1234",
	"FlagKey": "my-feature-flag",
	"Hypothesis": "Enabling the feature will increase conversion by 10%",
	"Id": "bsxyd7k",
	"Name": "Example-Experiment-Definition",
	"Status": "IDLE",
	"Treatments": [
		{
			"FlagValue": {
				"Enabled": true
			},
			"Key": "t1",
			"Weight": 50.0
		}
	],
	"UpdatedAt": "2026-06-16T18:04:33.632Z"
}
```

## See Also
<a name="API_UpdateExperimentDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/UpdateExperimentDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/UpdateExperimentDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/UpdateExperimentDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/UpdateExperimentDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/UpdateExperimentDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/UpdateExperimentDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/UpdateExperimentDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/UpdateExperimentDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/UpdateExperimentDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/UpdateExperimentDefinition)
