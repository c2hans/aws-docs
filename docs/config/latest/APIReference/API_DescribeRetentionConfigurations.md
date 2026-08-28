---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRetentionConfigurations.html
---

# DescribeRetentionConfigurations
<a name="API_DescribeRetentionConfigurations"></a>

Returns the details of one or more retention configurations. If the retention configuration name is not specified, this operation returns the details for all the retention configurations for that account.

**Note**
Currently, AWS Config supports only one retention configuration per region in your account.

## Request Syntax
<a name="API_DescribeRetentionConfigurations_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "RetentionConfigurationNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeRetentionConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_DescribeRetentionConfigurations_RequestSyntax) **   <a name="config-DescribeRetentionConfigurations-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

 ** [RetentionConfigurationNames](#API_DescribeRetentionConfigurations_RequestSyntax) **   <a name="config-DescribeRetentionConfigurations-request-RetentionConfigurationNames"></a>
A list of names of retention configurations for which you want details. If you do not specify a name, AWS Config returns details for all the retention configurations for that account.
Currently, AWS Config supports only one retention configuration per region in your account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: No

## Response Syntax
<a name="API_DescribeRetentionConfigurations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RetentionConfigurations": [
      {
         "Name": "string",
         "RetentionPeriodInDays": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRetentionConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeRetentionConfigurations_ResponseSyntax) **   <a name="config-DescribeRetentionConfigurations-response-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

 ** [RetentionConfigurations](#API_DescribeRetentionConfigurations_ResponseSyntax) **   <a name="config-DescribeRetentionConfigurations-response-RetentionConfigurations"></a>
Returns a retention configuration object.
Type: Array of [RetentionConfiguration](API_RetentionConfiguration.md) objects

## Errors
<a name="API_DescribeRetentionConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** NoSuchRetentionConfigurationException **
You have specified a retention configuration that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRetentionConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeRetentionConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeRetentionConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeRetentionConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeRetentionConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeRetentionConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeRetentionConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeRetentionConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeRetentionConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeRetentionConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeRetentionConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
