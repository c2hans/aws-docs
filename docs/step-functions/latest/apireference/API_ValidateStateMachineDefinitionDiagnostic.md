---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ValidateStateMachineDefinitionDiagnostic.html
---

# ValidateStateMachineDefinitionDiagnostic
<a name="API_ValidateStateMachineDefinitionDiagnostic"></a>

Describes potential issues found during state machine validation. Rather than raise an exception, validation will return a list of **diagnostic elements** containing diagnostic information.

**Note**
The [ValidateStateMachineDefinitionlAPI](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ValidateStateMachineDefinition.html) might add new diagnostics in the future, adjust diagnostic codes, or change the message wording. Your automated processes should only rely on the value of the **result** field value (OK, FAIL). Do **not** rely on the exact order, count, or wording of diagnostic messages.

 **List of warning codes**

NO\_DOLLAR
No `.$` on a field that appears to be a JSONPath or Intrinsic Function.

NO\_PATH
Field value looks like a path, but field name does not end with 'Path'.

PASS\_RESULT\_IS\_STATIC
Attempt to use a path in the result of a pass state.

 **List of error codes**

INVALID\_JSON\_DESCRIPTION
JSON syntax problem found.

MISSING\_DESCRIPTION
Received a null or empty workflow input.

SCHEMA\_VALIDATION\_FAILED
Schema validation reported errors.

INVALID\_RESOURCE
The value of a Task-state resource field is invalid.

MISSING\_END\_STATE
The workflow does not have a terminal state.

DUPLICATE\_STATE\_NAME
The same state name appears more than once.

INVALID\_STATE\_NAME
The state name does not follow the naming convention.

STATE\_MACHINE\_NAME\_EMPTY
The state machine name has not been specified.

STATE\_MACHINE\_NAME\_INVALID
The state machine name does not follow the naming convention.

STATE\_MACHINE\_NAME\_TOO\_LONG
The state name exceeds the allowed length.

STATE\_MACHINE\_NAME\_ALREADY\_EXISTS
The state name already exists.

DUPLICATE\_LABEL\_NAME
A label name appears more than once.

INVALID\_LABEL\_NAME
You have provided an invalid label name.

MISSING\_TRANSITION\_TARGET
The value of "Next" field doesn't match a known state name.

TOO\_DEEPLY\_NESTED
The states are too deeply nested.

## Contents
<a name="API_ValidateStateMachineDefinitionDiagnostic_Contents"></a>

 ** code **   <a name="StepFunctions-Type-ValidateStateMachineDefinitionDiagnostic-code"></a>
Identifying code for the diagnostic.
Type: String
Required: Yes

 ** message **   <a name="StepFunctions-Type-ValidateStateMachineDefinitionDiagnostic-message"></a>
Message describing the diagnostic condition.
Type: String
Required: Yes

 ** severity **   <a name="StepFunctions-Type-ValidateStateMachineDefinitionDiagnostic-severity"></a>
A value of `ERROR` means that you cannot create or update a state machine with this definition.
 `WARNING` level diagnostics alert you to potential issues, but they will not prevent you from creating or updating your state machine.
Type: String
Valid Values: `ERROR | WARNING`
Required: Yes

 ** location **   <a name="StepFunctions-Type-ValidateStateMachineDefinitionDiagnostic-location"></a>
Location of the issue in the state machine, if available.
For errors specific to a field, the location could be in the format: `/States/<StateName>/<FieldName>`, for example: `/States/FailState/ErrorPath`.
Type: String
Required: No

## See Also
<a name="API_ValidateStateMachineDefinitionDiagnostic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ValidateStateMachineDefinitionDiagnostic)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ValidateStateMachineDefinitionDiagnostic)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ValidateStateMachineDefinitionDiagnostic)
