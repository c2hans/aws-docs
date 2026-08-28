---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetGlossary.html
---

# GetGlossary
<a name="API_GetGlossary"></a>

Gets a business glossary in Amazon DataZone.

Prerequisites:
+ The specified glossary ID must exist and be associated with the given domain.
+ The caller must have the `datazone:GetGlossary` permission on the domain.

## Request Syntax
<a name="API_GetGlossary_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/glossaries/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetGlossary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetGlossary_RequestSyntax) **   <a name="datazone-GetGlossary-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which this business glossary exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetGlossary_RequestSyntax) **   <a name="datazone-GetGlossary-request-uri-identifier"></a>
The ID of the business glossary.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetGlossary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetGlossary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "id": "string",
   "name": "string",
   "owningProjectId": "string",
   "status": "string",
   "updatedAt": number,
   "updatedBy": "string",
   "usageRestrictions": [ "string" ]
}
```

## Response Elements
<a name="API_GetGlossary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetGlossary_ResponseSyntax) **   <a name="datazone-GetGlossary-response-createdAt"></a>
The timestamp of when this business glossary was created.
Type: Timestamp

 ** [createdBy](#API_GetGlossary_ResponseSyntax) **   <a name="datazone-GetGlossary-response-createdBy"></a>
The Amazon DataZone user who created this business glossary.
Type: String

 ** [description](#API_GetGlossary_ResponseSyntax) **   <a name="datazone-GetGlossary-response-description"></a>
The description of the business glossary.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [domainId](#API_GetGlossary_ResponseSyntax) **   <a name="datazone-GetGlossary-response-domainId"></a>
The ID of the Amazon DataZone domain in which this business glossary exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetGlossary_ResponseSyntax) **   <a name="datazone-GetGlossary-response-id"></a>
The ID of the business glossary.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_GetGlossary_ResponseSyntax) **   <a name="datazone-GetGlossary-response-name"></a>
The name of the business glossary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [owningProjectId](#API_GetGlossary_ResponseSyntax) **   <a name="datazone-GetGlossary-response-owningProjectId"></a>
The ID of the project that owns this business glossary.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [status](#API_GetGlossary_ResponseSyntax) **   <a name="datazone-GetGlossary-response-status"></a>
The status of the business glossary.
Type: String
Valid Values: `DISABLED | ENABLED`

 ** [updatedAt](#API_GetGlossary_ResponseSyntax) **   <a name="datazone-GetGlossary-response-updatedAt"></a>
The timestamp of when the business glossary was updated.
Type: Timestamp

 ** [updatedBy](#API_GetGlossary_ResponseSyntax) **   <a name="datazone-GetGlossary-response-updatedBy"></a>
The Amazon DataZone user who updated the business glossary.
Type: String

 ** [usageRestrictions](#API_GetGlossary_ResponseSyntax) **   <a name="datazone-GetGlossary-response-usageRestrictions"></a>
The usage restriction of the restricted glossary.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ASSET_GOVERNED_TERMS`

## Errors
<a name="API_GetGlossary_Errors"></a>

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
<a name="API_GetGlossary_Examples"></a>

### Example
<a name="API_GetGlossary_Example_1"></a>

This example illustrates one usage of GetGlossary.

#### Sample Request
<a name="API_GetGlossary_Example_1_Request"></a>

```
aws datazone get-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "gls8m3nqx2wkfp"
```

#### Sample Response
<a name="API_GetGlossary_Example_1_Response"></a>

```
{
    "createdAt": 1752573775.274,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "id": "gls8m3nqx2wkfp",
    "name": "CustomerAnalyticsGlossary",
    "owningProjectId": "prj7nx82mkl",
    "status": "ENABLED",
    "updatedAt": 1752573775.274,
    "updatedBy": "usr7nx82mkl"
}
```

### Example
<a name="API_GetGlossary_Example_2"></a>

Failure case - missing required parameter:

#### Sample Request
<a name="API_GetGlossary_Example_2_Request"></a>

```
aws datazone get-glossary \
--domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_GetGlossary_Example_2_Response"></a>

```
aws: error: the following arguments are required: —identifier
```

### Example
<a name="API_GetGlossary_Example_3"></a>

Failure case - resource does not exist:

#### Sample Request
<a name="API_GetGlossary_Example_3_Request"></a>

```
aws datazone get-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "gls_nonexistent"
```

#### Sample Response
<a name="API_GetGlossary_Example_3_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the GetGlossary operation: The given Glossary doesn't exist. Try creating Glossary before accessing it.
```

## See Also
<a name="API_GetGlossary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetGlossary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetGlossary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetGlossary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetGlossary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetGlossary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetGlossary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetGlossary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetGlossary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetGlossary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetGlossary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
