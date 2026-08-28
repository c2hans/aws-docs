---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetGlossaryTerm.html
---

# GetGlossaryTerm
<a name="API_GetGlossaryTerm"></a>

Gets a business glossary term in Amazon DataZone.

Prerequisites:
+ Glossary term with identifier must exist in the domain.
+ User must have permission on the glossary term.
+ Domain must be accessible and active.

## Request Syntax
<a name="API_GetGlossaryTerm_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/glossary-terms/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetGlossaryTerm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetGlossaryTerm_RequestSyntax) **   <a name="datazone-GetGlossaryTerm-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which this business glossary term exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetGlossaryTerm_RequestSyntax) **   <a name="datazone-GetGlossaryTerm-request-uri-identifier"></a>
The ID of the business glossary term.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetGlossaryTerm_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetGlossaryTerm_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
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
   "updatedAt": number,
   "updatedBy": "string",
   "usageRestrictions": [ "string" ]
}
```

## Response Elements
<a name="API_GetGlossaryTerm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-createdAt"></a>
The timestamp of when the business glossary term was created.
Type: Timestamp

 ** [createdBy](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-createdBy"></a>
The Amazon DataZone user who created the business glossary.
Type: String

 ** [domainId](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-domainId"></a>
The ID of the Amazon DataZone domain in which this business glossary term exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [glossaryId](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-glossaryId"></a>
The ID of the business glossary to which this term belongs.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-id"></a>
The ID of the business glossary term.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [longDescription](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-longDescription"></a>
The long description of the business glossary term.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [name](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-name"></a>
The name of the business glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [shortDescription](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-shortDescription"></a>
The short decription of the business glossary term.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [status](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-status"></a>
The status of the business glossary term.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [termRelations](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-termRelations"></a>
The relations of the business glossary term.
Type: [TermRelations](API_TermRelations.md) object

 ** [updatedAt](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-updatedAt"></a>
The timestamp of when the business glossary term was updated.
Type: Timestamp

 ** [updatedBy](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-updatedBy"></a>
The Amazon DataZone user who updated the business glossary term.
Type: String

 ** [usageRestrictions](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="datazone-GetGlossaryTerm-response-usageRestrictions"></a>
The usage restriction of a term within a restricted glossary.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ASSET_GOVERNED_TERMS`

## Errors
<a name="API_GetGlossaryTerm_Errors"></a>

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
<a name="API_GetGlossaryTerm_Examples"></a>

### Example
<a name="API_GetGlossaryTerm_Example_1"></a>

This example illustrates one usage of GetGlossaryTerm.

#### Sample Request
<a name="API_GetGlossaryTerm_Example_1_Request"></a>

```
aws datazone get-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "trm9k4pq7xwnmh"
```

#### Sample Response
<a name="API_GetGlossaryTerm_Example_1_Response"></a>

```
{
    "createdAt": 1752575686.928,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "glossaryId": "gls8m3nqx2wkfp",
    "id": "trm9k4pq7xwnmh",
    "longDescription": "The total value a customer is expected to generate over their entire relationship with the business.",
    "name": "CustomerLifetimeValue",
    "shortDescription": "Predicted net profit from a customer relationship",
    "status": "ENABLED",
    "updatedAt": 1752575686.928,
    "updatedBy": "usr7nx82mkl"
}
```

### Example
<a name="API_GetGlossaryTerm_Example_2"></a>

Failure case - resource does not exist:

#### Sample Request
<a name="API_GetGlossaryTerm_Example_2_Request"></a>

```
aws datazone get-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "trm_nonexistent"
```

#### Sample Response
<a name="API_GetGlossaryTerm_Example_2_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the GetGlossaryTerm operation: The given GlossaryTerm doesn't exist. Try creating GlossaryTerm before accessing it.
```

### Example
<a name="API_GetGlossaryTerm_Example_3"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_GetGlossaryTerm_Example_3_Request"></a>

```
aws datazone get-glossary-term \
--identifier "trm9k4pq7xwnmh"
```

#### Sample Response
<a name="API_GetGlossaryTerm_Example_3_Response"></a>

```
aws: error: the following arguments are required: —domain-identifier
```

## See Also
<a name="API_GetGlossaryTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetGlossaryTerm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetGlossaryTerm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetGlossaryTerm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetGlossaryTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetGlossaryTerm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetGlossaryTerm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetGlossaryTerm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetGlossaryTerm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetGlossaryTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetGlossaryTerm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
