---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateUsageLimit.html
---

# CreateUsageLimit
<a name="API_CreateUsageLimit"></a>

Creates a usage limit for a specified Amazon Redshift Serverless usage type. The usage limit is identified by the returned usage limit identifier.

## Request Syntax
<a name="API_CreateUsageLimit_RequestSyntax"></a>

```
{
   "amount": {{number}},
   "breachAction": "{{string}}",
   "period": "{{string}}",
   "resourceArn": "{{string}}",
   "usageType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateUsageLimit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [amount](#API_CreateUsageLimit_RequestSyntax) **   <a name="redshiftserverless-CreateUsageLimit-request-amount"></a>
The limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.
Type: Long
Required: Yes

 ** [breachAction](#API_CreateUsageLimit_RequestSyntax) **   <a name="redshiftserverless-CreateUsageLimit-request-breachAction"></a>
The action that Amazon Redshift Serverless takes when the limit is reached. The default is log.
Type: String
Valid Values: `log | emit-metric | deactivate`
Required: No

 ** [period](#API_CreateUsageLimit_RequestSyntax) **   <a name="redshiftserverless-CreateUsageLimit-request-period"></a>
The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly.
Type: String
Valid Values: `daily | weekly | monthly`
Required: No

 ** [resourceArn](#API_CreateUsageLimit_RequestSyntax) **   <a name="redshiftserverless-CreateUsageLimit-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the Amazon Redshift Serverless resource to create the usage limit for.
Type: String
Required: Yes

 ** [usageType](#API_CreateUsageLimit_RequestSyntax) **   <a name="redshiftserverless-CreateUsageLimit-request-usageType"></a>
The type of Amazon Redshift Serverless usage to create a usage limit for.
Type: String
Valid Values: `serverless-compute | cross-region-datasharing`
Required: Yes

## Response Syntax
<a name="API_CreateUsageLimit_ResponseSyntax"></a>

```
{
   "usageLimit": {
      "amount": number,
      "breachAction": "string",
      "period": "string",
      "resourceArn": "string",
      "usageLimitArn": "string",
      "usageLimitId": "string",
      "usageType": "string"
   }
}
```

## Response Elements
<a name="API_CreateUsageLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [usageLimit](#API_CreateUsageLimit_ResponseSyntax) **   <a name="redshiftserverless-CreateUsageLimit-response-usageLimit"></a>
The returned usage limit object.
Type: [UsageLimit](API_UsageLimit.md) object

## Errors
<a name="API_CreateUsageLimit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The service limit was exceeded.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateUsageLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/CreateUsageLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/CreateUsageLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/CreateUsageLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/CreateUsageLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/CreateUsageLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/CreateUsageLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/CreateUsageLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/CreateUsageLimit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/CreateUsageLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/CreateUsageLimit)
