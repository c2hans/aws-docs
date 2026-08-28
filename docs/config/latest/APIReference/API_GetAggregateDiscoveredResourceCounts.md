---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateDiscoveredResourceCounts.html
---

# GetAggregateDiscoveredResourceCounts
<a name="API_GetAggregateDiscoveredResourceCounts"></a>

Returns the resource counts across accounts and regions that are present in your AWS Config aggregator. You can request the resource counts by providing filters and GroupByKey.

For example, if the input contains accountID 12345678910 and region us-east-1 in filters, the API returns the count of resources in account ID 12345678910 and region us-east-1. If the input contains ACCOUNT\_ID as a GroupByKey, the API returns resource counts for all source accounts that are present in your aggregator.

## Request Syntax
<a name="API_GetAggregateDiscoveredResourceCounts_RequestSyntax"></a>

```
{
   "ConfigurationAggregatorName": "{{string}}",
   "Filters": {
      "AccountId": "{{string}}",
      "Region": "{{string}}",
      "ResourceType": "{{string}}"
   },
   "GroupByKey": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAggregateDiscoveredResourceCounts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationAggregatorName](#API_GetAggregateDiscoveredResourceCounts_RequestSyntax) **   <a name="config-GetAggregateDiscoveredResourceCounts-request-ConfigurationAggregatorName"></a>
The name of the configuration aggregator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: Yes

 ** [Filters](#API_GetAggregateDiscoveredResourceCounts_RequestSyntax) **   <a name="config-GetAggregateDiscoveredResourceCounts-request-Filters"></a>
Filters the results based on the `ResourceCountFilters` object.
Type: [ResourceCountFilters](API_ResourceCountFilters.md) object
Required: No

 ** [GroupByKey](#API_GetAggregateDiscoveredResourceCounts_RequestSyntax) **   <a name="config-GetAggregateDiscoveredResourceCounts-request-GroupByKey"></a>
The key to group the resource counts.
Type: String
Valid Values: `RESOURCE_TYPE | ACCOUNT_ID | AWS_REGION`
Required: No

 ** [Limit](#API_GetAggregateDiscoveredResourceCounts_RequestSyntax) **   <a name="config-GetAggregateDiscoveredResourceCounts-request-Limit"></a>
The maximum number of [GroupedResourceCount](API_GroupedResourceCount.md) objects returned on each page. The default is 1000. You cannot specify a number greater than 1000. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetAggregateDiscoveredResourceCounts_RequestSyntax) **   <a name="config-GetAggregateDiscoveredResourceCounts-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_GetAggregateDiscoveredResourceCounts_ResponseSyntax"></a>

```
{
   "GroupByKey": "string",
   "GroupedResourceCounts": [
      {
         "GroupName": "string",
         "ResourceCount": number
      }
   ],
   "NextToken": "string",
   "TotalDiscoveredResources": number
}
```

## Response Elements
<a name="API_GetAggregateDiscoveredResourceCounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GroupByKey](#API_GetAggregateDiscoveredResourceCounts_ResponseSyntax) **   <a name="config-GetAggregateDiscoveredResourceCounts-response-GroupByKey"></a>
The key passed into the request object. If `GroupByKey` is not provided, the result will be empty.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [GroupedResourceCounts](#API_GetAggregateDiscoveredResourceCounts_ResponseSyntax) **   <a name="config-GetAggregateDiscoveredResourceCounts-response-GroupedResourceCounts"></a>
Returns a list of GroupedResourceCount objects.
Type: Array of [GroupedResourceCount](API_GroupedResourceCount.md) objects

 ** [NextToken](#API_GetAggregateDiscoveredResourceCounts_ResponseSyntax) **   <a name="config-GetAggregateDiscoveredResourceCounts-response-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

 ** [TotalDiscoveredResources](#API_GetAggregateDiscoveredResourceCounts_ResponseSyntax) **   <a name="config-GetAggregateDiscoveredResourceCounts-response-TotalDiscoveredResources"></a>
The total number of resources that are present in an aggregator with the filters that you provide.
Type: Long

## Errors
<a name="API_GetAggregateDiscoveredResourceCounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** NoSuchConfigurationAggregatorException **
You have specified a configuration aggregator that does not exist.
HTTP Status Code: 400

 ** ValidationException **
The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.
For [PutStoredQuery](https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html), one of the following errors:
+ There are missing required fields.
+ The input value fails the validation.
+ You are trying to create more than 300 queries.
For [DescribeConfigurationRecorders](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html) and [DescribeConfigurationRecorderStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html), one of the following errors:
+ You have specified more than one configuration recorder.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
For [AssociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html) and [DisassociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html), one of the following errors:
+ Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.
+ One or more of the specified resource types are already associated or disassociated with the configuration recorder.
+ For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.
For [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html), one of the following errors:
+ You have provided both `Arn` and `ServicePrincipal`. Only one of `Arn` or `ServicePrincipal` can be specified.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetAggregateDiscoveredResourceCounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetAggregateDiscoveredResourceCounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetAggregateDiscoveredResourceCounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetAggregateDiscoveredResourceCounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetAggregateDiscoveredResourceCounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetAggregateDiscoveredResourceCounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetAggregateDiscoveredResourceCounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetAggregateDiscoveredResourceCounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetAggregateDiscoveredResourceCounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetAggregateDiscoveredResourceCounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetAggregateDiscoveredResourceCounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
