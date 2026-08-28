---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_GetCodegenJob.html
---

# GetCodegenJob
<a name="API_GetCodegenJob"></a>

Returns an existing code generation job.

## Request Syntax
<a name="API_GetCodegenJob_RequestSyntax"></a>

```
GET /app/{{appId}}/environment/{{environmentName}}/codegen-jobs/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCodegenJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_GetCodegenJob_RequestSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-request-uri-appId"></a>
The unique ID of the Amplify app associated with the code generation job.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `d[a-z0-9]+`
Required: Yes

 ** [environmentName](#API_GetCodegenJob_RequestSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-request-uri-environmentName"></a>
The name of the backend environment that is a part of the Amplify app associated with the code generation job.
Required: Yes

 ** [id](#API_GetCodegenJob_RequestSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-request-uri-id"></a>
The unique ID of the code generation job.
Required: Yes

## Request Body
<a name="API_GetCodegenJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCodegenJob_ResponseSyntax"></a>

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
<a name="API_GetCodegenJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appId](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-appId"></a>
The ID of the Amplify app associated with the code generation job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `d[a-z0-9]+`

 ** [asset](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-asset"></a>
The `CodegenJobAsset` to use for the code generation job.
Type: [CodegenJobAsset](API_CodegenJobAsset.md) object

 ** [autoGenerateForms](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-autoGenerateForms"></a>
Specifies whether to autogenerate forms in the code generation job.
Type: Boolean

 ** [createdAt](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-createdAt"></a>
The time that the code generation job was created.
Type: Timestamp

 ** [dependencies](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-dependencies"></a>
Lists the dependency packages that may be required for the project code to run.
Type: Array of [CodegenDependency](API_CodegenDependency.md) objects

 ** [environmentName](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-environmentName"></a>
The name of the backend environment associated with the code generation job.
Type: String

 ** [features](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-features"></a>
Describes the feature flags that you can specify for a code generation job.
Type: [CodegenFeatureFlags](API_CodegenFeatureFlags.md) object

 ** [genericDataSchema](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-genericDataSchema"></a>
Describes the data schema for a code generation job.
Type: [CodegenJobGenericDataSchema](API_CodegenJobGenericDataSchema.md) object

 ** [id](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-id"></a>
The unique ID for the code generation job.
Type: String

 ** [modifiedAt](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-modifiedAt"></a>
The time that the code generation job was modified.
Type: Timestamp

 ** [renderConfig](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-renderConfig"></a>
Describes the configuration information for rendering the UI component associated with the code generation job.
Type: [CodegenJobRenderConfig](API_CodegenJobRenderConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-status"></a>
The status of the code generation job.
Type: String
Valid Values: `in_progress | failed | succeeded`

 ** [statusMessage](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-statusMessage"></a>
The customized status message for the code generation job.
Type: String

 ** [tags](#API_GetCodegenJob_ResponseSyntax) **   <a name="amplifyuibuilder-GetCodegenJob-response-tags"></a>
One or more key-value pairs to use when tagging the code generation job.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_GetCodegenJob_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_GetCodegenJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/GetCodegenJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/GetCodegenJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/GetCodegenJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/GetCodegenJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/GetCodegenJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/GetCodegenJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/GetCodegenJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/GetCodegenJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/GetCodegenJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/GetCodegenJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
