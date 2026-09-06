---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeVcenterClients.html
---

# DescribeVcenterClients
<a name="API_DescribeVcenterClients"></a>

Returns a list of the installed vCenter clients.

## Request Syntax
<a name="API_DescribeVcenterClients_RequestSyntax"></a>

```
GET /DescribeVcenterClients?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeVcenterClients_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_DescribeVcenterClients_RequestSyntax) **   <a name="mgn-DescribeVcenterClients-request-uri-maxResults"></a>
Maximum results to be returned in DescribeVcenterClients.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_DescribeVcenterClients_RequestSyntax) **   <a name="mgn-DescribeVcenterClients-request-uri-nextToken"></a>
Next pagination token to be provided for DescribeVcenterClients.
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Request Body
<a name="API_DescribeVcenterClients_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeVcenterClients_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "datacenterName": "string",
         "hostname": "string",
         "lastSeenDatetime": "string",
         "sourceServerTags": {
            "string" : "string"
         },
         "tags": {
            "string" : "string"
         },
         "vcenterClientID": "string",
         "vcenterUUID": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeVcenterClients_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeVcenterClients_ResponseSyntax) **   <a name="mgn-DescribeVcenterClients-response-items"></a>
List of items returned by DescribeVcenterClients.
Type: Array of [VcenterClient](API_VcenterClient.md) objects

 ** [nextToken](#API_DescribeVcenterClients_ResponseSyntax) **   <a name="mgn-DescribeVcenterClients-response-nextToken"></a>
Next pagination token returned from DescribeVcenterClients.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeVcenterClients_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DescribeVcenterClients_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/DescribeVcenterClients)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/DescribeVcenterClients)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DescribeVcenterClients)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/DescribeVcenterClients)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DescribeVcenterClients)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/DescribeVcenterClients)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/DescribeVcenterClients)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/DescribeVcenterClients)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/DescribeVcenterClients)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DescribeVcenterClients)
