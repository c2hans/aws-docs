---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_BatchGetMemberAccountDetails.html
---

# BatchGetMemberAccountDetails
<a name="API_BatchGetMemberAccountDetails"></a>

Provides information on whether the supplied account IDs are associated with a membership.

**Note**
 AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be `123123123` which is nine digits, and with zero-prepend would be `000123123123`. Not zero-prepending to 12 digits could result in errors.

## Request Syntax
<a name="API_BatchGetMemberAccountDetails_RequestSyntax"></a>

```
POST /v1/membership/{{membershipId}}/batch-member-details HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetMemberAccountDetails_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipId](#API_BatchGetMemberAccountDetails_RequestSyntax) **   <a name="securityir-BatchGetMemberAccountDetails-request-uri-membershipId"></a>
Required element used in combination with BatchGetMemberAccountDetails to identify the membership ID to query.
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `m-[a-z0-9]{10,32}`
Required: Yes

## Request Body
<a name="API_BatchGetMemberAccountDetails_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_BatchGetMemberAccountDetails_RequestSyntax) **   <a name="securityir-BatchGetMemberAccountDetails-request-accountIds"></a>
Optional element to query the membership relationship status to a provided list of account IDs.
 AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be `123123123` which is nine digits, and with zero-prepend would be `000123123123`. Not zero-prepending to 12 digits could result in errors.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_BatchGetMemberAccountDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "accountId": "string",
         "error": "string",
         "message": "string"
      }
   ],
   "items": [
      {
         "accountId": "string",
         "relationshipStatus": "string",
         "relationshipType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetMemberAccountDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetMemberAccountDetails_ResponseSyntax) **   <a name="securityir-BatchGetMemberAccountDetails-response-errors"></a>
The response element providing error messages for requests to GetMembershipAccountDetails.
Type: Array of [GetMembershipAccountDetailError](API_GetMembershipAccountDetailError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [items](#API_BatchGetMemberAccountDetails_ResponseSyntax) **   <a name="securityir-BatchGetMemberAccountDetails-response-items"></a>
The response element providing responses for requests to GetMembershipAccountDetails.
Type: Array of [GetMembershipAccountDetailItem](API_GetMembershipAccountDetailItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_BatchGetMemberAccountDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** message **
The ID of the resource which lead to the access denial.
HTTP Status Code: 403

 ** ConflictException **
Returned when there is a conflict with the current state of the resource.
For UpdateResolverType, this error may occur when attempting to change an AWS-supported case to Self-managed, which is not supported.
 ** message **
The exception message.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **

 ** message **
The exception message.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
HTTP Status Code: 500

 ** InvalidTokenException **

 ** message **
The exception message.
HTTP Status Code: 423

 ** ResourceNotFoundException **

 ** message **
The exception message.
HTTP Status Code: 404

 ** SecurityIncidentResponseNotActiveException **

 ** message **
The exception message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

 ** message **
The exception message.
 ** quotaCode **
The code of the quota.
 ** resourceId **
The ID of the requested resource which lead to the service quota exception.
 ** resourceType **
The type of the requested resource which lead to the service quota exception.
 ** serviceCode **
The service code of the quota.
HTTP Status Code: 402

 ** ThrottlingException **

 ** message **
The exception message.
 ** quotaCode **
The quota code of the exception.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
 ** serviceCode **
The service code of the exception.
HTTP Status Code: 429

 ** ValidationException **
Returned when the request contains invalid parameters.
For UpdateResolverType, this error may occur when attempting an unsupported resolver type transition.
 ** fieldList **
The fields which lead to the exception.
 ** message **
The exception message.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetMemberAccountDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/BatchGetMemberAccountDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/BatchGetMemberAccountDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/BatchGetMemberAccountDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/BatchGetMemberAccountDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/BatchGetMemberAccountDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/BatchGetMemberAccountDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/BatchGetMemberAccountDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/BatchGetMemberAccountDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/BatchGetMemberAccountDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/BatchGetMemberAccountDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
