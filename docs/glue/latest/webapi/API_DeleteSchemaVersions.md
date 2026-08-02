---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DeleteSchemaVersions.html
---

# DeleteSchemaVersions
<a name="API_DeleteSchemaVersions"></a>

Remove versions from the specified schema. A version number or range may be supplied. If the compatibility mode forbids deleting of a version that is necessary, such as BACKWARDS\_FULL, an error is returned. Calling the `GetSchemaVersions` API after this call will list the status of the deleted versions.

When the range of version numbers contain check pointed version, the API will return a 409 conflict and will not proceed with the deletion. You have to remove the checkpoint first using the `DeleteSchemaCheckpoint` API before using this API.

You cannot use the `DeleteSchemaVersions` API to delete the first schema version in the schema set. The first schema version can only be deleted by the `DeleteSchema` API. This operation will also delete the attached `SchemaVersionMetadata` under the schema versions. Hard deletes will be enforced on the database.

If the compatibility mode forbids deleting of a version that is necessary, such as BACKWARDS\_FULL, an error is returned.

## Request Syntax
<a name="API_DeleteSchemaVersions_RequestSyntax"></a>

```
{
   "SchemaId": {
      "RegistryName": "{{string}}",
      "SchemaArn": "{{string}}",
      "SchemaName": "{{string}}"
   },
   "Versions": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSchemaVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SchemaId](#API_DeleteSchemaVersions_RequestSyntax) **   <a name="Glue-DeleteSchemaVersions-request-SchemaId"></a>
This is a wrapper structure that may contain the schema name and Amazon Resource Name (ARN).
Type: [SchemaId](API_SchemaId.md) object
Required: Yes

 ** [Versions](#API_DeleteSchemaVersions_RequestSyntax) **   <a name="Glue-DeleteSchemaVersions-request-Versions"></a>
A version range may be supplied which may be of the format:
+ a single version number, 5
+ a range, 5-8 : deletes versions 5, 6, 7, 8
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Pattern: `[1-9][0-9]*|[1-9][0-9]*-[1-9][0-9]*`
Required: Yes

## Response Syntax
<a name="API_DeleteSchemaVersions_ResponseSyntax"></a>

```
{
   "SchemaVersionErrors": [
      {
         "ErrorDetails": {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         },
         "VersionNumber": number
      }
   ]
}
```

## Response Elements
<a name="API_DeleteSchemaVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SchemaVersionErrors](#API_DeleteSchemaVersions_ResponseSyntax) **   <a name="Glue-DeleteSchemaVersions-response-SchemaVersionErrors"></a>
A list of `SchemaVersionErrorItem` objects, each containing an error and schema version.
Type: Array of [SchemaVersionErrorItem](API_SchemaVersionErrorItem.md) objects

## Errors
<a name="API_DeleteSchemaVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSchemaVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/DeleteSchemaVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/DeleteSchemaVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DeleteSchemaVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/DeleteSchemaVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DeleteSchemaVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/DeleteSchemaVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/DeleteSchemaVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/DeleteSchemaVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/DeleteSchemaVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DeleteSchemaVersions)
