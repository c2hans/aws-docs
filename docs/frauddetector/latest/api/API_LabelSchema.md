---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_LabelSchema.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# LabelSchema
<a name="API_LabelSchema"></a>

The label schema.

## Contents
<a name="API_LabelSchema_Contents"></a>

 ** labelMapper **   <a name="FraudDetector-Type-LabelSchema-labelMapper"></a>
The label mapper maps the Amazon Fraud Detector supported model classification labels (`FRAUD`, `LEGIT`) to the appropriate event type labels. For example, if "`FRAUD`" and "`LEGIT`" are Amazon Fraud Detector supported labels, this mapper could be: `{"FRAUD" => ["0"]`, `"LEGIT" => ["1"]}` or `{"FRAUD" => ["false"]`, `"LEGIT" => ["true"]}` or `{"FRAUD" => ["fraud", "abuse"]`, `"LEGIT" => ["legit", "safe"]}`. The value part of the mapper is a list, because you may have multiple label variants from your event type for a single Amazon Fraud Detector label.
Type: String to array of strings map
Required: No

 ** unlabeledEventsTreatment **   <a name="FraudDetector-Type-LabelSchema-unlabeledEventsTreatment"></a>
The action to take for unlabeled events.
+ Use `IGNORE` if you want the unlabeled events to be ignored. This is recommended when the majority of the events in the dataset are labeled.
+ Use `FRAUD` if you want to categorize all unlabeled events as “Fraud”. This is recommended when most of the events in your dataset are fraudulent.
+ Use `LEGIT` if you want to categorize all unlabeled events as “Legit”. This is recommended when most of the events in your dataset are legitimate.
+ Use `AUTO` if you want Amazon Fraud Detector to decide how to use the unlabeled data. This is recommended when there is significant unlabeled events in the dataset.
By default, Amazon Fraud Detector ignores the unlabeled data.
Type: String
Valid Values: `IGNORE | FRAUD | LEGIT | AUTO`
Required: No

## See Also
<a name="API_LabelSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/LabelSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/LabelSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/LabelSchema)
