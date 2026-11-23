---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationResolvedSource.html
---

# EvaluationResolvedSource

The resolved value of an external source that is used by the conditions in an evaluation form.

## Contents
<a name="API_EvaluationResolvedSource_Contents"></a>

 ** Source **   <a name="connect-Type-EvaluationResolvedSource-Source"></a>
The external source, such as contact data, evaluation metadata, form metadata, or AI metrics.
Type: [EvaluationFormItemEnablementSource](API_EvaluationFormItemEnablementSource.md) object
Required: Yes

 ** Status **   <a name="connect-Type-EvaluationResolvedSource-Status"></a>
The status of resolving the source. Valid values:
+  `PENDING` - The source has not been resolved yet.
+  `RESOLVED` - The source has been resolved.
+  `FAILED` - The source could not be resolved.
Type: String
Valid Values: `PENDING | RESOLVED | FAILED`
Required: Yes

 ** Values **   <a name="connect-Type-EvaluationResolvedSource-Values"></a>
The resolved values of the source. Present when `Status` is `RESOLVED`. Contains one value for a single-valued source, any number of values for a multi-valued source, and no values when the source is not present on the contact.
Type: Array of [EvaluationFormItemEnablementSourceValue](API_EvaluationFormItemEnablementSourceValue.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_EvaluationResolvedSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationResolvedSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationResolvedSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationResolvedSource)
