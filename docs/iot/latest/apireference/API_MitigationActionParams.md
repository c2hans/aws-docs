---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_MitigationActionParams.html
---

# MitigationActionParams
<a name="API_MitigationActionParams"></a>

The set of parameters for this mitigation action. You can specify only one type of parameter (in other words, you can apply only one action for each defined mitigation action).

## Contents
<a name="API_MitigationActionParams_Contents"></a>

 ** addThingsToThingGroupParams **   <a name="iot-Type-MitigationActionParams-addThingsToThingGroupParams"></a>
Parameters to define a mitigation action that moves devices associated with a certificate to one or more specified thing groups, typically for quarantine.
Type: [AddThingsToThingGroupParams](API_AddThingsToThingGroupParams.md) object
Required: No

 ** enableIoTLoggingParams **   <a name="iot-Type-MitigationActionParams-enableIoTLoggingParams"></a>
Parameters to define a mitigation action that enables AWS IoT Core logging at a specified level of detail.
Type: [EnableIoTLoggingParams](API_EnableIoTLoggingParams.md) object
Required: No

 ** publishFindingToSnsParams **   <a name="iot-Type-MitigationActionParams-publishFindingToSnsParams"></a>
Parameters to define a mitigation action that publishes findings to Amazon Simple Notification Service (Amazon SNS. You can implement your own custom actions in response to the Amazon SNS messages.
Type: [PublishFindingToSnsParams](API_PublishFindingToSnsParams.md) object
Required: No

 ** replaceDefaultPolicyVersionParams **   <a name="iot-Type-MitigationActionParams-replaceDefaultPolicyVersionParams"></a>
Parameters to define a mitigation action that adds a blank policy to restrict permissions.
Type: [ReplaceDefaultPolicyVersionParams](API_ReplaceDefaultPolicyVersionParams.md) object
Required: No

 ** updateCACertificateParams **   <a name="iot-Type-MitigationActionParams-updateCACertificateParams"></a>
Parameters to define a mitigation action that changes the state of the CA certificate to inactive.
Type: [UpdateCACertificateParams](API_UpdateCACertificateParams.md) object
Required: No

 ** updateDeviceCertificateParams **   <a name="iot-Type-MitigationActionParams-updateDeviceCertificateParams"></a>
Parameters to define a mitigation action that changes the state of the device certificate to inactive.
Type: [UpdateDeviceCertificateParams](API_UpdateDeviceCertificateParams.md) object
Required: No

## See Also
<a name="API_MitigationActionParams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/MitigationActionParams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/MitigationActionParams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/MitigationActionParams)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
