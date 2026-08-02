---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_ValidationException.html
---

# ValidationException
<a name="API_ValidationException"></a>

The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.

HTTP Status Code returned: 400

## Contents
<a name="API_ValidationException_Contents"></a>

 ** message **   <a name="evs-Type-ValidationException-message"></a>
Describes the error encountered.
Type: String
Required: Yes

 ** reason **   <a name="evs-Type-ValidationException-reason"></a>
The reason for the exception.
Type: String
Valid Values: `unknownOperation | cannotParse | fieldValidationFailed | other`
Required: Yes

 ** fieldList **   <a name="evs-Type-ValidationException-fieldList"></a>
A list of fields that didn't validate.
Type: Array of [ValidationExceptionField](API_ValidationExceptionField.md) objects
Required: No

## See Also
<a name="API_ValidationException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/ValidationException)
