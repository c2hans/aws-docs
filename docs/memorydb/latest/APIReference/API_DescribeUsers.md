---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeUsers.html
---

# DescribeUsers
<a name="API_DescribeUsers"></a>

Returns a list of users.

## Request Syntax
<a name="API_DescribeUsers_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "UserName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeUsers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeUsers_RequestSyntax) **   <a name="MemoryDB-DescribeUsers-request-Filters"></a>
Filter to determine the list of users to return.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxResults](#API_DescribeUsers_RequestSyntax) **   <a name="MemoryDB-DescribeUsers-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeUsers_RequestSyntax) **   <a name="MemoryDB-DescribeUsers-request-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

 ** [UserName](#API_DescribeUsers_RequestSyntax) **   <a name="MemoryDB-DescribeUsers-request-UserName"></a>
The name of the user.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

## Response Syntax
<a name="API_DescribeUsers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Users": [
      {
         "AccessString": "string",
         "ACLNames": [ "string" ],
         "ARN": "string",
         "Authentication": {
            "PasswordCount": number,
            "Type": "string"
         },
         "MinimumEngineVersion": "string",
         "Name": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeUsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeUsers_ResponseSyntax) **   <a name="MemoryDB-DescribeUsers-response-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

 ** [Users](#API_DescribeUsers_ResponseSyntax) **   <a name="MemoryDB-DescribeUsers-response-Users"></a>
A list of users.
Type: Array of [User](API_User.md) objects

## Errors
<a name="API_DescribeUsers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** UserNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DescribeUsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeUsers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeUsers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeUsers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeUsers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeUsers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeUsers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeUsers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeUsers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeUsers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeUsers)
