---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRemediationExecutionStatus.html
---

# DescribeRemediationExecutionStatus
<a name="API_DescribeRemediationExecutionStatus"></a>

Provides a detailed view of a Remediation Execution for a set of resources including state, timestamps for when steps for the remediation execution occur, and any error messages for steps that have failed. When you specify the limit and the next token, you receive a paginated response.

## Request Syntax
<a name="API_DescribeRemediationExecutionStatus_RequestSyntax"></a>

```
{
   "ConfigRuleName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "ResourceKeys": [
      {
         "resourceId": "{{string}}",
         "resourceType": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_DescribeRemediationExecutionStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigRuleName](#API_DescribeRemediationExecutionStatus_RequestSyntax) **   <a name="config-DescribeRemediationExecutionStatus-request-ConfigRuleName"></a>
The name of the AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [Limit](#API_DescribeRemediationExecutionStatus_RequestSyntax) **   <a name="config-DescribeRemediationExecutionStatus-request-Limit"></a>
The maximum number of RemediationExecutionStatuses returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeRemediationExecutionStatus_RequestSyntax) **   <a name="config-DescribeRemediationExecutionStatus-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

 ** [ResourceKeys](#API_DescribeRemediationExecutionStatus_RequestSyntax) **   <a name="config-DescribeRemediationExecutionStatus-request-ResourceKeys"></a>
A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.
Type: Array of [ResourceKey](API_ResourceKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_DescribeRemediationExecutionStatus_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RemediationExecutionStatuses": [
      {
         "InvocationTime": number,
         "LastUpdatedTime": number,
         "ResourceKey": {
            "resourceId": "string",
            "resourceType": "string"
         },
         "State": "string",
         "StepDetails": [
            {
               "ErrorMessage": "string",
               "Name": "string",
               "StartTime": number,
               "State": "string",
               "StopTime": number
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRemediationExecutionStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeRemediationExecutionStatus_ResponseSyntax) **   <a name="config-DescribeRemediationExecutionStatus-response-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

 ** [RemediationExecutionStatuses](#API_DescribeRemediationExecutionStatus_ResponseSyntax) **   <a name="config-DescribeRemediationExecutionStatus-response-RemediationExecutionStatuses"></a>
Returns a list of remediation execution statuses objects.
Type: Array of [RemediationExecutionStatus](API_RemediationExecutionStatus.md) objects

## Errors
<a name="API_DescribeRemediationExecutionStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** NoSuchRemediationConfigurationException **
You specified an AWS Config rule without a remediation configuration.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRemediationExecutionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeRemediationExecutionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeRemediationExecutionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeRemediationExecutionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeRemediationExecutionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeRemediationExecutionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeRemediationExecutionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeRemediationExecutionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeRemediationExecutionStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeRemediationExecutionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeRemediationExecutionStatus)
