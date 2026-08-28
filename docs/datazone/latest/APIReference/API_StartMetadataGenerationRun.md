---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_StartMetadataGenerationRun.html
---

# StartMetadataGenerationRun
<a name="API_StartMetadataGenerationRun"></a>

Starts the metadata generation run.

Prerequisites:
+ Asset must be created and belong to the specified domain and project.
+ Asset type must be supported for metadata generation (e.g., AWS Glue table).
+ Asset must have a structured schema with valid rows and columns.
+ Valid values for --type: BUSINESS\_DESCRIPTIONS, BUSINESS\_NAMES, BUSINESS\_GLOSSARY\_ASSOCIATIONS.
+ The user must have permission to run metadata generation in the domain/project.

## Request Syntax
<a name="API_StartMetadataGenerationRun_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/metadata-generation-runs HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "owningProjectIdentifier": "{{string}}",
   "target": {
      "identifier": "{{string}}",
      "revision": "{{string}}",
      "type": "{{string}}"
   },
   "type": "{{string}}",
   "types": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_StartMetadataGenerationRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_StartMetadataGenerationRun_RequestSyntax) **   <a name="datazone-StartMetadataGenerationRun-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain where you want to start a metadata generation run.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_StartMetadataGenerationRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartMetadataGenerationRun_RequestSyntax) **   <a name="datazone-StartMetadataGenerationRun-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [owningProjectIdentifier](#API_StartMetadataGenerationRun_RequestSyntax) **   <a name="datazone-StartMetadataGenerationRun-request-owningProjectIdentifier"></a>
The ID of the project that owns the asset for which you want to start a metadata generation run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [target](#API_StartMetadataGenerationRun_RequestSyntax) **   <a name="datazone-StartMetadataGenerationRun-request-target"></a>
The asset for which you want to start a metadata generation run.
Type: [MetadataGenerationRunTarget](API_MetadataGenerationRunTarget.md) object
Required: Yes

 ** [type](#API_StartMetadataGenerationRun_RequestSyntax) **   <a name="datazone-StartMetadataGenerationRun-request-type"></a>
 *This parameter has been deprecated.*
The type of the metadata generation run.
Type: String
Valid Values: `BUSINESS_DESCRIPTIONS | BUSINESS_NAMES | BUSINESS_GLOSSARY_ASSOCIATIONS`
Required: No

 ** [types](#API_StartMetadataGenerationRun_RequestSyntax) **   <a name="datazone-StartMetadataGenerationRun-request-types"></a>
The types of the metadata generation run.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `BUSINESS_DESCRIPTIONS | BUSINESS_NAMES | BUSINESS_GLOSSARY_ASSOCIATIONS`
Required: No

## Response Syntax
<a name="API_StartMetadataGenerationRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "domainId": "string",
   "id": "string",
   "owningProjectId": "string",
   "status": "string",
   "type": "string",
   "types": [ "string" ]
}
```

## Response Elements
<a name="API_StartMetadataGenerationRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_StartMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-StartMetadataGenerationRun-response-createdAt"></a>
The timestamp at which the metadata generation run was started.
Type: Timestamp

 ** [createdBy](#API_StartMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-StartMetadataGenerationRun-response-createdBy"></a>
The ID of the user who started the metadata generation run.
Type: String

 ** [domainId](#API_StartMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-StartMetadataGenerationRun-response-domainId"></a>
The ID of the Amazon DataZone domain in which the metadata generation run was started.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_StartMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-StartMetadataGenerationRun-response-id"></a>
The ID of the metadata generation run.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectId](#API_StartMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-StartMetadataGenerationRun-response-owningProjectId"></a>
The ID of the project that owns the asset for which the metadata generation run was started.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [status](#API_StartMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-StartMetadataGenerationRun-response-status"></a>
The status of the metadata generation run.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELED | SUCCEEDED | FAILED | PARTIALLY_SUCCEEDED`

 ** [type](#API_StartMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-StartMetadataGenerationRun-response-type"></a>
 *This parameter has been deprecated.*
The type of the metadata generation run.
Type: String
Valid Values: `BUSINESS_DESCRIPTIONS | BUSINESS_NAMES | BUSINESS_GLOSSARY_ASSOCIATIONS`

 ** [types](#API_StartMetadataGenerationRun_ResponseSyntax) **   <a name="datazone-StartMetadataGenerationRun-response-types"></a>
The types of the metadata generation run.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `BUSINESS_DESCRIPTIONS | BUSINESS_NAMES | BUSINESS_GLOSSARY_ASSOCIATIONS`

## Errors
<a name="API_StartMetadataGenerationRun_Errors"></a>

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

## Examples
<a name="API_StartMetadataGenerationRun_Examples"></a>

### Example
<a name="API_StartMetadataGenerationRun_Example_1"></a>

This example illustrates one usage of StartMetadataGenerationRun.

#### Sample Request
<a name="API_StartMetadataGenerationRun_Example_1_Request"></a>

```
aws datazone start-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--target '{
    "identifier": "ast6br2md6v9h",
    "revision": "1",
    "type": "ASSET"
}' \
--types ["BUSINESS_DESCRIPTIONS"]
```

#### Sample Response
<a name="API_StartMetadataGenerationRun_Example_1_Response"></a>

```
{
    "createdAt": 1752644436.666,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "id": "mgr5g0fy285m1q",
    "owningProjectId": "prj7nx82mkl",
    "status": "IN_PROGRESS",
    "types": ["BUSINESS_DESCRIPTIONS"]
}
```

### Example
<a name="API_StartMetadataGenerationRun_Example_2"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_StartMetadataGenerationRun_Example_2_Request"></a>

```
aws datazone start-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_StartMetadataGenerationRun_Example_2_Response"></a>

```
aws: error: the following arguments are required: —owning-project-identifier, —target
```

### Example
<a name="API_StartMetadataGenerationRun_Example_3"></a>

Failure case - invalid JSON:

#### Sample Request
<a name="API_StartMetadataGenerationRun_Example_3_Request"></a>

```
aws datazone start-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--target '{"identifier": "ast7k9mpq2xvn4", "revision": "1", "type": "ASSET"' \
--types ["BUSINESS_DESCRIPTIONS"]
```

#### Sample Response
<a name="API_StartMetadataGenerationRun_Example_3_Response"></a>

```
Error parsing parameter '--target': Invalid JSON: Expecting ',' delimiter: line 1 column 58 (char 57)
JSON received: {"identifier": "ast7k9mpq2xvn4", "revision": "1", "type": "ASSET"
```

### Example
<a name="API_StartMetadataGenerationRun_Example_4"></a>

Failuse case - invalid input:

#### Sample Request
<a name="API_StartMetadataGenerationRun_Example_4_Request"></a>

```
aws datazone start-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--target '{"identifier": "ast7k9mpq2xvn4", "revision": "1", "type": "ASSET"}' \
--type "INVALID_TYPE"
```

#### Sample Response
<a name="API_StartMetadataGenerationRun_Example_4_Response"></a>

```
An error occurred (ValidationException) when calling the StartMetadataGenerationRun operation: 1 validation error detected: Value at 'types' failed to satisfy constraint: Member must satisfy constraint: [Member must satisfy enum value set: [BUSINESS_NAMES, BUSINESS_GLOSSARY_ASSOCIATIONS, BUSINESS_DESCRIPTIONS]]
```

### Example
<a name="API_StartMetadataGenerationRun_Example_5"></a>

Failure case - resource not found:

#### Sample Request
<a name="API_StartMetadataGenerationRun_Example_5_Request"></a>

```
aws datazone start-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--target '{"identifier": "ast_nonexistent", "revision": "1", "type": "ASSET"}' \
--types ["BUSINESS_DESCRIPTIONS"]
```

#### Sample Response
<a name="API_StartMetadataGenerationRun_Example_5_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the StartMetadataGenerationRun operation: The given Asset doesn't exist. Try creating Asset before accessing it.
```

### Example
<a name="API_StartMetadataGenerationRun_Example_6"></a>

Failure case - not supported data type:

#### Sample Request
<a name="API_StartMetadataGenerationRun_Example_6_Request"></a>

```
aws datazone start-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--target '{
    "identifier": "ast7k9mpq2xvn4",
    "revision": "1",
    "type": "ASSET"
}' \
--types ["BUSINESS_DESCRIPTIONS"]
```

#### Sample Response
<a name="API_StartMetadataGenerationRun_Example_6_Response"></a>

```
An error occurred (ValidationException) when calling the StartMetadataGenerationRun operation: Metadata Descriptions Generation is not supported for input asset type
```

### Example
<a name="API_StartMetadataGenerationRun_Example_7"></a>

StartMetadataGenerationRun with multiple types:

#### Sample Request
<a name="API_StartMetadataGenerationRun_Example_7_Request"></a>

```
aws datazone start-metadata-generation-run \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--target '{
    "identifier": "ast6br2md6v9h",
    "revision": "1",
    "type": "ASSET"
}' \
--types ["BUSINESS_DESCRIPTIONS", "BUSINESS_NAMES", "BUSINESS_GLOSSARY_ASSOCIATIONS"]
```

#### Sample Response
<a name="API_StartMetadataGenerationRun_Example_7_Response"></a>

```
{
    "createdAt": 1752644436.666,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "id": "mgr5g0fy285m1q",
    "owningProjectId": "prj7nx82mkl",
    "status": "IN_PROGRESS",
    "types": ["BUSINESS_DESCRIPTIONS", "BUSINESS_NAMES", "BUSINESS_GLOSSARY_ASSOCIATIONS"]
}
```

## See Also
<a name="API_StartMetadataGenerationRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/StartMetadataGenerationRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/StartMetadataGenerationRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/StartMetadataGenerationRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/StartMetadataGenerationRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/StartMetadataGenerationRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/StartMetadataGenerationRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/StartMetadataGenerationRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/StartMetadataGenerationRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/StartMetadataGenerationRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/StartMetadataGenerationRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
