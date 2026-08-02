---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteResourceConfig.html
---

# DeleteResourceConfig
<a name="API_DeleteResourceConfig"></a>

Records the configuration state for a custom resource that has been deleted. This API records a new ConfigurationItem with a ResourceDeleted status. You can retrieve the ConfigurationItems recorded for this resource in your AWS Config History.

## Request Syntax
<a name="API_DeleteResourceConfig_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteResourceConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceId](#API_DeleteResourceConfig_RequestSyntax) **   <a name="config-DeleteResourceConfig-request-ResourceId"></a>
Unique identifier of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: Yes

 ** [ResourceType](#API_DeleteResourceConfig_RequestSyntax) **   <a name="config-DeleteResourceConfig-request-ResourceType"></a>
The type of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 196.
Required: Yes

## Response Elements
<a name="API_DeleteResourceConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourceConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoRunningConfigurationRecorderException **
There is no configuration recorder running.
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
<a name="API_DeleteResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DeleteResourceConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DeleteResourceConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DeleteResourceConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DeleteResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DeleteResourceConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DeleteResourceConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DeleteResourceConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DeleteResourceConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DeleteResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DeleteResourceConfig)
