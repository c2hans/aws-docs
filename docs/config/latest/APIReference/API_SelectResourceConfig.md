---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_SelectResourceConfig.html
---

# SelectResourceConfig
<a name="API_SelectResourceConfig"></a>

Accepts a structured query language (SQL) `SELECT` command, performs the corresponding search, and returns resource configurations matching the properties.

For more information about query components, see the [https://docs.aws.amazon.com/config/latest/developerguide/query-components.html](https://docs.aws.amazon.com/config/latest/developerguide/query-components.html) section in the * AWS Config Developer Guide*.

## Request Syntax
<a name="API_SelectResourceConfig_RequestSyntax"></a>

```
{
   "Expression": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_SelectResourceConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Expression](#API_SelectResourceConfig_RequestSyntax) **   <a name="config-SelectResourceConfig-request-Expression"></a>
The SQL query `SELECT` command.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** [Limit](#API_SelectResourceConfig_RequestSyntax) **   <a name="config-SelectResourceConfig-request-Limit"></a>
The maximum number of query results returned on each page.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_SelectResourceConfig_RequestSyntax) **   <a name="config-SelectResourceConfig-request-NextToken"></a>
The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_SelectResourceConfig_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "QueryInfo": {
      "SelectFields": [
         {
            "Name": "string"
         }
      ]
   },
   "Results": [ "string" ]
}
```

## Response Elements
<a name="API_SelectResourceConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SelectResourceConfig_ResponseSyntax) **   <a name="config-SelectResourceConfig-response-NextToken"></a>
The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String

 ** [QueryInfo](#API_SelectResourceConfig_ResponseSyntax) **   <a name="config-SelectResourceConfig-response-QueryInfo"></a>
Returns the `QueryInfo` object.
Type: [QueryInfo](API_QueryInfo.md) object

 ** [Results](#API_SelectResourceConfig_ResponseSyntax) **   <a name="config-SelectResourceConfig-response-Results"></a>
Returns the results for the SQL query.
Type: Array of strings

## Errors
<a name="API_SelectResourceConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidExpressionException **
The syntax of the query is incorrect.
HTTP Status Code: 400

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

## See Also
<a name="API_SelectResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/SelectResourceConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/SelectResourceConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/SelectResourceConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/SelectResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/SelectResourceConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/SelectResourceConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/SelectResourceConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/SelectResourceConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/SelectResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/SelectResourceConfig)
