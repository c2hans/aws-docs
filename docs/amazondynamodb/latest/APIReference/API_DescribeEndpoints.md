---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeEndpoints.html
---

# DescribeEndpoints
<a name="API_DescribeEndpoints"></a>

Returns the regional endpoint information. For more information on policy permissions, please see [Internetwork traffic privacy](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/inter-network-traffic-privacy.html#inter-network-traffic-DescribeEndpoints).

## Response Syntax
<a name="API_DescribeEndpoints_ResponseSyntax"></a>

```
{
   "Endpoints": [
      {
         "Address": "string",
         "CachePeriodInMinutes": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Endpoints](#API_DescribeEndpoints_ResponseSyntax) **   <a name="DDB-DescribeEndpoints-response-Endpoints"></a>
List of endpoints.
Type: Array of [Endpoint](API_Endpoint.md) objects

## Errors
<a name="API_DescribeEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/DescribeEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/DescribeEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DescribeEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/DescribeEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/DescribeEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/DescribeEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/DescribeEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/DescribeEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DescribeEndpoints)
