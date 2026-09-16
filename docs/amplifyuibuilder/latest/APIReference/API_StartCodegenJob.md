---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_StartCodegenJob.html
---

# StartCodegenJob
<a name="API_StartCodegenJob"></a>

Starts a code generation job for a specified Amplify app and backend environment.

## Request Syntax
<a name="API_StartCodegenJob_RequestSyntax"></a>

```
POST /app/{{appId}}/environment/{{environmentName}}/codegen-jobs?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "autoGenerateForms": {{boolean}},
   "features": {
      "isNonModelSupported": {{boolean}},
      "isRelationshipSupported": {{boolean}}
   },
   "genericDataSchema": {
      "dataSourceType": "{{string}}",
      "enums": {
         "{{string}}" : {
            "values": [ "{{string}}" ]
         }
      },
      "models": {
         "{{string}}" : {
            "fields": {
               "{{string}}" : {
                  "dataType": "{{string}}",
                  "dataTypeValue": "{{string}}",
                  "isArray": {{boolean}},
                  "readOnly": {{boolean}},
                  "relationship": {
                     "associatedFields": [ "{{string}}" ],
                     "belongsToFieldOnRelatedModel": "{{string}}",
                     "canUnlinkAssociatedModel": {{boolean}},
                     "isHasManyIndex": {{boolean}},
                     "relatedJoinFieldName": "{{string}}",
                     "relatedJoinTableName": "{{string}}",
                     "relatedModelFields": [ "{{string}}" ],
                     "relatedModelName": "{{string}}",
                     "type": "{{string}}"
                  },
                  "required": {{boolean}}
               }
            },
            "isJoinTable": {{boolean}},
            "primaryKeys": [ "{{string}}" ]
         }
      },
      "nonModels": {
         "{{string}}" : {
            "fields": {
               "{{string}}" : {
                  "dataType": "{{string}}",
                  "dataTypeValue": "{{string}}",
                  "isArray": {{boolean}},
                  "readOnly": {{boolean}},
                  "relationship": {
                     "associatedFields": [ "{{string}}" ],
                     "belongsToFieldOnRelatedModel": "{{string}}",
                     "canUnlinkAssociatedModel": {{boolean}},
                     "isHasManyIndex": {{boolean}},
                     "relatedJoinFieldName": "{{string}}",
                     "relatedJoinTableName": "{{string}}",
                     "relatedModelFields": [ "{{string}}" ],
                     "relatedModelName": "{{string}}",
                     "type": "{{string}}"
                  },
                  "required": {{boolean}}
               }
            }
         }
      }
   },
   "renderConfig": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartCodegenJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_StartCodegenJob_RequestSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-request-uri-appId"></a>
The unique ID for the Amplify app.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `d[a-z0-9]+`
Required: Yes

 ** [clientToken](#API_StartCodegenJob_RequestSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-request-uri-clientToken"></a>
The idempotency token used to ensure that the code generation job request completes only once.

 ** [environmentName](#API_StartCodegenJob_RequestSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-request-uri-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Required: Yes

## Request Body
<a name="API_StartCodegenJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [autoGenerateForms](#API_StartCodegenJob_RequestSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-request-autoGenerateForms"></a>
Specifies whether to autogenerate forms in the code generation job.
Type: Boolean
Required: No

 ** [features](#API_StartCodegenJob_RequestSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-request-features"></a>
The feature flags for a code generation job.
Type: [CodegenFeatureFlags](API_CodegenFeatureFlags.md) object
Required: No

 ** [genericDataSchema](#API_StartCodegenJob_RequestSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-request-genericDataSchema"></a>
The data schema to use for a code generation job.
Type: [CodegenJobGenericDataSchema](API_CodegenJobGenericDataSchema.md) object
Required: No

 ** [renderConfig](#API_StartCodegenJob_RequestSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-request-renderConfig"></a>
The code generation configuration for the codegen job.
Type: [CodegenJobRenderConfig](API_CodegenJobRenderConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [tags](#API_StartCodegenJob_RequestSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-request-tags"></a>
One or more key-value pairs to use when tagging the code generation job data.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartCodegenJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appId": "string",
   "asset": {
      "downloadUrl": "string"
   },
   "autoGenerateForms": boolean,
   "createdAt": "string",
   "dependencies": [
      {
         "isSemVer": boolean,
         "name": "string",
         "reason": "string",
         "supportedVersion": "string"
      }
   ],
   "environmentName": "string",
   "features": {
      "isNonModelSupported": boolean,
      "isRelationshipSupported": boolean
   },
   "genericDataSchema": {
      "dataSourceType": "string",
      "enums": {
         "string" : {
            "values": [ "string" ]
         }
      },
      "models": {
         "string" : {
            "fields": {
               "string" : {
                  "dataType": "string",
                  "dataTypeValue": "string",
                  "isArray": boolean,
                  "readOnly": boolean,
                  "relationship": {
                     "associatedFields": [ "string" ],
                     "belongsToFieldOnRelatedModel": "string",
                     "canUnlinkAssociatedModel": boolean,
                     "isHasManyIndex": boolean,
                     "relatedJoinFieldName": "string",
                     "relatedJoinTableName": "string",
                     "relatedModelFields": [ "string" ],
                     "relatedModelName": "string",
                     "type": "string"
                  },
                  "required": boolean
               }
            },
            "isJoinTable": boolean,
            "primaryKeys": [ "string" ]
         }
      },
      "nonModels": {
         "string" : {
            "fields": {
               "string" : {
                  "dataType": "string",
                  "dataTypeValue": "string",
                  "isArray": boolean,
                  "readOnly": boolean,
                  "relationship": {
                     "associatedFields": [ "string" ],
                     "belongsToFieldOnRelatedModel": "string",
                     "canUnlinkAssociatedModel": boolean,
                     "isHasManyIndex": boolean,
                     "relatedJoinFieldName": "string",
                     "relatedJoinTableName": "string",
                     "relatedModelFields": [ "string" ],
                     "relatedModelName": "string",
                     "type": "string"
                  },
                  "required": boolean
               }
            }
         }
      }
   },
   "id": "string",
   "modifiedAt": "string",
   "renderConfig": { ... },
   "status": "string",
   "statusMessage": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_StartCodegenJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appId](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-appId"></a>
The ID of the Amplify app associated with the code generation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `d[a-z0-9]+`

 ** [asset](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-asset"></a>
The `CodegenJobAsset` to use for the code generation job.
Type: [CodegenJobAsset](API_CodegenJobAsset.md) object

 ** [autoGenerateForms](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-autoGenerateForms"></a>
Specifies whether to autogenerate forms in the code generation job.
Type: Boolean

 ** [createdAt](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-createdAt"></a>
The time that the code generation job was created.
Type: Timestamp

 ** [dependencies](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-dependencies"></a>
Lists the dependency packages that may be required for the project code to run.
Type: Array of [CodegenDependency](API_CodegenDependency.md) objects

 ** [environmentName](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-environmentName"></a>
The name of the backend environment associated with the code generation job.
Type: String

 ** [features](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-features"></a>
Describes the feature flags that you can specify for a code generation job.
Type: [CodegenFeatureFlags](API_CodegenFeatureFlags.md) object

 ** [genericDataSchema](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-genericDataSchema"></a>
Describes the data schema for a code generation job.
Type: [CodegenJobGenericDataSchema](API_CodegenJobGenericDataSchema.md) object

 ** [id](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-id"></a>
The unique ID for the code generation job.
Type: String

 ** [modifiedAt](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-modifiedAt"></a>
The time that the code generation job was modified.
Type: Timestamp

 ** [renderConfig](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-renderConfig"></a>
Describes the configuration information for rendering the UI component associated with the code generation job.
Type: [CodegenJobRenderConfig](API_CodegenJobRenderConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-status"></a>
The status of the code generation job.
Type: String
Valid Values: `in_progress | failed | succeeded`

 ** [statusMessage](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-statusMessage"></a>
The customized status message for the code generation job.
Type: String

 ** [tags](#API_StartCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-StartCodegenJob-response-tags"></a>
One or more key-value pairs to use when tagging the code generation job.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_StartCodegenJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Please retry your request.
HTTP Status Code: 500

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_StartCodegenJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/StartCodegenJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/StartCodegenJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/StartCodegenJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/StartCodegenJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/StartCodegenJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/StartCodegenJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/StartCodegenJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/StartCodegenJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/StartCodegenJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/StartCodegenJob)
