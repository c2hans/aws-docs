---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeSubnetGroups.html
---

# DescribeSubnetGroups
<a name="API_DescribeSubnetGroups"></a>

Returns a list of subnet group descriptions. If a subnet group name is specified, the list contains only the description of that group.

## Request Syntax
<a name="API_DescribeSubnetGroups_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SubnetGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSubnetGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeSubnetGroups_RequestSyntax) **   <a name="MemoryDB-DescribeSubnetGroups-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeSubnetGroups_RequestSyntax) **   <a name="MemoryDB-DescribeSubnetGroups-request-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

 ** [SubnetGroupName](#API_DescribeSubnetGroups_RequestSyntax) **   <a name="MemoryDB-DescribeSubnetGroups-request-SubnetGroupName"></a>
The name of the subnet group to return details for.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeSubnetGroups_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SubnetGroups": [
      {
         "ARN": "string",
         "Description": "string",
         "Name": "string",
         "Subnets": [
            {
               "AvailabilityZone": {
                  "Name": "string"
               },
               "Identifier": "string",
               "SupportedNetworkTypes": [ "string" ]
            }
         ],
         "SupportedNetworkTypes": [ "string" ],
         "VpcId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSubnetGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeSubnetGroups_ResponseSyntax) **   <a name="MemoryDB-DescribeSubnetGroups-response-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

 ** [SubnetGroups](#API_DescribeSubnetGroups_ResponseSyntax) **   <a name="MemoryDB-DescribeSubnetGroups-response-SubnetGroups"></a>
A list of subnet groups. Each element in the list contains detailed information about one group.
Type: Array of [SubnetGroup](API_SubnetGroup.md) objects

## Errors
<a name="API_DescribeSubnetGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** SubnetGroupNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DescribeSubnetGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeSubnetGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeSubnetGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeSubnetGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeSubnetGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeSubnetGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeSubnetGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeSubnetGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeSubnetGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeSubnetGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeSubnetGroups)
