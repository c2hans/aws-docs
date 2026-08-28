---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_GetForm.html
---

# GetForm
<a name="API_GetForm"></a>

Returns an existing form for an Amplify app.

## Request Syntax
<a name="API_GetForm_RequestSyntax"></a>

```
GET /app/{{appId}}/environment/{{environmentName}}/forms/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetForm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_GetForm_RequestSyntax) **   <a name="amplifyuibuilder-GetForm-request-uri-appId"></a>
The unique ID of the Amplify app.
Required: Yes

 ** [environmentName](#API_GetForm_RequestSyntax) **   <a name="amplifyuibuilder-GetForm-request-uri-environmentName"></a>
The name of the backend environment that is part of the Amplify app.
Required: Yes

 ** [id](#API_GetForm_RequestSyntax) **   <a name="amplifyuibuilder-GetForm-request-uri-id"></a>
The unique ID of the form.
Required: Yes

## Request Body
<a name="API_GetForm_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetForm_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_GetForm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appId](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-appId"></a>
The unique ID of the Amplify app associated with the form.
Type: String

 ** [cta](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-cta"></a>
Stores the call to action configuration for the form.
Type: [FormCTA](API_FormCTA.md) object

 ** [dataType](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-dataType"></a>
The type of data source to use to create the form.
Type: [FormDataTypeConfig](API_FormDataTypeConfig.md) object

 ** [environmentName](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Type: String

 ** [fields](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-fields"></a>
Stores the information about the form's fields.
Type: String to [FieldConfig](API_FieldConfig.md) object map

 ** [formActionType](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-formActionType"></a>
The operation to perform on the specified form.
Type: String
Valid Values: `create | update`

 ** [id](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-id"></a>
The unique ID of the form.
Type: String

 ** [labelDecorator](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-labelDecorator"></a>
Specifies an icon or decoration to display on the form.
Type: String
Valid Values: `required | optional | none`

 ** [name](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-name"></a>
The name of the form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [schemaVersion](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-schemaVersion"></a>
The schema version of the form when it was imported.
Type: String

 ** [sectionalElements](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-sectionalElements"></a>
Stores the visual helper elements for the form that are not associated with any data.
Type: String to [SectionalElement](API_SectionalElement.md) object map

 ** [style](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-style"></a>
Stores the configuration for the form's style.
Type: [FormStyle](API_FormStyle.md) object

 ** [tags](#API_GetForm_ResponseSyntax) **   <a name="amplifyuibuilder-GetForm-response-tags"></a>
One or more key-value pairs to use when tagging the form.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_GetForm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Please retry your request.
HTTP Status Code: 500

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

## See Also
<a name="API_GetForm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/GetForm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/GetForm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/GetForm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/GetForm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/GetForm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/GetForm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/GetForm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/GetForm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/GetForm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/GetForm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
