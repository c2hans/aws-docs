---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ListAccountLinks.html
---

# ListAccountLinks
<a name="API_ListAccountLinks"></a>

Lists all account links.

## Request Syntax
<a name="API_ListAccountLinks_RequestSyntax"></a>

```
{
   "LinkStatusFilter": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAccountLinks_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [LinkStatusFilter](#API_ListAccountLinks_RequestSyntax) **   <a name="WorkSpaces-ListAccountLinks-request-LinkStatusFilter"></a>
Filters the account based on their link status.
Type: Array of strings
Valid Values: `LINKED | LINKING_FAILED | LINK_NOT_FOUND | PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT | REJECTED`
Required: No

 ** [MaxResults](#API_ListAccountLinks_RequestSyntax) **   <a name="WorkSpaces-ListAccountLinks-request-MaxResults"></a>
The maximum number of accounts to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_ListAccountLinks_RequestSyntax) **   <a name="WorkSpaces-ListAccountLinks-request-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListAccountLinks_ResponseSyntax"></a>

```
{
   "AccountLinks": [
      {
         "AccountLinkId": "string",
         "AccountLinkStatus": "string",
         "SourceAccountId": "string",
         "TargetAccountId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAccountLinks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountLinks](#API_ListAccountLinks_ResponseSyntax) **   <a name="WorkSpaces-ListAccountLinks-response-AccountLinks"></a>
Information about the account links.
Type: Array of [AccountLink](API_AccountLink.md) objects

 ** [NextToken](#API_ListAccountLinks_ResponseSyntax) **   <a name="WorkSpaces-ListAccountLinks-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListAccountLinks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected server error occured.
HTTP Status Code: 400

 ** ValidationException **
You either haven't provided a `TargetAccountId` or are using the same value for `TargetAccountId` and `SourceAccountId`.
HTTP Status Code: 400

## See Also
<a name="API_ListAccountLinks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ListAccountLinks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ListAccountLinks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ListAccountLinks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ListAccountLinks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ListAccountLinks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ListAccountLinks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ListAccountLinks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ListAccountLinks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ListAccountLinks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ListAccountLinks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
