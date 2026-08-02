---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListRepositoryLinks.html
---

# ListRepositoryLinks
<a name="API_ListRepositoryLinks"></a>

Lists the repository links created for connections in your account.

## Request Syntax
<a name="API_ListRepositoryLinks_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRepositoryLinks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRepositoryLinks_RequestSyntax) **   <a name="codeconnections-ListRepositoryLinks-request-MaxResults"></a>
 A non-zero, non-negative integer used to limit the number of returned results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListRepositoryLinks_RequestSyntax) **   <a name="codeconnections-ListRepositoryLinks-request-NextToken"></a>
 An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^.*$`
Required: No

## Response Syntax
<a name="API_ListRepositoryLinks_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RepositoryLinks": [
      {
         "ConnectionArn": "string",
         "EncryptionKeyArn": "string",
         "OwnerId": "string",
         "ProviderType": "string",
         "RepositoryLinkArn": "string",
         "RepositoryLinkId": "string",
         "RepositoryName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRepositoryLinks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRepositoryLinks_ResponseSyntax) **   <a name="codeconnections-ListRepositoryLinks-response-NextToken"></a>
An enumeration token that allows the operation to batch the results of the operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^.*$`

 ** [RepositoryLinks](#API_ListRepositoryLinks_ResponseSyntax) **   <a name="codeconnections-ListRepositoryLinks-response-RepositoryLinks"></a>
Lists the repository links called by the list repository links operation.
Type: Array of [RepositoryLinkInfo](API_RepositoryLinkInfo.md) objects

## Errors
<a name="API_ListRepositoryLinks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.
HTTP Status Code: 400

 ** InternalServerException **
Received an internal server exception. Try again later.
HTTP Status Code: 400

 ** InvalidInputException **
The input is not valid. Verify that the action is typed correctly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Resource not found. Verify the connection resource ARN and try again.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_ListRepositoryLinks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/ListRepositoryLinks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/ListRepositoryLinks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/ListRepositoryLinks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/ListRepositoryLinks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/ListRepositoryLinks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/ListRepositoryLinks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/ListRepositoryLinks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/ListRepositoryLinks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/ListRepositoryLinks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/ListRepositoryLinks)
