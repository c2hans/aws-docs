---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTimeToLive.html
---

# DescribeTimeToLive
<a name="API_DescribeTimeToLive"></a>

Gives a description of the Time to Live (TTL) status on the specified table.

## Request Syntax
<a name="API_DescribeTimeToLive_RequestSyntax"></a>

```
{
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTimeToLive_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TableName](#API_DescribeTimeToLive_RequestSyntax) **   <a name="DDB-DescribeTimeToLive-request-TableName"></a>
The name of the table to be described. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_DescribeTimeToLive_ResponseSyntax"></a>

```
{
   "TimeToLiveDescription": {
      "AttributeName": "string",
      "TimeToLiveStatus": "string"
   }
}
```

## Response Elements
<a name="API_DescribeTimeToLive_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TimeToLiveDescription](#API_DescribeTimeToLive_ResponseSyntax) **   <a name="DDB-DescribeTimeToLive-response-TimeToLiveDescription"></a>

Type: [TimeToLiveDescription](API_TimeToLiveDescription.md) object

## Errors
<a name="API_DescribeTimeToLive_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTimeToLive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/DescribeTimeToLive)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/DescribeTimeToLive)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DescribeTimeToLive)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/DescribeTimeToLive)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeTimeToLive)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/DescribeTimeToLive)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/DescribeTimeToLive)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/DescribeTimeToLive)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/DescribeTimeToLive)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DescribeTimeToLive)
