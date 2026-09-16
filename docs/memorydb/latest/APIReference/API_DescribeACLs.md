---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeACLs.html
---

# DescribeACLs
<a name="API_DescribeACLs"></a>

Returns a list of ACLs.

## Request Syntax
<a name="API_DescribeACLs_RequestSyntax"></a>

```
{
   "ACLName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeACLs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ACLName](#API_DescribeACLs_RequestSyntax) **   <a name="MemoryDB-DescribeACLs-request-ACLName"></a>
The name of the ACL.
Type: String
Required: No

 ** [MaxResults](#API_DescribeACLs_RequestSyntax) **   <a name="MemoryDB-DescribeACLs-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeACLs_RequestSyntax) **   <a name="MemoryDB-DescribeACLs-request-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeACLs_ResponseSyntax"></a>

```
{
   "ACLs": [
      {
         "ARN": "string",
         "Clusters": [ "string" ],
         "MinimumEngineVersion": "string",
         "Name": "string",
         "PendingChanges": {
            "UserNamesToAdd": [ "string" ],
            "UserNamesToRemove": [ "string" ]
         },
         "Status": "string",
         "UserNames": [ "string" ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeACLs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ACLs](#API_DescribeACLs_ResponseSyntax) **   <a name="MemoryDB-DescribeACLs-response-ACLs"></a>
The list of ACLs.
Type: Array of [ACL](API_ACL.md) objects

 ** [NextToken](#API_DescribeACLs_ResponseSyntax) **   <a name="MemoryDB-DescribeACLs-response-NextToken"></a>
If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

## Errors
<a name="API_DescribeACLs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ACLNotFoundFault **

HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

## See Also
<a name="API_DescribeACLs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeACLs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeACLs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeACLs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeACLs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeACLs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeACLs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeACLs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeACLs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeACLs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeACLs)
