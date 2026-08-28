---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetListing.html
---

# GetListing
<a name="API_GetListing"></a>

Gets a listing (a record of an asset at a given time). If you specify a listing version, only details that are specific to that version are returned.

## Request Syntax
<a name="API_GetListing_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/listings/{{identifier}}?listingRevision={{listingRevision}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetListing_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetListing_RequestSyntax) **   <a name="datazone-GetListing-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetListing_RequestSyntax) **   <a name="datazone-GetListing-request-uri-identifier"></a>
The ID of the listing.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [listingRevision](#API_GetListing_RequestSyntax) **   <a name="datazone-GetListing-request-uri-listingRevision"></a>
The revision of the listing.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_GetListing_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetListing_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "id": "string",
   "item": { ... },
   "listingRevision": "string",
   "name": "string",
   "status": "string",
   "updatedAt": number,
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_GetListing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetListing_ResponseSyntax) **   <a name="datazone-GetListing-response-createdAt"></a>
The timestamp of when the listing was created.
Type: Timestamp

 ** [createdBy](#API_GetListing_ResponseSyntax) **   <a name="datazone-GetListing-response-createdBy"></a>
The Amazon DataZone user who created the listing.
Type: String

 ** [description](#API_GetListing_ResponseSyntax) **   <a name="datazone-GetListing-response-description"></a>
The description of the listing.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetListing_ResponseSyntax) **   <a name="datazone-GetListing-response-domainId"></a>
The ID of the Amazon DataZone domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetListing_ResponseSyntax) **   <a name="datazone-GetListing-response-id"></a>
The ID of the listing.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [item](#API_GetListing_ResponseSyntax) **   <a name="datazone-GetListing-response-item"></a>
The details of a listing.
Type: [ListingItem](API_ListingItem.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [listingRevision](#API_GetListing_ResponseSyntax) **   <a name="datazone-GetListing-response-listingRevision"></a>
The revision of a listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [name](#API_GetListing_ResponseSyntax) **   <a name="datazone-GetListing-response-name"></a>
The name of the listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [status](#API_GetListing_ResponseSyntax) **   <a name="datazone-GetListing-response-status"></a>
The status of the listing.
Type: String
Valid Values: `CREATING | ACTIVE | INACTIVE`

 ** [updatedAt](#API_GetListing_ResponseSyntax) **   <a name="datazone-GetListing-response-updatedAt"></a>
The timestamp of when the listing was updated.
Type: Timestamp

 ** [updatedBy](#API_GetListing_ResponseSyntax) **   <a name="datazone-GetListing-response-updatedBy"></a>
The Amazon DataZone user who updated the listing.
Type: String

## Errors
<a name="API_GetListing_Errors"></a>

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

## See Also
<a name="API_GetListing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetListing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetListing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetListing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetListing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetListing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetListing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetListing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetListing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetListing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetListing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
