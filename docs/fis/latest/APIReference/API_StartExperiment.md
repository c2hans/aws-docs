---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_StartExperiment.html
---

# StartExperiment
<a name="API_StartExperiment"></a>

Starts running an experiment from the specified experiment template.

## Request Syntax
<a name="API_StartExperiment_RequestSyntax"></a>

```
POST /experiments HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "experimentOptions": {
      "actionsMode": "{{string}}"
   },
   "experimentTemplateId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartExperiment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartExperiment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartExperiment_RequestSyntax) **   <a name="fis-StartExperiment-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S]+`
Required: Yes

 ** [experimentOptions](#API_StartExperiment_RequestSyntax) **   <a name="fis-StartExperiment-request-experimentOptions"></a>
The experiment options for running the experiment.
Type: [StartExperimentExperimentOptionsInput](API_StartExperimentExperimentOptionsInput.md) object
Required: No

 ** [experimentTemplateId](#API_StartExperiment_RequestSyntax) **   <a name="fis-StartExperiment-request-experimentTemplateId"></a>
The ID of the experiment template.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: Yes

 ** [tags](#API_StartExperiment_RequestSyntax) **   <a name="fis-StartExperiment-request-tags"></a>
The tags to apply to the experiment.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]+`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_StartExperiment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "experiment": {
      "actions": {
         "string" : {
            "actionId": "string",
            "description": "string",
            "endTime": number,
            "parameters": {
               "string" : "string"
            },
            "startAfter": [ "string" ],
            "startTime": number,
            "state": {
               "reason": "string",
               "status": "string"
            },
            "targets": {
               "string" : "string"
            }
         }
      },
      "arn": "string",
      "creationTime": number,
      "endTime": number,
      "experimentOptions": {
         "accountTargeting": "string",
         "actionsMode": "string",
         "emptyTargetResolutionMode": "string"
      },
      "experimentReport": {
         "s3Reports": [
            {
               "arn": "string",
               "reportType": "string"
            }
         ],
         "state": {
            "error": {
               "code": "string"
            },
            "reason": "string",
            "status": "string"
         }
      },
      "experimentReportConfiguration": {
         "dataSources": {
            "cloudWatchDashboards": [
               {
                  "dashboardIdentifier": "string"
               }
            ]
         },
         "outputs": {
            "s3Configuration": {
               "bucketName": "string",
               "prefix": "string"
            }
         },
         "postExperimentDuration": "string",
         "preExperimentDuration": "string"
      },
      "experimentTemplateId": "string",
      "id": "string",
      "logConfiguration": {
         "cloudWatchLogsConfiguration": {
            "logGroupArn": "string"
         },
         "logSchemaVersion": number,
         "s3Configuration": {
            "bucketName": "string",
            "prefix": "string"
         }
      },
      "roleArn": "string",
      "startTime": number,
      "state": {
         "error": {
            "accountId": "string",
            "code": "string",
            "location": "string"
         },
         "reason": "string",
         "status": "string"
      },
      "stopConditions": [
         {
            "source": "string",
            "value": "string"
         }
      ],
      "tags": {
         "string" : "string"
      },
      "targetAccountConfigurationsCount": number,
      "targets": {
         "string" : {
            "filters": [
               {
                  "path": "string",
                  "values": [ "string" ]
               }
            ],
            "parameters": {
               "string" : "string"
            },
            "resourceArns": [ "string" ],
            "resourceTags": {
               "string" : "string"
            },
            "resourceType": "string",
            "selectionMode": "string"
         }
      }
   }
}
```

## Response Elements
<a name="API_StartExperiment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [experiment](#API_StartExperiment_ResponseSyntax) **   <a name="fis-StartExperiment-response-experiment"></a>
Information about the experiment.
Type: [Experiment](API_Experiment.md) object

## Errors
<a name="API_StartExperiment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be processed because of a conflict.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have exceeded your service quota.
HTTP Status Code: 402

 ** ValidationException **
The specified input is not valid, or fails to satisfy the constraints for the request.
HTTP Status Code: 400

## See Also
<a name="API_StartExperiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fis-2020-12-01/StartExperiment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fis-2020-12-01/StartExperiment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/StartExperiment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fis-2020-12-01/StartExperiment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/StartExperiment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fis-2020-12-01/StartExperiment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fis-2020-12-01/StartExperiment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fis-2020-12-01/StartExperiment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fis-2020-12-01/StartExperiment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/StartExperiment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
