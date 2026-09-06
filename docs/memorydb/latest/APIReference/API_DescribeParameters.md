---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeParameters.html
---

# DescribeParameters
<a name="API_DescribeParameters"></a>

Returns the detailed parameter list for a particular parameter group.

## Request Syntax
<a name="API_DescribeParameters_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ParameterGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeParameters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeParameters_RequestSyntax) **   <a name="MemoryDB-DescribeParameters-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeParameters_RequestSyntax) **   <a name="MemoryDB-DescribeParameters-request-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

 ** [ParameterGroupName](#API_DescribeParameters_RequestSyntax) **   <a name="MemoryDB-DescribeParameters-request-ParameterGroupName"></a>
he name of a specific parameter group to return details for.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeParameters_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Parameters": [
      {
         "AllowedValues": "string",
         "DataType": "string",
         "Description": "string",
         "MinimumEngineVersion": "string",
         "Name": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeParameters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeParameters_ResponseSyntax) **   <a name="MemoryDB-DescribeParameters-response-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

 ** [Parameters](#API_DescribeParameters_ResponseSyntax) **   <a name="MemoryDB-DescribeParameters-response-Parameters"></a>
A list of parameters specific to a particular parameter group. Each element in the list contains detailed information about one parameter.
Type: Array of [Parameter](API_Parameter.md) objects

## Errors
<a name="API_DescribeParameters_Errors"></a>

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
<a name="API_DescribeParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeParameters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeParameters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeParameters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeParameters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeParameters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeParameters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeParameters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeParameters)
