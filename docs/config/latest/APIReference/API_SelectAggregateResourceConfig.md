---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_SelectAggregateResourceConfig.html
---

# SelectAggregateResourceConfig
<a name="API_SelectAggregateResourceConfig"></a>

Accepts a structured query language (SQL) SELECT command and an aggregator to query configuration state of AWS resources across multiple accounts and regions, performs the corresponding search, and returns resource configurations matching the properties.

For more information about query components, see the [**Query Components**](https://docs.aws.amazon.com/config/latest/developerguide/query-components.html) section in the * AWS Config Developer Guide*.

**Note**
If you run an aggregation query (i.e., using `GROUP BY` or using aggregate functions such as `COUNT`; e.g., `SELECT resourceId, COUNT(*) WHERE resourceType = 'AWS::IAM::Role' GROUP BY resourceId`) and do not specify the `MaxResults` or the `Limit` query parameters, the default page size is set to 500.
If you run a non-aggregation query (i.e., not using `GROUP BY` or aggregate function; e.g., `SELECT * WHERE resourceType = 'AWS::IAM::Role'`) and do not specify the `MaxResults` or the `Limit` query parameters, the default page size is set to 25.

## Request Syntax
<a name="API_SelectAggregateResourceConfig_RequestSyntax"></a>

```
{
   "ConfigurationAggregatorName": "{{string}}",
   "Expression": "{{string}}",
   "Limit": {{number}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_SelectAggregateResourceConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationAggregatorName](#API_SelectAggregateResourceConfig_RequestSyntax) **   <a name="config-SelectAggregateResourceConfig-request-ConfigurationAggregatorName"></a>
The name of the configuration aggregator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: Yes

 ** [Expression](#API_SelectAggregateResourceConfig_RequestSyntax) **   <a name="config-SelectAggregateResourceConfig-request-Expression"></a>
The SQL query SELECT command.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** [Limit](#API_SelectAggregateResourceConfig_RequestSyntax) **   <a name="config-SelectAggregateResourceConfig-request-Limit"></a>
The maximum number of query results returned on each page.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [MaxResults](#API_SelectAggregateResourceConfig_RequestSyntax) **   <a name="config-SelectAggregateResourceConfig-request-MaxResults"></a>
The maximum number of query results returned on each page. AWS Config also allows the Limit request parameter.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_SelectAggregateResourceConfig_RequestSyntax) **   <a name="config-SelectAggregateResourceConfig-request-NextToken"></a>
The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_SelectAggregateResourceConfig_ResponseSyntax"></a>

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
<a name="API_SelectAggregateResourceConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SelectAggregateResourceConfig_ResponseSyntax) **   <a name="config-SelectAggregateResourceConfig-response-NextToken"></a>
The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String

 ** [QueryInfo](#API_SelectAggregateResourceConfig_ResponseSyntax) **   <a name="config-SelectAggregateResourceConfig-response-QueryInfo"></a>
Details about the query.
Type: [QueryInfo](API_QueryInfo.md) object

 ** [Results](#API_SelectAggregateResourceConfig_ResponseSyntax) **   <a name="config-SelectAggregateResourceConfig-response-Results"></a>
Returns the results for the SQL query.
Type: Array of strings

## Errors
<a name="API_SelectAggregateResourceConfig_Errors"></a>

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

 ** NoSuchConfigurationAggregatorException **
You have specified a configuration aggregator that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_SelectAggregateResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/SelectAggregateResourceConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/SelectAggregateResourceConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/SelectAggregateResourceConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/SelectAggregateResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/SelectAggregateResourceConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/SelectAggregateResourceConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/SelectAggregateResourceConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/SelectAggregateResourceConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/SelectAggregateResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/SelectAggregateResourceConfig)
