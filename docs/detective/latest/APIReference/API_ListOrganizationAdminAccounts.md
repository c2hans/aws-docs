---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_ListOrganizationAdminAccounts.html
---

# ListOrganizationAdminAccounts
<a name="API_ListOrganizationAdminAccounts"></a>

Returns information about the Detective administrator account for an organization. Can only be called by the organization management account.

ListOrganizationAdminAccounts is authorized on the `detective:ListOrganizationAdminAccount` identity-based action.

## Request Syntax
<a name="API_ListOrganizationAdminAccounts_RequestSyntax"></a>

```
POST /orgs/adminAccountslist HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListOrganizationAdminAccounts_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListOrganizationAdminAccounts_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListOrganizationAdminAccounts_RequestSyntax) **   <a name="detective-ListOrganizationAdminAccounts-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_ListOrganizationAdminAccounts_RequestSyntax) **   <a name="detective-ListOrganizationAdminAccounts-request-NextToken"></a>
For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListOrganizationAdminAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Administrators": [
      {
         "AccountId": "string",
         "DelegationTime": "string",
         "GraphArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListOrganizationAdminAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Administrators](#API_ListOrganizationAdminAccounts_ResponseSyntax) **   <a name="detective-ListOrganizationAdminAccounts-response-Administrators"></a>
The list of Detective administrator accounts.
Type: Array of [Administrator](API_Administrator.md) objects

 ** [NextToken](#API_ListOrganizationAdminAccounts_ResponseSyntax) **   <a name="detective-ListOrganizationAdminAccounts-response-NextToken"></a>
If there are more accounts remaining in the results, then this is the pagination token to use to request the next page of accounts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListOrganizationAdminAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request cannot be completed because too many other requests are occurring at the same time.
HTTP Status Code: 429

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## Examples
<a name="API_ListOrganizationAdminAccounts_Examples"></a>

### Example
<a name="API_ListOrganizationAdminAccounts_Example_1"></a>

This example illustrates one usage of ListOrganizationAdminAccounts.

#### Sample Request
<a name="API_ListOrganizationAdminAccounts_Example_1_Request"></a>

```
POST /orgs/adminAccountslist HTTP/1.1
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 0
Authorization: AUTHPARAMS
X-Amz-Date: 20210923T193018Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33
```

### Example
<a name="API_ListOrganizationAdminAccounts_Example_2"></a>

This example illustrates one usage of ListOrganizationAdminAccounts.

#### Sample Response
<a name="API_ListOrganizationAdminAccounts_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 173
Date: Thu, 23 Sep 2021 23:07:46 GMT
x-amzn-RequestId: 397d0549-0092-11e8-a0ee-a7f9aa6e7572
Connection: Keep-alive

{
   "Administrators": [
      {
         "AccountId": "111122223333",
         "DelegationTime": "2021-09-23T:14:17:40.812Z",
         "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899"
      }
   ]
}
```

## See Also
<a name="API_ListOrganizationAdminAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/ListOrganizationAdminAccounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
