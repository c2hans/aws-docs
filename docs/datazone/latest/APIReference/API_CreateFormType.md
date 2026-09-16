---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateFormType.html
---

# CreateFormType
<a name="API_CreateFormType"></a>

Creates a metadata form type.

Prerequisites:
+ The domain must exist and be in an `ENABLED` state.
+ The owning project must exist and be accessible.
+ The name must be unique within the domain.

For custom form types, to indicate that a field should be searchable, annotate it with `@amazon.datazone#searchable`. By default, searchable fields are indexed for semantic search, where related query terms will match the attribute value even if they are not stemmed or keyword matches. To indicate that a field should be indexed for lexical search (which disables semantic search but supports stemmed and partial matches), annotate it with `@amazon.datazone#searchable(modes:["LEXICAL"])`. To indicate that a field should be indexed for technical identifier search (for more information on technical identifier search, see: [https://aws.amazon.com/blogs/big-data/streamline-data-discovery-with-precise-technical-identifier-search-in-amazon-sagemaker-unified-studio/](https://aws.amazon.com/blogs/big-data/streamline-data-discovery-with-precise-technical-identifier-search-in-amazon-sagemaker-unified-studio/)), annotate it with `@amazon.datazone#searchable(modes:["TECHNICAL"])`.

To denote that a field will store glossary term ids (which are filterable via the Search/SearchListings APIs), annotate it with `@amazon.datazone#glossaryterm("${GLOSSARY_ID}")`, where `${GLOSSARY_ID}` is the id of the glossary that the glossary terms stored in the field belong to.

## Request Syntax
<a name="API_CreateFormType_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/form-types HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "model": { ... },
   "name": "{{string}}",
   "owningProjectIdentifier": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateFormType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateFormType_RequestSyntax) **   <a name="datazone-CreateFormType-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which this metadata form type is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateFormType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateFormType_RequestSyntax) **   <a name="datazone-CreateFormType-request-description"></a>
The description of this Amazon DataZone metadata form type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [model](#API_CreateFormType_RequestSyntax) **   <a name="datazone-CreateFormType-request-model"></a>
The model of this Amazon DataZone metadata form type.
Type: [Model](API_Model.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [name](#API_CreateFormType_RequestSyntax) **   <a name="datazone-CreateFormType-request-name"></a>
The name of this Amazon DataZone metadata form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(amazon.datazone.)?(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`
Required: Yes

 ** [owningProjectIdentifier](#API_CreateFormType_RequestSyntax) **   <a name="datazone-CreateFormType-request-owningProjectIdentifier"></a>
The ID of the Amazon DataZone project that owns this metadata form type.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [status](#API_CreateFormType_RequestSyntax) **   <a name="datazone-CreateFormType-request-status"></a>
The status of this Amazon DataZone metadata form type.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_CreateFormType_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "description": "string",
   "domainId": "string",
   "name": "string",
   "originDomainId": "string",
   "originProjectId": "string",
   "owningProjectId": "string",
   "revision": "string"
}
```

## Response Elements
<a name="API_CreateFormType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [description](#API_CreateFormType_ResponseSyntax) **   <a name="datazone-CreateFormType-response-description"></a>
The description of this Amazon DataZone metadata form type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateFormType_ResponseSyntax) **   <a name="datazone-CreateFormType-response-domainId"></a>
The ID of the Amazon DataZone domain in which this metadata form type is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [name](#API_CreateFormType_ResponseSyntax) **   <a name="datazone-CreateFormType-response-name"></a>
The name of this Amazon DataZone metadata form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(amazon.datazone.)?(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`

 ** [originDomainId](#API_CreateFormType_ResponseSyntax) **   <a name="datazone-CreateFormType-response-originDomainId"></a>
The ID of the Amazon DataZone domain in which this metadata form type was originally created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [originProjectId](#API_CreateFormType_ResponseSyntax) **   <a name="datazone-CreateFormType-response-originProjectId"></a>
The ID of the project in which this Amazon DataZone metadata form type was originally created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectId](#API_CreateFormType_ResponseSyntax) **   <a name="datazone-CreateFormType-response-owningProjectId"></a>
The ID of the project that owns this Amazon DataZone metadata form type.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [revision](#API_CreateFormType_ResponseSyntax) **   <a name="datazone-CreateFormType-response-revision"></a>
The revision of this Amazon DataZone metadata form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_CreateFormType_Errors"></a>

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
<a name="API_CreateFormType_Examples"></a>

### Example
<a name="API_CreateFormType_Example_1"></a>

This example illustrates one usage of CreateFormType.

#### Sample Request
<a name="API_CreateFormType_Example_1_Request"></a>

```
aws datazone create-form-type \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj9vn4wxyz8k2m" \
--name "DataProductMetadataForm" \
--status ENABLED \
--model '{
    "smithy": "namespace dzd_53ielnpxktdilj\n\nstructure DataProductMetadataForm {\n @required\n name: smithy.api#String,\n @required\n databaseName: smithy.api#String,\n @required\n catalog: smithy.api#String\n}"
}'
```

#### Sample Response
<a name="API_CreateFormType_Example_1_Response"></a>

```
{
    "domainId": "dzd_53ielnpxktdilj",
    "name": "DataProductMetadataForm",
    "revision": "1"
}
```

### Example
<a name="API_CreateFormType_Example_2"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_CreateFormType_Example_2_Request"></a>

```
aws datazone create-form-type \
--domain-identifier "dzd_53ielnpxktdilj" \
--name "CustomerPreferencesFormType" \
--model '{"smithy": "structure CustomerPreferencesFormType { }"}'
```

#### Sample Response
<a name="API_CreateFormType_Example_2_Response"></a>

```
aws: error: the following arguments are required: —owning-project-identifier
```

### Example
<a name="API_CreateFormType_Example_3"></a>

Failure case - wrong Smithy:

#### Sample Request
<a name="API_CreateFormType_Example_3_Request"></a>

```
aws datazone create-form-type \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl" \
--name "CustomerPreferencesFormType" \
--model '{"smithy": "structure CustomerPreferencesFormType {"}'  # malformed closing brace
```

#### Sample Response
<a name="API_CreateFormType_Example_3_Response"></a>

```
Unknown options: malformed, closing, brace, #
```

### Example
<a name="API_CreateFormType_Example_4"></a>

This example illustrates a usage of CreateFormType, using Smithy traits to specify that attributes should be indexed for search. In this case, we will create a single required field name that will be indexed for technical identifier search.

#### Sample Request
<a name="API_CreateFormType_Example_4_Request"></a>

```
aws datazone create-form-type \
--domain-identifier "dzd_4q2el0k35ngqa8" \
--owning-project-identifier "4mo2oiauaqbrtc" \
--name "DataProductMetadataForm" \
--status ENABLED \
--model '{ "smithy": "namespace dzd_4q2el0k35ngqa8\n\nstructure DataProductMetadataForm {\n @required\n @amazon.datazone#searchable(modes:[\"TECHNICAL\"])\n name: smithy.api#String\n}" }'
```

#### Sample Response
<a name="API_CreateFormType_Example_4_Response"></a>

```
{
    "domainId": "dzd_4q2el0k35ngqa8",
    "name": "DataProductMetadataForm",
    "revision": "1"
}
```

## See Also
<a name="API_CreateFormType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateFormType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateFormType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateFormType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateFormType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateFormType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateFormType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateFormType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateFormType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateFormType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateFormType)
