---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClarifyInferenceConfig.html
---

# ClarifyInferenceConfig
<a name="API_ClarifyInferenceConfig"></a>

The inference configuration parameter for the model container.

## Contents
<a name="API_ClarifyInferenceConfig_Contents"></a>

 ** ContentTemplate **   <a name="sagemaker-Type-ClarifyInferenceConfig-ContentTemplate"></a>
A template string used to format a JSON record into an acceptable model container input. For example, a `ContentTemplate` string `'{"myfeatures":$features}'` will format a list of features `[1,2,3]` into the record string `'{"myfeatures":[1,2,3]}'`. Required only when the model container input is in JSON Lines format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** FeatureHeaders **   <a name="sagemaker-Type-ClarifyInferenceConfig-FeatureHeaders"></a>
The names of the features. If provided, these are included in the endpoint response payload to help readability of the `InvokeEndpoint` output. See the [Response](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response) section under **Invoke the endpoint** in the Developer Guide for more information.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** FeaturesAttribute **   <a name="sagemaker-Type-ClarifyInferenceConfig-FeaturesAttribute"></a>
Provides the JMESPath expression to extract the features from a model container input in JSON Lines format. For example, if `FeaturesAttribute` is the JMESPath expression `'myfeatures'`, it extracts a list of features `[1,2,3]` from request data `'{"myfeatures":[1,2,3]}'`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** FeatureTypes **   <a name="sagemaker-Type-ClarifyInferenceConfig-FeatureTypes"></a>
A list of data types of the features (optional). Applicable only to NLP explainability. If provided, `FeatureTypes` must have at least one `'text'` string (for example, `['text']`). If `FeatureTypes` is not provided, the explainer infers the feature types based on the baseline data. The feature types are included in the endpoint response payload. For additional information see the [response](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response) section under **Invoke the endpoint** in the Developer Guide for more information.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 256 items.
Valid Values: `numerical | categorical | text`
Required: No

 ** LabelAttribute **   <a name="sagemaker-Type-ClarifyInferenceConfig-LabelAttribute"></a>
A JMESPath expression used to locate the list of label headers in the model container output.
 **Example**: If the model container output of a batch request is `'{"labels":["cat","dog","fish"],"probability":[0.6,0.3,0.1]}'`, then set `LabelAttribute` to `'labels'` to extract the list of label headers `["cat","dog","fish"]`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** LabelHeaders **   <a name="sagemaker-Type-ClarifyInferenceConfig-LabelHeaders"></a>
For multiclass classification problems, the label headers are the names of the classes. Otherwise, the label header is the name of the predicted label. These are used to help readability for the output of the `InvokeEndpoint` API. See the [response](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response) section under **Invoke the endpoint** in the Developer Guide for more information. If there are no label headers in the model container output, provide them manually using this parameter.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** LabelIndex **   <a name="sagemaker-Type-ClarifyInferenceConfig-LabelIndex"></a>
A zero-based index used to extract a label header or list of label headers from model container output in CSV format.
 **Example for a multiclass model:** If the model container output consists of label headers followed by probabilities: `'"[\'cat\',\'dog\',\'fish\']","[0.1,0.6,0.3]"'`, set `LabelIndex` to `0` to select the label headers `['cat','dog','fish']`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MaxPayloadInMB **   <a name="sagemaker-Type-ClarifyInferenceConfig-MaxPayloadInMB"></a>
The maximum payload size (MB) allowed of a request from the explainer to the model container. Defaults to `6` MB.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** MaxRecordCount **   <a name="sagemaker-Type-ClarifyInferenceConfig-MaxRecordCount"></a>
The maximum number of records in a request that the model container can process when querying the model container for the predictions of a [synthetic dataset](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-synthetic). A record is a unit of input data that inference can be made on, for example, a single line in CSV data. If `MaxRecordCount` is `1`, the model container expects one record per request. A value of 2 or greater means that the model expects batch requests, which can reduce overhead and speed up the inferencing process. If this parameter is not provided, the explainer will tune the record count per request according to the model container's capacity at runtime.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ProbabilityAttribute **   <a name="sagemaker-Type-ClarifyInferenceConfig-ProbabilityAttribute"></a>
A JMESPath expression used to extract the probability (or score) from the model container output if the model container is in JSON Lines format.
 **Example**: If the model container output of a single request is `'{"predicted_label":1,"probability":0.6}'`, then set `ProbabilityAttribute` to `'probability'`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** ProbabilityIndex **   <a name="sagemaker-Type-ClarifyInferenceConfig-ProbabilityIndex"></a>
A zero-based index used to extract a probability value (score) or list from model container output in CSV format. If this value is not provided, the entire model container output will be treated as a probability value (score) or list.
 **Example for a single class model:** If the model container output consists of a string-formatted prediction label followed by its probability: `'1,0.6'`, set `ProbabilityIndex` to `1` to select the probability value `0.6`.
 **Example for a multiclass model:** If the model container output consists of a string-formatted prediction label followed by its probability: `'"[\'cat\',\'dog\',\'fish\']","[0.1,0.6,0.3]"'`, set `ProbabilityIndex` to `1` to select the probability values `[0.1,0.6,0.3]`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ClarifyInferenceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClarifyInferenceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClarifyInferenceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClarifyInferenceConfig)
