---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html
---

# PutOrganizationConfigRule
<a name="API_PutOrganizationConfigRule"></a>

Adds or updates an AWS Config rule for your entire organization to evaluate if your AWS resources comply with your desired configurations. For information on how many organization AWS Config rules you can have per account, see [**Service Limits**](https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html) in the * AWS Config Developer Guide*.

 Only a management account and a delegated administrator can create or update an organization AWS Config rule. When calling this API with a delegated administrator, you must ensure AWS Organizations `ListDelegatedAdministrator` permissions are added. An organization can have up to 3 delegated administrators.

This API enables organization service access through the `EnableAWSServiceAccess` action and creates a service-linked role `AWSServiceRoleForConfigMultiAccountSetup` in the management or delegated administrator account of your organization. The service-linked role is created only when the role does not exist in the caller account. AWS Config verifies the existence of role with `GetRole` action.

To use this API with delegated administrator, register a delegated administrator by calling AWS Organization `register-delegated-administrator` for `config-multiaccountsetup.amazonaws.com`.

There are two types of rules: * AWS Config Managed Rules* and * AWS Config Custom Rules*. You can use `PutOrganizationConfigRule` to create both AWS Config Managed Rules and AWS Config Custom Rules.

 AWS Config Managed Rules are predefined, customizable rules created by AWS Config. For a list of managed rules, see [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html). If you are adding an AWS Config managed rule, you must specify the rule's identifier for the `RuleIdentifier` key.

 AWS Config Custom Rules are rules that you create from scratch. There are two ways to create AWS Config custom rules: with Lambda functions ([AWS Lambda Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/gettingstarted-concepts.html#gettingstarted-concepts-function)) and with Guard ([Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard)), a policy-as-code language. AWS Config custom rules created with AWS Lambda are called * AWS Config Custom Lambda Rules* and AWS Config custom rules created with Guard are called * AWS Config Custom Policy Rules*.

If you are adding a new AWS Config Custom Lambda rule, you first need to create an AWS Lambda function in the management account or a delegated administrator that the rule invokes to evaluate your resources. You also need to create an IAM role in the managed account that can be assumed by the Lambda function. When you use `PutOrganizationConfigRule` to add a Custom Lambda rule to AWS Config, you must specify the Amazon Resource Name (ARN) that AWS Lambda assigns to the function.

**Note**
Prerequisite: Ensure you call `EnableAllFeatures` API to enable all features in an organization.
Make sure to specify one of either `OrganizationCustomPolicyRuleMetadata` for Custom Policy rules, `OrganizationCustomRuleMetadata` for Custom Lambda rules, or `OrganizationManagedRuleMetadata` for managed rules.

## Request Syntax
<a name="API_PutOrganizationConfigRule_RequestSyntax"></a>

```
{
   "ExcludedAccounts": [ "{{string}}" ],
   "OrganizationConfigRuleName": "{{string}}",
   "OrganizationCustomPolicyRuleMetadata": {
      "DebugLogDeliveryAccounts": [ "{{string}}" ],
      "Description": "{{string}}",
      "InputParameters": "{{string}}",
      "MaximumExecutionFrequency": "{{string}}",
      "OrganizationConfigRuleTriggerTypes": [ "{{string}}" ],
      "PolicyRuntime": "{{string}}",
      "PolicyText": "{{string}}",
      "ResourceIdScope": "{{string}}",
      "ResourceTypesScope": [ "{{string}}" ],
      "TagKeyScope": "{{string}}",
      "TagValueScope": "{{string}}"
   },
   "OrganizationCustomRuleMetadata": {
      "Description": "{{string}}",
      "InputParameters": "{{string}}",
      "LambdaFunctionArn": "{{string}}",
      "MaximumExecutionFrequency": "{{string}}",
      "OrganizationConfigRuleTriggerTypes": [ "{{string}}" ],
      "ResourceIdScope": "{{string}}",
      "ResourceTypesScope": [ "{{string}}" ],
      "TagKeyScope": "{{string}}",
      "TagValueScope": "{{string}}"
   },
   "OrganizationManagedRuleMetadata": {
      "Description": "{{string}}",
      "InputParameters": "{{string}}",
      "MaximumExecutionFrequency": "{{string}}",
      "ResourceIdScope": "{{string}}",
      "ResourceTypesScope": [ "{{string}}" ],
      "RuleIdentifier": "{{string}}",
      "TagKeyScope": "{{string}}",
      "TagValueScope": "{{string}}"
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
<a name="API_PutOrganizationConfigRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExcludedAccounts](#API_PutOrganizationConfigRule_RequestSyntax) **   <a name="config-PutOrganizationConfigRule-request-ExcludedAccounts"></a>
A comma-separated list of accounts that you want to exclude from an organization AWS Config rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** [OrganizationConfigRuleName](#API_PutOrganizationConfigRule_RequestSyntax) **   <a name="config-PutOrganizationConfigRule-request-OrganizationConfigRuleName"></a>
The name that you assign to an organization AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

 ** [OrganizationCustomPolicyRuleMetadata](#API_PutOrganizationConfigRule_RequestSyntax) **   <a name="config-PutOrganizationConfigRule-request-OrganizationCustomPolicyRuleMetadata"></a>
An `OrganizationCustomPolicyRuleMetadata` object. This object specifies metadata for your organization's AWS Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of AWS resource, and organization trigger types that initiate AWS Config to evaluate AWS resources against a rule.
Type: [OrganizationCustomPolicyRuleMetadata](API_OrganizationCustomPolicyRuleMetadata.md) object
Required: No

 ** [OrganizationCustomRuleMetadata](#API_PutOrganizationConfigRule_RequestSyntax) **   <a name="config-PutOrganizationConfigRule-request-OrganizationCustomRuleMetadata"></a>
An `OrganizationCustomRuleMetadata` object. This object specifies organization custom rule metadata such as resource type, resource ID of AWS resource, Lambda function ARN, and organization trigger types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.
Type: [OrganizationCustomRuleMetadata](API_OrganizationCustomRuleMetadata.md) object
Required: No

 ** [OrganizationManagedRuleMetadata](#API_PutOrganizationConfigRule_RequestSyntax) **   <a name="config-PutOrganizationConfigRule-request-OrganizationManagedRuleMetadata"></a>
An `OrganizationManagedRuleMetadata` object. This object specifies organization managed rule metadata such as resource type and ID of AWS resource along with the rule identifier. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.
Type: [OrganizationManagedRuleMetadata](API_OrganizationManagedRuleMetadata.md) object
Required: No

 ** [Tags](#API_PutOrganizationConfigRule_RequestSyntax) **   <a name="config-PutOrganizationConfigRule-request-Tags"></a>
The tags for the organization AWS Config rule. Each tag consists of a key and an optional value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_PutOrganizationConfigRule_ResponseSyntax"></a>

```
{
   "OrganizationConfigRuleArn": "string"
}
```

## Response Elements
<a name="API_PutOrganizationConfigRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OrganizationConfigRuleArn](#API_PutOrganizationConfigRule_ResponseSyntax) **   <a name="config-PutOrganizationConfigRule-response-OrganizationConfigRuleArn"></a>
The Amazon Resource Name (ARN) of an organization AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_PutOrganizationConfigRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** MaxNumberOfOrganizationConfigRulesExceededException **
You have reached the limit of the number of organization AWS Config rules you can create. For more information, see see [**Service Limits**](https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html) in the * AWS Config Developer Guide*.
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

 ** ResourceInUseException **
You see this exception in the following cases:
+ For DeleteConfigRule, AWS Config is deleting this rule. Try your request again later.
+ For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.
+ For DeleteConfigRule, a remediation action is associated with the rule and AWS Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.
+ For PutConfigOrganizationRule, organization AWS Config rule deletion is in progress. Try your request again later.
+ For DeleteOrganizationConfigRule, organization AWS Config rule creation is in progress. Try your request again later.
+ For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.
+ For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.
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
<a name="API_PutOrganizationConfigRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutOrganizationConfigRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutOrganizationConfigRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutOrganizationConfigRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutOrganizationConfigRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutOrganizationConfigRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutOrganizationConfigRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutOrganizationConfigRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutOrganizationConfigRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutOrganizationConfigRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutOrganizationConfigRule)
