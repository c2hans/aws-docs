---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeServiceUpdates.html
---

# DescribeServiceUpdates
<a name="API_DescribeServiceUpdates"></a>

Returns details of the service updates.

## Request Syntax
<a name="API_DescribeServiceUpdates_RequestSyntax"></a>

```
{
   "ClusterNames": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ServiceUpdateName": "{{string}}",
   "Status": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeServiceUpdates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterNames](#API_DescribeServiceUpdates_RequestSyntax) **   <a name="MemoryDB-DescribeServiceUpdates-request-ClusterNames"></a>
The list of cluster names to identify service updates to apply.
Type: Array of strings
Array Members: Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_DescribeServiceUpdates_RequestSyntax) **   <a name="MemoryDB-DescribeServiceUpdates-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeServiceUpdates_RequestSyntax) **   <a name="MemoryDB-DescribeServiceUpdates-request-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

 ** [ServiceUpdateName](#API_DescribeServiceUpdates_RequestSyntax) **   <a name="MemoryDB-DescribeServiceUpdates-request-ServiceUpdateName"></a>
The unique ID of the service update to describe.
Type: String
Required: No

 ** [Status](#API_DescribeServiceUpdates_RequestSyntax) **   <a name="MemoryDB-DescribeServiceUpdates-request-Status"></a>
The status(es) of the service updates to filter on.
Type: Array of strings
Array Members: Maximum number of 4 items.
Valid Values: `available | in-progress | complete | scheduled`
Required: No

## Response Syntax
<a name="API_DescribeServiceUpdates_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ServiceUpdates": [
      {
         "AutoUpdateStartDate": number,
         "ClusterName": "string",
         "Description": "string",
         "Engine": "string",
         "NodesUpdated": "string",
         "ReleaseDate": number,
         "ServiceUpdateName": "string",
         "Status": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeServiceUpdates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeServiceUpdates_ResponseSyntax) **   <a name="MemoryDB-DescribeServiceUpdates-response-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

 ** [ServiceUpdates](#API_DescribeServiceUpdates_ResponseSyntax) **   <a name="MemoryDB-DescribeServiceUpdates-response-ServiceUpdates"></a>
A list of service updates
Type: Array of [ServiceUpdate](API_ServiceUpdate.md) objects

## Errors
<a name="API_DescribeServiceUpdates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

## See Also
<a name="API_DescribeServiceUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeServiceUpdates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeServiceUpdates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeServiceUpdates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeServiceUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeServiceUpdates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeServiceUpdates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeServiceUpdates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeServiceUpdates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeServiceUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeServiceUpdates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
