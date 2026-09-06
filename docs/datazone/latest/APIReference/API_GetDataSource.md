---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetDataSource.html
---

# GetDataSource
<a name="API_GetDataSource"></a>

Gets an Amazon DataZone data source.

## Request Syntax
<a name="API_GetDataSource_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/data-sources/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetDataSource_RequestSyntax) **   <a name="datazone-GetDataSource-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the data source exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetDataSource_RequestSyntax) **   <a name="datazone-GetDataSource-request-uri-identifier"></a>
The ID of the Amazon DataZone data source.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetDataSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataSource_ResponseSyntax"></a>

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
   "lastRunAssetCount": number,
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
   "selfGrantStatus": { ... },
   "status": "string",
   "type": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assetFormsOutput](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-assetFormsOutput"></a>
The metadata forms attached to the assets created by this data source.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [configuration](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-configuration"></a>
The configuration of the data source.
Type: [DataSourceConfigurationOutput](API_DataSourceConfigurationOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [connectionId](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-connectionId"></a>
The ID of the connection.
Type: String

 ** [createdAt](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-createdAt"></a>
The timestamp of when the data source was created.
Type: Timestamp

 ** [description](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-description"></a>
The description of the data source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-domainId"></a>
The ID of the Amazon DataZone domain in which the data source exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [enableSetting](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-enableSetting"></a>
Specifies whether this data source is enabled or not.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [environmentId](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-environmentId"></a>
The ID of the environment where this data source creates and publishes assets,
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [errorMessage](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-errorMessage"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object

 ** [id](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-id"></a>
The ID of the data source.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastRunAssetCount](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-lastRunAssetCount"></a>
The number of assets created by the data source during its last run.
Type: Integer

 ** [lastRunAt](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-lastRunAt"></a>
The timestamp of the last run of the data source.
Type: Timestamp

 ** [lastRunErrorMessage](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-lastRunErrorMessage"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object

 ** [lastRunStatus](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-lastRunStatus"></a>
The status of the last run of the data source.
Type: String
Valid Values: `REQUESTED | RUNNING | FAILED | PARTIALLY_SUCCEEDED | SUCCESS`

 ** [name](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-name"></a>
The name of the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [projectId](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-projectId"></a>
The ID of the project where the data source creates and publishes assets.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [publishOnImport](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-publishOnImport"></a>
Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.
Type: Boolean

 ** [recommendation](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-recommendation"></a>
The recommendation configuration of the data source.
Type: [RecommendationConfiguration](API_RecommendationConfiguration.md) object

 ** [schedule](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-schedule"></a>
The schedule of the data source runs.
Type: [ScheduleConfiguration](API_ScheduleConfiguration.md) object

 ** [selfGrantStatus](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-selfGrantStatus"></a>
Specifies the status of the self-granting functionality.
Type: [SelfGrantStatusOutput](API_SelfGrantStatusOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-status"></a>
The status of the data source.
Type: String
Valid Values: `CREATING | FAILED_CREATION | READY | UPDATING | FAILED_UPDATE | RUNNING | DELETING | FAILED_DELETION`

 ** [type](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-type"></a>
The type of the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [updatedAt](#API_GetDataSource_ResponseSyntax) **   <a name="datazone-GetDataSource-response-updatedAt"></a>
The timestamp of when the data source was updated.
Type: Timestamp

## Errors
<a name="API_GetDataSource_Errors"></a>

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
<a name="API_GetDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetDataSource)
