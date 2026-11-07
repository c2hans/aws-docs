---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_BatchUpdateCase.html
---

# BatchUpdateCase
<a name="API_connect-cases_BatchUpdateCase"></a>

Updates fields on multiple cases in a single request. All cases must belong to the same domain. Set the title, status, and customer ID through the top-level `title`, `status`, and `customerId` parameters, and set other fields through the `fields` array.

Each case is processed independently. If some cases fail, the remaining cases are still updated. To determine whether individual cases failed, inspect the `failedCases` array in the response.

The entire request fails, and no cases are updated, in the following cases:
+ The specified domain doesn't exist.
+ A reference ID doesn't match any case in the domain.
+ The request contains duplicate case IDs.
+ The request doesn't specify any update. Provide at least one entry in `fields`, or a `title`, `status`, or `customerId`.
+ A field identifier in `fields` doesn't resolve to a field in the domain, for example, an unknown field name.
+ A field name contains a pipe (`|`) or comma (`,`) character.
+  `fields` includes `title`, `status`, or `customerId`.

**Note**
This operation uses the same IAM action as [UpdateCase](https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateCase.html) (`cases:UpdateCase`). You can use the `cases:IsBatchAction` condition key in IAM policies to allow or deny batch operations independently from single-case operations.

**Note**
If you provide a value for `performedBy.userArn`, you must also have [DescribeUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html) permission on the ARN of the user that you provide.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_connect-cases_BatchUpdateCase_RequestSyntax"></a>

```
PUT /cases:batchUpdateCase HTTP/1.1
Content-type: application/json

{
   "cases": [
      {
         "caseIdentifier": { ... }
      }
   ],
   "clientToken": "{{string}}",
   "customerId": "{{string}}",
   "domainId": "{{string}}",
   "fields": [
      {
         "fieldIdentifier": { ... },
         "value": { ... }
      }
   ],
   "performedBy": { ... },
   "status": "{{string}}",
   "title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-cases_BatchUpdateCase_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_connect-cases_BatchUpdateCase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [cases](#API_connect-cases_BatchUpdateCase_RequestSyntax) **   <a name="connect-connect-cases_BatchUpdateCase-request-cases"></a>
The list of cases to update. All cases must belong to the same domain.
Type: Array of [BatchUpdateCaseIdentifier](API_connect-cases_BatchUpdateCaseIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [clientToken](#API_connect-cases_BatchUpdateCase_RequestSyntax) **   <a name="connect-connect-cases_BatchUpdateCase-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
If you retry a request with the same client token, the service returns the original response instead of processing the request again. If you reuse a client token with different request parameters, the request fails with a `ConflictException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [customerId](#API_connect-cases_BatchUpdateCase_RequestSyntax) **   <a name="connect-connect-cases_BatchUpdateCase-request-customerId"></a>
The ARN of the customer profile to associate with all cases in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[a-zA-Z0-9/_\-:.]+`
Required: No

 ** [domainId](#API_connect-cases_BatchUpdateCase_RequestSyntax) **   <a name="connect-connect-cases_BatchUpdateCase-request-domainId"></a>
The unique identifier of the Cases domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [fields](#API_connect-cases_BatchUpdateCase_RequestSyntax) **   <a name="connect-connect-cases_BatchUpdateCase-request-fields"></a>
An array of objects, each with a `fieldIdentifier` and a `value`. You can identify each field by its ID or by its name; identifying a field by name is supported only in `BatchUpdateCase`. The same field values are applied to every case in the request. This field must be present, but can be an empty list when you provide the top-level `title`, `status`, or `customerId` parameters. Do not include `title`, `status`, or `customerId` in this list; set those values only through their top-level parameters. Duplicating them in `fields` results in a validation error.
Type: Array of [FieldValueInput](API_connect-cases_FieldValueInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 220 items.
Required: Yes

 ** [performedBy](#API_connect-cases_BatchUpdateCase_RequestSyntax) **   <a name="connect-connect-cases_BatchUpdateCase-request-performedBy"></a>
The entity that performed the action.
Type: [UserUnion](API_connect-cases_UserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [status](#API_connect-cases_BatchUpdateCase_RequestSyntax) **   <a name="connect-connect-cases_BatchUpdateCase-request-status"></a>
The status to apply to all cases in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_\-\s]+`
Required: No

 ** [title](#API_connect-cases_BatchUpdateCase_RequestSyntax) **   <a name="connect-connect-cases_BatchUpdateCase-request-title"></a>
The title to apply to all cases in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_connect-cases_BatchUpdateCase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedCases": [
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
   "successfulCases": [
      {
         "caseIdentifier": {
            "caseId": "string",
            "referenceId": "string",
            "referenceNumber": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_connect-cases_BatchUpdateCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedCases](#API_connect-cases_BatchUpdateCase_ResponseSyntax) **   <a name="connect-connect-cases_BatchUpdateCase-response-failedCases"></a>
The list of cases that were not updated. Each entry includes an error code and message. Possible error codes include:
+  `CASE_NOT_FOUND` - No case exists with the specified case ID.
+  `VALIDATION_ERROR` - The request contains invalid input.
+  `CONFLICT` - Another operation is in progress on the case, such as a concurrent update or a merge of the case into another case.
+  `THROTTLED` - The request rate exceeded the allowed limit.
+  `ACCESS_DENIED` - The caller lacks permission to perform the operation.
+  `SERVICE_QUOTA_EXCEEDED` - The request exceeded a service quota.
+  `DOMAIN_NOT_FOUND` - The case domain was deleted while the request was being processed.
+  `INTERNAL_ERROR` - An unexpected error occurred on the server.
Type: Array of [BatchUpdateCaseErrorEntry](API_connect-cases_BatchUpdateCaseErrorEntry.md) objects

 ** [successfulCases](#API_connect-cases_BatchUpdateCase_ResponseSyntax) **   <a name="connect-connect-cases_BatchUpdateCase-response-successfulCases"></a>
The list of cases that were successfully updated.
Type: Array of [BatchUpdateCaseSuccessEntry](API_connect-cases_BatchUpdateCaseSuccessEntry.md) objects

## Errors
<a name="API_connect-cases_BatchUpdateCase_Errors"></a>

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

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_BatchUpdateCase_Examples"></a>

### Request and Response example
<a name="API_connect-cases_BatchUpdateCase_Example_1"></a>

This example illustrates one usage of BatchUpdateCase.

```
{
  "domainId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "cases": [
    { "caseIdentifier": { "caseId": "11111111-2222-3333-4444-EXAMPLE11111" } },
    { "caseIdentifier": { "referenceId": "8G3KX7Q2M" } }
  ],
  "fields": [
    {
      "fieldIdentifier": { "name": "Priority" },
      "value": { "stringValue": "High" }
    }
  ],
  "status": "closed"
}
```

```
{
  "successfulCases": [
    {
      "caseIdentifier": {
        "caseId": "11111111-2222-3333-4444-EXAMPLE11111"
      }
    }
  ],
  "failedCases": [
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
<a name="API_connect-cases_BatchUpdateCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/BatchUpdateCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/BatchUpdateCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/BatchUpdateCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/BatchUpdateCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/BatchUpdateCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/BatchUpdateCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/BatchUpdateCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/BatchUpdateCase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/BatchUpdateCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/BatchUpdateCase)
