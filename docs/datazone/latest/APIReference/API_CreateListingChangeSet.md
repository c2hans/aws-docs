---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateListingChangeSet.html
---

# CreateListingChangeSet
<a name="API_CreateListingChangeSet"></a>

Publishes a listing (a record of an asset at a given time) or removes a listing from the catalog.

## Request Syntax
<a name="API_CreateListingChangeSet_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/listings/change-set HTTP/1.1
Content-type: application/json

{
   "action": "{{string}}",
   "clientToken": "{{string}}",
   "entityIdentifier": "{{string}}",
   "entityRevision": "{{string}}",
   "entityType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateListingChangeSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateListingChangeSet_RequestSyntax) **   <a name="datazone-CreateListingChangeSet-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateListingChangeSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_CreateListingChangeSet_RequestSyntax) **   <a name="datazone-CreateListingChangeSet-request-action"></a>
Specifies whether to publish or unpublish a listing.
Type: String
Valid Values: `PUBLISH | UNPUBLISH`
Required: Yes

 ** [clientToken](#API_CreateListingChangeSet_RequestSyntax) **   <a name="datazone-CreateListingChangeSet-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [entityIdentifier](#API_CreateListingChangeSet_RequestSyntax) **   <a name="datazone-CreateListingChangeSet-request-entityIdentifier"></a>
The ID of the asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityRevision](#API_CreateListingChangeSet_RequestSyntax) **   <a name="datazone-CreateListingChangeSet-request-entityRevision"></a>
The revision of an asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [entityType](#API_CreateListingChangeSet_RequestSyntax) **   <a name="datazone-CreateListingChangeSet-request-entityType"></a>
The type of an entity.
Type: String
Valid Values: `ASSET | DATA_PRODUCT`
Required: Yes

## Response Syntax
<a name="API_CreateListingChangeSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "listingId": "string",
   "listingRevision": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateListingChangeSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [listingId](#API_CreateListingChangeSet_ResponseSyntax) **   <a name="datazone-CreateListingChangeSet-response-listingId"></a>
The ID of the listing (a record of an asset at a given time).
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [listingRevision](#API_CreateListingChangeSet_ResponseSyntax) **   <a name="datazone-CreateListingChangeSet-response-listingRevision"></a>
The revision of a listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [status](#API_CreateListingChangeSet_ResponseSyntax) **   <a name="datazone-CreateListingChangeSet-response-status"></a>
Specifies the status of the listing.
Type: String
Valid Values: `CREATING | ACTIVE | INACTIVE`

## Errors
<a name="API_CreateListingChangeSet_Errors"></a>

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

## See Also
<a name="API_CreateListingChangeSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateListingChangeSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateListingChangeSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateListingChangeSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateListingChangeSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateListingChangeSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateListingChangeSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateListingChangeSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateListingChangeSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateListingChangeSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateListingChangeSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
