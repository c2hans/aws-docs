---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamGroups.html
---

# ListStreamGroups
<a name="API_ListStreamGroups"></a>

Retrieves a list of all Amazon GameLift Streams stream groups that are associated with the AWS account in use. This operation returns stream groups in all statuses, in no particular order. You can paginate the results as needed.

## Request Syntax
<a name="API_ListStreamGroups_RequestSyntax"></a>

```
GET /streamgroups?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListStreamGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListStreamGroups_RequestSyntax) **   <a name="gameliftstreams-ListStreamGroups-request-uri-MaxResults"></a>
The number of results to return. Use this parameter with `NextToken` to return results in sequential pages. Default value is `25`.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListStreamGroups_RequestSyntax) **   <a name="gameliftstreams-ListStreamGroups-request-uri-NextToken"></a>
A token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set.

## Request Body
<a name="API_ListStreamGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListStreamGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Arn": "string",
         "CreatedAt": number,
         "DefaultApplication": {
            "Arn": "string",
            "Id": "string"
         },
         "Description": "string",
         "ExpiresAt": number,
         "Id": "string",
         "LastUpdatedAt": number,
         "Status": "string",
         "StreamClass": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListStreamGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListStreamGroups_ResponseSyntax) **   <a name="gameliftstreams-ListStreamGroups-response-Items"></a>
A collection of Amazon GameLift Streams stream groups that are associated with the AWS account in use. Each item includes stream group metadata and status, but doesn't include capacity information.
Type: Array of [StreamGroupSummary](API_StreamGroupSummary.md) objects

 ** [NextToken](#API_ListStreamGroups_ResponseSyntax) **   <a name="gameliftstreams-ListStreamGroups-response-NextToken"></a>
A token that marks the start of the next sequential page of results. If an operation doesn't return a token, you've reached the end of the list.
Type: String

## Errors
<a name="API_ListStreamGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error and is unable to complete the request.
 ** Message **
Description of the error.
HTTP Status Code: 500

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling. Retry the request after the suggested wait time.
 ** Message **
Description of the error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.
 ** Message **
Description of the error.
HTTP Status Code: 400

## Examples
<a name="API_ListStreamGroups_Examples"></a>

### CLI Example
<a name="API_ListStreamGroups_Example_1"></a>

The following example shows how to use the AWS CLI to retrieve a complete list of stream groups. Because the request doesn't include a `MaxResults` or a `NextToken`, the request returns the first 25 results in the list.

#### Sample Request
<a name="API_ListStreamGroups_Example_1_Request"></a>

```
aws gameliftstreams list-stream-groups
```

## See Also
<a name="API_ListStreamGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/ListStreamGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/ListStreamGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/ListStreamGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/ListStreamGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/ListStreamGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/ListStreamGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/ListStreamGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/ListStreamGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/ListStreamGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/ListStreamGroups)
