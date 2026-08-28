---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetFormType.html
---

# GetFormType
<a name="API_GetFormType"></a>

Gets a metadata form type in Amazon DataZone.

Form types define the structure and validation rules for collecting metadata about assets in Amazon DataZone. They act as templates that ensure consistent metadata capture across similar types of assets, while allowing for customization to meet specific organizational needs. Form types can include required fields, validation rules, and dependencies, helping maintain high-quality metadata that makes data assets more discoverable and usable.
+ The form type with the specified identifier must exist in the given domain.
+ The domain must be valid and active.
+ User must have permission on the form type.
+ The form type should not be deleted or in an invalid state.

One use case for this API is to determine whether a form field is indexed for search.

A searchable field will be annotated with `@amazon.datazone#searchable`. By default, searchable fields are indexed for semantic search, where related query terms will match the attribute value even if they are not stemmed or keyword matches. If a field is indexed technical identifier search, it will be annotated with `@amazon.datazone#searchable(modes:["TECHNICAL"])`. If a field is indexed for lexical search (supports stemmed and prefix matches but not semantic matches), it will be annotated with `@amazon.datazone#searchable(modes:["LEXICAL"])`.

A field storing glossary term IDs (which is filterable) will be annotated with `@amazon.datazone#glossaryterm("${glossaryId}")`.

## Request Syntax
<a name="API_GetFormType_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/form-types/{{formTypeIdentifier}}?revision={{revision}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFormType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetFormType_RequestSyntax) **   <a name="datazone-GetFormType-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which this metadata form type exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [formTypeIdentifier](#API_GetFormType_RequestSyntax) **   <a name="datazone-GetFormType-request-uri-formTypeIdentifier"></a>
The ID of the metadata form type.
Length Constraints: Minimum length of 1. Maximum length of 385.
Pattern: `(?!\.)[\w\.]*\w`
Required: Yes

 ** [revision](#API_GetFormType_RequestSyntax) **   <a name="datazone-GetFormType-request-uri-revision"></a>
The revision of this metadata form type.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_GetFormType_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFormType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "imports": [
      {
         "name": "string",
         "revision": "string"
      }
   ],
   "model": { ... },
   "name": "string",
   "originDomainId": "string",
   "originProjectId": "string",
   "owningProjectId": "string",
   "revision": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetFormType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-createdAt"></a>
The timestamp of when this metadata form type was created.
Type: Timestamp

 ** [createdBy](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-createdBy"></a>
The Amazon DataZone user who created this metadata form type.
Type: String

 ** [description](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-description"></a>
The description of the metadata form type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-domainId"></a>
The ID of the Amazon DataZone domain in which this metadata form type exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [imports](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-imports"></a>
The imports of the metadata form type.
Type: Array of [Import](API_Import.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [model](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-model"></a>
The model of the metadata form type.
Type: [Model](API_Model.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [name](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-name"></a>
The name of the metadata form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(amazon.datazone.)?(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`

 ** [originDomainId](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-originDomainId"></a>
The ID of the Amazon DataZone domain in which the metadata form type was originally created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [originProjectId](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-originProjectId"></a>
The ID of the project in which this metadata form type was originally created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectId](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-owningProjectId"></a>
The ID of the project that owns this metadata form type.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [revision](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-revision"></a>
The revision of the metadata form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [status](#API_GetFormType_ResponseSyntax) **   <a name="datazone-GetFormType-response-status"></a>
The status of the metadata form type.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_GetFormType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

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
<a name="API_GetFormType_Examples"></a>

### Example
<a name="API_GetFormType_Example_1"></a>

This example illustrates one usage of GetFormType.

#### Sample Request
<a name="API_GetFormType_Example_1_Request"></a>

```
aws datazone get-form-type \
--domain-identifier "dzd_53ielnpxktdilj" \
--form-type-identifier "CustomerProfileFormType"
```

#### Sample Response
<a name="API_GetFormType_Example_1_Response"></a>

```
{
    "createdAt": 1752600481.72,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "imports": [],
    "model": {
        "smithy": "structure CustomerProfileFormType {\n    @required\n    customerId: String,\n    firstName: String,\n    lastName: String,\n    email: String\n}"
    },
    "name": "CustomerProfileFormType",
    "owningProjectId": "prj7nx82mkl",
    "revision": "2",
    "status": "ENABLED"
}
```

### Example
<a name="API_GetFormType_Example_2"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_GetFormType_Example_2_Request"></a>

```
aws datazone get-form-type \
--domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_GetFormType_Example_2_Response"></a>

```
aws: error: the following arguments are required: —form-type-identifier
```

### Example
<a name="API_GetFormType_Example_3"></a>

Failure case - resource does not exist:

#### Sample Request
<a name="API_GetFormType_Example_3_Request"></a>

```
aws datazone get-form-type \
--domain-identifier "dzd_53ielnpxktdilj" \
--form-type-identifier "NonExistentFormType"
```

#### Sample Response
<a name="API_GetFormType_Example_3_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the GetFormType operation: The given FormType doesn't exist. Try creating FormType before accessing it.
```

### Example
<a name="API_GetFormType_Example_4"></a>

Failure case - invalid input:

#### Sample Request
<a name="API_GetFormType_Example_4_Request"></a>

```
aws datazone get-form-type \
--domain-identifier "invalid_domain" \
--form-type-identifier "CustomerProfileFormType"
```

#### Sample Response
<a name="API_GetFormType_Example_4_Response"></a>

```
An error occurred (ValidationException) when calling the GetFormType operation: 1 validation error detected: Value at 'domainIdentifier' failed to satisfy constraint: Member must satisfy regular expression pattern: dzd[-_][a-zA-Z0-9_-]{1,36}
```

## See Also
<a name="API_GetFormType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetFormType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetFormType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetFormType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetFormType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetFormType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetFormType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetFormType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetFormType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetFormType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetFormType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
