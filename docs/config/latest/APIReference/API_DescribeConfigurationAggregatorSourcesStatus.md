---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationAggregatorSourcesStatus.html
---

# DescribeConfigurationAggregatorSourcesStatus
<a name="API_DescribeConfigurationAggregatorSourcesStatus"></a>

Returns status information for sources within an aggregator. The status includes information about the last time AWS Config verified authorization between the source account and an aggregator account. In case of a failure, the status contains the related error code or message.

## Request Syntax
<a name="API_DescribeConfigurationAggregatorSourcesStatus_RequestSyntax"></a>

```
{
   "ConfigurationAggregatorName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "UpdateStatus": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeConfigurationAggregatorSourcesStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationAggregatorName](#API_DescribeConfigurationAggregatorSourcesStatus_RequestSyntax) **   <a name="config-DescribeConfigurationAggregatorSourcesStatus-request-ConfigurationAggregatorName"></a>
The name of the configuration aggregator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: Yes

 ** [Limit](#API_DescribeConfigurationAggregatorSourcesStatus_RequestSyntax) **   <a name="config-DescribeConfigurationAggregatorSourcesStatus-request-Limit"></a>
The maximum number of AggregatorSourceStatus returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeConfigurationAggregatorSourcesStatus_RequestSyntax) **   <a name="config-DescribeConfigurationAggregatorSourcesStatus-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

 ** [UpdateStatus](#API_DescribeConfigurationAggregatorSourcesStatus_RequestSyntax) **   <a name="config-DescribeConfigurationAggregatorSourcesStatus-request-UpdateStatus"></a>
Filters the status type.
+ Valid value FAILED indicates errors while moving data.
+ Valid value SUCCEEDED indicates the data was successfully moved.
+ Valid value OUTDATED indicates the data is not the most recent.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `FAILED | SUCCEEDED | OUTDATED`
Required: No

## Response Syntax
<a name="API_DescribeConfigurationAggregatorSourcesStatus_ResponseSyntax"></a>

```
{
   "AggregatedSourceStatusList": [
      {
         "AwsRegion": "string",
         "LastErrorCode": "string",
         "LastErrorMessage": "string",
         "LastUpdateStatus": "string",
         "LastUpdateTime": number,
         "SourceId": "string",
         "SourceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConfigurationAggregatorSourcesStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AggregatedSourceStatusList](#API_DescribeConfigurationAggregatorSourcesStatus_ResponseSyntax) **   <a name="config-DescribeConfigurationAggregatorSourcesStatus-response-AggregatedSourceStatusList"></a>
Returns an AggregatedSourceStatus object.
Type: Array of [AggregatedSourceStatus](API_AggregatedSourceStatus.md) objects

 ** [NextToken](#API_DescribeConfigurationAggregatorSourcesStatus_ResponseSyntax) **   <a name="config-DescribeConfigurationAggregatorSourcesStatus-response-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_DescribeConfigurationAggregatorSourcesStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** NoSuchConfigurationAggregatorException **
You have specified a configuration aggregator that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConfigurationAggregatorSourcesStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeConfigurationAggregatorSourcesStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
