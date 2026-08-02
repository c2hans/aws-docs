---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UsageLimit.html
---

# UsageLimit
<a name="API_UsageLimit"></a>

The usage limit object.

## Contents
<a name="API_UsageLimit_Contents"></a>

 ** amount **   <a name="redshiftserverless-Type-UsageLimit-amount"></a>
The limit amount. If time-based, this amount is in RPUs consumed per hour. If data-based, this amount is in terabytes (TB). The value must be a positive number.
Type: Long
Required: No

 ** breachAction **   <a name="redshiftserverless-Type-UsageLimit-breachAction"></a>
The action that Amazon Redshift Serverless takes when the limit is reached.
Type: String
Valid Values: `log | emit-metric | deactivate`
Required: No

 ** period **   <a name="redshiftserverless-Type-UsageLimit-period"></a>
The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly.
Type: String
Valid Values: `daily | weekly | monthly`
Required: No

 ** resourceArn **   <a name="redshiftserverless-Type-UsageLimit-resourceArn"></a>
The Amazon Resource Name (ARN) that identifies the Amazon Redshift Serverless resource.
Type: String
Required: No

 ** usageLimitArn **   <a name="redshiftserverless-Type-UsageLimit-usageLimitArn"></a>
The Amazon Resource Name (ARN) of the resource associated with the usage limit.
Type: String
Required: No

 ** usageLimitId **   <a name="redshiftserverless-Type-UsageLimit-usageLimitId"></a>
The identifier of the usage limit.
Type: String
Required: No

 ** usageType **   <a name="redshiftserverless-Type-UsageLimit-usageType"></a>
The Amazon Redshift Serverless feature to limit.
Type: String
Valid Values: `serverless-compute | cross-region-datasharing`
Required: No

## See Also
<a name="API_UsageLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/UsageLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/UsageLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/UsageLimit)
