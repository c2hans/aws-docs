---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceSummaryByConfigRule.html
---

# GetComplianceSummaryByConfigRule
<a name="API_GetComplianceSummaryByConfigRule"></a>

Returns the number of AWS Config rules that are compliant and noncompliant, up to a maximum of 25 for each.

## Response Syntax
<a name="API_GetComplianceSummaryByConfigRule_ResponseSyntax"></a>

```
{
   "ComplianceSummary": {
      "ComplianceSummaryTimestamp": number,
      "CompliantResourceCount": {
         "CapExceeded": boolean,
         "CappedCount": number
      },
      "NonCompliantResourceCount": {
         "CapExceeded": boolean,
         "CappedCount": number
      }
   }
}
```

## Response Elements
<a name="API_GetComplianceSummaryByConfigRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComplianceSummary](#API_GetComplianceSummaryByConfigRule_ResponseSyntax) **   <a name="config-GetComplianceSummaryByConfigRule-response-ComplianceSummary"></a>
The number of AWS Config rules that are compliant and the number that are noncompliant, up to a maximum of 25 for each.
Type: [ComplianceSummary](API_ComplianceSummary.md) object

## Errors
<a name="API_GetComplianceSummaryByConfigRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetComplianceSummaryByConfigRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetComplianceSummaryByConfigRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetComplianceSummaryByConfigRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetComplianceSummaryByConfigRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetComplianceSummaryByConfigRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetComplianceSummaryByConfigRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetComplianceSummaryByConfigRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetComplianceSummaryByConfigRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetComplianceSummaryByConfigRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetComplianceSummaryByConfigRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetComplianceSummaryByConfigRule)
