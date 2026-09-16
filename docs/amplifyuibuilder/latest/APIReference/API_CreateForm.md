---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CreateForm.html
---

# CreateForm
<a name="API_CreateForm"></a>

Creates a new form for an Amplify app.

## Request Syntax
<a name="API_CreateForm_RequestSyntax"></a>

```
POST /app/{{appId}}/environment/{{environmentName}}/forms?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "cta": {
      "cancel": {
         "children": "{{string}}",
         "excluded": {{boolean}},
         "position": { ... }
      },
      "clear": {
         "children": "{{string}}",
         "excluded": {{boolean}},
         "position": { ... }
      },
      "position": "{{string}}",
      "submit": {
         "children": "{{string}}",
         "excluded": {{boolean}},
         "position": { ... }
      }
   },
   "dataType": {
      "dataSourceType": "{{string}}",
      "dataTypeName": "{{string}}"
   },
   "fields": {
      "{{string}}" : {
         "excluded": {{boolean}},
         "inputType": {
            "defaultChecked": {{boolean}},
            "defaultCountryCode": "{{string}}",
            "defaultValue": "{{string}}",
            "descriptiveText": "{{string}}",
            "fileUploaderConfig": {
               "acceptedFileTypes": [ "{{string}}" ],
               "accessLevel": "{{string}}",
               "isResumable": {{boolean}},
               "maxFileCount": {{number}},
               "maxSize": {{number}},
               "showThumbnails": {{boolean}}
            },
            "isArray": {{boolean}},
            "maxValue": {{number}},
            "minValue": {{number}},
            "name": "{{string}}",
            "placeholder": "{{string}}",
            "readOnly": {{boolean}},
            "required": {{boolean}},
            "step": {{number}},
            "type": "{{string}}",
            "value": "{{string}}",
            "valueMappings": {
               "bindingProperties": {
                  "{{string}}" : {
                     "bindingProperties": {
                        "model": "{{string}}"
                     },
                     "type": "{{string}}"
                  }
               },
               "values": [
                  {
                     "displayValue": {
                        "bindingProperties": {
                           "field": "{{string}}",
                           "property": "{{string}}"
                        },
                        "concat": [
                           "FormInputValueProperty"
                        ],
                        "value": "{{string}}"
                     },
                     "value": {
                        "bindingProperties": {
                           "field": "{{string}}",
                           "property": "{{string}}"
                        },
                        "concat": [
                           "FormInputValueProperty"
                        ],
                        "value": "{{string}}"
                     }
                  }
               ]
            }
         },
         "label": "{{string}}",
         "position": { ... },
         "validations": [
            {
               "numValues": [ {{number}} ],
               "strValues": [ "{{string}}" ],
               "type": "{{string}}",
               "validationMessage": "{{string}}"
            }
         ]
      }
   },
   "formActionType": "{{string}}",
   "labelDecorator": "{{string}}",
   "name": "{{string}}",
   "schemaVersion": "{{string}}",
   "sectionalElements": {
      "{{string}}" : {
         "excluded": {{boolean}},
         "level": {{number}},
         "orientation": "{{string}}",
         "position": { ... },
         "text": "{{string}}",
         "type": "{{string}}"
      }
   },
   "style": {
      "horizontalGap": { ... },
      "outerPadding": { ... },
      "verticalGap": { ... }
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateForm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-uri-appId"></a>
The unique ID of the Amplify app to associate with the form.
Required: Yes

 ** [clientToken](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-uri-clientToken"></a>
The unique client token.

 ** [environmentName](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-uri-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Required: Yes

## Request Body
<a name="API_CreateForm_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [cta](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-cta"></a>
The `FormCTA` object that stores the call to action configuration for the form.
Type: [FormCTA](API_FormCTA.md) object
Required: No

 ** [dataType](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-dataType"></a>
The type of data source to use to create the form.
Type: [FormDataTypeConfig](API_FormDataTypeConfig.md) object
Required: Yes

 ** [fields](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-fields"></a>
The configuration information for the form's fields.
Type: String to [FieldConfig](API_FieldConfig.md) object map
Required: Yes

 ** [formActionType](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-formActionType"></a>
Specifies whether to perform a create or update action on the form.
Type: String
Valid Values: `create | update`
Required: Yes

 ** [labelDecorator](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-labelDecorator"></a>
Specifies an icon or decoration to display on the form.
Type: String
Valid Values: `required | optional | none`
Required: No

 ** [name](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-name"></a>
The name of the form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [schemaVersion](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-schemaVersion"></a>
The schema version of the form.
Type: String
Required: Yes

 ** [sectionalElements](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-sectionalElements"></a>
The configuration information for the visual helper elements for the form. These elements are not associated with any data.
Type: String to [SectionalElement](API_SectionalElement.md) object map
Required: Yes

 ** [style](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-style"></a>
The configuration for the form's style.
Type: [FormStyle](API_FormStyle.md) object
Required: Yes

 ** [tags](#API_CreateForm_RequestSyntax) **   <a name="amplifyuibuilder-CreateForm-request-tags"></a>
One or more key-value pairs to use when tagging the form data.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateForm_ResponseSyntax"></a>

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
<a name="API_CreateForm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appId](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-appId"></a>
The unique ID of the Amplify app associated with the form.
Type: String

 ** [cta](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-cta"></a>
Stores the call to action configuration for the form.
Type: [FormCTA](API_FormCTA.md) object

 ** [dataType](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-dataType"></a>
The type of data source to use to create the form.
Type: [FormDataTypeConfig](API_FormDataTypeConfig.md) object

 ** [environmentName](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Type: String

 ** [fields](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-fields"></a>
Stores the information about the form's fields.
Type: String to [FieldConfig](API_FieldConfig.md) object map

 ** [formActionType](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-formActionType"></a>
The operation to perform on the specified form.
Type: String
Valid Values: `create | update`

 ** [id](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-id"></a>
The unique ID of the form.
Type: String

 ** [labelDecorator](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-labelDecorator"></a>
Specifies an icon or decoration to display on the form.
Type: String
Valid Values: `required | optional | none`

 ** [name](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-name"></a>
The name of the form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [schemaVersion](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-schemaVersion"></a>
The schema version of the form when it was imported.
Type: String

 ** [sectionalElements](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-sectionalElements"></a>
Stores the visual helper elements for the form that are not associated with any data.
Type: String to [SectionalElement](API_SectionalElement.md) object map

 ** [style](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-style"></a>
Stores the configuration for the form's style.
Type: [FormStyle](API_FormStyle.md) object

 ** [tags](#API_CreateForm_ResponseSyntax) **   <a name="amplifyuibuilder-CreateForm-response-tags"></a>
One or more key-value pairs to use when tagging the form.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreateForm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Please retry your request.
HTTP Status Code: 500

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource specified in the request conflicts with an existing resource.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
HTTP Status Code: 402

## See Also
<a name="API_CreateForm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/CreateForm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/CreateForm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/CreateForm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/CreateForm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/CreateForm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/CreateForm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/CreateForm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/CreateForm)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/CreateForm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/CreateForm)
