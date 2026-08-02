---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_StartRemediationExecution.html
---

# StartRemediationExecution
<a name="API_StartRemediationExecution"></a>

Runs an on-demand remediation for the specified AWS Config rules against the last known remediation configuration. It runs an execution against the current state of your resources. Remediation execution is asynchronous.

You can specify up to 100 resource keys per request. An existing StartRemediationExecution call for the specified resource keys must complete before you can call the API again.

## Request Syntax
<a name="API_StartRemediationExecution_RequestSyntax"></a>

```
{
   "ConfigRuleName": "{{string}}",
   "ResourceKeys": [
      {
         "resourceId": "{{string}}",
         "resourceType": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_StartRemediationExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigRuleName](#API_StartRemediationExecution_RequestSyntax) **   <a name="config-StartRemediationExecution-request-ConfigRuleName"></a>
The list of names of AWS Config rules that you want to run remediation execution for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** [ResourceKeys](#API_StartRemediationExecution_RequestSyntax) **   <a name="config-StartRemediationExecution-request-ResourceKeys"></a>
A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.
Type: Array of [ResourceKey](API_ResourceKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_StartRemediationExecution_ResponseSyntax"></a>

```
{
   "FailedItems": [
      {
         "resourceId": "string",
         "resourceType": "string"
      }
   ],
   "FailureMessage": "string"
}
```

## Response Elements
<a name="API_StartRemediationExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedItems](#API_StartRemediationExecution_ResponseSyntax) **   <a name="config-StartRemediationExecution-response-FailedItems"></a>
For resources that have failed to start execution, the API returns a resource key object.
Type: Array of [ResourceKey](API_ResourceKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [FailureMessage](#API_StartRemediationExecution_ResponseSyntax) **   <a name="config-StartRemediationExecution-response-FailureMessage"></a>
Returns a failure message. For example, the resource is already compliant.
Type: String

## Errors
<a name="API_StartRemediationExecution_Errors"></a>

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

 ** NoSuchRemediationConfigurationException **
You specified an AWS Config rule without a remediation configuration.
HTTP Status Code: 400

## See Also
<a name="API_StartRemediationExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/StartRemediationExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/StartRemediationExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/StartRemediationExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/StartRemediationExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/StartRemediationExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/StartRemediationExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/StartRemediationExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/StartRemediationExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/StartRemediationExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/StartRemediationExecution)
