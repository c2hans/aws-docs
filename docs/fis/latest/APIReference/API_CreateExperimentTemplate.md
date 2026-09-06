---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplate.html
---

# CreateExperimentTemplate
<a name="API_CreateExperimentTemplate"></a>

Creates an experiment template.

An experiment template includes the following components:
+  **Targets**: A target can be a specific resource in your AWS environment, or one or more resources that match criteria that you specify, for example, resources that have specific tags.
+  **Actions**: The actions to carry out on the target. You can specify multiple actions, the duration of each action, and when to start each action during an experiment.
+  **Stop conditions**: If a stop condition is triggered while an experiment is running, the experiment is automatically stopped. You can define a stop condition as a CloudWatch alarm.

For more information, see [experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html) in the * AWS Fault Injection Service User Guide*.

## Request Syntax
<a name="API_CreateExperimentTemplate_RequestSyntax"></a>

```
POST /experimentTemplates HTTP/1.1
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
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "experimentOptions": {
      "accountTargeting": "{{string}}",
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
   "tags": {
      "{{string}}" : "{{string}}"
   },
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
<a name="API_CreateExperimentTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateExperimentTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actions](#API_CreateExperimentTemplate_RequestSyntax) **   <a name="fis-CreateExperimentTemplate-request-actions"></a>
The actions for the experiment.
Type: String to [CreateExperimentTemplateActionInput](API_CreateExperimentTemplateActionInput.md) object map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Required: Yes

 ** [clientToken](#API_CreateExperimentTemplate_RequestSyntax) **   <a name="fis-CreateExperimentTemplate-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S]+`
Required: Yes

 ** [description](#API_CreateExperimentTemplate_RequestSyntax) **   <a name="fis-CreateExperimentTemplate-request-description"></a>
A description for the experiment template.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: Yes

 ** [experimentOptions](#API_CreateExperimentTemplate_RequestSyntax) **   <a name="fis-CreateExperimentTemplate-request-experimentOptions"></a>
The experiment options for the experiment template.
Type: [CreateExperimentTemplateExperimentOptionsInput](API_CreateExperimentTemplateExperimentOptionsInput.md) object
Required: No

 ** [experimentReportConfiguration](#API_CreateExperimentTemplate_RequestSyntax) **   <a name="fis-CreateExperimentTemplate-request-experimentReportConfiguration"></a>
The experiment report configuration for the experiment template.
Type: [CreateExperimentTemplateReportConfigurationInput](API_CreateExperimentTemplateReportConfigurationInput.md) object
Required: No

 ** [logConfiguration](#API_CreateExperimentTemplate_RequestSyntax) **   <a name="fis-CreateExperimentTemplate-request-logConfiguration"></a>
The configuration for experiment logging.
Type: [CreateExperimentTemplateLogConfigurationInput](API_CreateExperimentTemplateLogConfigurationInput.md) object
Required: No

 ** [roleArn](#API_CreateExperimentTemplate_RequestSyntax) **   <a name="fis-CreateExperimentTemplate-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that grants the AWS FIS service permission to perform service actions on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: Yes

 ** [stopConditions](#API_CreateExperimentTemplate_RequestSyntax) **   <a name="fis-CreateExperimentTemplate-request-stopConditions"></a>
The stop conditions.
Type: Array of [CreateExperimentTemplateStopConditionInput](API_CreateExperimentTemplateStopConditionInput.md) objects
Required: Yes

 ** [tags](#API_CreateExperimentTemplate_RequestSyntax) **   <a name="fis-CreateExperimentTemplate-request-tags"></a>
The tags to apply to the experiment template.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]+`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: No

 ** [targets](#API_CreateExperimentTemplate_RequestSyntax) **   <a name="fis-CreateExperimentTemplate-request-targets"></a>
The targets for the experiment.
Type: String to [CreateExperimentTemplateTargetInput](API_CreateExperimentTemplateTargetInput.md) object map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Required: No

## Response Syntax
<a name="API_CreateExperimentTemplate_ResponseSyntax"></a>

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
<a name="API_CreateExperimentTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [experimentTemplate](#API_CreateExperimentTemplate_ResponseSyntax) **   <a name="fis-CreateExperimentTemplate-response-experimentTemplate"></a>
Information about the experiment template.
Type: [ExperimentTemplate](API_ExperimentTemplate.md) object

## Errors
<a name="API_CreateExperimentTemplate_Errors"></a>

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

## Examples
<a name="API_CreateExperimentTemplate_Examples"></a>

### Terminate EC2 instances
<a name="API_CreateExperimentTemplate_Example_1"></a>

The following example terminates three instances in the specified VPC with the tag env=test.

#### Sample Request
<a name="API_CreateExperimentTemplate_Example_1_Request"></a>

```
{
    "description": "Test instance termination",
    "targets": {
        "to-terminate": {
            "resourceType": "aws:ec2:instance",
            "resourceTags": {
                "env": "test"
            },
            "filters": [
                "path": "VpcId",
                "values": [
                    "vpc-1234567890abcdef0"
                ]
            ],
            "selectionMode": "COUNT(3)"
        }
    },
    "actions": {
        "TerminateInstances": {
            "actionId": "aws:ec2-terminate-instances",
            "description": "terminate instances",
            "targets": {
                "Instances": "to-terminate"
            }
        }
    },
    "stopConditions": [
        {
            "source": "none"
        }
    ],
    "roleArn": "arn:aws:iam:123456789012:role/ExperimentRole",

}
```

## See Also
<a name="API_CreateExperimentTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fis-2020-12-01/CreateExperimentTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fis-2020-12-01/CreateExperimentTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/CreateExperimentTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fis-2020-12-01/CreateExperimentTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/CreateExperimentTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fis-2020-12-01/CreateExperimentTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fis-2020-12-01/CreateExperimentTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fis-2020-12-01/CreateExperimentTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fis-2020-12-01/CreateExperimentTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/CreateExperimentTemplate)
