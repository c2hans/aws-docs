---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetInvestigation.html
---

# GetInvestigation
<a name="API_GetInvestigation"></a>

This API is currently available as a preview. This feature is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), and Asia Pacific (Tokyo).

Retrieves the results and status of a specific GuardDuty investigation.

GuardDuty returns the results, including the summary and the scope of the investigation, only when the investigation status is `COMPLETED`. By default, GuardDuty returns the summary as text in `Summary`. To return a typed summary in `SummaryData` instead, set `SummaryFormat` to `STRUCTURED`.

An administrator account can retrieve any investigation within the organization. Member accounts can only retrieve investigations that belong to them.

## Request Syntax
<a name="API_GetInvestigation_RequestSyntax"></a>

```
GET /detector/{{DetectorId}}/investigation/{{InvestigationId}}?summaryFormat={{SummaryFormat}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetInvestigation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetInvestigation_RequestSyntax) **   <a name="guardduty-GetInvestigation-request-uri-DetectorId"></a>
The unique ID of the GuardDuty detector associated with the investigation.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [InvestigationId](#API_GetInvestigation_RequestSyntax) **   <a name="guardduty-GetInvestigation-request-uri-InvestigationId"></a>
The unique identifier of the investigation to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-fA-F0-9\-]+`
Required: Yes

 ** [SummaryFormat](#API_GetInvestigation_RequestSyntax) **   <a name="guardduty-GetInvestigation-request-uri-SummaryFormat"></a>
The format in which to return the investigation summary. Possible values:
+  `STRING` – (Default) Returns the summary as text in `Summary`.
+  `STRUCTURED` – Returns a typed summary in `SummaryData`.
GuardDuty returns a summary only when the investigation status is `COMPLETED`.
Valid Values: `STRING | STRUCTURED`

## Request Body
<a name="API_GetInvestigation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetInvestigation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "investigation": {
      "cloud": {
         "account": "string",
         "provider": "string",
         "region": "string"
      },
      "confidence": "string",
      "endTime": number,
      "error": "string",
      "investigationId": "string",
      "metadata": {
         "product": {
            "feature": "string",
            "name": "string"
         },
         "version": "string"
      },
      "risk": "string",
      "riskLevel": "string",
      "scope": {
         "accountId": "string",
         "adminAccountId": "string",
         "findingId": "string",
         "investigationType": "string",
         "queryTimeWindow": {
            "endTime": number,
            "startTime": number
         }
      },
      "startTime": number,
      "status": "string",
      "summary": "string",
      "summaryData": {
         "accountAnalysis": {
            "affectedResources": [
               {
                  "findingCount": number,
                  "identifier": "string",
                  "type": "string"
               }
            ],
            "findingsSummary": {
               "byTimeWindow": [
                  {
                     "endTime": number,
                     "findingCount": number,
                     "startTime": number
                  }
               ],
               "severityBreakdown": {
                  "critical": number,
                  "high": number,
                  "info": number,
                  "low": number,
                  "medium": number
               },
               "topFindingTypes": [
                  {
                     "count": number,
                     "findingType": "string"
                  }
               ],
               "totalFindings": number
            },
            "tacticCoverage": [
               {
                  "findingCount": number,
                  "findingTypes": [ "string" ],
                  "phase": "string",
                  "techniques": [
                     {
                        "findingCount": number,
                        "findingTypes": [ "string" ],
                        "technique": {
                           "name": "string",
                           "uid": "string"
                        }
                     }
                  ]
               }
            ]
         },
         "countermeasures": [
            {
               "actions": [
                  {
                     "affectedResources": [
                        {
                           "arn": "string",
                           "identifier": "string",
                           "type": "string"
                        }
                     ],
                     "cliCommands": [ "string" ],
                     "defenseTechnique": "string",
                     "description": "string",
                     "disposition": "string",
                     "dispositionId": number,
                     "mitigates": [ "string" ],
                     "priority": "string",
                     "title": "string"
                  }
               ],
               "defenseTactic": "string",
               "description": "string"
            }
         ],
         "findingType": "string",
         "keyObservations": {
            "narrative": "string",
            "observations": [ "string" ],
            "title": "string"
         },
         "organizationAnalysis": {
            "accountBreakdown": [
               {
                  "accountId": "string",
                  "findingCount": number
               }
            ],
            "findingsSummary": {
               "affectedAccountCount": number,
               "byTimeWindow": [
                  {
                     "endTime": number,
                     "findingCount": number,
                     "startTime": number
                  }
               ],
               "severityBreakdown": {
                  "critical": number,
                  "high": number,
                  "info": number,
                  "low": number,
                  "medium": number
               },
               "topFindingTypes": [
                  {
                     "count": number,
                     "findingType": "string"
                  }
               ],
               "totalAccountCount": number,
               "totalFindings": number
            }
         },
         "recommendations": [
            {
               "category": "string",
               "cliCommands": [ "string" ],
               "priority": "string",
               "rationale": "string",
               "title": "string"
            }
         ],
         "threatAssessment": {
            "attackProgression": [
               {
                  "attacks": [
                     {
                        "findings": [
                           {
                              "findingType": "string",
                              "uid": "string"
                           }
                        ],
                        "tactic": {
                           "name": "string",
                           "uid": "string"
                        },
                        "technique": {
                           "name": "string",
                           "uid": "string"
                        },
                        "version": "string"
                     }
                  ],
                  "description": "string",
                  "phase": "string"
               }
            ],
            "threatActorProfile": "string"
         }
      },
      "triggeredBy": "string",
      "triggerPrompt": "string"
   }
}
```

## Response Elements
<a name="API_GetInvestigation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [investigation](#API_GetInvestigation_ResponseSyntax) **   <a name="guardduty-GetInvestigation-response-investigation"></a>
The details and results of the requested investigation.
Type: [Investigation](API_Investigation.md) object

## Errors
<a name="API_GetInvestigation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An access denied exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 403

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 404

## See Also
<a name="API_GetInvestigation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetInvestigation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetInvestigation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetInvestigation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetInvestigation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetInvestigation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetInvestigation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetInvestigation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetInvestigation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetInvestigation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetInvestigation)
