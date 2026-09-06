---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ExportForms.html
---

# ExportForms
<a name="API_ExportForms"></a>

Exports form configurations to code that is ready to integrate into an Amplify app.

## Request Syntax
<a name="API_ExportForms_RequestSyntax"></a>

```
GET /export/app/{{appId}}/environment/{{environmentName}}/forms?nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ExportForms_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_ExportForms_RequestSyntax) **   <a name="amplifyuibuilder-ExportForms-request-uri-appId"></a>
The unique ID of the Amplify app to export forms to.
Required: Yes

 ** [environmentName](#API_ExportForms_RequestSyntax) **   <a name="amplifyuibuilder-ExportForms-request-uri-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Required: Yes

 ** [nextToken](#API_ExportForms_RequestSyntax) **   <a name="amplifyuibuilder-ExportForms-request-uri-nextToken"></a>
The token to request the next page of results.

## Request Body
<a name="API_ExportForms_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ExportForms_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "entities": [
      {
         "appId": "string",
         "cta": {
            "cancel": {
               "children": "string",
               "excluded": boolean,
               "position": { ... }
            },
            "clear": {
               "children": "string",
               "excluded": boolean,
               "position": { ... }
            },
            "position": "string",
            "submit": {
               "children": "string",
               "excluded": boolean,
               "position": { ... }
            }
         },
         "dataType": {
            "dataSourceType": "string",
            "dataTypeName": "string"
         },
         "environmentName": "string",
         "fields": {
            "string" : {
               "excluded": boolean,
               "inputType": {
                  "defaultChecked": boolean,
                  "defaultCountryCode": "string",
                  "defaultValue": "string",
                  "descriptiveText": "string",
                  "fileUploaderConfig": {
                     "acceptedFileTypes": [ "string" ],
                     "accessLevel": "string",
                     "isResumable": boolean,
                     "maxFileCount": number,
                     "maxSize": number,
                     "showThumbnails": boolean
                  },
                  "isArray": boolean,
                  "maxValue": number,
                  "minValue": number,
                  "name": "string",
                  "placeholder": "string",
                  "readOnly": boolean,
                  "required": boolean,
                  "step": number,
                  "type": "string",
                  "value": "string",
                  "valueMappings": {
                     "bindingProperties": {
                        "string" : {
                           "bindingProperties": {
                              "model": "string"
                           },
                           "type": "string"
                        }
                     },
                     "values": [
                        {
                           "displayValue": {
                              "bindingProperties": {
                                 "field": "string",
                                 "property": "string"
                              },
                              "concat": [
                                 "FormInputValueProperty"
                              ],
                              "value": "string"
                           },
                           "value": {
                              "bindingProperties": {
                                 "field": "string",
                                 "property": "string"
                              },
                              "concat": [
                                 "FormInputValueProperty"
                              ],
                              "value": "string"
                           }
                        }
                     ]
                  }
               },
               "label": "string",
               "position": { ... },
               "validations": [
                  {
                     "numValues": [ number ],
                     "strValues": [ "string" ],
                     "type": "string",
                     "validationMessage": "string"
                  }
               ]
            }
         },
         "formActionType": "string",
         "id": "string",
         "labelDecorator": "string",
         "name": "string",
         "schemaVersion": "string",
         "sectionalElements": {
            "string" : {
               "excluded": boolean,
               "level": number,
               "orientation": "string",
               "position": { ... },
               "text": "string",
               "type": "string"
            }
         },
         "style": {
            "horizontalGap": { ... },
            "outerPadding": { ... },
            "verticalGap": { ... }
         },
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ExportForms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entities](#API_ExportForms_ResponseSyntax) **   <a name="amplifyuibuilder-ExportForms-response-entities"></a>
Represents the configuration of the exported forms.
Type: Array of [Form](API_Form.md) objects

 ** [nextToken](#API_ExportForms_ResponseSyntax) **   <a name="amplifyuibuilder-ExportForms-response-nextToken"></a>
The pagination token that's included if more results are available.
Type: String

## Errors
<a name="API_ExportForms_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Please retry your request.
HTTP Status Code: 500

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_ExportForms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/ExportForms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/ExportForms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ExportForms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/ExportForms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ExportForms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/ExportForms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/ExportForms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/ExportForms)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/ExportForms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ExportForms)
