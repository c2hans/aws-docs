---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_TtlDuration.html
---

# TtlDuration
<a name="API_feature_store_TtlDuration"></a>

Time to live duration, where the record is hard deleted after the expiration time is reached; `ExpiresAt` = `EventTime` \+ `TtlDuration`. For information on HardDelete, see the [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html) API in the Amazon SageMaker API Reference guide.

## Contents
<a name="API_feature_store_TtlDuration_Contents"></a>

 ** Unit **   <a name="sagemaker-Type-feature_store_TtlDuration-Unit"></a>
 `TtlDuration` time unit.
Type: String
Valid Values: `Seconds | Minutes | Hours | Days | Weeks`
Required: Yes

 ** Value **   <a name="sagemaker-Type-feature_store_TtlDuration-Value"></a>
 `TtlDuration` time value.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_feature_store_TtlDuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-featurestore-runtime-2020-07-01/TtlDuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-featurestore-runtime-2020-07-01/TtlDuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-featurestore-runtime-2020-07-01/TtlDuration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
