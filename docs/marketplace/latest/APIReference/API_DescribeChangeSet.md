---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_DescribeChangeSet.html
---

# DescribeChangeSet
<a name="API_DescribeChangeSet"></a>

Provides information about a given change set.

## Request Syntax
<a name="API_DescribeChangeSet_RequestSyntax"></a>

```
GET /DescribeChangeSet?catalog={{Catalog}}&changeSetId={{ChangeSetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeChangeSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Catalog](#API_DescribeChangeSet_RequestSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-request-uri-Catalog"></a>
Required. The catalog related to the request. Fixed value: `AWSMarketplace`
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z]+$`
Required: Yes

 ** [ChangeSetId](#API_DescribeChangeSet_RequestSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-request-uri-ChangeSetId"></a>
Required. The unique identifier for the `StartChangeSet` request that you want to describe the details for.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`
Required: Yes

## Request Body
<a name="API_DescribeChangeSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeChangeSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChangeSet": [
      {
         "ChangeName": "string",
         "ChangeType": "string",
         "Details": "string",
         "DetailsDocument": JSON value,
         "Entity": {
            "Identifier": "string",
            "Type": "string"
         },
         "ErrorDetailList": [
            {
               "ErrorCode": "string",
               "ErrorMessage": "string"
            }
         ]
      }
   ],
   "ChangeSetArn": "string",
   "ChangeSetId": "string",
   "ChangeSetName": "string",
   "EndTime": "string",
   "FailureCode": "string",
   "FailureDescription": "string",
   "Intent": "string",
   "StartTime": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeChangeSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeSet](#API_DescribeChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-response-ChangeSet"></a>
An array of `ChangeSummary` objects.
Type: Array of [ChangeSummary](API_ChangeSummary.md) objects

 ** [ChangeSetArn](#API_DescribeChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-response-ChangeSetArn"></a>
The ARN associated with the unique identifier for the change set referenced in this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9:*/-]+$`

 ** [ChangeSetId](#API_DescribeChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-response-ChangeSetId"></a>
Required. The unique identifier for the change set referenced in this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`

 ** [ChangeSetName](#API_DescribeChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-response-ChangeSetName"></a>
The optional name provided in the `StartChangeSet` request. If you do not provide a name, one is set by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w\s+=.:@-]+$`

 ** [EndTime](#API_DescribeChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-response-EndTime"></a>
The date and time, in ISO 8601 format (2018-02-27T13:45:22Z), the request transitioned to a terminal state. The change cannot transition to a different state. Null if the request is not in a terminal state.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`

 ** [FailureCode](#API_DescribeChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-response-FailureCode"></a>
Returned if the change set is in `FAILED` status. Can be either `CLIENT_ERROR`, which means that there are issues with the request (see the `ErrorDetailList`), or `SERVER_FAULT`, which means that there is a problem in the system, and you should retry your request.
Type: String
Valid Values: `CLIENT_ERROR | SERVER_FAULT`

 ** [FailureDescription](#API_DescribeChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-response-FailureDescription"></a>
Returned if there is a failure on the change set, but that failure is not related to any of the changes in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(.)+$`

 ** [Intent](#API_DescribeChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-response-Intent"></a>
The optional intent provided in the `StartChangeSet` request. If you do not provide an intent, `APPLY` is set by default.
Type: String
Valid Values: `VALIDATE | APPLY`

 ** [StartTime](#API_DescribeChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-response-StartTime"></a>
The date and time, in ISO 8601 format (2018-02-27T13:45:22Z), the request started.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^([\d]{4})\-(1[0-2]|0[1-9])\-(3[01]|0[1-9]|[12][\d])T(2[0-3]|[01][\d]):([0-5][\d]):([0-5][\d])Z$`

 ** [Status](#API_DescribeChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-DescribeChangeSet-response-Status"></a>
The status of the change request.
Type: String
Valid Values: `PREPARING | APPLYING | SUCCEEDED | CANCELLED | FAILED`

## Errors
<a name="API_DescribeChangeSet_Errors"></a>

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

 ** ThrottlingException **
Too many requests.
HTTP status code: 429
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
HTTP status code: 422
HTTP Status Code: 422

## See Also
<a name="API_DescribeChangeSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-catalog-2018-09-17/DescribeChangeSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-catalog-2018-09-17/DescribeChangeSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/DescribeChangeSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-catalog-2018-09-17/DescribeChangeSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/DescribeChangeSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-catalog-2018-09-17/DescribeChangeSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-catalog-2018-09-17/DescribeChangeSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-catalog-2018-09-17/DescribeChangeSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/DescribeChangeSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/DescribeChangeSet)
