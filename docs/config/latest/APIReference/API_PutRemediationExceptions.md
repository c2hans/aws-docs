---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PutRemediationExceptions.html
---

# PutRemediationExceptions
<a name="API_PutRemediationExceptions"></a>

A remediation exception is when a specified resource is no longer considered for auto-remediation. This API adds a new exception or updates an existing exception for a specified resource with a specified AWS Config rule.

**Note**
 **Exceptions block auto remediation**
 AWS Config generates a remediation exception when a problem occurs running a remediation action for a specified resource. Remediation exceptions blocks auto-remediation until the exception is cleared.

**Note**
 **Manual remediation is recommended when placing an exception**
When placing an exception on an AWS resource, it is recommended that remediation is set as manual remediation until the given AWS Config rule for the specified resource evaluates the resource as `NON_COMPLIANT`. Once the resource has been evaluated as `NON_COMPLIANT`, you can add remediation exceptions and change the remediation type back from Manual to Auto if you want to use auto-remediation. Otherwise, using auto-remediation before a `NON_COMPLIANT` evaluation result can delete resources before the exception is applied.

**Note**
 **Exceptions can only be performed on non-compliant resources**
Placing an exception can only be performed on resources that are `NON_COMPLIANT`. If you use this API for `COMPLIANT` resources or resources that are `NOT_APPLICABLE`, a remediation exception will not be generated. For more information on the conditions that initiate the possible AWS Config evaluation results, see [Concepts \| AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#aws-config-rules) in the * AWS Config Developer Guide*.

**Note**
 **Exceptions cannot be placed on service-linked remediation actions**
You cannot place an exception on service-linked remediation actions, such as remediation actions put by an organizational conformance pack.

**Note**
 **Auto remediation can be initiated even for compliant resources**
If you enable auto remediation for a specific AWS Config rule using the [PutRemediationConfigurations](https://docs.aws.amazon.com/config/latest/APIReference/emAPI_PutRemediationConfigurations.html) API or the AWS Config console, it initiates the remediation process for all non-compliant resources for that specific rule. The auto remediation process relies on the compliance data snapshot which is captured on a periodic basis. Any non-compliant resource that is updated between the snapshot schedule will continue to be remediated based on the last known compliance data snapshot.
This means that in some cases auto remediation can be initiated even for compliant resources, since the bootstrap processor uses a database that can have stale evaluation results based on the last known compliance data snapshot.

## Request Syntax
<a name="API_PutRemediationExceptions_RequestSyntax"></a>

```
{
   "ConfigRuleName": "{{string}}",
   "ExpirationTime": {{number}},
   "Message": "{{string}}",
   "ResourceKeys": [
      {
         "ResourceId": "{{string}}",
         "ResourceType": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutRemediationExceptions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigRuleName](#API_PutRemediationExceptions_RequestSyntax) **   <a name="config-PutRemediationExceptions-request-ConfigRuleName"></a>
The name of the AWS Config rule for which you want to create remediation exception.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [ExpirationTime](#API_PutRemediationExceptions_RequestSyntax) **   <a name="config-PutRemediationExceptions-request-ExpirationTime"></a>
The exception is automatically deleted after the expiration date.
Type: Timestamp
Required: No

 ** [Message](#API_PutRemediationExceptions_RequestSyntax) **   <a name="config-PutRemediationExceptions-request-Message"></a>
The message contains an explanation of the exception.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [ResourceKeys](#API_PutRemediationExceptions_RequestSyntax) **   <a name="config-PutRemediationExceptions-request-ResourceKeys"></a>
An exception list of resource exception keys to be processed with the current request. AWS Config adds exception for each resource key. For example, AWS Config adds 3 exceptions for 3 resource keys.
Type: Array of [RemediationExceptionResourceKey](API_RemediationExceptionResourceKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_PutRemediationExceptions_ResponseSyntax"></a>

```
{
   "FailedBatches": [
      {
         "FailedItems": [
            {
               "ConfigRuleName": "string",
               "ExpirationTime": number,
               "Message": "string",
               "ResourceId": "string",
               "ResourceType": "string"
            }
         ],
         "FailureMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_PutRemediationExceptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedBatches](#API_PutRemediationExceptions_ResponseSyntax) **   <a name="config-PutRemediationExceptions-response-FailedBatches"></a>
Returns a list of failed remediation exceptions batch objects. Each object in the batch consists of a list of failed items and failure messages.
Type: Array of [FailedRemediationExceptionBatch](API_FailedRemediationExceptionBatch.md) objects

## Errors
<a name="API_PutRemediationExceptions_Errors"></a>

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
<a name="API_PutRemediationExceptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/PutRemediationExceptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/PutRemediationExceptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PutRemediationExceptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/PutRemediationExceptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PutRemediationExceptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/PutRemediationExceptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/PutRemediationExceptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/PutRemediationExceptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutRemediationExceptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PutRemediationExceptions)
