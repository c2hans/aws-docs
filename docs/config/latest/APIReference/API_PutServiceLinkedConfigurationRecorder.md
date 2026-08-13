---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html
---

# PutServiceLinkedConfigurationRecorder
<a name="API_PutServiceLinkedConfigurationRecorder"></a>

Creates a service-linked configuration recorder that is linked to a specific AWS service based on the `ServicePrincipal` you specify.

The configuration recorder's `name`, `recordingGroup`, `recordingMode`, and `recordingScope` is set by the service that is linked to the configuration recorder.

For more information and a list of supported services/service principals, see [**Working with the Configuration Recorder**](https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html) in the * AWS Config Developer Guide*.

This API creates a service-linked role `AWSServiceRoleForConfig` in your account. The service-linked role is created only when the role does not exist in your account.

**Note**
 **The recording scope determines if you receive configuration items**
The recording scope is set by the service that is linked to the configuration recorder and determines whether you receive configuration items (CIs) in the delivery channel. If the recording scope is internal, you will not receive CIs in the delivery channel.
 **Tags are added at creation and cannot be updated with this operation**
Use [TagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html) to update tags after creation.

## Request Syntax
<a name="API_PutServiceLinkedConfigurationRecorder_RequestSyntax"></a>

```
{
   "ServicePrincipal": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutServiceLinkedConfigurationRecorder_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ServicePrincipal](#API_PutServiceLinkedConfigurationRecorder_RequestSyntax) **   <a name="config-PutServiceLinkedConfigurationRecorder-request-ServicePrincipal"></a>
The service principal of the AWS service for the service-linked configuration recorder that you want to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** [Tags](#API_PutServiceLinkedConfigurationRecorder_RequestSyntax) **   <a name="config-PutServiceLinkedConfigurationRecorder-request-Tags"></a>
The tags for a service-linked configuration recorder. Each tag consists of a key and an optional value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_PutServiceLinkedConfigurationRecorder_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Name": "string"
}
```

## Response Elements
<a name="API_PutServiceLinkedConfigurationRecorder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_PutServiceLinkedConfigurationRecorder_ResponseSyntax) **   <a name="config-PutServiceLinkedConfigurationRecorder-response-Arn"></a>
The Amazon Resource Name (ARN) of the specified configuration recorder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [Name](#API_PutServiceLinkedConfigurationRecorder_ResponseSyntax) **   <a name="config-PutServiceLinkedConfigurationRecorder-response-Name"></a>
The name of the specified configuration recorder.
For service-linked configuration recorders, AWS Config automatically assigns a name that has the prefix "`AWSConfigurationRecorderFor`" to the new service-linked configuration recorder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_PutServiceLinkedConfigurationRecorder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
For [PutServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html), you cannot create a service-linked recorder because a service-linked recorder already exists for the specified service.
For [PutThirdPartyServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html), you cannot create a service-linked recorder because the specified service principal does not support multiple configuration recorders and one already exists.
For [PutThirdPartyServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html), another in-progress operation is currently referencing the same connector or service principal. Please try again later.
For [PutConnector](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html), you cannot create a connector because a connector already exists for the specified connector configuration.
For [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html), you cannot delete the service-linked recorder because it is currently in use by the linked AWS service.
For [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html), another in-progress operation is currently referencing the same connector. Please try again later.
For [DeleteConnector](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConnector.html), another in-progress operation is currently referencing the connector. Please try again later.
For [DeleteDeliveryChannel](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteDeliveryChannel.html), you cannot delete the specified delivery channel because the customer managed configuration recorder is running. Use the [StopConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html) operation to stop the customer managed configuration recorder.
For [AssociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html) and [DisassociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html), one of the following errors:
+ For service-linked configuration recorders, the configuration recorder is not in use by the service. No association or dissociation of resource types is permitted.
+ For service-linked configuration recorders, your requested change to the configuration recorder has been denied by its linked AWS service.
HTTP Status Code: 400

 ** InsufficientPermissionsException **
Indicates one of the following errors:
+ For [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html), the rule cannot be created because the IAM role assigned to AWS Config lacks permissions to perform the config:Put\* action.
+ For [PutConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html), the AWS Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.
+ For [PutOrganizationConfigRule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html), organization AWS Config rule cannot be created because you do not have permissions to call IAM `GetRole` action or create a service-linked role.
+ For [PutConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html) and [PutOrganizationConformancePack](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html), a conformance pack cannot be created because you do not have the following permissions:
  + You do not have permission to call IAM `GetRole` action or create a service-linked role.
  + You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.
+ For [PutServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html), a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM `CreateServiceLinkedRole`.
+ For [PutConnector](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html), a connector cannot be created because you do not have the following permissions: IAM `CreateServiceLinkedRole`.
HTTP Status Code: 400

 ** LimitExceededException **
For `PutServiceLinkedConfigurationRecorder` API, this exception is thrown if the number of service-linked roles in the account exceeds the limit.
For `StartConfigRulesEvaluation` API, this exception is thrown if an evaluation is in progress or if you call the [StartConfigRulesEvaluation](API_StartConfigRulesEvaluation.md) API more than once per minute.
For `PutConfigurationAggregator` API, this exception is thrown if the number of accounts and aggregators exceeds the limit.
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
<a name="API_PutServiceLinkedConfigurationRecorder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutServiceLinkedConfigurationRecorder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutServiceLinkedConfigurationRecorder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutServiceLinkedConfigurationRecorder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutServiceLinkedConfigurationRecorder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutServiceLinkedConfigurationRecorder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutServiceLinkedConfigurationRecorder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutServiceLinkedConfigurationRecorder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutServiceLinkedConfigurationRecorder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutServiceLinkedConfigurationRecorder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutServiceLinkedConfigurationRecorder)
