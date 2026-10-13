---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_Datum.html
---

# Datum
<a name="API_training_session_runtime_Datum"></a>

A single training datum containing model input and optional loss function inputs.

## Contents
<a name="API_training_session_runtime_Datum_Contents"></a>

 ** modelInput **   <a name="sagemaker-Type-training_session_runtime_Datum-modelInput"></a>
The tokenized input to feed to the model.
Type: [ModelInput](API_training_session_runtime_ModelInput.md) object
Required: Yes

 ** lossFnInputs **   <a name="sagemaker-Type-training_session_runtime_Datum-lossFnInputs"></a>
The tensor inputs for the loss function, keyed by name. Unsupported keys are rejected. Supported keys: `target_tokens`, `weights`, `advantages`, `logprobs`, `ref_log_prob`, `temperature`. Required keys depend on the loss function type: SFT (`cross_entropy`) requires `target_tokens` and `weights`; RL (`ppo`, `cispo`, `importance_sampling`) requires `target_tokens`, `weights`, `advantages`, and `logprobs`.
Type: String to [TensorData](API_training_session_runtime_TensorData.md) object map
Required: No

## See Also
<a name="API_training_session_runtime_Datum_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/Datum)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/Datum)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/Datum)
