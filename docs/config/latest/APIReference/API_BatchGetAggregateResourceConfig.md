---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_BatchGetAggregateResourceConfig.html
---

# BatchGetAggregateResourceConfig
<a name="API_BatchGetAggregateResourceConfig"></a>

Returns the current configuration items for resources that are present in your AWS Config aggregator. The operation also returns a list of resources that are not processed in the current request. If there are no unprocessed resources, the operation returns an empty `unprocessedResourceIdentifiers` list.

**Note**
The API does not return results for deleted resources.
 The API does not return tags and relationships.

## Request Syntax
<a name="API_BatchGetAggregateResourceConfig_RequestSyntax"></a>

```
{
   "ConfigurationAggregatorName": "{{string}}",
   "ResourceIdentifiers": [
      {
         "ResourceId": "{{string}}",
         "ResourceName": "{{string}}",
         "ResourceType": "{{string}}",
         "SourceAccountId": "{{string}}",
         "SourceRegion": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_BatchGetAggregateResourceConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationAggregatorName](#API_BatchGetAggregateResourceConfig_RequestSyntax) **   <a name="config-BatchGetAggregateResourceConfig-request-ConfigurationAggregatorName"></a>
The name of the configuration aggregator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: Yes

 ** [ResourceIdentifiers](#API_BatchGetAggregateResourceConfig_RequestSyntax) **   <a name="config-BatchGetAggregateResourceConfig-request-ResourceIdentifiers"></a>
A list of aggregate ResourceIdentifiers objects.
Type: Array of [AggregateResourceIdentifier](API_AggregateResourceIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_BatchGetAggregateResourceConfig_ResponseSyntax"></a>

```
{
   "BaseConfigurationItems": [
      {
         "accountId": "string",
         "arn": "string",
         "availabilityZone": "string",
         "awsRegion": "string",
         "configuration": "string",
         "configurationItemCaptureTime": number,
         "configurationItemDeliveryTime": number,
         "configurationItemStatus": "string",
         "configurationStateId": "string",
         "recordingFrequency": "string",
         "resourceCreationTime": number,
         "resourceId": "string",
         "resourceName": "string",
         "resourceType": "string",
         "supplementaryConfiguration": {
            "string" : "string"
         },
         "version": "string"
      }
   ],
   "UnprocessedResourceIdentifiers": [
      {
         "ResourceId": "string",
         "ResourceName": "string",
         "ResourceType": "string",
         "SourceAccountId": "string",
         "SourceRegion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetAggregateResourceConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BaseConfigurationItems](#API_BatchGetAggregateResourceConfig_ResponseSyntax) **   <a name="config-BatchGetAggregateResourceConfig-response-BaseConfigurationItems"></a>
A list that contains the current configuration of one or more resources.
Type: Array of [BaseConfigurationItem](API_BaseConfigurationItem.md) objects

 ** [UnprocessedResourceIdentifiers](#API_BatchGetAggregateResourceConfig_ResponseSyntax) **   <a name="config-BatchGetAggregateResourceConfig-response-UnprocessedResourceIdentifiers"></a>
A list of resource identifiers that were not processed with current scope. The list is empty if all the resources are processed.
Type: Array of [AggregateResourceIdentifier](API_AggregateResourceIdentifier.md) objects

## Errors
<a name="API_BatchGetAggregateResourceConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_BatchGetAggregateResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/BatchGetAggregateResourceConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/BatchGetAggregateResourceConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/BatchGetAggregateResourceConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/BatchGetAggregateResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/BatchGetAggregateResourceConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/BatchGetAggregateResourceConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/BatchGetAggregateResourceConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/BatchGetAggregateResourceConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/BatchGetAggregateResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/BatchGetAggregateResourceConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
