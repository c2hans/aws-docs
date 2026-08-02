---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationAggregator.html
---

# PutConfigurationAggregator
<a name="API_PutConfigurationAggregator"></a>

Creates and updates the configuration aggregator with the selected source accounts and regions. The source account can be individual account(s) or an organization.

 `accountIds` that are passed will be replaced with existing accounts. If you want to add additional accounts into the aggregator, call `DescribeConfigurationAggregators` to get the previous accounts and then append new ones.

**Note**
 AWS Config should be enabled in source accounts and regions you want to aggregate.
If your source type is an organization, you must be signed in to the management account or a registered delegated administrator and all the features must be enabled in your organization. If the caller is a management account, AWS Config calls `EnableAwsServiceAccess` API to enable integration between AWS Config and AWS Organizations. If the caller is a registered delegated administrator, AWS Config calls `ListDelegatedAdministrators` API to verify whether the caller is a valid delegated administrator.
To register a delegated administrator, see [Register a Delegated Administrator](https://docs.aws.amazon.com/config/latest/developerguide/set-up-aggregator-cli.html#register-a-delegated-administrator-cli) in the * AWS Config developer guide*.

**Note**
 **Tags are added at creation and cannot be updated with this operation**
 `PutConfigurationAggregator` is an idempotent API. Subsequent requests won’t create a duplicate resource if one was already created. If a following request has different `tags` values, AWS Config will ignore these differences and treat it as an idempotent request of the previous. In this case, `tags` will not be updated, even if they are different.
Use [TagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html) to update tags after creation.

## Request Syntax
<a name="API_PutConfigurationAggregator_RequestSyntax"></a>

```
{
   "AccountAggregationSources": [
      {
         "AccountIds": [ "{{string}}" ],
         "AllAwsRegions": {{boolean}},
         "AwsRegions": [ "{{string}}" ]
      }
   ],
   "AggregatorFilters": {
      "ResourceType": {
         "Type": "{{string}}",
         "Value": [ "{{string}}" ]
      },
      "ServicePrincipal": {
         "Type": "{{string}}",
         "Value": [ "{{string}}" ]
      }
   },
   "ConfigurationAggregatorName": "{{string}}",
   "OrganizationAggregationSource": {
      "AllAwsRegions": {{boolean}},
      "AwsRegions": [ "{{string}}" ],
      "RoleArn": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutConfigurationAggregator_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountAggregationSources](#API_PutConfigurationAggregator_RequestSyntax) **   <a name="config-PutConfigurationAggregator-request-AccountAggregationSources"></a>
A list of AccountAggregationSource object.
Type: Array of [AccountAggregationSource](API_AccountAggregationSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [AggregatorFilters](#API_PutConfigurationAggregator_RequestSyntax) **   <a name="config-PutConfigurationAggregator-request-AggregatorFilters"></a>
An object to filter configuration recorders in an aggregator. Either `ResourceType` or `ServicePrincipal` is required.
Type: [AggregatorFilters](API_AggregatorFilters.md) object
Required: No

 ** [ConfigurationAggregatorName](#API_PutConfigurationAggregator_RequestSyntax) **   <a name="config-PutConfigurationAggregator-request-ConfigurationAggregatorName"></a>
The name of the configuration aggregator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: Yes

 ** [OrganizationAggregationSource](#API_PutConfigurationAggregator_RequestSyntax) **   <a name="config-PutConfigurationAggregator-request-OrganizationAggregationSource"></a>
An OrganizationAggregationSource object.
Type: [OrganizationAggregationSource](API_OrganizationAggregationSource.md) object
Required: No

 ** [Tags](#API_PutConfigurationAggregator_RequestSyntax) **   <a name="config-PutConfigurationAggregator-request-Tags"></a>
An array of tag object.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_PutConfigurationAggregator_ResponseSyntax"></a>

```
{
   "ConfigurationAggregator": {
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
}
```

## Response Elements
<a name="API_PutConfigurationAggregator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationAggregator](#API_PutConfigurationAggregator_ResponseSyntax) **   <a name="config-PutConfigurationAggregator-response-ConfigurationAggregator"></a>
Returns a ConfigurationAggregator object.
Type: [ConfigurationAggregator](API_ConfigurationAggregator.md) object

## Errors
<a name="API_PutConfigurationAggregator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** InvalidRoleException **
You have provided a null or empty Amazon Resource Name (ARN) for the IAM role assumed by AWS Config and used by the customer managed configuration recorder.
HTTP Status Code: 400

 ** LimitExceededException **
For `PutServiceLinkedConfigurationRecorder` API, this exception is thrown if the number of service-linked roles in the account exceeds the limit.
For `StartConfigRulesEvaluation` API, this exception is thrown if an evaluation is in progress or if you call the [StartConfigRulesEvaluation](API_StartConfigRulesEvaluation.md) API more than once per minute.
For `PutConfigurationAggregator` API, this exception is thrown if the number of accounts and aggregators exceeds the limit.
HTTP Status Code: 400

 ** NoAvailableOrganizationException **
Organization is no longer available.
HTTP Status Code: 400

 ** OrganizationAccessDeniedException **
For `PutConfigurationAggregator` API, you can see this exception for the following reasons:
+ No permission to call `EnableAWSServiceAccess` API
+ The configuration aggregator cannot be updated because your AWS Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current AWS Organization.
+ The configuration aggregator is associated with a previous AWS Organization and AWS Config cannot aggregate data with current AWS Organization. Delete this aggregator and create a new one with the current AWS Organization.
+ You are not a registered delegated administrator for AWS Config with permissions to call `ListDelegatedAdministrators` API. Ensure that the management account registers delagated administrator for AWS Config service principal name before the delegated administrator creates an aggregator.
For all `OrganizationConfigRule` and `OrganizationConformancePack` APIs, AWS Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.
HTTP Status Code: 400

 ** OrganizationAllFeaturesNotEnabledException **
 AWS Config resource cannot be created because your organization does not have all features enabled.
HTTP Status Code: 400

## See Also
<a name="API_PutConfigurationAggregator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutConfigurationAggregator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutConfigurationAggregator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutConfigurationAggregator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutConfigurationAggregator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutConfigurationAggregator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutConfigurationAggregator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutConfigurationAggregator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutConfigurationAggregator)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutConfigurationAggregator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutConfigurationAggregator)
