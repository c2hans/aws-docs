---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_DeleteExperimentTemplate.html
---

# DeleteExperimentTemplate
<a name="API_DeleteExperimentTemplate"></a>

Deletes the specified experiment template.

## Request Syntax
<a name="API_DeleteExperimentTemplate_RequestSyntax"></a>

```
DELETE /experimentTemplates/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteExperimentTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_DeleteExperimentTemplate_RequestSyntax) **   <a name="fis-DeleteExperimentTemplate-request-uri-id"></a>
The ID of the experiment template.
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: Yes

## Request Body
<a name="API_DeleteExperimentTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteExperimentTemplate_ResponseSyntax"></a>

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
<a name="API_DeleteExperimentTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [experimentTemplate](#API_DeleteExperimentTemplate_ResponseSyntax) **   <a name="fis-DeleteExperimentTemplate-response-experimentTemplate"></a>
Information about the experiment template.
Type: [ExperimentTemplate](API_ExperimentTemplate.md) object

## Errors
<a name="API_DeleteExperimentTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ValidationException **
The specified input is not valid, or fails to satisfy the constraints for the request.
HTTP Status Code: 400

## See Also
<a name="API_DeleteExperimentTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fis-2020-12-01/DeleteExperimentTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fis-2020-12-01/DeleteExperimentTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/DeleteExperimentTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fis-2020-12-01/DeleteExperimentTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/DeleteExperimentTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fis-2020-12-01/DeleteExperimentTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fis-2020-12-01/DeleteExperimentTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fis-2020-12-01/DeleteExperimentTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fis-2020-12-01/DeleteExperimentTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/DeleteExperimentTemplate)
