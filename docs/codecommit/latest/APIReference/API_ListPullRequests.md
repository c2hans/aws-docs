---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListPullRequests.html
---

# ListPullRequests
<a name="API_ListPullRequests"></a>

Returns a list of pull requests for a specified repository. The return list can be refined by pull request status or pull request author ARN.

## Request Syntax
<a name="API_ListPullRequests_RequestSyntax"></a>

```
{
   "authorArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "pullRequestStatus": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPullRequests_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [authorArn](#API_ListPullRequests_RequestSyntax) **   <a name="CodeCommit-ListPullRequests-request-authorArn"></a>
Optional. The Amazon Resource Name (ARN) of the user who created the pull request. If used, this filters the results to pull requests created by that user.
Type: String
Required: No

 ** [maxResults](#API_ListPullRequests_RequestSyntax) **   <a name="CodeCommit-ListPullRequests-request-maxResults"></a>
A non-zero, non-negative integer used to limit the number of returned results.
Type: Integer
Required: No

 ** [nextToken](#API_ListPullRequests_RequestSyntax) **   <a name="CodeCommit-ListPullRequests-request-nextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Required: No

 ** [pullRequestStatus](#API_ListPullRequests_RequestSyntax) **   <a name="CodeCommit-ListPullRequests-request-pullRequestStatus"></a>
Optional. The status of the pull request. If used, this refines the results to the pull requests that match the specified status.
Type: String
Valid Values: `OPEN | CLOSED`
Required: No

 ** [repositoryName](#API_ListPullRequests_RequestSyntax) **   <a name="CodeCommit-ListPullRequests-request-repositoryName"></a>
The name of the repository for which you want to list pull requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_ListPullRequests_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "pullRequestIds": [ "string" ]
}
```

## Response Elements
<a name="API_ListPullRequests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPullRequests_ResponseSyntax) **   <a name="CodeCommit-ListPullRequests-response-nextToken"></a>
An enumeration token that allows the operation to batch the next results of the operation.
Type: String

 ** [pullRequestIds](#API_ListPullRequests_ResponseSyntax) **   <a name="CodeCommit-ListPullRequests-response-pullRequestIds"></a>
The system-generated IDs of the pull requests.
Type: Array of strings

## Errors
<a name="API_ListPullRequests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorDoesNotExistException **
The specified Amazon Resource Name (ARN) does not exist in the AWS account.
HTTP Status Code: 400

 ** EncryptionIntegrityChecksFailedException **
An encryption integrity check failed.
HTTP Status Code: 500

 ** EncryptionKeyAccessDeniedException **
An encryption key could not be accessed.
HTTP Status Code: 400

 ** EncryptionKeyDisabledException **
The encryption key is disabled.
HTTP Status Code: 400

 ** EncryptionKeyNotFoundException **
No encryption key was found.
HTTP Status Code: 400

 ** EncryptionKeyUnavailableException **
The encryption key is not available.
HTTP Status Code: 400

 ** InvalidAuthorArnException **
The Amazon Resource Name (ARN) is not valid. Make sure that you have provided the full ARN for the author of the pull request, and then try again.
HTTP Status Code: 400

 ** InvalidContinuationTokenException **
The specified continuation token is not valid.
HTTP Status Code: 400

 ** InvalidMaxResultsException **
The specified number of maximum results is not valid.
HTTP Status Code: 400

 ** InvalidPullRequestStatusException **
The pull request status is not valid. The only valid values are `OPEN` and `CLOSED`.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_ListPullRequests_Examples"></a>

### Example
<a name="API_ListPullRequests_Example_1"></a>

This example illustrates one usage of ListPullRequests.

#### Sample Request
<a name="API_ListPullRequests_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 174
X-Amz-Target: CodeCommit_20150413.ListPullRequests
X-Amz-Date: 20171025T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "authorArn": "arn:aws:iam::123456789012:user/Li_Juan",
   "maxResults": 20,
   "nextToken": "",
   "pullRequestStatus": "CLOSED",
   "repositoryName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_ListPullRequests_Example_1_Response"></a>

```
{
   "nextToken": "exampleToken",
   "pullRequestIds": ["2","12","16","22","30","23","35","39","47"]
}
```

## See Also
<a name="API_ListPullRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/ListPullRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/ListPullRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ListPullRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/ListPullRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ListPullRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/ListPullRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/ListPullRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/ListPullRequests)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/ListPullRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ListPullRequests)
