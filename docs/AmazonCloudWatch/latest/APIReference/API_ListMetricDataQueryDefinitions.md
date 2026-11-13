---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetricDataQueryDefinitions.html
---

# ListMetricDataQueryDefinitions
<a name="API_ListMetricDataQueryDefinitions"></a>

Lists the metric data query definitions in your account and Region.

The results are summaries that don't include the expression. To get the full definition, call `GetMetricDataQueryDefinition` with its ID.

This operation supports pagination. Use the `MaxResults` and `NextToken` parameters to retrieve results in multiple calls.

 **Permissions**

To list definitions, you need the `cloudwatch:ListMetricDataQueryDefinitions` permission. This permission applies to all definitions in the account and Region. The results aren't filtered by tags.

## Request Syntax
<a name="API_ListMetricDataQueryDefinitions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMetricDataQueryDefinitions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListMetricDataQueryDefinitions_RequestSyntax) **   <a name="ACW-ListMetricDataQueryDefinitions-request-MaxResults"></a>
The maximum number of metric data query definitions to return in one call. The default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListMetricDataQueryDefinitions_RequestSyntax) **   <a name="ACW-ListMetricDataQueryDefinitions-request-NextToken"></a>
The token returned by a previous call to indicate where to continue retrieving results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_-]+`
Required: No

## Response Syntax
<a name="API_ListMetricDataQueryDefinitions_ResponseSyntax"></a>

```
{
   "Items": [
      {
         "Id": "string",
         "Path": "string",
         "Type": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMetricDataQueryDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListMetricDataQueryDefinitions_ResponseSyntax) **   <a name="ACW-ListMetricDataQueryDefinitions-response-Items"></a>
A list of metric data query definition summaries.
Type: Array of [MetricDataQueryDefinitionSummary](API_MetricDataQueryDefinitionSummary.md) objects

 ** [NextToken](#API_ListMetricDataQueryDefinitions_ResponseSyntax) **   <a name="ACW-ListMetricDataQueryDefinitions-response-NextToken"></a>
The token to use when requesting the next set of results. If this field is absent, there are no more results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_-]+`

## Errors
<a name="API_ListMetricDataQueryDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ListMetricDataQueryDefinitions_Examples"></a>

### Example – List metric data query definitions
<a name="API_ListMetricDataQueryDefinitions_Example_1"></a>

The following AWS CLI command lists the metric data query definitions in your account and Region. The JSON response follows the command.

#### Sample Request
<a name="API_ListMetricDataQueryDefinitions_Example_1_Request"></a>

```
PROMPT> aws cloudwatch list-metric-data-query-definitions
```

#### Sample Response
<a name="API_ListMetricDataQueryDefinitions_Example_1_Response"></a>

```
{
    "Items": [
        {
            "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "Path": "ec2/top-cpu-instances",
            "Type": "SQL",
            "UpdatedAt": "2026-11-09T10:30:00Z"
        },
        {
            "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "Path": "ec2/cpu-all-instances",
            "Type": "METRIC_MATH",
            "UpdatedAt": "2026-11-08T16:45:00Z"
        }
    ]
}
```

## See Also
<a name="API_ListMetricDataQueryDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/ListMetricDataQueryDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListMetricDataQueryDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListMetricDataQueryDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/ListMetricDataQueryDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListMetricDataQueryDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/ListMetricDataQueryDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/ListMetricDataQueryDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/ListMetricDataQueryDefinitions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListMetricDataQueryDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListMetricDataQueryDefinitions)
