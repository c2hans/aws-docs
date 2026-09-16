---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetEventTrigger.html
---

# GetEventTrigger
<a name="API_connect-customer-profiles_GetEventTrigger"></a>

Get a specific Event Trigger from the domain.

## Request Syntax
<a name="API_connect-customer-profiles_GetEventTrigger_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/event-triggers/{{EventTriggerName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetEventTrigger_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetEventTrigger-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [EventTriggerName](#API_connect-customer-profiles_GetEventTrigger_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetEventTrigger-request-uri-EventTriggerName"></a>
The unique name of the event trigger.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetEventTrigger_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetEventTrigger_ResponseSyntax"></a>

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
<a name="API_connect-customer-profiles_GetEventTrigger_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_GetEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventTrigger-response-CreatedAt"></a>
The timestamp of when the event trigger was created.
Type: Timestamp

 ** [Description](#API_connect-customer-profiles_GetEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventTrigger-response-Description"></a>
The description of the event trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [EventTriggerConditions](#API_connect-customer-profiles_GetEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventTrigger-response-EventTriggerConditions"></a>
A list of conditions that determine when an event should trigger the destination.
Type: Array of [EventTriggerCondition](API_connect-customer-profiles_EventTriggerCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [EventTriggerLimits](#API_connect-customer-profiles_GetEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventTrigger-response-EventTriggerLimits"></a>
Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.
Type: [EventTriggerLimits](API_connect-customer-profiles_EventTriggerLimits.md) object

 ** [EventTriggerName](#API_connect-customer-profiles_GetEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventTrigger-response-EventTriggerName"></a>
The unique name of the event trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [LastUpdatedAt](#API_connect-customer-profiles_GetEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventTrigger-response-LastUpdatedAt"></a>
The timestamp of when the event trigger was most recently updated.
Type: Timestamp

 ** [ObjectTypeName](#API_connect-customer-profiles_GetEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventTrigger-response-ObjectTypeName"></a>
The unique name of the object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`

 ** [SegmentFilter](#API_connect-customer-profiles_GetEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventTrigger-response-SegmentFilter"></a>
The destination is triggered only for profiles that meet the criteria of a segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [Tags](#API_connect-customer-profiles_GetEventTrigger_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetEventTrigger-response-Tags"></a>
An array of key-value pairs to apply to this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-customer-profiles_GetEventTrigger_Errors"></a>

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
<a name="API_connect-customer-profiles_GetEventTrigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetEventTrigger)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetEventTrigger)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetEventTrigger)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetEventTrigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetEventTrigger)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetEventTrigger)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetEventTrigger)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetEventTrigger)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetEventTrigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetEventTrigger)
