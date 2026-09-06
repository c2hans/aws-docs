---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationAggregators.html
---

# DescribeConfigurationAggregators
<a name="API_DescribeConfigurationAggregators"></a>

Returns the details of one or more configuration aggregators. If the configuration aggregator is not specified, this operation returns the details for all the configuration aggregators associated with the account.

## Request Syntax
<a name="API_DescribeConfigurationAggregators_RequestSyntax"></a>

```
{
   "ConfigurationAggregatorNames": [ "{{string}}" ],
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConfigurationAggregators_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationAggregatorNames](#API_DescribeConfigurationAggregators_RequestSyntax) **   <a name="config-DescribeConfigurationAggregators-request-ConfigurationAggregatorNames"></a>
The name of the configuration aggregators.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: No

 ** [Limit](#API_DescribeConfigurationAggregators_RequestSyntax) **   <a name="config-DescribeConfigurationAggregators-request-Limit"></a>
The maximum number of configuration aggregators returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeConfigurationAggregators_RequestSyntax) **   <a name="config-DescribeConfigurationAggregators-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeConfigurationAggregators_ResponseSyntax"></a>

```
{
   "ConfigurationAggregators": [
      {
         "AccountAggregationSources": [
            {
               "AccountIds": [ "string" ],
               "AllAwsRegions": boolean,
               "AwsRegions": [ "string" ]
            }
         ],
         "AggregatorFilters": {
            "ResourceType": {
               "Type": "string",
               "Value": [ "string" ]
            },
            "ServicePrincipal": {
               "Type": "string",
               "Value": [ "string" ]
            }
         },
         "ConfigurationAggregatorArn": "string",
         "ConfigurationAggregatorName": "string",
         "CreatedBy": "string",
         "CreationTime": number,
         "LastUpdatedTime": number,
         "OrganizationAggregationSource": {
            "AllAwsRegions": boolean,
            "AwsRegions": [ "string" ],
            "RoleArn": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConfigurationAggregators_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationAggregators](#API_DescribeConfigurationAggregators_ResponseSyntax) **   <a name="config-DescribeConfigurationAggregators-response-ConfigurationAggregators"></a>
Returns a ConfigurationAggregators object.
Type: Array of [ConfigurationAggregator](API_ConfigurationAggregator.md) objects

 ** [NextToken](#API_DescribeConfigurationAggregators_ResponseSyntax) **   <a name="config-DescribeConfigurationAggregators-response-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_DescribeConfigurationAggregators_Errors"></a>

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
<a name="API_DescribeConfigurationAggregators_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeConfigurationAggregators)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeConfigurationAggregators)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeConfigurationAggregators)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeConfigurationAggregators)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeConfigurationAggregators)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeConfigurationAggregators)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeConfigurationAggregators)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeConfigurationAggregators)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeConfigurationAggregators)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeConfigurationAggregators)
