---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRemediationExceptions.html
---

# DescribeRemediationExceptions
<a name="API_DescribeRemediationExceptions"></a>

Returns the details of one or more remediation exceptions. A detailed view of a remediation exception for a set of resources that includes an explanation of an exception and the time when the exception will be deleted. When you specify the limit and the next token, you receive a paginated response.

**Note**
 AWS Config generates a remediation exception when a problem occurs executing a remediation action to a specific resource. Remediation exceptions blocks auto-remediation until the exception is cleared.
When you specify the limit and the next token, you receive a paginated response.
Limit and next token are not applicable if you request resources in batch. It is only applicable, when you request all resources.

## Request Syntax
<a name="API_DescribeRemediationExceptions_RequestSyntax"></a>

```
{
   "ConfigRuleName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "ResourceKeys": [
      {
         "ResourceId": "{{string}}",
         "ResourceType": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_DescribeRemediationExceptions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigRuleName](#API_DescribeRemediationExceptions_RequestSyntax) **   <a name="config-DescribeRemediationExceptions-request-ConfigRuleName"></a>
The name of the AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [Limit](#API_DescribeRemediationExceptions_RequestSyntax) **   <a name="config-DescribeRemediationExceptions-request-Limit"></a>
The maximum number of RemediationExceptionResourceKey returned on each page. The default is 25. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeRemediationExceptions_RequestSyntax) **   <a name="config-DescribeRemediationExceptions-request-NextToken"></a>
The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String
Required: No

 ** [ResourceKeys](#API_DescribeRemediationExceptions_RequestSyntax) **   <a name="config-DescribeRemediationExceptions-request-ResourceKeys"></a>
An exception list of resource exception keys to be processed with the current request. AWS Config adds exception for each resource key. For example, AWS Config adds 3 exceptions for 3 resource keys.
Type: Array of [RemediationExceptionResourceKey](API_RemediationExceptionResourceKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_DescribeRemediationExceptions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RemediationExceptions": [
      {
         "ConfigRuleName": "string",
         "ExpirationTime": number,
         "Message": "string",
         "ResourceId": "string",
         "ResourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRemediationExceptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeRemediationExceptions_ResponseSyntax) **   <a name="config-DescribeRemediationExceptions-response-NextToken"></a>
The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.
Type: String

 ** [RemediationExceptions](#API_DescribeRemediationExceptions_ResponseSyntax) **   <a name="config-DescribeRemediationExceptions-response-RemediationExceptions"></a>
Returns a list of remediation exception objects.
Type: Array of [RemediationException](API_RemediationException.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_DescribeRemediationExceptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRemediationExceptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeRemediationExceptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeRemediationExceptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeRemediationExceptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeRemediationExceptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeRemediationExceptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeRemediationExceptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeRemediationExceptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeRemediationExceptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeRemediationExceptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeRemediationExceptions)
