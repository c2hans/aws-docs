---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutIntegration.html
---

# PutIntegration
<a name="API_connect-customer-profiles_PutIntegration"></a>

Adds an integration between the service and a third-party service, which includes Amazon AppFlow and Amazon Connect.

An integration can belong to only one domain.

To add or remove tags on an existing Integration, see [ TagResource ](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html)/[ UntagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html).

## Request Syntax
<a name="API_connect-customer-profiles_PutIntegration_RequestSyntax"></a>

```
PUT /domains/{{DomainName}}/integrations HTTP/1.1
Content-type: application/json

{
   "EventTriggerNames": [ "{{string}}" ],
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
   },
   "ObjectTypeName": "{{string}}",
   "ObjectTypeNames": {
      "{{string}}" : "{{string}}"
   },
   "RoleArn": "{{string}}",
   "Scope": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Uri": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_PutIntegration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_PutIntegration_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_PutIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EventTriggerNames](#API_connect-customer-profiles_PutIntegration_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-request-EventTriggerNames"></a>
A list of unique names for active event triggers associated with the integration.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** [FlowDefinition](#API_connect-customer-profiles_PutIntegration_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-request-FlowDefinition"></a>
The configuration that controls how Customer Profiles retrieves data from the source.
Type: [FlowDefinition](API_connect-customer-profiles_FlowDefinition.md) object
Required: No

 ** [ObjectTypeName](#API_connect-customer-profiles_PutIntegration_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-request-ObjectTypeName"></a>
The name of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: No

 ** [ObjectTypeNames](#API_connect-customer-profiles_PutIntegration_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-request-ObjectTypeNames"></a>
A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an `ObjectTypeName` (template) used to ingest the event. It supports the following event types: `SegmentIdentify`, `ShopifyCreateCustomers`, `ShopifyUpdateCustomers`, `ShopifyCreateDraftOrders`, `ShopifyUpdateDraftOrders`, `ShopifyCreateOrders`, and `ShopifyUpdatedOrders`.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: No

 ** [RoleArn](#API_connect-customer-profiles_PutIntegration_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. The Integration uses this role to make Customer Profiles requests on your behalf.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:iam:.*:[0-9]+:.*`
Required: No

 ** [Scope](#API_connect-customer-profiles_PutIntegration_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-request-Scope"></a>
Specifies whether the integration applies to profile level data (associated with profiles) or domain level data (not associated with any specific profile). The default value is PROFILE.
Type: String
Valid Values: `PROFILE | DOMAIN`
Required: No

 ** [Tags](#API_connect-customer-profiles_PutIntegration_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-request-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [Uri](#API_connect-customer-profiles_PutIntegration_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-request-Uri"></a>
The URI of the S3 bucket or any other type of data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_PutIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "DomainName": "string",
   "EventTriggerNames": [ "string" ],
   "IsUnstructured": boolean,
   "LastUpdatedAt": number,
   "ObjectTypeName": "string",
   "ObjectTypeNames": {
      "string" : "string"
   },
   "RoleArn": "string",
   "Scope": "string",
   "Tags": {
      "string" : "string"
   },
   "Uri": "string",
   "WorkflowId": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_PutIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-CreatedAt"></a>
The timestamp of when the domain was created.
Type: Timestamp

 ** [DomainName](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [EventTriggerNames](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-EventTriggerNames"></a>
A list of unique names for active event triggers associated with the integration. This list would be empty if no Event Trigger is associated with the integration.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [IsUnstructured](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-IsUnstructured"></a>
Boolean that shows if the Flow that's associated with the Integration is created in Amazon Appflow, or with ObjectTypeName equals \_unstructured via API/CLI in flowDefinition.
Type: Boolean

 ** [LastUpdatedAt](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-LastUpdatedAt"></a>
The timestamp of when the domain was most recently edited.
Type: Timestamp

 ** [ObjectTypeName](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-ObjectTypeName"></a>
The name of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`

 ** [ObjectTypeNames](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-ObjectTypeNames"></a>
A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an `ObjectTypeName` (template) used to ingest the event. It supports the following event types: `SegmentIdentify`, `ShopifyCreateCustomers`, `ShopifyUpdateCustomers`, `ShopifyCreateDraftOrders`, `ShopifyUpdateDraftOrders`, `ShopifyCreateOrders`, and `ShopifyUpdatedOrders`.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`

 ** [RoleArn](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. The Integration uses this role to make Customer Profiles requests on your behalf.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:iam:.*:[0-9]+:.*`

 ** [Scope](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-Scope"></a>
Specifies whether the integration applies to profile level data (associated with profiles) or domain level data (not associated with any specific profile). The default value is PROFILE.
Type: String
Valid Values: `PROFILE | DOMAIN`

 ** [Tags](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

 ** [Uri](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-Uri"></a>
The URI of the S3 bucket or any other type of data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [WorkflowId](#API_connect-customer-profiles_PutIntegration_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutIntegration-response-WorkflowId"></a>
Unique identifier for the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_connect-customer-profiles_PutIntegration_Errors"></a>

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

## Examples
<a name="API_connect-customer-profiles_PutIntegration_Examples"></a>

### Example
<a name="API_connect-customer-profiles_PutIntegration_Example_1"></a>

This example illustrates one usage of PutIntegration.

#### Sample Request
<a name="API_connect-customer-profiles_PutIntegration_Example_1_Request"></a>

```
PUT /domains/ExampleDomainName/integrations HTTP/1.1

Content-type: application/json
{
   "ObjectTypeName": "MyCustomObject",
   "Uri": "arn:aws:flow:us-east-1:123456789012:URIOfIntegration1"
}
```

#### Sample Response
<a name="API_connect-customer-profiles_PutIntegration_Example_1_Response"></a>

```
Content-type: application/json
{
   "CreatedAt": 1479249799770,
    "DomainName": "ExampleDomainName",
    "LastUpdatedAt": 1479249799770,
    "ObjectTypeName": "MyCustomObject",
    "Uri": "arn:aws:flow:us-east-1:123456789012:URIOfIntegration1"
}
```

## See Also
<a name="API_connect-customer-profiles_PutIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/PutIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/PutIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/PutIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/PutIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/PutIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/PutIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/PutIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/PutIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/PutIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/PutIntegration)
