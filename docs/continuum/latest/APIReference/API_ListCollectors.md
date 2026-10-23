---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_ListCollectors.html
---

# ListCollectors
<a name="API_ListCollectors"></a>

Lists the Collectors owned by the authenticated caller's account, including a Collector whose deletion is in progress. A Collector that is still being created is omitted. The account-scoped Collector quota currently permits at most one result, so no result ordering applies.

## Request Syntax
<a name="API_ListCollectors_RequestSyntax"></a>

```
GET /collectors HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCollectors_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCollectors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCollectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "collectorArn": "string",
         "collectorId": "string",
         "createdAt": "string",
         "status": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListCollectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListCollectors_ResponseSyntax) **   <a name="continuum-ListCollectors-response-items"></a>
The items.
Type: Array of [CollectorSummary](API_CollectorSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

## Errors
<a name="API_ListCollectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_ListCollectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/ListCollectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/ListCollectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/ListCollectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/ListCollectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/ListCollectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/ListCollectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/ListCollectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/ListCollectors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/ListCollectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/ListCollectors)
