---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateMatchingWorkflow.html
---

# CreateMatchingWorkflow
<a name="API_CreateMatchingWorkflow"></a>

Creates a matching workflow that defines the configuration for a data processing job. The workflow name must be unique. To modify an existing workflow, use `UpdateMatchingWorkflow`.

**Important**
For workflows where `resolutionType` is `PROVIDER`, incremental processing is not supported.

## Request Syntax
<a name="API_CreateMatchingWorkflow_RequestSyntax"></a>

```
POST /matchingworkflows HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "incrementalRunConfig": {
      "incrementalRunType": "{{string}}"
   },
   "inputSourceConfig": [
      {
         "applyNormalization": {{boolean}},
         "inputSourceARN": "{{string}}",
         "schemaName": "{{string}}"
      }
   ],
   "outputSourceConfig": [
      {
         "applyNormalization": {{boolean}},
         "customerProfilesIntegrationConfig": {
            "domainArn": "{{string}}",
            "objectTypeArn": "{{string}}"
         },
         "KMSArn": "{{string}}",
         "output": [
            {
               "hashed": {{boolean}},
               "name": "{{string}}"
            }
         ],
         "outputS3Path": "{{string}}"
      }
   ],
   "resolutionTechniques": {
      "enableRealTimeMatching": {{boolean}},
      "providerProperties": {
         "intermediateSourceConfiguration": {
            "intermediateS3Path": "{{string}}"
         },
         "providerConfiguration": {{JSON value}},
         "providerServiceArn": "{{string}}"
      },
      "resolutionType": "{{string}}",
      "ruleBasedProperties": {
         "attributeMatchingModel": "{{string}}",
         "matchPurpose": "{{string}}",
         "rules": [
            {
               "matchingKeys": [ "{{string}}" ],
               "ruleName": "{{string}}"
            }
         ]
      },
      "ruleConditionProperties": {
         "matchingConfig": {
            "enableTransitiveMatching": {{boolean}}
         },
         "rules": [
            {
               "condition": "{{string}}",
               "ruleName": "{{string}}"
            }
         ]
      }
   },
   "roleArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "workflowName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateMatchingWorkflow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMatchingWorkflow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateMatchingWorkflow_RequestSyntax) **   <a name="API-CreateMatchingWorkflow-request-description"></a>
A description of the workflow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [incrementalRunConfig](#API_CreateMatchingWorkflow_RequestSyntax) **   <a name="API-CreateMatchingWorkflow-request-incrementalRunConfig"></a>
Optional. An object that defines the incremental run type. This object contains only the `incrementalRunType` field, which appears as "Automatic" in the console.
For workflows where `resolutionType` is `PROVIDER`, incremental processing is not supported.
Type: [IncrementalRunConfig](API_IncrementalRunConfig.md) object
Required: No

 ** [inputSourceConfig](#API_CreateMatchingWorkflow_RequestSyntax) **   <a name="API-CreateMatchingWorkflow-request-inputSourceConfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
Type: Array of [InputSource](API_InputSource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** [outputSourceConfig](#API_CreateMatchingWorkflow_RequestSyntax) **   <a name="API-CreateMatchingWorkflow-request-outputSourceConfig"></a>
A list of `OutputSource` objects, each of which contains fields `outputS3Path`, `applyNormalization`, `KMSArn`, and `output`.
Type: Array of [OutputSource](API_OutputSource.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [resolutionTechniques](#API_CreateMatchingWorkflow_RequestSyntax) **   <a name="API-CreateMatchingWorkflow-request-resolutionTechniques"></a>
An object which defines the `resolutionType` and the `ruleBasedProperties`.
Type: [ResolutionTechniques](API_ResolutionTechniques.md) object
Required: Yes

 ** [roleArn](#API_CreateMatchingWorkflow_RequestSyntax) **   <a name="API-CreateMatchingWorkflow-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.
Type: String
Required: Yes

 ** [tags](#API_CreateMatchingWorkflow_RequestSyntax) **   <a name="API-CreateMatchingWorkflow-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [workflowName](#API_CreateMatchingWorkflow_RequestSyntax) **   <a name="API-CreateMatchingWorkflow-request-workflowName"></a>
The name of the workflow. There can't be multiple `MatchingWorkflows` with the same name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Response Syntax
<a name="API_CreateMatchingWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "incrementalRunConfig": {
      "incrementalRunType": "string"
   },
   "inputSourceConfig": [
      {
         "applyNormalization": boolean,
         "inputSourceARN": "string",
         "schemaName": "string"
      }
   ],
   "outputSourceConfig": [
      {
         "applyNormalization": boolean,
         "customerProfilesIntegrationConfig": {
            "domainArn": "string",
            "objectTypeArn": "string"
         },
         "KMSArn": "string",
         "output": [
            {
               "hashed": boolean,
               "name": "string"
            }
         ],
         "outputS3Path": "string"
      }
   ],
   "resolutionTechniques": {
      "enableRealTimeMatching": boolean,
      "providerProperties": {
         "intermediateSourceConfiguration": {
            "intermediateS3Path": "string"
         },
         "providerConfiguration": JSON value,
         "providerServiceArn": "string"
      },
      "resolutionType": "string",
      "ruleBasedProperties": {
         "attributeMatchingModel": "string",
         "matchPurpose": "string",
         "rules": [
            {
               "matchingKeys": [ "string" ],
               "ruleName": "string"
            }
         ]
      },
      "ruleConditionProperties": {
         "matchingConfig": {
            "enableTransitiveMatching": boolean
         },
         "rules": [
            {
               "condition": "string",
               "ruleName": "string"
            }
         ]
      }
   },
   "roleArn": "string",
   "workflowArn": "string",
   "workflowName": "string"
}
```

