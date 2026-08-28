---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteRemediationExceptions.html
---

# DeleteRemediationExceptions
<a name="API_DeleteRemediationExceptions"></a>

Deletes one or more remediation exceptions mentioned in the resource keys.

**Note**
 AWS Config generates a remediation exception when a problem occurs executing a remediation action to a specific resource. Remediation exceptions blocks auto-remediation until the exception is cleared.

## Request Syntax
<a name="API_DeleteRemediationExceptions_RequestSyntax"></a>

```
{
   "ConfigRuleName": "{{string}}",
   "ResourceKeys": [
      {
         "ResourceId": "{{string}}",
         "ResourceType": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_DeleteRemediationExceptions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigRuleName](#API_DeleteRemediationExceptions_RequestSyntax) **   <a name="config-DeleteRemediationExceptions-request-ConfigRuleName"></a>
The name of the AWS Config rule for which you want to delete remediation exception configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** [ResourceKeys](#API_DeleteRemediationExceptions_RequestSyntax) **   <a name="config-DeleteRemediationExceptions-request-ResourceKeys"></a>
An exception list of resource exception keys to be processed with the current request. AWS Config adds exception for each resource key. For example, AWS Config adds 3 exceptions for 3 resource keys.
Type: Array of [RemediationExceptionResourceKey](API_RemediationExceptionResourceKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_DeleteRemediationExceptions_ResponseSyntax"></a>

```
{
   "FailedBatches": [
      {
         "FailedItems": [
            {
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
<a name="API_DeleteRemediationExceptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedBatches](#API_DeleteRemediationExceptions_ResponseSyntax) **   <a name="config-DeleteRemediationExceptions-response-FailedBatches"></a>
Returns a list of failed delete remediation exceptions batch objects. Each object in the batch consists of a list of failed items and failure messages.
Type: Array of [FailedDeleteRemediationExceptionsBatch](API_FailedDeleteRemediationExceptionsBatch.md) objects

## Errors
<a name="API_DeleteRemediationExceptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** NoSuchRemediationExceptionException **
You tried to delete a remediation exception that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRemediationExceptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DeleteRemediationExceptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DeleteRemediationExceptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DeleteRemediationExceptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DeleteRemediationExceptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DeleteRemediationExceptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DeleteRemediationExceptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DeleteRemediationExceptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DeleteRemediationExceptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DeleteRemediationExceptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DeleteRemediationExceptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
