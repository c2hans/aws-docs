---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetExperimentRun.html
---

# GetExperimentRun
<a name="API_GetExperimentRun"></a>

Retrieves information about an experiment run, including its status, start time, and exposure settings.

## Request Syntax
<a name="API_GetExperimentRun_RequestSyntax"></a>

```
GET /applications/{{ApplicationIdentifier}}/experimentdefinitions/{{ExperimentDefinitionIdentifier}}/experimentruns/{{Run}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetExperimentRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_GetExperimentRun_RequestSyntax) **   <a name="appconfig-GetExperimentRun-request-uri-ApplicationIdentifier"></a>
The application ID or name.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [ExperimentDefinitionIdentifier](#API_GetExperimentRun_RequestSyntax) **   <a name="appconfig-GetExperimentRun-request-uri-ExperimentDefinitionIdentifier"></a>
The experiment definition ID or name.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [Run](#API_GetExperimentRun_RequestSyntax) **   <a name="appconfig-GetExperimentRun-request-uri-Run"></a>
The run number to retrieve.
Valid Range: Minimum value of 1.
Required: Yes

## Request Body
<a name="API_GetExperimentRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetExperimentRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationId": "string",
   "Description": "string",
   "EndedAt": "string",
   "ExperimentDefinitionId": "string",
   "ExperimentDefinitionSnapshot": {
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
      "EnvironmentId": "string",
      "FlagKey": "string",
      "Hypothesis": "string",
      "Id": "string",
      "LaunchCriteria": "string",
      "Name": "string",
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
      ]
   },
   "ExposurePercentage": number,
   "Result": {
      "ExecutiveSummary": "string",
      "ReasonsNotToLaunch": "string",
      "ReasonsToLaunch": "string"
   },
   "Run": number,
   "StartedAt": "string",
   "Status": "string",
   "TreatmentOverrides": { ... },
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_GetExperimentRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Description](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-Description"></a>
A description of the experiment run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [EndedAt](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-EndedAt"></a>
The date and time the experiment run ended, in ISO 8601 format.
Type: Timestamp

 ** [ExperimentDefinitionId](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-ExperimentDefinitionId"></a>
The experiment definition ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [ExperimentDefinitionSnapshot](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-ExperimentDefinitionSnapshot"></a>
A snapshot of the experiment definition at the time the run was started.
Type: [ExperimentDefinitionSnapshot](API_ExperimentDefinitionSnapshot.md) object

 ** [ExposurePercentage](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-ExposurePercentage"></a>
The percentage of the target audience exposed to treatments.
Type: Float
Valid Range: Minimum value of 0.0. Maximum value of 100.0.

 ** [Result](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-Result"></a>
The result of the experiment run, including the executive summary and launch decision rationale.
Type: [ExperimentRunResult](API_ExperimentRunResult.md) object

 ** [Run](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-Run"></a>
The experiment run number.
Type: Integer

 ** [StartedAt](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-StartedAt"></a>
The date and time the experiment run started, in ISO 8601 format.
Type: Timestamp

 ** [Status](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-Status"></a>
The current status of the experiment run. Valid values: `RUNNING`, `DONE`.
Type: String
Valid Values: `RUNNING | DONE`

 ** [TreatmentOverrides](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-TreatmentOverrides"></a>
Treatment assignment overrides that assign specific entity IDs to treatments.
Type: [TreatmentOverrides](API_TreatmentOverrides.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [UpdatedAt](#API_GetExperimentRun_ResponseSyntax) **   <a name="appconfig-GetExperimentRun-response-UpdatedAt"></a>
The date and time the experiment run was last updated, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_GetExperimentRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_GetExperimentRun_Examples"></a>

### Example
<a name="API_GetExperimentRun_Example_1"></a>

This example illustrates one usage of GetExperimentRun.

#### Sample Request
<a name="API_GetExperimentRun_Example_1_Request"></a>

```
GET /applications/abc1234/experimentdefinitions/bsxyd7k/experimentruns/1 HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
User-Agent: aws-cli
X-Amz-Date: 20210916T175455Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210916/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_GetExperimentRun_Example_1_Response"></a>

```
{
	"ApplicationId": "abc1234",
	"ExperimentDefinitionId": "bsxyd7k",
	"ExperimentDefinitionSnapshot": {
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
		"EnvironmentId": "env1234",
		"FlagKey": "my-feature-flag",
		"Id": "bsxyd7k",
		"Name": "Example-Experiment-Definition",
		"Treatments": [
			{
				"FlagValue": {
					"Enabled": true
				},
				"Key": "t1",
				"Weight": 50.0
			}
		]
	},
	"ExposurePercentage": 50.0,
	"Run": 1,
	"StartedAt": "2026-06-16T17:57:10.046Z",
	"Status": "RUNNING",
	"UpdatedAt": "2026-06-16T17:57:10.567Z"
}
```

## See Also
<a name="API_GetExperimentRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/GetExperimentRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/GetExperimentRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/GetExperimentRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/GetExperimentRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/GetExperimentRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/GetExperimentRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/GetExperimentRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/GetExperimentRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/GetExperimentRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/GetExperimentRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
