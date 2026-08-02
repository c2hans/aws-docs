---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ValidateStateMachineDefinition.html
---

# ValidateStateMachineDefinition
<a name="API_ValidateStateMachineDefinition"></a>

Validates the syntax of a state machine definition specified in [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) (ASL), a JSON-based, structured language.

You can validate that a state machine definition is correct without creating a state machine resource.

Suggested uses for `ValidateStateMachineDefinition`:
+ Integrate automated checks into your code review or Continuous Integration (CI) process to check state machine definitions before starting deployments.
+ Run validation from a Git pre-commit hook to verify the definition before committing to your source repository.

Validation will look for problems in your state machine definition and return a **result** and a list of **diagnostic elements**.

The **result** value will be `OK` when your workflow definition can be successfully created or updated. Note the result can be `OK` even when diagnostic warnings are present in the response. The **result** value will be `FAIL` when the workflow definition contains errors that would prevent you from creating or updating your state machine.

The list of [ValidateStateMachineDefinitionDiagnostic](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ValidateStateMachineDefinitionDiagnostic.html) data elements can contain zero or more **WARNING** and/or **ERROR** elements.

**Note**
The **ValidateStateMachineDefinition API** might add new diagnostics in the future, adjust diagnostic codes, or change the message wording. Your automated processes should only rely on the value of the **result** field value (OK, FAIL). Do **not** rely on the exact order, count, or wording of diagnostic messages.

## Request Syntax
<a name="API_ValidateStateMachineDefinition_RequestSyntax"></a>

```
{
   "definition": "{{string}}",
   "maxResults": {{number}},
   "severity": "{{string}}",
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_ValidateStateMachineDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [definition](#API_ValidateStateMachineDefinition_RequestSyntax) **   <a name="StepFunctions-ValidateStateMachineDefinition-request-definition"></a>
The Amazon States Language definition of the state machine. For more information, see [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) (ASL).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: Yes

 ** [maxResults](#API_ValidateStateMachineDefinition_RequestSyntax) **   <a name="StepFunctions-ValidateStateMachineDefinition-request-maxResults"></a>
The maximum number of diagnostics that are returned per call. The default and maximum value is 100. Setting the value to 0 will also use the default of 100.
If the number of diagnostics returned in the response exceeds `maxResults`, the value of the `truncated` field in the response will be set to `true`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [severity](#API_ValidateStateMachineDefinition_RequestSyntax) **   <a name="StepFunctions-ValidateStateMachineDefinition-request-severity"></a>
Minimum level of diagnostics to return. `ERROR` returns only `ERROR` diagnostics, whereas `WARNING` returns both `WARNING` and `ERROR` diagnostics. The default is `ERROR`.
Type: String
Valid Values: `ERROR | WARNING`
Required: No

 ** [type](#API_ValidateStateMachineDefinition_RequestSyntax) **   <a name="StepFunctions-ValidateStateMachineDefinition-request-type"></a>
The target type of state machine for this definition. The default is `STANDARD`.
Type: String
Valid Values: `STANDARD | EXPRESS`
Required: No

## Response Syntax
<a name="API_ValidateStateMachineDefinition_ResponseSyntax"></a>

```
{
   "diagnostics": [
      {
         "code": "string",
         "location": "string",
         "message": "string",
         "severity": "string"
      }
   ],
   "result": "string",
   "truncated": boolean
}
```

## Response Elements
<a name="API_ValidateStateMachineDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [diagnostics](#API_ValidateStateMachineDefinition_ResponseSyntax) **   <a name="StepFunctions-ValidateStateMachineDefinition-response-diagnostics"></a>
An array of diagnostic errors and warnings found during validation of the state machine definition. Since **warnings** do not prevent deploying your workflow definition, the **result** value could be `OK` even when warning diagnostics are present in the response.
Type: Array of [ValidateStateMachineDefinitionDiagnostic](API_ValidateStateMachineDefinitionDiagnostic.md) objects

 ** [result](#API_ValidateStateMachineDefinition_ResponseSyntax) **   <a name="StepFunctions-ValidateStateMachineDefinition-response-result"></a>
The result value will be `OK` when no syntax errors are found, or `FAIL` if the workflow definition does not pass verification.
Type: String
Valid Values: `OK | FAIL`

 ** [truncated](#API_ValidateStateMachineDefinition_ResponseSyntax) **   <a name="StepFunctions-ValidateStateMachineDefinition-response-truncated"></a>
The result value will be `true` if the number of diagnostics found in the workflow definition exceeds `maxResults`. When all diagnostics results are returned, the value will be `false`.
Type: Boolean

## Errors
<a name="API_ValidateStateMachineDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_ValidateStateMachineDefinition_Examples"></a>

### Validate an inline state machine definition
<a name="API_ValidateStateMachineDefinition_Example_1"></a>

The following example shows how to invoke the API from the CLI:

```
aws stepfunctions validate-state-machine-definition \
    --definition '{"StartAt":"WaitState","States":{"WaitState":{"Type":"Wait","Seconds":5,"End":true}}}' \
    --type 'STANDARD'
