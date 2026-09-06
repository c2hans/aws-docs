---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeEngineVersions.html
---

# DescribeEngineVersions
<a name="API_DescribeEngineVersions"></a>

Returns a list of the available Redis OSS engine versions.

## Request Syntax
<a name="API_DescribeEngineVersions_RequestSyntax"></a>

```
{
   "DefaultOnly": {{boolean}},
   "Engine": "{{string}}",
   "EngineVersion": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ParameterGroupFamily": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEngineVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DefaultOnly](#API_DescribeEngineVersions_RequestSyntax) **   <a name="MemoryDB-DescribeEngineVersions-request-DefaultOnly"></a>
If true, specifies that only the default version of the specified engine or engine and major version combination is to be returned.
Type: Boolean
Required: No

 ** [Engine](#API_DescribeEngineVersions_RequestSyntax) **   <a name="MemoryDB-DescribeEngineVersions-request-Engine"></a>
The name of the engine for which to list available versions.
Type: String
Required: No

 ** [EngineVersion](#API_DescribeEngineVersions_RequestSyntax) **   <a name="MemoryDB-DescribeEngineVersions-request-EngineVersion"></a>
The Redis OSS engine version
Type: String
Required: No

 ** [MaxResults](#API_DescribeEngineVersions_RequestSyntax) **   <a name="MemoryDB-DescribeEngineVersions-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeEngineVersions_RequestSyntax) **   <a name="MemoryDB-DescribeEngineVersions-request-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

 ** [ParameterGroupFamily](#API_DescribeEngineVersions_RequestSyntax) **   <a name="MemoryDB-DescribeEngineVersions-request-ParameterGroupFamily"></a>
The name of a specific parameter group family to return details for.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeEngineVersions_ResponseSyntax"></a>

```
{
   "EngineVersions": [
      {
         "Engine": "string",
         "EnginePatchVersion": "string",
         "EngineVersion": "string",
         "ParameterGroupFamily": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeEngineVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EngineVersions](#API_DescribeEngineVersions_ResponseSyntax) **   <a name="MemoryDB-DescribeEngineVersions-response-EngineVersions"></a>
A list of engine version details. Each element in the list contains detailed information about one engine version.
Type: Array of [EngineVersionInfo](API_EngineVersionInfo.md) objects

 ** [NextToken](#API_DescribeEngineVersions_ResponseSyntax) **   <a name="MemoryDB-DescribeEngineVersions-response-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

## Errors
<a name="API_DescribeEngineVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DescribeEngineVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeEngineVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeEngineVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeEngineVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeEngineVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeEngineVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeEngineVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeEngineVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeEngineVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeEngineVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeEngineVersions)
