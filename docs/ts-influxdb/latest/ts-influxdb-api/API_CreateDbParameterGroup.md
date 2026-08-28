---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_CreateDbParameterGroup.html
---

# CreateDbParameterGroup
<a name="API_CreateDbParameterGroup"></a>

Creates a new Timestream for InfluxDB DB parameter group to associate with DB instances.

## Request Syntax
<a name="API_CreateDbParameterGroup_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "name": "{{string}}",
   "parameters": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateDbParameterGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateDbParameterGroup_RequestSyntax) **   <a name="tsinfluxdb-CreateDbParameterGroup-request-description"></a>
A description of the DB parameter group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [name](#API_CreateDbParameterGroup_RequestSyntax) **   <a name="tsinfluxdb-CreateDbParameterGroup-request-name"></a>
The name of the DB parameter group. The name must be unique per customer and per region.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`
Required: Yes

 ** [parameters](#API_CreateDbParameterGroup_RequestSyntax) **   <a name="tsinfluxdb-CreateDbParameterGroup-request-parameters"></a>
A list of the parameters that comprise the DB parameter group.
Type: [Parameters](API_Parameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [tags](#API_CreateDbParameterGroup_RequestSyntax) **   <a name="tsinfluxdb-CreateDbParameterGroup-request-tags"></a>
A list of key-value pairs to associate with the DB parameter group.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDbParameterGroup_ResponseSyntax"></a>

```
{
   "arn": "string",
   "description": "string",
   "id": "string",
   "name": "string",
   "parameters": { ... }
}
```

## Response Elements
<a name="API_CreateDbParameterGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateDbParameterGroup_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbParameterGroup-response-arn"></a>
The Amazon Resource Name (ARM) of the DB parameter group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws[a-z\-]*:timestream\-influxdb:[a-z0-9\-]+:[0-9]{12}:(db\-instance|db\-cluster|db\-parameter\-group)/[a-zA-Z0-9]{3,64}`

 ** [description](#API_CreateDbParameterGroup_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbParameterGroup-response-description"></a>
The description of the DB parameter group.
Type: String

 ** [id](#API_CreateDbParameterGroup_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbParameterGroup-response-id"></a>
A service-generated unique identifier.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`

 ** [name](#API_CreateDbParameterGroup_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbParameterGroup-response-name"></a>
The customer-supplied name that uniquely identifies the DB parameter group when interacting with the Amazon Timestream for InfluxDB API and CLI commands.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`

 ** [parameters](#API_CreateDbParameterGroup_ResponseSyntax) **   <a name="tsinfluxdb-CreateDbParameterGroup-response-parameters"></a>
A list of the parameters that comprise the DB parameter group.
Type: [Parameters](API_Parameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_CreateDbParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request conflicts with an existing resource in Timestream for InfluxDB.
 ** resourceId **
The identifier for the Timestream for InfluxDB resource associated with the request.
 ** resourceType **
The type of Timestream for InfluxDB resource associated with the request.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found or does not exist.
 ** resourceId **
The identifier for the Timestream for InfluxDB resource associated with the request.
 ** resourceType **
The type of Timestream for InfluxDB resource associated with the request.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request exceeds the service quota.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by Timestream for InfluxDB.
 ** reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_CreateDbParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-influxdb-2023-01-27/CreateDbParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-influxdb-2023-01-27/CreateDbParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/CreateDbParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-influxdb-2023-01-27/CreateDbParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/CreateDbParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-influxdb-2023-01-27/CreateDbParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-influxdb-2023-01-27/CreateDbParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-influxdb-2023-01-27/CreateDbParameterGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-influxdb-2023-01-27/CreateDbParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/CreateDbParameterGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Timestream for InfluxDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ts-influxdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
