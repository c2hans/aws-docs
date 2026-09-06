---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetPropertyValue.html
---

# GetPropertyValue
<a name="API_GetPropertyValue"></a>

Gets the property values for a component, component type, entity, or workspace.

You must specify a value for either `componentName`, `componentTypeId`, `entityId`, or `workspaceId`.

## Request Syntax
<a name="API_GetPropertyValue_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/entity-properties/value HTTP/1.1
Content-type: application/json

{
   "componentName": "{{string}}",
   "componentPath": "{{string}}",
   "componentTypeId": "{{string}}",
   "entityId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "propertyGroupName": "{{string}}",
   "selectedProperties": [ "{{string}}" ],
   "tabularConditions": {
      "orderBy": [
         {
            "order": "{{string}}",
            "propertyName": "{{string}}"
         }
      ],
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
      ]
   }
}
```

## URI Request Parameters
<a name="API_GetPropertyValue_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_GetPropertyValue_RequestSyntax) **   <a name="tm-GetPropertyValue-request-uri-workspaceId"></a>
The ID of the workspace whose values the operation returns.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_GetPropertyValue_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [componentName](#API_GetPropertyValue_RequestSyntax) **   <a name="tm-GetPropertyValue-request-componentName"></a>
The name of the component whose property values the operation returns.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** [componentPath](#API_GetPropertyValue_RequestSyntax) **   <a name="tm-GetPropertyValue-request-componentPath"></a>
This string specifies the path to the composite component, starting from the top-level component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z_\-0-9/]+`
Required: No

 ** [componentTypeId](#API_GetPropertyValue_RequestSyntax) **   <a name="tm-GetPropertyValue-request-componentTypeId"></a>
The ID of the component type whose property values the operation returns.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: No

 ** [entityId](#API_GetPropertyValue_RequestSyntax) **   <a name="tm-GetPropertyValue-request-entityId"></a>
The ID of the entity whose property values the operation returns.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: No

 ** [maxResults](#API_GetPropertyValue_RequestSyntax) **   <a name="tm-GetPropertyValue-request-maxResults"></a>
The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 200.
Required: No

 ** [nextToken](#API_GetPropertyValue_RequestSyntax) **   <a name="tm-GetPropertyValue-request-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`
Required: No

 ** [propertyGroupName](#API_GetPropertyValue_RequestSyntax) **   <a name="tm-GetPropertyValue-request-propertyGroupName"></a>
The property group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\-0-9]+`
Required: No

 ** [selectedProperties](#API_GetPropertyValue_RequestSyntax) **   <a name="tm-GetPropertyValue-request-selectedProperties"></a>
The properties whose values the operation returns.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** [tabularConditions](#API_GetPropertyValue_RequestSyntax) **   <a name="tm-GetPropertyValue-request-tabularConditions"></a>
The tabular conditions.
Type: [TabularConditions](API_TabularConditions.md) object
Required: No

## Response Syntax
<a name="API_GetPropertyValue_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "propertyValues": {
      "string" : {
         "propertyReference": {
            "componentName": "string",
            "componentPath": "string",
            "entityId": "string",
            "externalIdProperty": {
               "string" : "string"
            },
            "propertyName": "string"
         },
         "propertyValue": {
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
   },
   "tabularPropertyValues": [
      [
         {
            "string" : {
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
   ]
}
```

## Response Elements
<a name="API_GetPropertyValue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetPropertyValue_ResponseSyntax) **   <a name="tm-GetPropertyValue-response-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`

 ** [propertyValues](#API_GetPropertyValue_ResponseSyntax) **   <a name="tm-GetPropertyValue-response-propertyValues"></a>
An object that maps strings to the properties and latest property values in the response. Each string in the mapping must be unique to this object.
Type: String to [PropertyLatestValue](API_PropertyLatestValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`

 ** [tabularPropertyValues](#API_GetPropertyValue_ResponseSyntax) **   <a name="tm-GetPropertyValue-response-tabularPropertyValues"></a>
A table of property values.
Type: Array of arrays of string to [DataValue](API_DataValue.md) object maps
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`

## Errors
<a name="API_GetPropertyValue_Errors"></a>

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
<a name="API_GetPropertyValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/GetPropertyValue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/GetPropertyValue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/GetPropertyValue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/GetPropertyValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/GetPropertyValue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/GetPropertyValue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/GetPropertyValue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/GetPropertyValue)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/GetPropertyValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/GetPropertyValue)
