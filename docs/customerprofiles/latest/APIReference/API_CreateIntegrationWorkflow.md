---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateIntegrationWorkflow.html
---

# CreateIntegrationWorkflow
<a name="API_connect-customer-profiles_CreateIntegrationWorkflow"></a>

 Creates an integration workflow. An integration workflow is an async process which ingests historic data and sets up an integration for ongoing updates. The supported Amazon AppFlow sources are Salesforce, ServiceNow, and Marketo.

## Request Syntax
<a name="API_connect-customer-profiles_CreateIntegrationWorkflow_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/workflows/integrations HTTP/1.1
Content-type: application/json

{
   "IntegrationConfig": {
      "AppflowIntegration": {
         "Batches": [
            {
               "EndTime": {{number}},
               "StartTime": {{number}}
            }
         ],
         "FlowDefinition": {
            "Description": "{{string}}",
            "FlowName": "{{string}}",
            "KmsArn": "{{string}}",
            "SourceFlowConfig": {
               "ConnectorProfileName": "{{string}}",
               "ConnectorType": "{{string}}",
               "IncrementalPullConfig": {
                  "DatetimeTypeFieldName": "{{string}}"
               },
               "SourceConnectorProperties": {
                  "Marketo": {
                     "Object": "{{string}}"
                  },
                  "S3": {
                     "BucketName": "{{string}}",
                     "BucketPrefix": "{{string}}"
                  },
                  "Salesforce": {
                     "EnableDynamicFieldUpdate": {{boolean}},
                     "IncludeDeletedRecords": {{boolean}},
                     "Object": "{{string}}"
                  },
                  "ServiceNow": {
                     "Object": "{{string}}"
                  },
                  "Zendesk": {
                     "Object": "{{string}}"
                  }
               }
            },
            "Tasks": [
               {
                  "ConnectorOperator": {
                     "Marketo": "{{string}}",
                     "S3": "{{string}}",
                     "Salesforce": "{{string}}",
                     "ServiceNow": "{{string}}",
                     "Zendesk": "{{string}}"
                  },
                  "DestinationField": "{{string}}",
                  "SourceFields": [ "{{string}}" ],
                  "TaskProperties": {
                     "{{string}}" : "{{string}}"
                  },
                  "TaskType": "{{string}}"
               }
            ],
            "TriggerConfig": {
               "TriggerProperties": {
                  "Scheduled": {
                     "DataPullMode": "{{string}}",
                     "FirstExecutionFrom": {{number}},
                     "ScheduleEndTime": {{number}},
                     "ScheduleExpression": "{{string}}",
                     "ScheduleOffset": {{number}},
                     "ScheduleStartTime": {{number}},
                     "Timezone": "{{string}}"
                  }
               },
               "TriggerType": "{{string}}"
            }
         }
      }
   },
   "ObjectTypeName": "{{string}}",
   "RoleArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "WorkflowType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_CreateIntegrationWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_CreateIntegrationWorkflow_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateIntegrationWorkflow-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_CreateIntegrationWorkflow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IntegrationConfig](#API_connect-customer-profiles_CreateIntegrationWorkflow_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateIntegrationWorkflow-request-IntegrationConfig"></a>
Configuration data for integration workflow.
Type: [IntegrationConfig](API_connect-customer-profiles_IntegrationConfig.md) object
Required: Yes

 ** [ObjectTypeName](#API_connect-customer-profiles_CreateIntegrationWorkflow_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateIntegrationWorkflow-request-ObjectTypeName"></a>
The name of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

 ** [RoleArn](#API_connect-customer-profiles_CreateIntegrationWorkflow_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateIntegrationWorkflow-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. Customer Profiles assumes this role to create resources on your behalf as part of workflow execution.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:iam:.*:[0-9]+:.*`
Required: Yes

 ** [Tags](#API_connect-customer-profiles_CreateIntegrationWorkflow_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateIntegrationWorkflow-request-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [WorkflowType](#API_connect-customer-profiles_CreateIntegrationWorkflow_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateIntegrationWorkflow-request-WorkflowType"></a>
The type of workflow. The only supported value is APPFLOW\_INTEGRATION.
Type: String
Valid Values: `APPFLOW_INTEGRATION`
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_CreateIntegrationWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Message": "string",
   "WorkflowId": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_CreateIntegrationWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Message](#API_connect-customer-profiles_CreateIntegrationWorkflow_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateIntegrationWorkflow-response-Message"></a>
A message indicating create request was received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [WorkflowId](#API_connect-customer-profiles_CreateIntegrationWorkflow_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateIntegrationWorkflow-response-WorkflowId"></a>
Unique identifier for the workflow.
Type: String
Pattern: `[a-f0-9]{32}`

## Errors
<a name="API_connect-customer-profiles_CreateIntegrationWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_CreateIntegrationWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/CreateIntegrationWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/CreateIntegrationWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CreateIntegrationWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/CreateIntegrationWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CreateIntegrationWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/CreateIntegrationWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/CreateIntegrationWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/CreateIntegrationWorkflow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/CreateIntegrationWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CreateIntegrationWorkflow)