## Response Elements
<a name="API_CreateMatchingWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_CreateMatchingWorkflow_ResponseSyntax) **   <a name="API-CreateMatchingWorkflow-response-description"></a>
A description of the workflow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [incrementalRunConfig](#API_CreateMatchingWorkflow_ResponseSyntax) **   <a name="API-CreateMatchingWorkflow-response-incrementalRunConfig"></a>
An object which defines an incremental run type and has only `incrementalRunType` as a field.
Type: [IncrementalRunConfig](API_IncrementalRunConfig.md) object

 ** [inputSourceConfig](#API_CreateMatchingWorkflow_ResponseSyntax) **   <a name="API-CreateMatchingWorkflow-response-inputSourceConfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
Type: Array of [InputSource](API_InputSource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.

 ** [outputSourceConfig](#API_CreateMatchingWorkflow_ResponseSyntax) **   <a name="API-CreateMatchingWorkflow-response-outputSourceConfig"></a>
A list of `OutputSource` objects, each of which contains fields `outputS3Path`, `applyNormalization`, `KMSArn`, and `output`.
Type: Array of [OutputSource](API_OutputSource.md) objects
Array Members: Fixed number of 1 item.

 ** [resolutionTechniques](#API_CreateMatchingWorkflow_ResponseSyntax) **   <a name="API-CreateMatchingWorkflow-response-resolutionTechniques"></a>
An object which defines the `resolutionType` and the `ruleBasedProperties`.
Type: [ResolutionTechniques](API_ResolutionTechniques.md) object

 ** [roleArn](#API_CreateMatchingWorkflow_ResponseSyntax) **   <a name="API-CreateMatchingWorkflow-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.
Type: String

 ** [workflowArn](#API_CreateMatchingWorkflow_ResponseSyntax) **   <a name="API-CreateMatchingWorkflow-response-workflowArn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the `MatchingWorkflow`.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})`

 ** [workflowName](#API_CreateMatchingWorkflow_ResponseSyntax) **   <a name="API-CreateMatchingWorkflow-response-workflowName"></a>
The name of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

## Errors
<a name="API_CreateMatchingWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc.
HTTP Status Code: 400

 ** ExceedsLimitException **
The request was rejected because it attempted to create resources beyond the current AWS Entity Resolution account limits. The error message describes the limit exceeded.
 ** quotaName **
The name of the quota that has been breached.
 ** quotaValue **
The current quota value for the customers.
HTTP Status Code: 402

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## Examples
<a name="API_CreateMatchingWorkflow_Examples"></a>

### Example of a rule-based matching workﬂow with batch (manual) processing
<a name="API_CreateMatchingWorkflow_Example_1"></a>

The following example uses the `CreateMatchingWorkflow` API to create a rule-based matching workflow with batch processing in AWS Entity Resolution. It sets up a workflow named "sample" that uses an AWS Glue table as the input source and configures output for ID, email, and gender fields. The workflow employs rule-based matching techniques with a single rule ("Rule1") that uses the email field as a matching key. The request specifies an attribute matching model of "ONE\_TO\_ONE" and includes settings to not apply normalization to the input data. Since no `incrementalRunConfig` is specified, this workflow will use the default batch processing mode.

#### Sample Request
<a name="API_CreateMatchingWorkflow_Example_1_Request"></a>

```
{
    "workflowName": "sample",
    "inputSourceConfig": [
        {
            "applyNormalization": false,
            "inputSourceARN": "arn:aws:glue:<region>:<accountId>:table/<glueDatabaseName>/<glueTableName>",
            "schemaName": "sampleSchemaName"
        }
    ],
    "outputSourceConfig": [
        {
            "outputS3Path": "s3://<bucketName>/prefix",
            "output": [
                {
                    "name": "id",
                    "hashed": false
                },
                {
                    "name": "email",
                    "hashed": false
                },
                {
                    "name": "gender",
                    "hashed": false
                }
            ]
        }
    ],
    "resolutionTechniques": {
        "resolutionType": "RULE_MATCHING",
        "ruleBasedProperties": {
            "rules": [
                {
                    "ruleName": "Rule1",
                    "matchingKeys": [
                        "email"
                    ]
                }
            ],
            "attributeMatchingModel": "ONE_TO_ONE"
        }
    },
    "roleArn": "arn:aws:iam::<region>:role/passRoleArn"
}
```

### Example of a rule-based matching workﬂow with incremental (automatic) processing
<a name="API_CreateMatchingWorkflow_Example_2"></a>

The following example uses the `CreateMatchingWorkflow` API to create a rule-based matching workflow with incremental processing in AWS Entity Resolution. It sets up a workflow named "sample" that uses an AWS Glue table as the input source and configures output for ID, email, and gender fields. The workflow employs rule-based matching techniques with a single rule ("Rule1") that uses the email field as a matching key. The request specifies an attribute matching model of "ONE\_TO\_ONE" and enables immediate incremental processing. It also includes settings to not apply normalization to the input data and provides the necessary IAM role for workflow execution.

#### Sample Request
<a name="API_CreateMatchingWorkflow_Example_2_Request"></a>

```
{
    "workflowName": "sample",
    "inputSourceConfig": [
        {
            "applyNormalization": false,
            "inputSourceARN": "arn:aws:glue:<region>:<accountId>:table/<glueDatabaseName>/<glueTableName>",
            "schemaName": "sampleSchemaName"
        }
    ],
    "outputSourceConfig": [
        {
            "outputS3Path": "s3://<bucketName>/prefix",
            "output": [
                {
                    "name": "id",
                    "hashed": false
                },
                {
                    "name": "email",
                    "hashed": false
                },
                {
                    "name": "gender",
                    "hashed": false
                }
            ]
        }
    ],
    "resolutionTechniques": {
        "resolutionType": "RULE_MATCHING",
        "ruleBasedProperties": {
            "rules": [
                {
                    "ruleName": "Rule1",
                    "matchingKeys": [
                        "email"
                    ]
                }
            ],
            "attributeMatchingModel": "ONE_TO_ONE"
        }
    },
    "incrementalRunConfig": {
        "incrementalRunType": "IMMEDIATE"
    },
    "roleArn": "arn:aws:iam::<region>:role/passRoleArn"
}
```

### Example of a machine learning-based matching workﬂow
<a name="API_CreateMatchingWorkflow_Example_3"></a>

The following example uses the `CreateMatchingWorkflow` API to create a machine learning-based matching workflow in AWS Entity Resolution. It sets up a workflow named "sample" that uses an AWS Glue table as the input source, configures output for ID, email, and gender fields, and employs ML-based matching techniques. The request specifies not to apply normalization to the input data and includes the necessary IAM role for workflow execution.

#### Sample Request
<a name="API_CreateMatchingWorkflow_Example_3_Request"></a>

```
{
    "workflowName": "sample",
    "inputSourceConfig": [
        {
            "applyNormalization": false,
            "inputSourceARN": "arn:aws:glue:<region>:<accountId>:table/<glueDatabaseName>/<glueTableName>",
            "schemaName": "sampleSchemaName"
        }
    ],
    "outputSourceConfig": [
        {
            "outputS3Path": "s3://<bucketName>/prefix",
            "output": [
                {
                    "name": "id",
                    "hashed": false
                },
                {
                    "name": "email",
                    "hashed": false
                },
                {
                    "name": "gender",
                    "hashed": false
                }
            ]
        }
    ],
    "resolutionTechniques": {
        "resolutionType": "ML_MATCHING"
    },
    "roleArn": "arn:aws:iam::<region>:role/passRoleArn"
}
```

## See Also
<a name="API_CreateMatchingWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/CreateMatchingWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/CreateMatchingWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/CreateMatchingWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/CreateMatchingWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/CreateMatchingWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/CreateMatchingWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/CreateMatchingWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/CreateMatchingWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/CreateMatchingWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/CreateMatchingWorkflow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
