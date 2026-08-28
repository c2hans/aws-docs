---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateEventTrigger.html
---

# CreateEventTrigger
<a name="API_connect-customer-profiles_CreateEventTrigger"></a>

Creates an event trigger, which specifies the rules when to perform action based on customer's ingested data.

Each event stream can be associated with only one integration in the same region and AWS account as the event stream.

## Request Syntax
<a name="API_connect-customer-profiles_CreateEventTrigger_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/event-triggers/{{EventTriggerName}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "EventTriggerConditions": [
      {
         "EventTriggerDimensions": [
            {
               "ObjectAttributes": [
                  {
                     "ComparisonOperator": "{{string}}",
                     "FieldName": "{{string}}",
                     "Source": "{{string}}",
                     "Values": [ "{{string}}" ]
                  }
               ]
            }
         ],
         "LogicalOperator": "{{string}}"
      }
   ],
   "EventTriggerLimits": {
      "EventExpiration": {{number}},
      "Periods": [
         {
            "MaxInvocationsPerProfile": {{number}},
            "Unit": "{{string}}",
            "Unlimited": {{boolean}},
            "Value": {{number}}
         }
      ]
   },
   "ObjectTypeName": "{{string}}",
   "SegmentFilter": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_CreateEventTrigger_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_CreateEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [EventTriggerName](#API_connect-customer-profiles_CreateEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-request-uri-EventTriggerName"></a>
The unique name of the event trigger.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_CreateEventTrigger_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_connect-customer-profiles_CreateEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-request-Description"></a>
The description of the event trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [EventTriggerConditions](#API_connect-customer-profiles_CreateEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-request-EventTriggerConditions"></a>
A list of conditions that determine when an event should trigger the destination.
Type: Array of [EventTriggerCondition](API_connect-customer-profiles_EventTriggerCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** [EventTriggerLimits](#API_connect-customer-profiles_CreateEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-request-EventTriggerLimits"></a>
Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.
Type: [EventTriggerLimits](API_connect-customer-profiles_EventTriggerLimits.md) object
Required: No

 ** [ObjectTypeName](#API_connect-customer-profiles_CreateEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-request-ObjectTypeName"></a>
The unique name of the object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

 ** [SegmentFilter](#API_connect-customer-profiles_CreateEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-request-SegmentFilter"></a>
The destination is triggered only for profiles that meet the criteria of a segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** [Tags](#API_connect-customer-profiles_CreateEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-request-Tags"></a>
An array of key-value pairs to apply to this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_CreateEventTrigger_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "Description": "string",
   "EventTriggerConditions": [
      {
         "EventTriggerDimensions": [
            {
               "ObjectAttributes": [
                  {
                     "ComparisonOperator": "string",
                     "FieldName": "string",
                     "Source": "string",
                     "Values": [ "string" ]
                  }
               ]
            }
         ],
         "LogicalOperator": "string"
      }
   ],
   "EventTriggerLimits": {
      "EventExpiration": number,
      "Periods": [
         {
            "MaxInvocationsPerProfile": number,
            "Unit": "string",
            "Unlimited": boolean,
            "Value": number
         }
      ]
   },
   "EventTriggerName": "string",
   "LastUpdatedAt": number,
   "ObjectTypeName": "string",
   "SegmentFilter": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-customer-profiles_CreateEventTrigger_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_CreateEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-response-CreatedAt"></a>
The timestamp of when the event trigger was created.
Type: Timestamp

 ** [Description](#API_connect-customer-profiles_CreateEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-response-Description"></a>
The description of the event trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [EventTriggerConditions](#API_connect-customer-profiles_CreateEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-response-EventTriggerConditions"></a>
A list of conditions that determine when an event should trigger the destination.
Type: Array of [EventTriggerCondition](API_connect-customer-profiles_EventTriggerCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [EventTriggerLimits](#API_connect-customer-profiles_CreateEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-response-EventTriggerLimits"></a>
Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.
Type: [EventTriggerLimits](API_connect-customer-profiles_EventTriggerLimits.md) object

 ** [EventTriggerName](#API_connect-customer-profiles_CreateEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-response-EventTriggerName"></a>
The unique name of the event trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [LastUpdatedAt](#API_connect-customer-profiles_CreateEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-response-LastUpdatedAt"></a>
The timestamp of when the event trigger was most recently updated.
Type: Timestamp

 ** [ObjectTypeName](#API_connect-customer-profiles_CreateEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-response-ObjectTypeName"></a>
The unique name of the object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`

 ** [SegmentFilter](#API_connect-customer-profiles_CreateEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-response-SegmentFilter"></a>
The destination is triggered only for profiles that meet the criteria of a segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [Tags](#API_connect-customer-profiles_CreateEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateEventTrigger-response-Tags"></a>
An array of key-value pairs to apply to this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-customer-profiles_CreateEventTrigger_Errors"></a>

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
<a name="API_connect-customer-profiles_CreateEventTrigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/CreateEventTrigger)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/CreateEventTrigger)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CreateEventTrigger)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/CreateEventTrigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CreateEventTrigger)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/CreateEventTrigger)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/CreateEventTrigger)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/CreateEventTrigger)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/CreateEventTrigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CreateEventTrigger)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
