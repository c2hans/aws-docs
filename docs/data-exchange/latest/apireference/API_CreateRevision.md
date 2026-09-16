---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateRevision.html
---

# CreateRevision
<a name="API_CreateRevision"></a>

This operation creates a revision for a data set.

## Request Syntax
<a name="API_CreateRevision_RequestSyntax"></a>

```
POST /v1/data-sets/{{DataSetId}}/revisions HTTP/1.1
Content-type: application/json

{
   "Comment": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRevision_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataSetId](#API_CreateRevision_RequestSyntax) **   <a name="dataexchange-CreateRevision-request-uri-DataSetId"></a>
The unique identifier for a data set.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## Request Body
<a name="API_CreateRevision_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Comment](#API_CreateRevision_RequestSyntax) **   <a name="dataexchange-CreateRevision-request-Comment"></a>
An optional comment about the revision.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** [Tags](#API_CreateRevision_RequestSyntax) **   <a name="dataexchange-CreateRevision-request-Tags"></a>
A revision tag is an optional label that you can assign to a revision when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateRevision_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "Comment": "string",
   "CreatedAt": "string",
   "DataSetId": "string",
   "Finalized": boolean,
   "Id": "string",
   "RevocationComment": "string",
   "Revoked": boolean,
   "RevokedAt": "string",
   "SourceId": "string",
   "Tags": {
      "string" : "string"
   },
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_CreateRevision_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-Arn"></a>
The ARN for the revision.
Type: String

 ** [Comment](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-Comment"></a>
An optional comment about the revision.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.

 ** [CreatedAt](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-CreatedAt"></a>
The date and time that the revision was created, in ISO 8601 format.
Type: Timestamp

 ** [DataSetId](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-DataSetId"></a>
The unique identifier for the data set associated with the data set revision.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Finalized](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-Finalized"></a>
To publish a revision to a data set in a product, the revision must first be finalized. Finalizing a revision tells AWS Data Exchange that your changes to the assets in the revision are complete. After it's in this read-only state, you can publish the revision to your products. Finalized revisions can be published through the AWS Data Exchange console or the AWS Marketplace Catalog API, using the StartChangeSet AWS Marketplace Catalog API action. When using the API, revisions are uniquely identified by their ARN.
Type: Boolean

 ** [Id](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-Id"></a>
The unique identifier for the revision.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [RevocationComment](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-RevocationComment"></a>
A required comment to inform subscribers of the reason their access to the revision was revoked.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 512.

 ** [Revoked](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-Revoked"></a>
A status indicating that subscribers' access to the revision was revoked.
Type: Boolean

 ** [RevokedAt](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-RevokedAt"></a>
The date and time that the revision was revoked, in ISO 8601 format.
Type: Timestamp

 ** [SourceId](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-SourceId"></a>
The revision ID of the owned revision corresponding to the entitled revision being viewed. This parameter is returned when a revision owner is viewing the entitled copy of its owned revision.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Tags](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-Tags"></a>
The tags for the revision.
Type: String to string map

 ** [UpdatedAt](#API_CreateRevision_ResponseSyntax) **   <a name="dataexchange-CreateRevision-response-UpdatedAt"></a>
The date and time that the revision was last updated, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_CreateRevision_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the resource is denied.
 ** Message **
Access to the resource is denied.
HTTP Status Code: 403

 ** InternalServerException **
An exception occurred with the service.
 ** Message **
The message identifying the service exception that occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
 ** Message **
The resource couldn't be found.
 ** ResourceId **
The unique identifier for the resource that couldn't be found.
 ** ResourceType **
The type of resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** Message **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request was invalid.
 ** ExceptionCause **
The unique identifier for the resource that couldn't be found.
 ** Message **
The message that informs you about what was invalid about the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/CreateRevision)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/CreateRevision)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/CreateRevision)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/CreateRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/CreateRevision)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/CreateRevision)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/CreateRevision)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/CreateRevision)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/CreateRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/CreateRevision)
