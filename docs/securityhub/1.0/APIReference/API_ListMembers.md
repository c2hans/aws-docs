---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListMembers.html
---

# ListMembers
<a name="API_ListMembers"></a>

Lists details about all member accounts for the current Security Hub CSPM administrator account.

The results include both member accounts that belong to an organization and member accounts that were invited manually.

## Request Syntax
<a name="API_ListMembers_RequestSyntax"></a>

```
GET /members?MaxResults={{MaxResults}}&NextToken={{NextToken}}&OnlyAssociated={{OnlyAssociated}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMembers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListMembers_RequestSyntax) **   <a name="securityhub-ListMembers-request-uri-MaxResults"></a>
The maximum number of items to return in the response.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListMembers_RequestSyntax) **   <a name="securityhub-ListMembers-request-uri-NextToken"></a>
The token that is required for pagination. On your first call to the `ListMembers` operation, set the value of this parameter to `NULL`.
For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.

 ** [OnlyAssociated](#API_ListMembers_RequestSyntax) **   <a name="securityhub-ListMembers-request-uri-OnlyAssociated"></a>
Specifies which member accounts to include in the response based on their relationship status with the administrator account. The default value is `TRUE`.
If `OnlyAssociated` is set to `TRUE`, the response includes member accounts whose relationship status with the administrator account is set to `ENABLED`.
If `OnlyAssociated` is set to `FALSE`, the response includes all existing member accounts.

## Request Body
<a name="API_ListMembers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMembers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Members": [
      {
         "AccountId": "string",
         "AdministratorId": "string",
         "Email": "string",
         "InvitedAt": "string",
         "MasterId": "string",
         "MemberStatus": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Members](#API_ListMembers_ResponseSyntax) **   <a name="securityhub-ListMembers-response-Members"></a>
Member details returned by the operation.
Type: Array of [Member](API_Member.md) objects

 ** [NextToken](#API_ListMembers_ResponseSyntax) **   <a name="securityhub-ListMembers-response-NextToken"></a>
The pagination token to use to request the next page of results.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_ListMembers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListMembers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListMembers)
