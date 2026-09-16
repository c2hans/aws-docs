---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateDataSource.html
---

# CreateDataSource
<a name="API_CreateDataSource"></a>

Creates an Amazon DataZone data source.

## Request Syntax
<a name="API_CreateDataSource_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/data-sources HTTP/1.1
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
   "clientToken": "{{string}}",
   "configuration": { ... },
   "connectionIdentifier": "{{string}}",
   "description": "{{string}}",
   "enableSetting": "{{string}}",
   "environmentIdentifier": "{{string}}",
   "name": "{{string}}",
   "projectIdentifier": "{{string}}",
   "publishOnImport": {{boolean}},
   "recommendation": {
      "enableBusinessNameGeneration": {{boolean}}
   },
   "schedule": {
      "schedule": "{{string}}",
      "timezone": "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain where the data source is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assetFormsInput](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-assetFormsInput"></a>
The metadata forms that are to be attached to the assets that this data source works with.
Type: Array of [FormInput](API_FormInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [clientToken](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Required: No

 ** [configuration](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-configuration"></a>
Specifies the configuration of the data source. It can be set to either `glueRunConfiguration` or `redshiftRunConfiguration`.
Type: [DataSourceConfigurationInput](API_DataSourceConfigurationInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [connectionIdentifier](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-connectionIdentifier"></a>
The ID of the connection.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [description](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-description"></a>
The description of the data source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [enableSetting](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-enableSetting"></a>
Specifies whether the data source is enabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [environmentIdentifier](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-environmentIdentifier"></a>
The unique identifier of the Amazon DataZone environment to which the data source publishes assets.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [name](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-name"></a>
The name of the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [projectIdentifier](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-projectIdentifier"></a>
The identifier of the Amazon DataZone project in which you want to add this data source.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [publishOnImport](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-publishOnImport"></a>
Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.
Type: Boolean
Required: No

 ** [recommendation](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-recommendation"></a>
Specifies whether the business name generation is to be enabled for this data source.
Type: [RecommendationConfiguration](API_RecommendationConfiguration.md) object
Required: No

 ** [schedule](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-schedule"></a>
The schedule of the data source runs.
Type: [ScheduleConfiguration](API_ScheduleConfiguration.md) object
Required: No

 ** [type](#API_CreateDataSource_RequestSyntax) **   <a name="datazone-CreateDataSource-request-type"></a>
The type of the data source. In Amazon DataZone, you can use data sources to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone. In the current release of Amazon DataZone, you can create and run data sources for AWS Glue and Amazon Redshift.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_CreateDataSource_ResponseSyntax"></a>

```
HTTP/1.1 201
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
   "schedule": {
      "schedule": "string",
      "timezone": "string"
   },
   "status": "string",
   "type": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_CreateDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [assetFormsOutput](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-assetFormsOutput"></a>
The metadata forms attached to the assets that this data source creates.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [configuration](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-configuration"></a>
Specifies the configuration of the data source. It can be set to either `glueRunConfiguration` or `redshiftRunConfiguration`.
Type: [DataSourceConfigurationOutput](API_DataSourceConfigurationOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [connectionId](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-connectionId"></a>
The ID of the connection.
Type: String

 ** [createdAt](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-createdAt"></a>
The timestamp of when the data source was created.
Type: Timestamp

 ** [description](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-description"></a>
The description of the data source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-domainId"></a>
The ID of the Amazon DataZone domain in which the data source is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [enableSetting](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-enableSetting"></a>
Specifies whether the data source is enabled.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [environmentId](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-environmentId"></a>
The unique identifier of the Amazon DataZone environment to which the data source publishes assets.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [errorMessage](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-errorMessage"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object

 ** [id](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-id"></a>
The unique identifier of the data source.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastRunAt](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-lastRunAt"></a>
The timestamp that specifies when the data source was last run.
Type: Timestamp

 ** [lastRunErrorMessage](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-lastRunErrorMessage"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object

 ** [lastRunStatus](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-lastRunStatus"></a>
The status of the last run of this data source.
Type: String
Valid Values: `REQUESTED | RUNNING | FAILED | PARTIALLY_SUCCEEDED | SUCCESS`

 ** [name](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-name"></a>
The name of the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [projectId](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-projectId"></a>
The ID of the Amazon DataZone project to which the data source is added.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [publishOnImport](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-publishOnImport"></a>
Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.
Type: Boolean

 ** [recommendation](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-recommendation"></a>
Specifies whether the business name generation is to be enabled for this data source.
Type: [RecommendationConfiguration](API_RecommendationConfiguration.md) object

 ** [schedule](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-schedule"></a>
The schedule of the data source runs.
Type: [ScheduleConfiguration](API_ScheduleConfiguration.md) object

 ** [status](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-status"></a>
The status of the data source.
Type: String
Valid Values: `CREATING | FAILED_CREATION | READY | UPDATING | FAILED_UPDATE | RUNNING | DELETING | FAILED_DELETION`

 ** [type](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-type"></a>
The type of the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [updatedAt](#API_CreateDataSource_ResponseSyntax) **   <a name="datazone-CreateDataSource-response-updatedAt"></a>
The timestamp of when the data source was updated.
Type: Timestamp

## Errors
<a name="API_CreateDataSource_Errors"></a>

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
<a name="API_CreateDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateDataSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateDataSource)