```

### Validate a state machine definition from a file
<a name="API_ValidateStateMachineDefinition_Example_2"></a>

If your state machine definition is saved in a JSON file, you can use the `file://` notation to pass the file contents to the API.

```
aws stepfunctions validate-state-machine-definition \
    --definition file://my-state-machine-definition.asl.json
```

### Parse the validation result
<a name="API_ValidateStateMachineDefinition_Example_3"></a>

On POSIX compliant systems, you can use a command-line utility like grep to parse the output and generate a non-zero return code if the definition did not successfully pass the syntax check:

```
aws stepfunctions validate-state-machine-definition \
    --definition file://my-state-machine-definition.asl.json | grep '"result": "OK"'
```

### Validate a state machine definition with static analysis
<a name="API_ValidateStateMachineDefinition_Example_4"></a>

By setting the **severity level** to `WARNING`, you can gain visibility into potential issues with your definition before deploying your state machine. In the following example, the four `WARNING` level diagnostics alert you to potential issues, but they will not prevent you from creating or updating your state machine. Any diagnostic results with `ERROR` level severity will prevent you from deploying the state machine.

Example results with static analysis warnings:

```
$ aws stepfunctions validate-state-machine-definition \
                    --definition file://my-workflow-definition.asl.json \
                    --severity WARNING
```

```
{
    "result": "OK",
    "diagnostics": [
        {
            "severity": "WARNING",
            "code": "NO_DOLLAR",
            "message": "The value of 'a' looks like a JSONPath. Instead of 'a', use 'a.$' to evaluate it as a JSONPath at runtime.",
            "location": "/States/HelloWorld/Parameters"
        },
        {
            "severity": "WARNING",
            "code": "PASS_RESULT_IS_STATIC",
            "message": "The value of 'c.$' will not evaluate as a JSONPath or Intrinsic Function at runtime. Instead of 'Result', use 'Parameters' to evaluate it as a JSONPath or Intrinsic Function at runtime.",
            "location": "/States/HelloWorld/Result"
        },
        {
            "severity": "WARNING",
            "code": "NO_PATH",
            "message": "The value of 'Error' looks like a JSONPath. Instead of 'Error', use 'ErrorPath' to evaluate it as a JSONPath at runtime.",
            "location": "/States/FailState/Error"
        },
        {
            "severity": "WARNING",
            "code": "NO_PATH",
            "message": "The value of 'Cause' looks like a JSONPath. Instead of 'Cause', use 'CausePath' to evaluate it as a JSONPath at runtime.",
            "location": "/States/FailState/Cause"
        }
    ],
    "truncated": false
}
```

## See Also
<a name="API_ValidateStateMachineDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/ValidateStateMachineDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/ValidateStateMachineDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ValidateStateMachineDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/ValidateStateMachineDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ValidateStateMachineDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/ValidateStateMachineDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/ValidateStateMachineDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/ValidateStateMachineDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/ValidateStateMachineDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ValidateStateMachineDefinition)
