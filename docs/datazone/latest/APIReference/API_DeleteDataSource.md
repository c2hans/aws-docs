---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteDataSource.html
---

# DeleteDataSource
<a name="API_DeleteDataSource"></a>

Deletes a data source in Amazon DataZone.

## Request Syntax
<a name="API_DeleteDataSource_RequestSyntax"></a>

```
DELETE /v2/domains/{{domainIdentifier}}/data-sources/{{identifier}}?clientToken={{clientToken}}&retainPermissionsOnRevokeFailure={{retainPermissionsOnRevokeFailure}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeleteDataSource_RequestSyntax) **   <a name="datazone-DeleteDataSource-request-uri-clientToken"></a>
 *This parameter has been deprecated.*
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.

 ** [domainIdentifier](#API_DeleteDataSource_RequestSyntax) **   <a name="datazone-DeleteDataSource-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the data source is deleted.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_DeleteDataSource_RequestSyntax) **   <a name="datazone-DeleteDataSource-request-uri-identifier"></a>
The identifier of the data source that is deleted.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [retainPermissionsOnRevokeFailure](#API_DeleteDataSource_RequestSyntax) **   <a name="datazone-DeleteDataSource-request-uri-retainPermissionsOnRevokeFailure"></a>
Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.

## Request Body
<a name="API_DeleteDataSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDataSource_ResponseSyntax"></a>

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
<a name="API_DeleteDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assetFormsOutput](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-assetFormsOutput"></a>
The asset data forms associated with this data source.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [configuration](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-configuration"></a>
The configuration of the data source that is deleted.
Type: [DataSourceConfigurationOutput](API_DataSourceConfigurationOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [connectionId](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-connectionId"></a>
The ID of the connection that is deleted.
Type: String

 ** [createdAt](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-createdAt"></a>
The timestamp of when this data source was created.
Type: Timestamp

 ** [description](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-description"></a>
The description of the data source that is deleted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-domainId"></a>
The ID of the Amazon DataZone domain in which the data source is deleted.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [enableSetting](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-enableSetting"></a>
The enable setting of the data source that specifies whether the data source is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [environmentId](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-environmentId"></a>
The ID of the environemnt associated with this data source.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [errorMessage](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-errorMessage"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object

 ** [id](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-id"></a>
The ID of the data source that is deleted.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastRunAt](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-lastRunAt"></a>
The timestamp of when the data source was last run.
Type: Timestamp

 ** [lastRunErrorMessage](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-lastRunErrorMessage"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: [DataSourceErrorMessage](API_DataSourceErrorMessage.md) object

 ** [lastRunStatus](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-lastRunStatus"></a>
The status of the last run of this data source.
Type: String
Valid Values: `REQUESTED | RUNNING | FAILED | PARTIALLY_SUCCEEDED | SUCCESS`

 ** [name](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-name"></a>
The name of the data source that is deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [projectId](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-projectId"></a>
The ID of the project in which this data source exists and from which it's deleted.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [publishOnImport](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-publishOnImport"></a>
Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.
Type: Boolean

 ** [retainPermissionsOnRevokeFailure](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-retainPermissionsOnRevokeFailure"></a>
Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.
Type: Boolean

 ** [schedule](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-schedule"></a>
The schedule of runs for this data source.
Type: [ScheduleConfiguration](API_ScheduleConfiguration.md) object

 ** [selfGrantStatus](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-selfGrantStatus"></a>
Specifies the status of the self-granting functionality.
Type: [SelfGrantStatusOutput](API_SelfGrantStatusOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-status"></a>
The status of this data source.
Type: String
Valid Values: `CREATING | FAILED_CREATION | READY | UPDATING | FAILED_UPDATE | RUNNING | DELETING | FAILED_DELETION`

 ** [type](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-type"></a>
The type of this data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [updatedAt](#API_DeleteDataSource_ResponseSyntax) **   <a name="datazone-DeleteDataSource-response-updatedAt"></a>
The timestamp of when this data source was updated.
Type: Timestamp

## Errors
<a name="API_DeleteDataSource_Errors"></a>

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
<a name="API_DeleteDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
