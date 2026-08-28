---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutRemediationConfigurations.html
---

# PutRemediationConfigurations
<a name="API_PutRemediationConfigurations"></a>

Adds or updates the remediation configuration with a specific AWS Config rule with the selected target or action. The API creates the `RemediationConfiguration` object for the AWS Config rule. The AWS Config rule must already exist for you to add a remediation configuration. The target (SSM document) must exist and have permissions to use the target.

**Note**
 **Be aware of backward incompatible changes**
If you make backward incompatible changes to the SSM document, you must call this again to ensure the remediations can run.
This API does not support adding remediation configurations for service-linked AWS Config Rules such as Organization AWS Config rules, the rules deployed by conformance packs, and rules deployed by AWS Security Hub.

**Note**
 **Required fields**
For manual remediation configuration, you need to provide a value for `automationAssumeRole` or use a value in the `assumeRole`field to remediate your resources. The SSM automation document can use either as long as it maps to a valid parameter.
However, for automatic remediation configuration, the only valid `assumeRole` field value is `AutomationAssumeRole` and you need to provide a value for `AutomationAssumeRole` to remediate your resources.

**Note**
 **Auto remediation can be initiated even for compliant resources**
If you enable auto remediation for a specific AWS Config rule using the [PutRemediationConfigurations](https://docs.aws.amazon.com/config/latest/APIReference/emAPI_PutRemediationConfigurations.html) API or the AWS Config console, it initiates the remediation process for all non-compliant resources for that specific rule. The auto remediation process relies on the compliance data snapshot which is captured on a periodic basis. Any non-compliant resource that is updated between the snapshot schedule will continue to be remediated based on the last known compliance data snapshot.
This means that in some cases auto remediation can be initiated even for compliant resources, since the bootstrap processor uses a database that can have stale evaluation results based on the last known compliance data snapshot.

## Request Syntax
<a name="API_PutRemediationConfigurations_RequestSyntax"></a>

```
{
   "RemediationConfigurations": [
      {
         "Arn": "{{string}}",
         "Automatic": {{boolean}},
         "ConfigRuleName": "{{string}}",
         "CreatedByService": "{{string}}",
         "ExecutionControls": {
            "SsmControls": {
               "ConcurrentExecutionRatePercentage": {{number}},
               "ErrorPercentage": {{number}}
            }
         },
         "MaximumAutomaticAttempts": {{number}},
         "Parameters": {
            "{{string}}" : {
               "ResourceValue": {
                  "Value": "{{string}}"
               },
               "StaticValue": {
                  "Values": [ "{{string}}" ]
               }
            }
         },
         "ResourceType": "{{string}}",
         "RetryAttemptSeconds": {{number}},
         "TargetId": "{{string}}",
         "TargetType": "{{string}}",
         "TargetVersion": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutRemediationConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RemediationConfigurations](#API_PutRemediationConfigurations_RequestSyntax) **   <a name="config-PutRemediationConfigurations-request-RemediationConfigurations"></a>
A list of remediation configuration objects.
Type: Array of [RemediationConfiguration](API_RemediationConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_PutRemediationConfigurations_ResponseSyntax"></a>

```
{
   "FailedBatches": [
      {
         "FailedItems": [
            {
               "Arn": "string",
               "Automatic": boolean,
               "ConfigRuleName": "string",
               "CreatedByService": "string",
               "ExecutionControls": {
                  "SsmControls": {
                     "ConcurrentExecutionRatePercentage": number,
                     "ErrorPercentage": number
                  }
               },
               "MaximumAutomaticAttempts": number,
               "Parameters": {
                  "string" : {
                     "ResourceValue": {
                        "Value": "string"
                     },
                     "StaticValue": {
                        "Values": [ "string" ]
                     }
                  }
               },
               "ResourceType": "string",
               "RetryAttemptSeconds": number,
               "TargetId": "string",
               "TargetType": "string",
               "TargetVersion": "string"
            }
         ],
         "FailureMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_PutRemediationConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedBatches](#API_PutRemediationConfigurations_ResponseSyntax) **   <a name="config-PutRemediationConfigurations-response-FailedBatches"></a>
Returns a list of failed remediation batch objects.
Type: Array of [FailedRemediationBatch](API_FailedRemediationBatch.md) objects

## Errors
<a name="API_PutRemediationConfigurations_Errors"></a>

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

## See Also
<a name="API_PutRemediationConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutRemediationConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutRemediationConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutRemediationConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutRemediationConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutRemediationConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutRemediationConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutRemediationConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutRemediationConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutRemediationConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutRemediationConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
