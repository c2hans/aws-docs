---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ValidationException.html
---

# ValidationException
<a name="API_ValidationException"></a>

The input parameters for the request are invalid.

HTTP Status Code returned: 400

## Contents
<a name="API_ValidationException_Contents"></a>

 ** message **   <a name="novaact-Type-ValidationException-message"></a>
The input fails to satisfy the constraints specified by the service.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** reason **   <a name="novaact-Type-ValidationException-reason"></a>
The reason for the validation failure.
Type: String
Valid Values: `FieldValidationFailed | InvalidStatus | GuardrailIntervened`
Required: Yes

 ** fieldList **   <a name="novaact-Type-ValidationException-fieldList"></a>
The list of fields that failed validation.
Type: Array of [ValidationExceptionField](API_ValidationExceptionField.md) objects
Required: No

## See Also
<a name="API_ValidationException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ValidationException)
