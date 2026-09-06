---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_DescribeEntity.html
---

# DescribeEntity
<a name="API_DescribeEntity"></a>

Returns the metadata and content of the entity.

## Request Syntax
<a name="API_DescribeEntity_RequestSyntax"></a>

```
GET /DescribeEntity?catalog={{Catalog}}&entityId={{EntityId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeEntity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Catalog](#API_DescribeEntity_RequestSyntax) **   <a name="AWSMarketplaceService-DescribeEntity-request-uri-Catalog"></a>
Required. The catalog related to the request. Fixed value: `AWSMarketplace`
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z]+$`
Required: Yes

 ** [EntityId](#API_DescribeEntity_RequestSyntax) **   <a name="AWSMarketplaceService-DescribeEntity-request-uri-EntityId"></a>
Required. The unique ID of the entity to describe.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`
Required: Yes

## Request Body
<a name="API_DescribeEntity_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeEntity_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Details": "string",
   "DetailsDocument": JSON value,
   "EntityArn": "string",
   "EntityIdentifier": "string",
   "EntityType": "string",
   "LastModifiedDate": "string"
}
```

## Response Elements
<a name="API_DescribeEntity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Details](#API_DescribeEntity_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeEntity-response-Details"></a>
This stringified JSON object includes the details of the entity.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 16384.
Pattern: `^[\s]*\{[\s\S]*\}[\s]*$`

 ** [DetailsDocument](#API_DescribeEntity_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeEntity-response-DetailsDocument"></a>
The JSON value of the details specific to the entity.
To download "DetailsDocument" shapes, see the [Python](https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python) and [Java](https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-java/tree/main) shapes on GitHub.
Type: JSON value

 ** [EntityArn](#API_DescribeEntity_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeEntity-response-EntityArn"></a>
The ARN associated to the unique identifier for the entity referenced in this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9:*/-]+$`

 ** [EntityIdentifier](#API_DescribeEntity_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeEntity-response-EntityIdentifier"></a>
The identifier of the entity, in the format of `EntityId@RevisionId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-@]+$`

 ** [EntityType](#API_DescribeEntity_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeEntity-response-EntityType"></a>
The named type of the entity, in the format of `EntityType@Version`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z]+$`

 ** [LastModifiedDate](#API_DescribeEntity_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeEntity-response-LastModifiedDate"></a>
The last modified date of the entity, in ISO 8601 format (2018-02-27T13:45:22Z).
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`

## Errors
<a name="API_DescribeEntity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP status code: 403
HTTP Status Code: 403

 ** InternalServiceException **
There was an internal service exception.
HTTP status code: 500
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource wasn't found.
HTTP status code: 404
HTTP Status Code: 404

 ** ResourceNotSupportedException **
Currently, the specified resource is not supported.
HTTP Status Code: 415

 ** ThrottlingException **
Too many requests.
HTTP status code: 429
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
HTTP status code: 422
HTTP Status Code: 422

## See Also
<a name="API_DescribeEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-catalog-2018-09-17/DescribeEntity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-catalog-2018-09-17/DescribeEntity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/DescribeEntity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-catalog-2018-09-17/DescribeEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/DescribeEntity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-catalog-2018-09-17/DescribeEntity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-catalog-2018-09-17/DescribeEntity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-catalog-2018-09-17/DescribeEntity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/DescribeEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/DescribeEntity)
