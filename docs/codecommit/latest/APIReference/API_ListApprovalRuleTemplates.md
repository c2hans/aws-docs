---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListApprovalRuleTemplates.html
---

# ListApprovalRuleTemplates
<a name="API_ListApprovalRuleTemplates"></a>

Lists all approval rule templates in the specified AWS Region in your AWS account. If an AWS Region is not specified, the AWS Region where you are signed in is used.

## Request Syntax
<a name="API_ListApprovalRuleTemplates_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListApprovalRuleTemplates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListApprovalRuleTemplates_RequestSyntax) **   <a name="CodeCommit-ListApprovalRuleTemplates-request-maxResults"></a>
A non-zero, non-negative integer used to limit the number of returned results.
Type: Integer
Required: No

 ** [nextToken](#API_ListApprovalRuleTemplates_RequestSyntax) **   <a name="CodeCommit-ListApprovalRuleTemplates-request-nextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Required: No

## Response Syntax
<a name="API_ListApprovalRuleTemplates_ResponseSyntax"></a>

```
{
   "approvalRuleTemplateNames": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApprovalRuleTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalRuleTemplateNames](#API_ListApprovalRuleTemplates_ResponseSyntax) **   <a name="CodeCommit-ListApprovalRuleTemplates-response-approvalRuleTemplateNames"></a>
The names of all the approval rule templates found in the AWS Region for your AWS account.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [nextToken](#API_ListApprovalRuleTemplates_ResponseSyntax) **   <a name="CodeCommit-ListApprovalRuleTemplates-response-nextToken"></a>
An enumeration token that allows the operation to batch the next results of the operation.
Type: String

## Errors
<a name="API_ListApprovalRuleTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidContinuationTokenException **
The specified continuation token is not valid.
HTTP Status Code: 400

 ** InvalidMaxResultsException **
The specified number of maximum results is not valid.
HTTP Status Code: 400

## Examples
<a name="API_ListApprovalRuleTemplates_Examples"></a>

### Example
<a name="API_ListApprovalRuleTemplates_Example_1"></a>

This example illustrates one usage of ListApprovalRuleTemplates.

#### Sample Request
<a name="API_ListApprovalRuleTemplates_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 33
X-Amz-Target: CodeCommit_20150413.ListApprovalRuleTemplates
X-Amz-Date: 20191021T230050Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{}
```

#### Sample Response
<a name="API_ListApprovalRuleTemplates_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 248
Date: Mon, 21 Oct 2019 23:00:52 GMT

{
    "approvalRuleTemplateNames": [
        "2-approver-rule-for-main",
        "1-approver-rule-for-all-pull-requests"
    ]
}
```

## See Also
<a name="API_ListApprovalRuleTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/ListApprovalRuleTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/ListApprovalRuleTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ListApprovalRuleTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/ListApprovalRuleTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ListApprovalRuleTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/ListApprovalRuleTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/ListApprovalRuleTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/ListApprovalRuleTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/ListApprovalRuleTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ListApprovalRuleTemplates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
