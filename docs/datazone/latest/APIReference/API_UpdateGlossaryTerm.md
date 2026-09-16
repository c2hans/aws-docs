---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateGlossaryTerm.html
---

# UpdateGlossaryTerm
<a name="API_UpdateGlossaryTerm"></a>

Updates a business glossary term in Amazon DataZone.

Prerequisites:
+ Glossary term must exist in the specified domain.
+ New name must not conflict with existing terms in the same glossary.
+ User must have permissions on the term.
+ The term must not be in DELETED status.

## Request Syntax
<a name="API_UpdateGlossaryTerm_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/glossary-terms/{{identifier}} HTTP/1.1
Content-type: application/json

{
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
<a name="API_UpdateGlossaryTerm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="datazone-UpdateGlossaryTerm-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which a business glossary term is to be updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="datazone-UpdateGlossaryTerm-request-uri-identifier"></a>
The identifier of the business glossary term that is to be updated.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateGlossaryTerm_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [glossaryIdentifier](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="datazone-UpdateGlossaryTerm-request-glossaryIdentifier"></a>
The identifier of the business glossary in which a term is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [longDescription](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="datazone-UpdateGlossaryTerm-request-longDescription"></a>
The long description to be updated as part of the `UpdateGlossaryTerm` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [name](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="datazone-UpdateGlossaryTerm-request-name"></a>
The name to be updated as part of the `UpdateGlossaryTerm` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [shortDescription](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="datazone-UpdateGlossaryTerm-request-shortDescription"></a>
The short description to be updated as part of the `UpdateGlossaryTerm` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [status](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="datazone-UpdateGlossaryTerm-request-status"></a>
The status to be updated as part of the `UpdateGlossaryTerm` action.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [termRelations](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="datazone-UpdateGlossaryTerm-request-termRelations"></a>
The term relations to be updated as part of the `UpdateGlossaryTerm` action.
Type: [TermRelations](API_TermRelations.md) object
Required: No

## Response Syntax
<a name="API_UpdateGlossaryTerm_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateGlossaryTerm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainId](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="datazone-UpdateGlossaryTerm-response-domainId"></a>
The identifier of the Amazon DataZone domain in which a business glossary term is to be updated.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [glossaryId](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="datazone-UpdateGlossaryTerm-response-glossaryId"></a>
The identifier of the business glossary in which a term is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="datazone-UpdateGlossaryTerm-response-id"></a>
The identifier of the business glossary term that is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [longDescription](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="datazone-UpdateGlossaryTerm-response-longDescription"></a>
The long description to be updated as part of the `UpdateGlossaryTerm` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [name](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="datazone-UpdateGlossaryTerm-response-name"></a>
The name to be updated as part of the `UpdateGlossaryTerm` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [shortDescription](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="datazone-UpdateGlossaryTerm-response-shortDescription"></a>
The short description to be updated as part of the `UpdateGlossaryTerm` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [status](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="datazone-UpdateGlossaryTerm-response-status"></a>
The status to be updated as part of the `UpdateGlossaryTerm` action.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [termRelations](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="datazone-UpdateGlossaryTerm-response-termRelations"></a>
The term relations to be updated as part of the `UpdateGlossaryTerm` action.
Type: [TermRelations](API_TermRelations.md) object

 ** [usageRestrictions](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="datazone-UpdateGlossaryTerm-response-usageRestrictions"></a>
The usage restriction of a term within a restricted glossary.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ASSET_GOVERNED_TERMS`

## Errors
<a name="API_UpdateGlossaryTerm_Errors"></a>

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
<a name="API_UpdateGlossaryTerm_Examples"></a>

### Example
<a name="API_UpdateGlossaryTerm_Example_1"></a>

This example illustrates one usage of UpdateGlossaryTerm.

#### Sample Request
<a name="API_UpdateGlossaryTerm_Example_1_Request"></a>

```
aws datazone update-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "trm9k4pq7xwnmh" \
--name "CustomerLifetimeValueMetric"
```

#### Sample Response
<a name="API_UpdateGlossaryTerm_Example_1_Response"></a>

```
{
    "domainId": "dzd_53ielnpxktdilj",
    "glossaryId": "gls8m3nqx2wkfp",
    "id": "trm9k4pq7xwnmh",
    "name": "CustomerLifetimeValueMetric",
    "status": "ENABLED"
}
```

### Example
<a name="API_UpdateGlossaryTerm_Example_2"></a>

Failure case - resource does not exist:

#### Sample Request
<a name="API_UpdateGlossaryTerm_Example_2_Request"></a>

```
aws datazone update-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "trm_nonexistent" \
--name "NewTermName"
```

#### Sample Response
<a name="API_UpdateGlossaryTerm_Example_2_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the UpdateGlossaryTerm operation: The given GlossaryTerm doesn't exist. Try creating GlossaryTerm before accessing it.
```

### Example
<a name="API_UpdateGlossaryTerm_Example_3"></a>

Failure case - invalid input:

#### Sample Request
<a name="API_UpdateGlossaryTerm_Example_3_Request"></a>

```
aws datazone update-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "trm9k4pq7xwnmh" \
--name "$(head -c 300 </dev/zero | tr '\0' 'A')"
```

#### Sample Response
<a name="API_UpdateGlossaryTerm_Example_3_Response"></a>

```
An error occurred (ValidationException) when calling the UpdateGlossaryTerm operation: 1 validation error detected: Value at 'name' failed to satisfy constraint: Member must have length less than or equal to 256
```

## See Also
<a name="API_UpdateGlossaryTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateGlossaryTerm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateGlossaryTerm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateGlossaryTerm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateGlossaryTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateGlossaryTerm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateGlossaryTerm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateGlossaryTerm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateGlossaryTerm)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateGlossaryTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateGlossaryTerm)
