---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateDataSource.html
---

# UpdateDataSource
<a name="API_UpdateDataSource"></a>

Updates the specified data source in Amazon DataZone.

## Request Syntax
<a name="API_UpdateDataSource_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/data-sources/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "assetFormsInput": [
      {
         "content": "{{string}}",
         "formName": "{{string}}",
         "typeIdentifier": "{{string}}",
         "typeRevision": "{{string}}"
      }
   ],
   "configuration": { ... },
   "description": "{{string}}",
   "enableSetting": "{{string}}",
   "name": "{{string}}",
   "publishOnImport": {{boolean}},
   "recommendation": {
      "enableBusinessNameGeneration": {{boolean}}
   },
   "retainPermissionsOnRevokeFailure": {{boolean}},
   "schedule": {
      "schedule": "{{string}}",
      "timezone": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateDataSource_RequestSyntax) **   <a name="datazone-UpdateDataSource-request-uri-domainIdentifier"></a>
The identifier of the domain in which to update a data source.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateDataSource_RequestSyntax) **   <a name="datazone-UpdateDataSource-request-uri-identifier"></a>
The identifier of the data source to be updated.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assetFormsInput](#API_UpdateDataSource_RequestSyntax) **   <a name="datazone-UpdateDataSource-request-assetFormsInput"></a>
The asset forms to be updated as part of the `UpdateDataSource` action.
Type: Array of [FormInput](API_FormInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [configuration](#API_UpdateDataSource_RequestSyntax) **   <a name="datazone-UpdateDataSource-request-configuration"></a>
The configuration to be updated as part of the `UpdateDataSource` action.
Type: [DataSourceConfigurationInput](API_DataSourceConfigurationInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [description](#API_UpdateDataSource_RequestSyntax) **   <a name="datazone-UpdateDataSource-request-description"></a>
The description to be updated as part of the `UpdateDataSource` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [enableSetting](#API_UpdateDataSource_RequestSyntax) **   <a name="datazone-UpdateDataSource-request-enableSetting"></a>
The enable setting to be updated as part of the `UpdateDataSource` action.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [name](#API_UpdateDataSource_RequestSyntax) **   <a name="datazone-UpdateDataSource-request-name"></a>
The name to be updated as part of the `UpdateDataSource` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [publishOnImport](#API_UpdateDataSource_RequestSyntax) **   <a name="datazone-UpdateDataSource-request-publishOnImport"></a>
The publish on import setting to be updated as part of the `UpdateDataSource` action.
Type: Boolean
Required: No

 ** [recommendation](#API_UpdateDataSource_RequestSyntax) **   <a name="datazone-UpdateDataSource-request-recommendation"></a>
The recommendation to be updated as part of the `UpdateDataSource` action.
Type: [RecommendationConfiguration](API_RecommendationConfiguration.md) object
Required: No

 ** [retainPermissionsOnRevokeFailure](#API_UpdateDataSource_RequestSyntax) **   <a name="datazone-UpdateDataSource-request-retainPermissionsOnRevokeFailure"></a>
Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.
Type: Boolean
Required: No

 ** [schedule](#API_UpdateDataSource_RequestSyntax) **   <a name="datazone-UpdateDataSource-request-schedule"></a>
The schedule to be updated as part of the `UpdateDataSource` action.
Type: [ScheduleConfiguration](API_ScheduleConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assetFormsOutput": [
      {
         "content": "string",
         "formName": "string",
         "typeName": "string",
         "typeRevision": "string"
      }
   ],
   "configuration": { ... },
   "connectionId": "string",
   "createdAt": "string",
   "description": "string",
   "domainId": "string",
   "enableSetting": "string",
   "environmentId": "string",
   "errorMessage": {
      "errorDetail": "string",
      "errorType": "string"
   },
   "id": "string",
   "lastRunAt": "string",
   "lastRunErrorMessage": {
      "errorDetail": "string",
      "errorType": "string"
   },
   "lastRunStatus": "string",
   "name": "string",
   "projectId": "string",
   "publishOnImport": boolean,
   "recommendation": {
      "enableBusinessNameGeneration": boolean
   },
   "retainPermissionsOnRevokeFailure": boolean,
   "schedule": {
      "schedule": "string",
      "timezone": "string"
   },
   "selfGrantStatus": { ... },
   "status": "string",
   "type": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assetFormsOutput](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-assetFormsOutput"></a>
The asset forms to be updated as part of the `UpdateDataSource` action.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [configuration](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-configuration"></a>
The configuration to be updated as part of the `UpdateDataSource` action.
Type: [DataSourceConfigurationOutput](API_DataSourceConfigurationOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [connectionId](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-connectionId"></a>
The connection ID.
Type: String

 ** [createdAt](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-createdAt"></a>
The timestamp of when the data source was updated.
Type: Timestamp

 ** [description](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-description"></a>
The description to be updated as part of the `UpdateDataSource` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-domainId"></a>
The identifier of the Amazon DataZone domain in which a data source is to be updated.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [enableSetting](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-enableSetting"></a>
The enable setting to be updated as part of the `UpdateDataSource` action.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [environmentId](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-environmentId"></a>
The identifier of the environment in which a data source is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [errorMessage](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-errorMessage"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object

 ** [id](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-id"></a>
The identifier of the data source to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastRunAt](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-lastRunAt"></a>
The timestamp of when the data source was last run.
Type: Timestamp

 ** [lastRunErrorMessage](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-lastRunErrorMessage"></a>
The last run error message of the data source.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object

 ** [lastRunStatus](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-lastRunStatus"></a>
The last run status of the data source.
Type: String
Valid Values: `REQUESTED | RUNNING | FAILED | PARTIALLY_SUCCEEDED | SUCCESS`

 ** [name](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-name"></a>
The name to be updated as part of the `UpdateDataSource` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [projectId](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-projectId"></a>
The identifier of the project where data source is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [publishOnImport](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-publishOnImport"></a>
The publish on import setting to be updated as part of the `UpdateDataSource` action.
Type: Boolean

 ** [recommendation](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-recommendation"></a>
The recommendation to be updated as part of the `UpdateDataSource` action.
Type: [RecommendationConfiguration](API_RecommendationConfiguration.md) object

 ** [retainPermissionsOnRevokeFailure](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-retainPermissionsOnRevokeFailure"></a>
Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.
Type: Boolean

 ** [schedule](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-schedule"></a>
The schedule to be updated as part of the `UpdateDataSource` action.
Type: [ScheduleConfiguration](API_ScheduleConfiguration.md) object

 ** [selfGrantStatus](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-selfGrantStatus"></a>
Specifies the status of the self-granting functionality.
Type: [SelfGrantStatusOutput](API_SelfGrantStatusOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-status"></a>
The status to be updated as part of the `UpdateDataSource` action.
Type: String
Valid Values: `CREATING | FAILED_CREATION | READY | UPDATING | FAILED_UPDATE | RUNNING | DELETING | FAILED_DELETION`

 ** [type](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-type"></a>
The type to be updated as part of the `UpdateDataSource` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [updatedAt](#API_UpdateDataSource_ResponseSyntax) **   <a name="datazone-UpdateDataSource-response-updatedAt"></a>
The timestamp of when the data source was updated.
Type: Timestamp

## Errors
<a name="API_UpdateDataSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateDataSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateDataSource)
