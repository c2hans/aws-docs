---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateQuantumTask.html
---

# CreateQuantumTask
<a name="API_CreateQuantumTask"></a>

Creates a quantum task.

## Request Syntax
<a name="API_CreateQuantumTask_RequestSyntax"></a>

```
POST /quantum-task HTTP/1.1
Content-type: application/json

{
   "action": "{{string}}",
   "associations": [
      {
         "arn": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "clientToken": "{{string}}",
   "deviceArn": "{{string}}",
   "deviceParameters": "{{string}}",
   "experimentalCapabilities": { ... },
   "jobToken": "{{string}}",
   "outputS3Bucket": "{{string}}",
   "outputS3KeyPrefix": "{{string}}",
   "shots": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateQuantumTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateQuantumTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_CreateQuantumTask_RequestSyntax) **   <a name="braket-CreateQuantumTask-request-action"></a>
The action associated with the quantum task.
Type: String
Required: Yes

 ** [associations](#API_CreateQuantumTask_RequestSyntax) **   <a name="braket-CreateQuantumTask-request-associations"></a>
The list of Amazon Braket resources associated with the quantum task.
Type: Array of [Association](API_Association.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [clientToken](#API_CreateQuantumTask_RequestSyntax) **   <a name="braket-CreateQuantumTask-request-clientToken"></a>
The client token associated with the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [deviceArn](#API_CreateQuantumTask_RequestSyntax) **   <a name="braket-CreateQuantumTask-request-deviceArn"></a>
The ARN of the device to run the quantum task on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [deviceParameters](#API_CreateQuantumTask_RequestSyntax) **   <a name="braket-CreateQuantumTask-request-deviceParameters"></a>
The parameters for the device to run the quantum task on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48000.
Required: No

 ** [experimentalCapabilities](#API_CreateQuantumTask_RequestSyntax) **   <a name="braket-CreateQuantumTask-request-experimentalCapabilities"></a>
Enable experimental capabilities for the quantum task.
Type: [ExperimentalCapabilities](API_ExperimentalCapabilities.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [jobToken](#API_CreateQuantumTask_RequestSyntax) **   <a name="braket-CreateQuantumTask-request-jobToken"></a>
The token for an Amazon Braket hybrid job that associates it with the quantum task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [outputS3Bucket](#API_CreateQuantumTask_RequestSyntax) **   <a name="braket-CreateQuantumTask-request-outputS3Bucket"></a>
The S3 bucket to store quantum task result files in.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** [outputS3KeyPrefix](#API_CreateQuantumTask_RequestSyntax) **   <a name="braket-CreateQuantumTask-request-outputS3KeyPrefix"></a>
The key prefix for the location in the S3 bucket to store quantum task results in. For example, `results/`. Must not contain path traversal sequences such as `../` or `./`. The following characters are not valid in the key prefix:
+ Braces (`{` or `}`)
+ Brackets (`[` or `]`)
+ Less than or greater than sign (`<` or `>`)
+ Backslash (`\`)
+ Vertical bar or pipe (`|`)
+ Caret or circumflex (`^`)
+ Tilde (`~`)
+ Grave accent or backtick (```)
+ Percent character (`%`)
+ Pound sign (`#`)
+ Quotation mark (`"`)
+ Non-printable ASCII characters (128–255 decimal characters)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [shots](#API_CreateQuantumTask_RequestSyntax) **   <a name="braket-CreateQuantumTask-request-shots"></a>
The number of shots to use for the quantum task.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** [tags](#API_CreateQuantumTask_RequestSyntax) **   <a name="braket-CreateQuantumTask-request-tags"></a>
Tags to be added to the quantum task you're creating.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateQuantumTask_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "quantumTaskArn": "string"
}
```

## Response Elements
<a name="API_CreateQuantumTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [quantumTaskArn](#API_CreateQuantumTask_ResponseSyntax) **   <a name="braket-CreateQuantumTask-response-quantumTaskArn"></a>
The ARN of the quantum task created by the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateQuantumTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DeviceOfflineException **
The specified device is currently offline.
HTTP Status Code: 424

 ** DeviceRetiredException **
The specified device has been retired.
HTTP Status Code: 410

 ** InternalServiceException **
The request failed because of an unknown error.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request failed because a service quota is exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The API throttling rate limit is exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input request failed to satisfy constraints expected by Amazon Braket.
 ** programSetValidationFailures **
The validation failures in the program set submitted in the request.
 ** reason **
The reason for validation failure.
HTTP Status Code: 400

## Examples
<a name="API_CreateQuantumTask_Examples"></a>

### OpenQASM 3.0 action example
<a name="API_CreateQuantumTask_Example_1"></a>

The following code is an example of the `action` parameter for creating an OpenQASM 3.0 quantum task.

```
{
  "braketSchemaHeader": {
    "name": "braket.ir.openqasm.program",
    "version": "1"
  },
  "source": "OPENQASM 3; qubit[2] q; bit[2] c; h q[0]; cnot q[0], q[1]; c = measure q;"
}
```

### ProgramSet action example
<a name="API_CreateQuantumTask_Example_2"></a>

The following code shows the `action` parameter for creating a `ProgramSet` quantum task with two programs: one with three sets of input parameters (theta and phi), and one with no input parameters.

```
{
    "braketSchemaHeader": {
        "name": "braket.ir.openqasm.program_set",
        "version": "1"
    },
    "programs": [
        {
            "braketSchemaHeader": {
                "name": "braket.ir.openqasm.program",
                "version": "1"
            },
            "source": "OPENQASM 3.0;\\ninput float phi;\\ninput float theta;\\nbit[2] b;\\nqubit[2] q;\\nrx(theta) q[0];\\ncnot q[0], q[1];\\nrz(phi) q[1];\\nb[0] = measure q[0];\\nb[1] = measure q[1];",
            "inputs": {
                "theta": [
                    1.23,
                    1.73,
                    0.73
                ],
                "phi": [
                    0.12,
                    -0.38,
                    0.62
                ]
            }
        },
        {
            "braketSchemaHeader": {
                "name": "braket.ir.openqasm.program",
                "version": "1"
            },
            "source": "OPENQASM 3.0;\\nbit[2] b;\\nqubit[2] q;\\nh q[0];\\ncnot q[0], q[1];\\nb[0] = measure q[0];\\nb[1] = measure q[1];",
            "inputs": {}
        }
    ]
}
```

## See Also
<a name="API_CreateQuantumTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/CreateQuantumTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/CreateQuantumTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/CreateQuantumTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/CreateQuantumTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/CreateQuantumTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/CreateQuantumTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/CreateQuantumTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/CreateQuantumTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/CreateQuantumTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/CreateQuantumTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
