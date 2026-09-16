---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetAggregateResourceConfig.html
---

# GetAggregateResourceConfig
<a name="API_GetAggregateResourceConfig"></a>

Returns configuration item that is aggregated for your specific resource in a specific source account and region.

**Note**
The API does not return results for deleted resources.

## Request Syntax
<a name="API_GetAggregateResourceConfig_RequestSyntax"></a>

```
{
   "ConfigurationAggregatorName": "{{string}}",
   "ResourceIdentifier": {
      "ResourceId": "{{string}}",
      "ResourceName": "{{string}}",
      "ResourceType": "{{string}}",
      "SourceAccountId": "{{string}}",
      "SourceRegion": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetAggregateResourceConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationAggregatorName](#API_GetAggregateResourceConfig_RequestSyntax) **   <a name="config-GetAggregateResourceConfig-request-ConfigurationAggregatorName"></a>
The name of the configuration aggregator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: Yes

 ** [ResourceIdentifier](#API_GetAggregateResourceConfig_RequestSyntax) **   <a name="config-GetAggregateResourceConfig-request-ResourceIdentifier"></a>
An object that identifies aggregate resource.
Type: [AggregateResourceIdentifier](API_AggregateResourceIdentifier.md) object
Required: Yes

## Response Syntax
<a name="API_GetAggregateResourceConfig_ResponseSyntax"></a>

```
{
   "ConfigurationItem": {
      "accountId": "string",
      "arn": "string",
      "availabilityZone": "string",
      "awsRegion": "string",
      "configuration": "string",
      "configurationItemCaptureTime": number,
      "configurationItemDeliveryTime": number,
      "configurationItemMD5Hash": "string",
      "configurationItemStatus": "string",
      "configurationStateId": "string",
      "recordingFrequency": "string",
      "relatedEvents": [ "string" ],
      "relationships": [
         {
            "relationshipName": "string",
            "resourceId": "string",
            "resourceName": "string",
            "resourceType": "string"
         }
      ],
      "resourceCreationTime": number,
      "resourceId": "string",
      "resourceName": "string",
      "resourceType": "string",
      "supplementaryConfiguration": {
         "string" : "string"
      },
      "tags": {
         "string" : "string"
      },
      "version": "string"
   }
}
```

## Response Elements
<a name="API_GetAggregateResourceConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationItem](#API_GetAggregateResourceConfig_ResponseSyntax) **   <a name="config-GetAggregateResourceConfig-response-ConfigurationItem"></a>
Returns a `ConfigurationItem` object.
Type: [ConfigurationItem](API_ConfigurationItem.md) object

## Errors
<a name="API_GetAggregateResourceConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchConfigurationAggregatorException **
You have specified a configuration aggregator that does not exist.
HTTP Status Code: 400

 ** OversizedConfigurationItemException **
The configuration item size is outside the allowable range.
HTTP Status Code: 400

 ** ResourceNotDiscoveredException **
You have specified a resource that is either unknown or has not been discovered.
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
<a name="API_GetAggregateResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetAggregateResourceConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetAggregateResourceConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetAggregateResourceConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetAggregateResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetAggregateResourceConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetAggregateResourceConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetAggregateResourceConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetAggregateResourceConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetAggregateResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetAggregateResourceConfig)
