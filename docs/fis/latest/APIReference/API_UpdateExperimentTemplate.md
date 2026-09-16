---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_UpdateExperimentTemplate.html
---

# UpdateExperimentTemplate
<a name="API_UpdateExperimentTemplate"></a>

Updates the specified experiment template.

## Request Syntax
<a name="API_UpdateExperimentTemplate_RequestSyntax"></a>

```
PATCH /experimentTemplates/{{id}} HTTP/1.1
Content-type: application/json

{
   "actions": {
      "{{string}}" : {
         "actionId": "{{string}}",
         "description": "{{string}}",
         "parameters": {
            "{{string}}" : "{{string}}"
         },
         "startAfter": [ "{{string}}" ],
         "targets": {
            "{{string}}" : "{{string}}"
         }
      }
   },
   "description": "{{string}}",
   "experimentOptions": {
      "emptyTargetResolutionMode": "{{string}}"
   },
   "experimentReportConfiguration": {
      "dataSources": {
         "cloudWatchDashboards": [
            {
               "dashboardIdentifier": "{{string}}"
            }
         ]
      },
      "outputs": {
         "s3Configuration": {
            "bucketName": "{{string}}",
            "prefix": "{{string}}"
         }
      },
      "postExperimentDuration": "{{string}}",
      "preExperimentDuration": "{{string}}"
   },
   "logConfiguration": {
      "cloudWatchLogsConfiguration": {
         "logGroupArn": "{{string}}"
      },
      "logSchemaVersion": {{number}},
      "s3Configuration": {
         "bucketName": "{{string}}",
         "prefix": "{{string}}"
      }
   },
   "roleArn": "{{string}}",
   "stopConditions": [
      {
         "source": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "targets": {
      "{{string}}" : {
         "filters": [
            {
               "path": "{{string}}",
               "values": [ "{{string}}" ]
            }
         ],
         "parameters": {
            "{{string}}" : "{{string}}"
         },
         "resourceArns": [ "{{string}}" ],
         "resourceTags": {
            "{{string}}" : "{{string}}"
         },
         "resourceType": "{{string}}",
         "selectionMode": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateExperimentTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateExperimentTemplate_RequestSyntax) **   <a name="fis-UpdateExperimentTemplate-request-uri-id"></a>
The ID of the experiment template.
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: Yes

## Request Body
<a name="API_UpdateExperimentTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actions](#API_UpdateExperimentTemplate_RequestSyntax) **   <a name="fis-UpdateExperimentTemplate-request-actions"></a>
The actions for the experiment.
Type: String to [UpdateExperimentTemplateActionInputItem](API_UpdateExperimentTemplateActionInputItem.md) object map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Required: No

 ** [description](#API_UpdateExperimentTemplate_RequestSyntax) **   <a name="fis-UpdateExperimentTemplate-request-description"></a>
A description for the template.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: No

 ** [experimentOptions](#API_UpdateExperimentTemplate_RequestSyntax) **   <a name="fis-UpdateExperimentTemplate-request-experimentOptions"></a>
The experiment options for the experiment template.
Type: [UpdateExperimentTemplateExperimentOptionsInput](API_UpdateExperimentTemplateExperimentOptionsInput.md) object
Required: No

 ** [experimentReportConfiguration](#API_UpdateExperimentTemplate_RequestSyntax) **   <a name="fis-UpdateExperimentTemplate-request-experimentReportConfiguration"></a>
The experiment report configuration for the experiment template.
Type: [UpdateExperimentTemplateReportConfigurationInput](API_UpdateExperimentTemplateReportConfigurationInput.md) object
Required: No

 ** [logConfiguration](#API_UpdateExperimentTemplate_RequestSyntax) **   <a name="fis-UpdateExperimentTemplate-request-logConfiguration"></a>
The configuration for experiment logging.
Type: [UpdateExperimentTemplateLogConfigurationInput](API_UpdateExperimentTemplateLogConfigurationInput.md) object
Required: No

 ** [roleArn](#API_UpdateExperimentTemplate_RequestSyntax) **   <a name="fis-UpdateExperimentTemplate-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that grants the AWS FIS service permission to perform service actions on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** [stopConditions](#API_UpdateExperimentTemplate_RequestSyntax) **   <a name="fis-UpdateExperimentTemplate-request-stopConditions"></a>
The stop conditions for the experiment.
Type: Array of [UpdateExperimentTemplateStopConditionInput](API_UpdateExperimentTemplateStopConditionInput.md) objects
Required: No

 ** [targets](#API_UpdateExperimentTemplate_RequestSyntax) **   <a name="fis-UpdateExperimentTemplate-request-targets"></a>
The targets for the experiment.
Type: String to [UpdateExperimentTemplateTargetInput](API_UpdateExperimentTemplateTargetInput.md) object map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Required: No

## Response Syntax
<a name="API_UpdateExperimentTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "experimentTemplate": {
      "actions": {
         "string" : {
            "actionId": "string",
            "description": "string",
            "parameters": {
               "string" : "string"
            },
            "startAfter": [ "string" ],
            "targets": {
               "string" : "string"
            }
         }
      },
      "arn": "string",
      "creationTime": number,
      "description": "string",
      "experimentOptions": {
         "accountTargeting": "string",
         "emptyTargetResolutionMode": "string"
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
      "id": "string",
      "lastUpdateTime": number,
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
<a name="API_UpdateExperimentTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [experimentTemplate](#API_UpdateExperimentTemplate_ResponseSyntax) **   <a name="fis-UpdateExperimentTemplate-response-experimentTemplate"></a>
Information about the experiment template.
Type: [ExperimentTemplate](API_ExperimentTemplate.md) object

## Errors
<a name="API_UpdateExperimentTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_UpdateExperimentTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fis-2020-12-01/UpdateExperimentTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fis-2020-12-01/UpdateExperimentTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/UpdateExperimentTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fis-2020-12-01/UpdateExperimentTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/UpdateExperimentTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fis-2020-12-01/UpdateExperimentTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fis-2020-12-01/UpdateExperimentTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fis-2020-12-01/UpdateExperimentTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fis-2020-12-01/UpdateExperimentTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/UpdateExperimentTemplate)
