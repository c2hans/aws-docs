---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetIndexingRules.html
---

# GetIndexingRules
<a name="API_GetIndexingRules"></a>

 Retrieves all indexing rules.

Indexing rules are used to determine the server-side sampling rate for spans ingested through the CloudWatchLogs destination and indexed by X-Ray. For more information, see [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html).

## Request Syntax
<a name="API_GetIndexingRules_RequestSyntax"></a>

```
POST /GetIndexingRules HTTP/1.1
Content-type: application/json

{
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetIndexingRules_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetIndexingRules_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [NextToken](#API_GetIndexingRules_RequestSyntax) **   <a name="xray-GetIndexingRules-request-NextToken"></a>
 Specify the pagination token returned by a previous request to retrieve the next page of indexes.
Type: String
Required: No

## Response Syntax
<a name="API_GetIndexingRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IndexingRules": [
      {
         "ModifiedAt": number,
         "Name": "string",
         "Rule": { ... }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetIndexingRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IndexingRules](#API_GetIndexingRules_ResponseSyntax) **   <a name="xray-GetIndexingRules-response-IndexingRules"></a>
 Retrieves all indexing rules.
Type: Array of [IndexingRule](API_IndexingRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [NextToken](#API_GetIndexingRules_ResponseSyntax) **   <a name="xray-GetIndexingRules-response-NextToken"></a>
 Specify the pagination token returned by a previous request to retrieve the next page of indexes.
Type: String

## Errors
<a name="API_GetIndexingRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetIndexingRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetIndexingRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetIndexingRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetIndexingRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetIndexingRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetIndexingRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetIndexingRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetIndexingRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetIndexingRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetIndexingRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetIndexingRules)
