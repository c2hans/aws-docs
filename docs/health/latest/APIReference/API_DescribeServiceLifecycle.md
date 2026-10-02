---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeServiceLifecycle.html
---

# DescribeServiceLifecycle
<a name="API_DescribeServiceLifecycle"></a>

Returns lifecycle information for AWS services, including end-of-life dates, version recommendations, and lifecycle events.

## Request Syntax
<a name="API_DescribeServiceLifecycle_RequestSyntax"></a>

```
{
   "filter": {
      "service": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeServiceLifecycle_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_DescribeServiceLifecycle_RequestSyntax) **   <a name="AWSHealth-DescribeServiceLifecycle-request-filter"></a>
Values to narrow the results returned.
Type: [ServiceLifecycleFilter](API_ServiceLifecycleFilter.md) object
Required: No

 ** [maxResults](#API_DescribeServiceLifecycle_RequestSyntax) **   <a name="AWSHealth-DescribeServiceLifecycle-request-maxResults"></a>
The maximum number of items to return in one batch, between 1 and 20, inclusive.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [nextToken](#API_DescribeServiceLifecycle_RequestSyntax) **   <a name="AWSHealth-DescribeServiceLifecycle-request-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`
Required: No

## Response Syntax
<a name="API_DescribeServiceLifecycle_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "serviceLifecycles": [
      {
         "lifecycleEvents": [
            {
               "date": number,
               "description": "string",
               "impactRisks": [ "string" ],
               "lifecycleEventType": "string",
               "regions": [ "string" ]
            }
         ],
         "recommendedVersion": "string",
         "service": "string",
         "title": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeServiceLifecycle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeServiceLifecycle_ResponseSyntax) **   <a name="AWSHealth-DescribeServiceLifecycle-response-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`

 ** [serviceLifecycles](#API_DescribeServiceLifecycle_ResponseSyntax) **   <a name="AWSHealth-DescribeServiceLifecycle-response-serviceLifecycles"></a>
The list of service lifecycle entries matching the filter criteria.
Type: Array of [ServiceLifecycle](API_ServiceLifecycle.md) objects

## Errors
<a name="API_DescribeServiceLifecycle_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPaginationToken **
The specified pagination token (`nextToken`) is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeServiceLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeServiceLifecycle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeServiceLifecycle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeServiceLifecycle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeServiceLifecycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeServiceLifecycle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeServiceLifecycle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeServiceLifecycle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeServiceLifecycle)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeServiceLifecycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeServiceLifecycle)
