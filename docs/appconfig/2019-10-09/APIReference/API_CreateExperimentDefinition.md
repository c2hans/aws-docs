---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateExperimentDefinition.html
---

# CreateExperimentDefinition
<a name="API_CreateExperimentDefinition"></a>

Creates an experiment definition in AWS AppConfig. An experiment definition describes the purpose, scope, and operational configuration of an experiment, including the target audience, feature flag, and treatment configurations.

## Request Syntax
<a name="API_CreateExperimentDefinition_RequestSyntax"></a>

```
POST /applications/{{ApplicationIdentifier}}/experimentdefinitions HTTP/1.1
Content-type: application/json

{
   "AudienceDescription": "{{string}}",
   "AudienceRule": "{{string}}",
   "ConfigurationProfileIdentifier": "{{string}}",
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
   "EnvironmentIdentifier": "{{string}}",
   "FlagKey": "{{string}}",
   "Hypothesis": "{{string}}",
   "LaunchCriteria": "{{string}}",
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
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
<a name="API_CreateExperimentDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-uri-ApplicationIdentifier"></a>
The application ID or name.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_CreateExperimentDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AudienceDescription](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-AudienceDescription"></a>
A description of the intended audience for the experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [AudienceRule](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-AudienceRule"></a>
A rule that defines which users are eligible to be assigned to treatments during the experiment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: Yes

 ** [ConfigurationProfileIdentifier](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-ConfigurationProfileIdentifier"></a>
The configuration profile ID or name that stores the feature flag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [Control](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-Control"></a>
The control treatment that represents the baseline experience for comparison.
Type: [TreatmentInput](API_TreatmentInput.md) object
Required: Yes

 ** [EnvironmentIdentifier](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-EnvironmentIdentifier"></a>
The environment ID or name where the experiment will run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [FlagKey](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-FlagKey"></a>
The key of the existing feature flag to use with the experiment.
Type: String
Pattern: `^[a-z][a-zA-Z0-9_-]{1,64}`
Required: Yes

 ** [Hypothesis](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-Hypothesis"></a>
A description of the goal or hypothesis the experiment is designed to validate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [LaunchCriteria](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-LaunchCriteria"></a>
Information about the conditions under which you would launch the winning treatment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Name](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-Name"></a>
A name for the experiment definition.
Type: String
Pattern: `^(?!AWS\.).{1,64}$`
Required: Yes

 ** [Tags](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-Tags"></a>
The tags to assign to the experiment definition. Tags help organize and categorize your AWS AppConfig resources.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

 ** [Treatments](#API_CreateExperimentDefinition_RequestSyntax) **   <a name="appconfig-CreateExperimentDefinition-request-Treatments"></a>
A list of treatments to evaluate during the experiment. Each treatment defines a distinct variation compared to the control.
Type: Array of [TreatmentInput](API_TreatmentInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

## Response Syntax
<a name="API_CreateExperimentDefinition_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateExperimentDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [AudienceDescription](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-AudienceDescription"></a>
A description of the intended audience for the experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [AudienceRule](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-AudienceRule"></a>
The rule that defines which users are eligible to be assigned to treatments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.

 ** [ConfigurationProfileId](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-ConfigurationProfileId"></a>
The configuration profile ID associated with the experiment.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Control](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-Control"></a>
The control treatment used as the baseline for comparison.
Type: [Treatment](API_Treatment.md) object

 ** [CreatedAt](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-CreatedAt"></a>
The date and time the experiment definition was created, in ISO 8601 format.
Type: Timestamp

 ** [EnvironmentId](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-EnvironmentId"></a>
The environment ID where the experiment runs.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [FlagKey](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-FlagKey"></a>
The key of the feature flag used by the experiment.
Type: String
Pattern: `^[a-z][a-zA-Z0-9_-]{1,64}`

 ** [Hypothesis](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-Hypothesis"></a>
The hypothesis that the experiment is designed to validate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Id](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-Id"></a>
The experiment definition ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [KmsKeyIdentifier](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-KmsKeyIdentifier"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt experiment data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [LaunchCriteria](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-LaunchCriteria"></a>
The conditions under which the winning treatment should be launched.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Name](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-Name"></a>
The name of the experiment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [Status](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-Status"></a>
The current status of the experiment definition. Valid values: `ACTIVE`, `IDLE`, `ARCHIVED`.
Type: String
Valid Values: `ACTIVE | IDLE | ARCHIVED`

 ** [Treatments](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-Treatments"></a>
The list of treatments defined for the experiment.
Type: Array of [Treatment](API_Treatment.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [UpdatedAt](#API_CreateExperimentDefinition_ResponseSyntax) **   <a name="appconfig-CreateExperimentDefinition-response-UpdatedAt"></a>
The date and time the experiment definition was last updated, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_CreateExperimentDefinition_Errors"></a>

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

 ** ServiceQuotaExceededException **
The number of one more AWS AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:
Applications: 100 max
To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see [Service quotas for AWS AppConfig](https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig) in the Amazon Web Services General Reference.
HTTP Status Code: 402

## Examples
<a name="API_CreateExperimentDefinition_Examples"></a>

### Example
<a name="API_CreateExperimentDefinition_Example_1"></a>

This example illustrates one usage of CreateExperimentDefinition.

#### Sample Request
<a name="API_CreateExperimentDefinition_Example_1_Request"></a>

```
POST /applications/abc1234/experimentdefinitions HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Content-Type: application/json
User-Agent: aws-cli
X-Amz-Date: 20210916T175455Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210916/us-east-1/appconfig/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 306

{
	"Name": "Example-Experiment-Definition",
	"ConfigurationProfileIdentifier": "ur8hx2f",
	"EnvironmentIdentifier": "env1234",
	"FlagKey": "my-feature-flag",
	"Treatments": [
		{
			"Weight": 50,
			"FlagValue": {
				"Enabled": true
			}
		}
	],
	"Control": {
		"Weight": 50,
		"FlagValue": {
			"Enabled": false
		}
	},
	"AudienceRule": "(eq $country \"US\")"
}
```

#### Sample Response
<a name="API_CreateExperimentDefinition_Example_1_Response"></a>

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
	"UpdatedAt": "2026-06-16T17:54:55.847Z"
}
```

## See Also
<a name="API_CreateExperimentDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/CreateExperimentDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/CreateExperimentDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/CreateExperimentDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/CreateExperimentDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/CreateExperimentDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/CreateExperimentDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/CreateExperimentDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/CreateExperimentDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/CreateExperimentDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/CreateExperimentDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
