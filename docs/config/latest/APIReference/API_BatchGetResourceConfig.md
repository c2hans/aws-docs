---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_BatchGetResourceConfig.html
---

# BatchGetResourceConfig
<a name="API_BatchGetResourceConfig"></a>

Returns the `BaseConfigurationItem` for one or more requested resources. The operation also returns a list of resources that are not processed in the current request. If there are no unprocessed resources, the operation returns an empty unprocessedResourceKeys list.

**Note**
The API does not return results for deleted resources.
 The API does not return any tags for the requested resources. This information is filtered out of the supplementaryConfiguration section of the API response.

## Request Syntax
<a name="API_BatchGetResourceConfig_RequestSyntax"></a>

```
{
   "resourceKeys": [
      {
         "resourceId": "{{string}}",
         "resourceType": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_BatchGetResourceConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceKeys](#API_BatchGetResourceConfig_RequestSyntax) **   <a name="config-BatchGetResourceConfig-request-resourceKeys"></a>
A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.
Type: Array of [ResourceKey](API_ResourceKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_BatchGetResourceConfig_ResponseSyntax"></a>

```
{
   "baseConfigurationItems": [
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
   "unprocessedResourceKeys": [
      {
         "resourceId": "string",
         "resourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetResourceConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [baseConfigurationItems](#API_BatchGetResourceConfig_ResponseSyntax) **   <a name="config-BatchGetResourceConfig-response-baseConfigurationItems"></a>
A list that contains the current configuration of one or more resources.
Type: Array of [BaseConfigurationItem](API_BaseConfigurationItem.md) objects

 ** [unprocessedResourceKeys](#API_BatchGetResourceConfig_ResponseSyntax) **   <a name="config-BatchGetResourceConfig-response-unprocessedResourceKeys"></a>
A list of resource keys that were not processed with the current response. The unprocessesResourceKeys value is in the same form as ResourceKeys, so the value can be directly provided to a subsequent BatchGetResourceConfig operation. If there are no unprocessed resource keys, the response contains an empty unprocessedResourceKeys list.
Type: Array of [ResourceKey](API_ResourceKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_BatchGetResourceConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoAvailableConfigurationRecorderException **
There are no customer managed configuration recorders available to record your resources. Use the [PutConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html) operation to create the customer managed configuration recorder.
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
<a name="API_BatchGetResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/BatchGetResourceConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/BatchGetResourceConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/BatchGetResourceConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/BatchGetResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/BatchGetResourceConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/BatchGetResourceConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/BatchGetResourceConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/BatchGetResourceConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/BatchGetResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/BatchGetResourceConfig)
