---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeParameterGroups.html
---

# DescribeParameterGroups
<a name="API_DescribeParameterGroups"></a>

Returns a list of parameter group descriptions. If a parameter group name is specified, the list contains only the descriptions for that group.

## Request Syntax
<a name="API_DescribeParameterGroups_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ParameterGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeParameterGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeParameterGroups_RequestSyntax) **   <a name="MemoryDB-DescribeParameterGroups-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeParameterGroups_RequestSyntax) **   <a name="MemoryDB-DescribeParameterGroups-request-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

 ** [ParameterGroupName](#API_DescribeParameterGroups_RequestSyntax) **   <a name="MemoryDB-DescribeParameterGroups-request-ParameterGroupName"></a>
The name of a specific parameter group to return details for.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeParameterGroups_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ParameterGroups": [
      {
         "ARN": "string",
         "Description": "string",
         "Family": "string",
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeParameterGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeParameterGroups_ResponseSyntax) **   <a name="MemoryDB-DescribeParameterGroups-response-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

 ** [ParameterGroups](#API_DescribeParameterGroups_ResponseSyntax) **   <a name="MemoryDB-DescribeParameterGroups-response-ParameterGroups"></a>
A list of parameter groups. Each element in the list contains detailed information about one parameter group.
Type: Array of [ParameterGroup](API_ParameterGroup.md) objects

## Errors
<a name="API_DescribeParameterGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ParameterGroupNotFoundFault **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DescribeParameterGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeParameterGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeParameterGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeParameterGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeParameterGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeParameterGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeParameterGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeParameterGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeParameterGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeParameterGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeParameterGroups)
