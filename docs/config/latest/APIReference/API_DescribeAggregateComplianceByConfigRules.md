---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeAggregateComplianceByConfigRules.html
---

# DescribeAggregateComplianceByConfigRules
<a name="API_DescribeAggregateComplianceByConfigRules"></a>

Returns a list of compliant and noncompliant rules with the number of resources for compliant and noncompliant rules. Does not display rules that do not have compliance results.

**Note**
The results can return an empty result page, but if you have a `nextToken`, the results are displayed on the next page.

## Request Syntax
<a name="API_DescribeAggregateComplianceByConfigRules_RequestSyntax"></a>

```
{
   "ConfigurationAggregatorName": "{{string}}",
   "Filters": {
      "AccountId": "{{string}}",
      "AwsRegion": "{{string}}",
      "ComplianceType": "{{string}}",
      "ConfigRuleName": "{{string}}"
   },
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAggregateComplianceByConfigRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationAggregatorName](#API_DescribeAggregateComplianceByConfigRules_RequestSyntax) **   <a name="config-DescribeAggregateComplianceByConfigRules-request-ConfigurationAggregatorName"></a>
The name of the configuration aggregator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: Yes

 ** [Filters](#API_DescribeAggregateComplianceByConfigRules_RequestSyntax) **   <a name="config-DescribeAggregateComplianceByConfigRules-request-Filters"></a>
Filters the results by ConfigRuleComplianceFilters object.
Type: [ConfigRuleComplianceFilters](API_ConfigRuleComplianceFilters.md) object
Required: No

 ** [Limit](#API_DescribeAggregateComplianceByConfigRules_RequestSyntax) **   <a name="config-DescribeAggregateComplianceByConfigRules-request-Limit"></a>
The maximum number of evaluation results returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [NextToken](#API_DescribeAggregateComplianceByConfigRules_RequestSyntax) **   <a name="config-DescribeAggregateComplianceByConfigRules-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeAggregateComplianceByConfigRules_ResponseSyntax"></a>

```
{
   "AggregateComplianceByConfigRules": [
      {
         "AccountId": "string",
         "AwsRegion": "string",
         "Compliance": {
            "ComplianceContributorCount": {
               "CapExceeded": boolean,
               "CappedCount": number
            },
            "ComplianceType": "string"
         },
         "ConfigRuleName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAggregateComplianceByConfigRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AggregateComplianceByConfigRules](#API_DescribeAggregateComplianceByConfigRules_ResponseSyntax) **   <a name="config-DescribeAggregateComplianceByConfigRules-response-AggregateComplianceByConfigRules"></a>
Returns a list of AggregateComplianceByConfigRule object.
Type: Array of [AggregateComplianceByConfigRule](API_AggregateComplianceByConfigRule.md) objects

 ** [NextToken](#API_DescribeAggregateComplianceByConfigRules_ResponseSyntax) **   <a name="config-DescribeAggregateComplianceByConfigRules-response-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_DescribeAggregateComplianceByConfigRules_Errors"></a>

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
<a name="API_DescribeAggregateComplianceByConfigRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeAggregateComplianceByConfigRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeAggregateComplianceByConfigRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeAggregateComplianceByConfigRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeAggregateComplianceByConfigRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeAggregateComplianceByConfigRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeAggregateComplianceByConfigRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeAggregateComplianceByConfigRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeAggregateComplianceByConfigRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeAggregateComplianceByConfigRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeAggregateComplianceByConfigRules)
