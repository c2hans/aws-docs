---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetPropertyValueHistory.html
---

# GetPropertyValueHistory
<a name="API_GetPropertyValueHistory"></a>

Retrieves information about the history of a time series property value for a component, component type, entity, or workspace.

You must specify a value for `workspaceId`. For entity-specific queries, specify values for `componentName` and `entityId`. For cross-entity queries, specify a value for `componentTypeId`.

## Request Syntax
<a name="API_GetPropertyValueHistory_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/entity-properties/history HTTP/1.1
Content-type: application/json

{
   "componentName": "{{string}}",
   "componentPath": "{{string}}",
   "componentTypeId": "{{string}}",
   "endDateTime": {{number}},
   "endTime": "{{string}}",
   "entityId": "{{string}}",
   "interpolation": {
      "interpolationType": "{{string}}",
      "intervalInSeconds": {{number}}
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "orderByTime": "{{string}}",
   "propertyFilters": [
      {
         "operator": "{{string}}",
         "propertyName": "{{string}}",
         "value": {
            "booleanValue": {{boolean}},
            "doubleValue": {{number}},
            "expression": "{{string}}",
            "integerValue": {{number}},
            "listValue": [
               "DataValue"
            ],
            "longValue": {{number}},
            "mapValue": {
               "{{string}}" : "DataValue"
            },
            "relationshipValue": {
               "targetComponentName": "{{string}}",
               "targetEntityId": "{{string}}"
            },
            "stringValue": "{{string}}"
         }
      }
   ],
   "selectedProperties": [ "{{string}}" ],
   "startDateTime": {{number}},
   "startTime": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetPropertyValueHistory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-uri-workspaceId"></a>
The ID of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_GetPropertyValueHistory_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [componentName](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-componentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** [componentPath](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-componentPath"></a>
This string specifies the path to the composite component, starting from the top-level component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z_\-0-9/]+`
Required: No

 ** [componentTypeId](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-componentTypeId"></a>
The ID of the component type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: No

 ** [endDateTime](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-endDateTime"></a>
 *This parameter has been deprecated.*
The date and time of the latest property value to return.
Type: Timestamp
Required: No

 ** [endTime](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-endTime"></a>
The ISO8601 DateTime of the latest property value to return.
For more information about the ISO8601 DateTime format, see the data type [PropertyValue](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyValue.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 35.
Required: No

 ** [entityId](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-entityId"></a>
The ID of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: No

 ** [interpolation](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-interpolation"></a>
An object that specifies the interpolation type and the interval over which to interpolate data.
Type: [InterpolationParameters](API_InterpolationParameters.md) object
Required: No

 ** [maxResults](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-maxResults"></a>
The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 200.
Required: No

 ** [nextToken](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`
Required: No

 ** [orderByTime](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-orderByTime"></a>
The time direction to use in the result order.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

 ** [propertyFilters](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-propertyFilters"></a>
A list of objects that filter the property value history request.
Type: Array of [PropertyFilter](API_PropertyFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [selectedProperties](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-selectedProperties"></a>
A list of properties whose value histories the request retrieves.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** [startDateTime](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-startDateTime"></a>
 *This parameter has been deprecated.*
The date and time of the earliest property value to return.
Type: Timestamp
Required: No

 ** [startTime](#API_GetPropertyValueHistory_RequestSyntax) **   <a name="tm-GetPropertyValueHistory-request-startTime"></a>
The ISO8601 DateTime of the earliest property value to return.
For more information about the ISO8601 DateTime format, see the data type [PropertyValue](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyValue.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 35.
Required: No

## Response Syntax
<a name="API_GetPropertyValueHistory_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "propertyValues": [
      {
         "entityPropertyReference": {
            "componentName": "string",
            "componentPath": "string",
            "entityId": "string",
            "externalIdProperty": {
               "string" : "string"
            },
            "propertyName": "string"
         },
         "values": [
            {
               "time": "string",
               "timestamp": number,
               "value": {
                  "booleanValue": boolean,
                  "doubleValue": number,
                  "expression": "string",
                  "integerValue": number,
                  "listValue": [
                     "DataValue"
                  ],
                  "longValue": number,
                  "mapValue": {
                     "string" : "DataValue"
                  },
                  "relationshipValue": {
                     "targetComponentName": "string",
                     "targetEntityId": "string"
                  },
                  "stringValue": "string"
               }
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetPropertyValueHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetPropertyValueHistory_ResponseSyntax) **   <a name="tm-GetPropertyValueHistory-response-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`

 ** [propertyValues](#API_GetPropertyValueHistory_ResponseSyntax) **   <a name="tm-GetPropertyValueHistory-response-propertyValues"></a>
An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.
Type: Array of [PropertyValueHistory](API_PropertyValueHistory.md) objects

## Errors
<a name="API_GetPropertyValueHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConnectorFailureException **
The connector failed.
HTTP Status Code: 424

 ** ConnectorTimeoutException **
The connector timed out.
HTTP Status Code: 424

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_GetPropertyValueHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/GetPropertyValueHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/GetPropertyValueHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/GetPropertyValueHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/GetPropertyValueHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/GetPropertyValueHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/GetPropertyValueHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/GetPropertyValueHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/GetPropertyValueHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/GetPropertyValueHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/GetPropertyValueHistory)
