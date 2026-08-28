---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateGlossaryTerm.html
---

# CreateGlossaryTerm
<a name="API_CreateGlossaryTerm"></a>

Creates a business glossary term.

A glossary term represents an individual entry within the Amazon DataZone glossary, serving as a standardized definition for a specific business concept or data element. Each term can include rich metadata such as detailed definitions, synonyms, related terms, and usage examples. Glossary terms can be linked directly to data assets, providing business context to technical data elements. This linking capability helps users understand the business meaning of data fields and ensures consistent interpretation across different systems and teams. Terms can also have relationships with other terms, creating a semantic network that reflects the complexity of business concepts.

Prerequisites:
+ Domain must exist.
+ Glossary must exist.
+ The term name must be unique within the glossary.
+ Ensure term does not conflict with existing terms in hierarchy.

## Request Syntax
<a name="API_CreateGlossaryTerm_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/glossary-terms HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "glossaryIdentifier": "{{string}}",
   "longDescription": "{{string}}",
   "name": "{{string}}",
   "shortDescription": "{{string}}",
   "status": "{{string}}",
   "termRelations": {
      "classifies": [ "{{string}}" ],
      "isA": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_CreateGlossaryTerm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateGlossaryTerm_RequestSyntax) **   <a name="datazone-CreateGlossaryTerm-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which this business glossary term is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateGlossaryTerm_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateGlossaryTerm_RequestSyntax) **   <a name="datazone-CreateGlossaryTerm-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [glossaryIdentifier](#API_CreateGlossaryTerm_RequestSyntax) **   <a name="datazone-CreateGlossaryTerm-request-glossaryIdentifier"></a>
The ID of the business glossary in which this term is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [longDescription](#API_CreateGlossaryTerm_RequestSyntax) **   <a name="datazone-CreateGlossaryTerm-request-longDescription"></a>
The long description of this business glossary term.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [name](#API_CreateGlossaryTerm_RequestSyntax) **   <a name="datazone-CreateGlossaryTerm-request-name"></a>
The name of this business glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [shortDescription](#API_CreateGlossaryTerm_RequestSyntax) **   <a name="datazone-CreateGlossaryTerm-request-shortDescription"></a>
The short description of this business glossary term.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [status](#API_CreateGlossaryTerm_RequestSyntax) **   <a name="datazone-CreateGlossaryTerm-request-status"></a>
The status of this business glossary term.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [termRelations](#API_CreateGlossaryTerm_RequestSyntax) **   <a name="datazone-CreateGlossaryTerm-request-termRelations"></a>
The term relations of this business glossary term.
Type: [TermRelations](API_TermRelations.md) object
Required: No

## Response Syntax
<a name="API_CreateGlossaryTerm_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "domainId": "string",
   "glossaryId": "string",
   "id": "string",
   "longDescription": "string",
   "name": "string",
   "shortDescription": "string",
   "status": "string",
   "termRelations": {
      "classifies": [ "string" ],
      "isA": [ "string" ]
   },
   "usageRestrictions": [ "string" ]
}
```

## Response Elements
<a name="API_CreateGlossaryTerm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [domainId](#API_CreateGlossaryTerm_ResponseSyntax) **   <a name="datazone-CreateGlossaryTerm-response-domainId"></a>
The ID of the Amazon DataZone domain in which this business glossary term is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [glossaryId](#API_CreateGlossaryTerm_ResponseSyntax) **   <a name="datazone-CreateGlossaryTerm-response-glossaryId"></a>
The ID of the business glossary in which this term is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateGlossaryTerm_ResponseSyntax) **   <a name="datazone-CreateGlossaryTerm-response-id"></a>
The ID of this business glossary term.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [longDescription](#API_CreateGlossaryTerm_ResponseSyntax) **   <a name="datazone-CreateGlossaryTerm-response-longDescription"></a>
The long description of this business glossary term.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [name](#API_CreateGlossaryTerm_ResponseSyntax) **   <a name="datazone-CreateGlossaryTerm-response-name"></a>
The name of this business glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [shortDescription](#API_CreateGlossaryTerm_ResponseSyntax) **   <a name="datazone-CreateGlossaryTerm-response-shortDescription"></a>
The short description of this business glossary term.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [status](#API_CreateGlossaryTerm_ResponseSyntax) **   <a name="datazone-CreateGlossaryTerm-response-status"></a>
The status of this business glossary term.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [termRelations](#API_CreateGlossaryTerm_ResponseSyntax) **   <a name="datazone-CreateGlossaryTerm-response-termRelations"></a>
The term relations of this business glossary term.
Type: [TermRelations](API_TermRelations.md) object

 ** [usageRestrictions](#API_CreateGlossaryTerm_ResponseSyntax) **   <a name="datazone-CreateGlossaryTerm-response-usageRestrictions"></a>
The usage restriction of the restricted glossary.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ASSET_GOVERNED_TERMS`

## Errors
<a name="API_CreateGlossaryTerm_Errors"></a>

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
<a name="API_CreateGlossaryTerm_Examples"></a>

### Example
<a name="API_CreateGlossaryTerm_Example_1"></a>

This example illustrates one usage of CreateGlossaryTerm.

#### Sample Request
<a name="API_CreateGlossaryTerm_Example_1_Request"></a>

```
aws datazone create-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--glossary-identifier "gls8m3nqx2wkfp" \
--name "CustomerLifetimeValue"
```

#### Sample Response
<a name="API_CreateGlossaryTerm_Example_1_Response"></a>

```
{
    "domainId": "dzd_53ielnpxktdilj",
    "glossaryId": "gls8m3nqx2wkfp",
    "id": "trm9k4pq7xwnmh",
    "name": "CustomerLifetimeValue",
    "status": "ENABLED"
}
```

### Example
<a name="API_CreateGlossaryTerm_Example_2"></a>

Failure case - missing required parameter:

#### Sample Request
<a name="API_CreateGlossaryTerm_Example_2_Request"></a>

```
aws datazone create-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--name "CustomerLifetimeValue"
```

#### Sample Response
<a name="API_CreateGlossaryTerm_Example_2_Response"></a>

```
aws: error: the following arguments are required: —glossary-identifier
```

### Example
<a name="API_CreateGlossaryTerm_Example_3"></a>

Failure case - glossary does not exist:

#### Sample Request
<a name="API_CreateGlossaryTerm_Example_3_Request"></a>

```
    aws datazone create-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--glossary-identifier "gls_nonexistent" \
--name "CustomerLifetimeValue"
```

#### Sample Response
<a name="API_CreateGlossaryTerm_Example_3_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the CreateGlossaryTerm operation: The given Glossary doesn't exist. Try creating Glossary before accessing it.
```

### Example
<a name="API_CreateGlossaryTerm_Example_4"></a>

Failure case - duplicate term:

#### Sample Request
<a name="API_CreateGlossaryTerm_Example_4_Request"></a>

```
aws datazone create-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--glossary-identifier "gls8m3nqx2wkfp" \
--name "CustomerLifetimeValue"
```

#### Sample Response
<a name="API_CreateGlossaryTerm_Example_4_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the CreateGlossaryTerm operation: The given Glossary doesn't exist. Try creating Glossary before accessing it.
```

### Example
<a name="API_CreateGlossaryTerm_Example_5"></a>

Failure case - delete related resources

#### Sample Request
<a name="API_CreateGlossaryTerm_Example_5_Request"></a>

```
 aws datazone create-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--glossary-identifier "gls8m3nqx2wkfp" \
--name "CustomerLifetimeValue"
```

#### Sample Response
<a name="API_CreateGlossaryTerm_Example_5_Response"></a>

```
An error occurred (ConflictException) when calling the CreateGlossaryTerm operation: Conflict with glossaryTerm trm9k4pq7xwnmh
```

## See Also
<a name="API_CreateGlossaryTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateGlossaryTerm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateGlossaryTerm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateGlossaryTerm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateGlossaryTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateGlossaryTerm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateGlossaryTerm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateGlossaryTerm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateGlossaryTerm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateGlossaryTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateGlossaryTerm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
