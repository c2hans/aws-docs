---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListRepositories.html
---

# ListRepositories
<a name="API_ListRepositories"></a>

Gets information about one or more repositories.

## Request Syntax
<a name="API_ListRepositories_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}",
   "order": "{{string}}",
   "sortBy": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRepositories_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListRepositories_RequestSyntax) **   <a name="CodeCommit-ListRepositories-request-nextToken"></a>
An enumeration token that allows the operation to batch the results of the operation. Batch sizes are 1,000 for list repository operations. When the client sends the token back to AWS CodeCommit, another page of 1,000 records is retrieved.
Type: String
Required: No

 ** [order](#API_ListRepositories_RequestSyntax) **   <a name="CodeCommit-ListRepositories-request-order"></a>
The order in which to sort the results of a list repositories operation.
Type: String
Valid Values: `ascending | descending`
Required: No

 ** [sortBy](#API_ListRepositories_RequestSyntax) **   <a name="CodeCommit-ListRepositories-request-sortBy"></a>
The criteria used to sort the results of a list repositories operation.
Type: String
Valid Values: `repositoryName | lastModifiedDate`
Required: No

## Response Syntax
<a name="API_ListRepositories_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "repositories": [
      {
         "repositoryId": "string",
         "repositoryName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRepositories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRepositories_ResponseSyntax) **   <a name="CodeCommit-ListRepositories-response-nextToken"></a>
An enumeration token that allows the operation to batch the results of the operation. Batch sizes are 1,000 for list repository operations. When the client sends the token back to AWS CodeCommit, another page of 1,000 records is retrieved.
Type: String

 ** [repositories](#API_ListRepositories_ResponseSyntax) **   <a name="CodeCommit-ListRepositories-response-repositories"></a>
Lists the repositories called by the list repositories operation.
Type: Array of [RepositoryNameIdPair](API_RepositoryNameIdPair.md) objects

## Errors
<a name="API_ListRepositories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidContinuationTokenException **
The specified continuation token is not valid.
HTTP Status Code: 400

 ** InvalidOrderException **
The specified sort order is not valid.
HTTP Status Code: 400

 ** InvalidSortByException **
The specified sort by value is not valid.
HTTP Status Code: 400

## Examples
<a name="API_ListRepositories_Examples"></a>

### Example
<a name="API_ListRepositories_Example_1"></a>

This example illustrates one usage of ListRepositories.

#### Sample Request
<a name="API_ListRepositories_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: CodeCommit_20150413.ListRepositories
X-Amz-Date: 20151028T212036Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{}
```

#### Sample Response
<a name="API_ListRepositories_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 721
Date: Wed, 28 Oct 2015 21:20:37 GMT

{
  "repositories":[
    {
	  "repositoryId": "f7579e13-b83e-4027-aaef-650c0EXAMPLE",
      "repositoryName": "MyDemoRepo"
    },
    {
      "repositoryId": "cfc29ac4-b0cb-44dc-9990-f6f51EXAMPLE"
	  "repositoryName": "MyOtherDemoRepo"
    }
  ]
}
```

## See Also
<a name="API_ListRepositories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/ListRepositories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/ListRepositories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ListRepositories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/ListRepositories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ListRepositories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/ListRepositories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/ListRepositories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/ListRepositories)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/ListRepositories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ListRepositories)
