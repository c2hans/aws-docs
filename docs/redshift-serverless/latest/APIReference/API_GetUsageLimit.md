---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetUsageLimit.html
---

# GetUsageLimit
<a name="API_GetUsageLimit"></a>

Returns information about a usage limit.

## Request Syntax
<a name="API_GetUsageLimit_RequestSyntax"></a>

```
{
   "usageLimitId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetUsageLimit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [usageLimitId](#API_GetUsageLimit_RequestSyntax) **   <a name="redshiftserverless-GetUsageLimit-request-usageLimitId"></a>
The unique identifier of the usage limit to return information for.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetUsageLimit_ResponseSyntax"></a>

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
<a name="API_GetUsageLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [usageLimit](#API_GetUsageLimit_ResponseSyntax) **   <a name="redshiftserverless-GetUsageLimit-response-usageLimit"></a>
The returned usage limit object.
Type: [UsageLimit](API_UsageLimit.md) object

## Errors
<a name="API_GetUsageLimit_Errors"></a>

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

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetUsageLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/GetUsageLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/GetUsageLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/GetUsageLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/GetUsageLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/GetUsageLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/GetUsageLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/GetUsageLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/GetUsageLimit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/GetUsageLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/GetUsageLimit)
