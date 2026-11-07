---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_BatchCreateRelatedItem.html
---

# BatchCreateRelatedItem
<a name="API_connect-cases_BatchCreateRelatedItem"></a>

Creates a comment and associates it with multiple cases in a single request. All cases must belong to the same domain. This operation supports only the Comment related item type.

Each case is processed independently. If some cases fail, the remaining cases still receive the related item. To determine whether individual items failed, inspect the `failedItems` array in the response.

The entire request fails, and no related items are created, in the following cases:
+ The specified domain doesn't exist.
+ A reference ID doesn't match any case in the domain.
+ The request contains duplicate case IDs.
+ The content isn't comment content.

**Note**
This operation uses the same IAM action as [CreateRelatedItem](https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateRelatedItem.html) (`cases:CreateRelatedItem`). You can use the `cases:IsBatchAction` condition key in IAM policies to allow or deny batch operations independently from single-case operations.

**Note**
If you provide a value for `performedBy.userArn`, you must also have [DescribeUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html) permission on the ARN of the user that you provide.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_connect-cases_BatchCreateRelatedItem_RequestSyntax"></a>

```
POST /cases:batchCreateRelatedItem HTTP/1.1
Content-type: application/json

{
   "cases": [
      {
         "caseIdentifier": { ... }
      }
   ],
   "clientToken": "{{string}}",
   "content": { ... },
   "domainId": "{{string}}",
   "performedBy": { ... }
}
```

## URI Request Parameters
<a name="API_connect-cases_BatchCreateRelatedItem_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_connect-cases_BatchCreateRelatedItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [cases](#API_connect-cases_BatchCreateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_BatchCreateRelatedItem-request-cases"></a>
The list of cases to associate the related item with. All cases must belong to the same domain.
Type: Array of [BatchCreateRelatedItemIdentifier](API_connect-cases_BatchCreateRelatedItemIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [clientToken](#API_connect-cases_BatchCreateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_BatchCreateRelatedItem-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
If you retry a request with the same client token, the service returns the original response instead of processing the request again. If you reuse a client token with different request parameters, the request fails with a `ConflictException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [content](#API_connect-cases_BatchCreateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_BatchCreateRelatedItem-request-content"></a>
The content of the related item to be created. The same content is applied to every case in the request. Only comment content is supported for batch creation.
Type: [RelatedItemInputContent](API_connect-cases_RelatedItemInputContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [domainId](#API_connect-cases_BatchCreateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_BatchCreateRelatedItem-request-domainId"></a>
The unique identifier of the Cases domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [performedBy](#API_connect-cases_BatchCreateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_BatchCreateRelatedItem-request-performedBy"></a>
The entity that created the related item.
Type: [UserUnion](API_connect-cases_UserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_connect-cases_BatchCreateRelatedItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedItems": [
      {
         "caseIdentifier": {
            "caseId": "string",
            "referenceId": "string",
            "referenceNumber": "string"
         },
         "errorCode": "string",
         "errorMessage": "string"
      }
   ],
   "successfulItems": [
      {
         "caseIdentifier": {
            "caseId": "string",
            "referenceId": "string",
            "referenceNumber": "string"
         },
         "relatedItemArn": "string",
         "relatedItemId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-cases_BatchCreateRelatedItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedItems](#API_connect-cases_BatchCreateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_BatchCreateRelatedItem-response-failedItems"></a>
The list of related items that were not created. Each entry includes an error code and message. Possible error codes include:
+  `CASE_NOT_FOUND` - No case exists with the specified case ID.
+  `VALIDATION_ERROR` - The request contains invalid input.
+  `CONFLICT` - Another operation is in progress on the case, such as a concurrent update or a merge of the case into another case.
+  `THROTTLED` - The request rate exceeded the allowed limit.
+  `ACCESS_DENIED` - The caller lacks permission to perform the operation.
+  `SERVICE_QUOTA_EXCEEDED` - The request exceeded a service quota.
+  `DOMAIN_NOT_FOUND` - The case domain was deleted while the request was being processed.
+  `INTERNAL_ERROR` - An unexpected error occurred on the server.
Type: Array of [BatchCreateRelatedItemErrorEntry](API_connect-cases_BatchCreateRelatedItemErrorEntry.md) objects

 ** [successfulItems](#API_connect-cases_BatchCreateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_BatchCreateRelatedItem-response-successfulItems"></a>
The list of related items that were successfully created and associated with their cases.
Type: Array of [BatchCreateRelatedItemSuccessEntry](API_connect-cases_BatchCreateRelatedItemSuccessEntry.md) objects

## Errors
<a name="API_connect-cases_BatchCreateRelatedItem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.
HTTP Status Code: 409

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
 ** resourceId **
Unique identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded. For a list of service quotas, see [Connect Customer Service Quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html) in the *Connect Customer Administrator Guide*.
HTTP Status Code: 402

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_BatchCreateRelatedItem_Examples"></a>

### Request and Response example
<a name="API_connect-cases_BatchCreateRelatedItem_Example_1"></a>

This example illustrates one usage of BatchCreateRelatedItem.

```
{
  "domainId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "content": {
    "comment": {
      "body": "We've identified the cause of the outage and are working on a fix.",
      "contentType": "Text/Plain"
    }
  },
  "cases": [
    { "caseIdentifier": { "caseId": "11111111-2222-3333-4444-EXAMPLE11111" } },
    { "caseIdentifier": { "referenceId": "8G3KX7Q2M" } }
  ]
}
```

```
{
  "successfulItems": [
    {
      "caseIdentifier": {
        "caseId": "11111111-2222-3333-4444-EXAMPLE11111"
      },
      "relatedItemId": "22222222-3333-4444-5555-EXAMPLE33333",
      "relatedItemArn": "arn:aws:cases:us-west-2:111122223333:domain/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/case/11111111-2222-3333-4444-EXAMPLE11111/related-item/22222222-3333-4444-5555-EXAMPLE33333"
    }
  ],
  "failedItems": [
    {
      "caseIdentifier": {
        "caseId": "11111111-2222-3333-4444-EXAMPLE22222",
        "referenceId": "8G3KX7Q2M"
      },
      "errorCode": "CONFLICT",
      "errorMessage": "The case has a conflicting operation in progress"
    }
  ]
}
```

## See Also
<a name="API_connect-cases_BatchCreateRelatedItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/BatchCreateRelatedItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/BatchCreateRelatedItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/BatchCreateRelatedItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/BatchCreateRelatedItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/BatchCreateRelatedItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/BatchCreateRelatedItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/BatchCreateRelatedItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/BatchCreateRelatedItem)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/BatchCreateRelatedItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/BatchCreateRelatedItem)
