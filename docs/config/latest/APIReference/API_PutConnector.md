---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html
---

# PutConnector
<a name="API_PutConnector"></a>

Creates a connector that specifies the connection between a third-party cloud service provider and AWS Config.

A connector is required to create a service-linked configuration recorder for a third-party cloud service provider using the [PutThirdPartyServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html) operation.

This API creates a service-linked role `AWSServiceRoleForConfigThirdParty` in your account. The service-linked role is created only when the role does not exist in your account.

**Note**
 **Connectors cannot be updated**
To update the connector configuration, you must delete all associated configuration recorders, delete the connector, and recreate it with the updated configuration.

**Note**
 **Tags are added at creation and cannot be updated with this operation**
Use [TagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html) to update tags after creation.

## Request Syntax
<a name="API_PutConnector_RequestSyntax"></a>

```
{
   "ConnectorConfiguration": {
      "azure": {
         "clientIdentifier": "{{string}}",
         "tenantIdentifier": "{{string}}"
      }
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
<a name="API_PutConnector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectorConfiguration](#API_PutConnector_RequestSyntax) **   <a name="config-PutConnector-request-ConnectorConfiguration"></a>
The provider-specific configuration for connecting to the third-party cloud service provider.
Type: [ConnectorConfiguration](API_ConnectorConfiguration.md) object
Required: Yes

 ** [Tags](#API_PutConnector_RequestSyntax) **   <a name="config-PutConnector-request-Tags"></a>
The tags for the connector. Each tag consists of a key and an optional value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_PutConnector_ResponseSyntax"></a>

```
{
   "Arn": "string"
}
```

## Response Elements
<a name="API_PutConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_PutConnector_ResponseSyntax) **   <a name="config-PutConnector-response-Arn"></a>
The Amazon Resource Name (ARN) of the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

## Errors
<a name="API_PutConnector_Errors"></a>

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

 ** MaxNumberOfConnectorsExceededException **
You have reached the limit of the number of connectors in your account.
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
<a name="API_PutConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
