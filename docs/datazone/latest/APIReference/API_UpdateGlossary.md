---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateGlossary.html
---

# UpdateGlossary
<a name="API_UpdateGlossary"></a>

Updates the business glossary in Amazon DataZone.

Prerequisites:
+ The glossary must exist in the given domain.
+ The caller must have the `datazone:UpdateGlossary` permission to update it.
+ When updating the name, the new name must be unique within the domain.
+ The glossary must not be deleted or in a terminal state.

## Request Syntax
<a name="API_UpdateGlossary_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/glossaries/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateGlossary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateGlossary_RequestSyntax) **   <a name="datazone-UpdateGlossary-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which a business glossary is to be updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateGlossary_RequestSyntax) **   <a name="datazone-UpdateGlossary-request-uri-identifier"></a>
The identifier of the business glossary to be updated.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateGlossary_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateGlossary_RequestSyntax) **   <a name="datazone-UpdateGlossary-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_UpdateGlossary_RequestSyntax) **   <a name="datazone-UpdateGlossary-request-description"></a>
The description to be updated as part of the `UpdateGlossary` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [name](#API_UpdateGlossary_RequestSyntax) **   <a name="datazone-UpdateGlossary-request-name"></a>
The name to be updated as part of the `UpdateGlossary` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [status](#API_UpdateGlossary_RequestSyntax) **   <a name="datazone-UpdateGlossary-request-status"></a>
The status to be updated as part of the `UpdateGlossary` action.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

## Response Syntax
<a name="API_UpdateGlossary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "domainId": "string",
   "id": "string",
   "name": "string",
   "owningProjectId": "string",
   "status": "string",
   "usageRestrictions": [ "string" ]
}
```

## Response Elements
<a name="API_UpdateGlossary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_UpdateGlossary_ResponseSyntax) **   <a name="datazone-UpdateGlossary-response-description"></a>
The description to be updated as part of the `UpdateGlossary` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [domainId](#API_UpdateGlossary_ResponseSyntax) **   <a name="datazone-UpdateGlossary-response-domainId"></a>
The identifier of the Amazon DataZone domain in which a business glossary is to be updated.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_UpdateGlossary_ResponseSyntax) **   <a name="datazone-UpdateGlossary-response-id"></a>
The identifier of the business glossary that is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_UpdateGlossary_ResponseSyntax) **   <a name="datazone-UpdateGlossary-response-name"></a>
The name to be updated as part of the `UpdateGlossary` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [owningProjectId](#API_UpdateGlossary_ResponseSyntax) **   <a name="datazone-UpdateGlossary-response-owningProjectId"></a>
The identifier of the project in which to update a business glossary.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [status](#API_UpdateGlossary_ResponseSyntax) **   <a name="datazone-UpdateGlossary-response-status"></a>
The status to be updated as part of the `UpdateGlossary` action.
Type: String
Valid Values: `DISABLED | ENABLED`

 ** [usageRestrictions](#API_UpdateGlossary_ResponseSyntax) **   <a name="datazone-UpdateGlossary-response-usageRestrictions"></a>
The usage restriction of the restricted glossary.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ASSET_GOVERNED_TERMS`

## Errors
<a name="API_UpdateGlossary_Errors"></a>

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
<a name="API_UpdateGlossary_Examples"></a>

### Example
<a name="API_UpdateGlossary_Example_1"></a>

This example illustrates one usage of UpdateGlossary.

#### Sample Request
<a name="API_UpdateGlossary_Example_1_Request"></a>

```
aws datazone update-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "gls8m3nqx2wkfp" \
--name "UpdatedCustomerAnalyticsGlossary"
```

#### Sample Response
<a name="API_UpdateGlossary_Example_1_Response"></a>

```
{
    "domainId": "dzd_53ielnpxktdilj",
    "id": "gls8m3nqx2wkfp",
    "name": "UpdatedCustomerAnalyticsGlossary",
    "owningProjectId": "prj7nx82mkl",
    "status": "ENABLED"
}
```

### Example
<a name="API_UpdateGlossary_Example_2"></a>

Failure case - invalid input:

#### Sample Request
<a name="API_UpdateGlossary_Example_2_Request"></a>

```
aws datazone update-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "gls8m3nqx2wkfp" \
--name ""
```

#### Sample Response
<a name="API_UpdateGlossary_Example_2_Response"></a>

```
Parameter validation failed:
Invalid length for parameter name, value: 0, valid min length: 1
```

### Example
<a name="API_UpdateGlossary_Example_3"></a>

Failure case - resource not found:

#### Sample Request
<a name="API_UpdateGlossary_Example_3_Request"></a>

```
aws datazone update-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "gls_nonexistent" \
--name "NewGlossaryName"
```

#### Sample Response
<a name="API_UpdateGlossary_Example_3_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the UpdateGlossary operation: Requested businessGlossary cannot be found in domain
```

### Example
<a name="API_UpdateGlossary_Example_4"></a>

Failure case - duplicate terms:

#### Sample Request
<a name="API_UpdateGlossary_Example_4_Request"></a>

```
 aws datazone update-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "gls8m3nqx2wkfp" \
--name "ExistingGlossaryName"
```

#### Sample Response
<a name="API_UpdateGlossary_Example_4_Response"></a>

```
An error occurred (ConflictException) when calling the UpdateGlossary operation: Conflict with businessGlossary 41dkjgc9m5xj8n
```

## See Also
<a name="API_UpdateGlossary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateGlossary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateGlossary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateGlossary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateGlossary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateGlossary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateGlossary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateGlossary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateGlossary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateGlossary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateGlossary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
