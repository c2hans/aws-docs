---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_ListGraphs.html
---

# ListGraphs
<a name="API_ListGraphs"></a>

Returns the list of behavior graphs that the calling account is an administrator account of. This operation can only be called by an administrator account.

Because an account can currently only be the administrator of one behavior graph within a Region, the results always contain a single behavior graph.

## Request Syntax
<a name="API_ListGraphs_RequestSyntax"></a>

```
POST /graphs/list HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListGraphs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListGraphs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListGraphs_RequestSyntax) **   <a name="detective-ListGraphs-request-MaxResults"></a>
The maximum number of graphs to return at a time. The total must be less than the overall limit on the number of results to return, which is currently 200.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_ListGraphs_RequestSyntax) **   <a name="detective-ListGraphs-request-NextToken"></a>
For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListGraphs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "GraphList": [
      {
         "Arn": "string",
         "CreatedTime": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListGraphs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GraphList](#API_ListGraphs_ResponseSyntax) **   <a name="detective-ListGraphs-response-GraphList"></a>
A list of behavior graphs that the account is an administrator account for.
Type: Array of [Graph](API_Graph.md) objects

 ** [NextToken](#API_ListGraphs_ResponseSyntax) **   <a name="detective-ListGraphs-response-NextToken"></a>
If there are more behavior graphs remaining in the results, then this is the pagination token to use to request the next page of behavior graphs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListGraphs_Errors"></a>

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

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## Examples
<a name="API_ListGraphs_Examples"></a>

### Example
<a name="API_ListGraphs_Example_1"></a>

This example illustrates one usage of ListGraphs.

#### Sample Request
<a name="API_ListGraphs_Example_1_Request"></a>

```
POST /graphs/list HTTP/1.1
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 0
Authorization: AUTHPARAMS
X-Amz-Date: 20200123T193018Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33
```

### Example
<a name="API_ListGraphs_Example_2"></a>

This example illustrates one usage of ListGraphs.

#### Sample Response
<a name="API_ListGraphs_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 144
Date: Thu, 23 Jan 2020 23:07:46 GMT
x-amzn-RequestId: 397d0549-0092-11e8-a0ee-a7f9aa6e7572
Connection: Keep-alive

{
 "GraphList": [
 {
  "Arn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899",
  "CreatedTime": "2020-01-22T11:35:11.372Z"
 }
 ]
}
```

## See Also
<a name="API_ListGraphs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/ListGraphs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/ListGraphs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/ListGraphs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/ListGraphs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/ListGraphs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/ListGraphs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/ListGraphs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/ListGraphs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/ListGraphs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/ListGraphs)
