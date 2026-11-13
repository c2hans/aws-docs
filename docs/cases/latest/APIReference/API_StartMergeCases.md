---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_StartMergeCases.html
---

# StartMergeCases
<a name="API_connect-cases_StartMergeCases"></a>

Merges a secondary case into a primary case. The primary case, which you specify in the request URI, remains active. Both cases must belong to the same domain.

The merge runs asynchronously. To track its progress, call [GetMergeCasesStatus](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetMergeCasesStatus.html). When the merge finishes, the selected field values and related items from the secondary case are on the primary case, the two cases are linked, and the secondary case is closed. Both cases record the merge in their audit history. For more information, see [GetCaseAuditEvents](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCaseAuditEvents.html).

 **Important things to know**
+ Both cases must have the same customer, or at least one of them must have no customer.
+ While the merge runs, you can't modify the secondary case or its related items, and you can't delete the primary case. These requests return a `ConflictException`.
+ After the merge, the secondary case can be reopened, updated, and deleted, but it can't be merged again.

The request fails with a `ValidationException`, and no merge starts, if:
+ The primary case and the secondary case are the same case.
+ Either case is closed.
+ Both cases have a customer, and the customers are different.
+  `fieldsConfiguration` selects a field that can't be merged, or a field that the secondary case doesn't have.
+ After the merge, the primary case would have more than 500 field values, or would exceed the maximum case size.

The request fails with a `ServiceQuotaExceededException` if, after the merge, either case would exceed the quota for related items per case. For the primary case, the count is its existing related items, plus the related items moved from the secondary case, plus the new case link. See [Connect Customer Cases quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#cases-quotas).

The request fails with a `ConflictException` if either case is already part of a merge that is running, or was previously merged into another case as the secondary case.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_connect-cases_StartMergeCases_RequestSyntax"></a>

```
POST /domains/{{domainId}}/cases/{{caseId}}/merge HTTP/1.1
Content-type: application/json

{
   "fieldsConfiguration": [
      {
         "fieldIds": [
            {
               "id": "{{string}}"
            }
         ],
         "sourceCaseId": "{{string}}"
      }
   ],
   "performedBy": { ... },
   "relatedItemsConfiguration": {
      "comment": {{boolean}},
      "connectCase": {{boolean}},
      "contact": {{boolean}},
      "custom": {{boolean}}
   },
   "secondaryCaseIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_connect-cases_StartMergeCases_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_connect-cases_StartMergeCases_RequestSyntax) **   <a name="connect-connect-cases_StartMergeCases-request-uri-caseId"></a>
The unique identifier of the primary case. The primary case remains active and receives the merged field values and related items. The cases can use different templates, and the primary case keeps its template.
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`
Required: Yes

 ** [domainId](#API_connect-cases_StartMergeCases_RequestSyntax) **   <a name="connect-connect-cases_StartMergeCases-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_StartMergeCases_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [fieldsConfiguration](#API_connect-cases_StartMergeCases_RequestSyntax) **   <a name="connect-connect-cases_StartMergeCases-request-fieldsConfiguration"></a>
The fields whose values to take from the secondary case. You can only merge custom fields and the following system fields: `assigned_queue`, `assigned_user`, `summary`, and `case_reason`. If you select any other system field, the request fails with a `ValidationException`.
For each field that can be merged, the merge works as follows:
+ If you select the field, the primary case gets the secondary case's value. If the secondary case's value is empty, the primary case's value is cleared.
+ If you don't select the field and the primary case has a value for it, the primary case keeps its value.
+ If you don't select the field and the primary case doesn't have the field, or its value is empty, the primary case gets the secondary case's value. This applies even when the field isn't on the primary case's template.
Field values are read from both cases when the merge runs, so changes that you make to the primary case after you start the merge are taken into account.
Specify at most one entry, and set its `sourceCaseId` to the secondary case ID.
Type: Array of [FieldsConfiguration](API_connect-cases_FieldsConfiguration.md) objects
Required: No

 ** [performedBy](#API_connect-cases_StartMergeCases_RequestSyntax) **   <a name="connect-connect-cases_StartMergeCases-request-performedBy"></a>
The user who performed the merge. If you provide `userArn`, you must also have [DescribeUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html) permission on the ARN of that user.
Type: [UserUnion](API_connect-cases_UserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [relatedItemsConfiguration](#API_connect-cases_StartMergeCases_RequestSyntax) **   <a name="connect-connect-cases_StartMergeCases-request-relatedItemsConfiguration"></a>
The types of related items to move from the secondary case to the primary case. Related items of a type that you don't select, or set to `false`, stay on the closed secondary case. If you omit this parameter, no related items are moved.
File, SLA, and work plan related items are never moved. They stay on the secondary case.
Type: [RelatedItemsConfiguration](API_connect-cases_RelatedItemsConfiguration.md) object
Required: No

 ** [secondaryCaseIds](#API_connect-cases_StartMergeCases_RequestSyntax) **   <a name="connect-connect-cases_StartMergeCases-request-secondaryCaseIds"></a>
The unique identifier of the secondary case to merge into the primary case. The secondary case is closed when the merge finishes. Specify exactly one case ID.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`
Required: Yes

## Response Syntax
<a name="API_connect-cases_StartMergeCases_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-cases_StartMergeCases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-cases_StartMergeCases_Errors"></a>

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
<a name="API_connect-cases_StartMergeCases_Examples"></a>

### Request and Response example
<a name="API_connect-cases_StartMergeCases_Example_1"></a>

This example illustrates one usage of StartMergeCases.

```
{
  "secondaryCaseIds": [
    "[secondary_case_id]"
  ],
  "fieldsConfiguration": [
    {
      "sourceCaseId": "[secondary_case_id]",
      "fieldIds": [
        { "id": "[field_id]" }
      ]
    }
  ],
  "relatedItemsConfiguration": {
    "comment": true,
    "connectCase": true,
    "contact": true,
    "custom": true
  },
  "performedBy": {
    "userArn": "arn:aws:connect:us-west-2:[account_id]:instance/[instance_id]/agent/[agent_id]"
  }
}
```

```
{ }
```

## See Also
<a name="API_connect-cases_StartMergeCases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/StartMergeCases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/StartMergeCases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/StartMergeCases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/StartMergeCases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/StartMergeCases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/StartMergeCases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/StartMergeCases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/StartMergeCases)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/StartMergeCases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/StartMergeCases)
