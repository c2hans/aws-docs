---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRemediationConfigurations.html
---

# DescribeRemediationConfigurations
<a name="API_DescribeRemediationConfigurations"></a>

Returns the details of one or more remediation configurations.

## Request Syntax
<a name="API_DescribeRemediationConfigurations_RequestSyntax"></a>

```
{
   "ConfigRuleNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeRemediationConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigRuleNames](#API_DescribeRemediationConfigurations_RequestSyntax) **   <a name="config-DescribeRemediationConfigurations-request-ConfigRuleNames"></a>
A list of AWS Config rule names of remediation configurations for which you want details.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeRemediationConfigurations_ResponseSyntax"></a>

```
{
   "RemediationConfigurations": [
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
   ]
}
```

## Response Elements
<a name="API_DescribeRemediationConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RemediationConfigurations](#API_DescribeRemediationConfigurations_ResponseSyntax) **   <a name="config-DescribeRemediationConfigurations-response-RemediationConfigurations"></a>
Returns a remediation configuration object.
Type: Array of [RemediationConfiguration](API_RemediationConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_DescribeRemediationConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeRemediationConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeRemediationConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeRemediationConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeRemediationConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeRemediationConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeRemediationConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeRemediationConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeRemediationConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeRemediationConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeRemediationConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeRemediationConfigurations)
