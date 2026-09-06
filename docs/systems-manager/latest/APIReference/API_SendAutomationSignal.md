---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendAutomationSignal.html
---

# SendAutomationSignal
<a name="API_SendAutomationSignal"></a>

Sends a signal to an Automation execution to change the current behavior or status of the execution.

## Request Syntax
<a name="API_SendAutomationSignal_RequestSyntax"></a>

```
{
   "AutomationExecutionId": "{{string}}",
   "Payload": {
      "{{string}}" : [ "{{string}}" ]
   },
   "SignalType": "{{string}}"
}
```

## Request Parameters
<a name="API_SendAutomationSignal_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutomationExecutionId](#API_SendAutomationSignal_RequestSyntax) **   <a name="systemsmanager-SendAutomationSignal-request-AutomationExecutionId"></a>
The unique identifier for an existing Automation execution that you want to send the signal to.
Type: String
Length Constraints: Fixed length of 36.
Required: Yes

 ** [Payload](#API_SendAutomationSignal_RequestSyntax) **   <a name="systemsmanager-SendAutomationSignal-request-Payload"></a>
The data sent with the signal. The data schema depends on the type of signal used in the request.
For `Approve` and `Reject` signal types, the payload is an optional comment that you can send with the signal type. For example:
 `Comment="Looks good"`
For `StartStep` and `Resume` signal types, you must send the name of the Automation step to start or resume as the payload. For example:
 `StepName="step1"`
For the `StopStep` signal type, you must send the step execution ID as the payload. For example:
 `StepExecutionId="97fff367-fc5a-4299-aed8-0123456789ab"`
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [SignalType](#API_SendAutomationSignal_RequestSyntax) **   <a name="systemsmanager-SendAutomationSignal-request-SignalType"></a>
The type of signal to send to an Automation execution.
Type: String
Valid Values: `Approve | Reject | StartStep | StopStep | Resume | Revoke`
Required: Yes

## Response Elements
<a name="API_SendAutomationSignal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SendAutomationSignal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AutomationExecutionNotFoundException **
There is no automation execution information for the requested automation execution ID.
HTTP Status Code: 400

 ** AutomationStepNotFoundException **
The specified step name and execution ID don't exist. Verify the information and try again.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidAutomationSignalException **
The signal isn't valid for the current Automation execution.
HTTP Status Code: 400

## Examples
<a name="API_SendAutomationSignal_Examples"></a>

### Example
<a name="API_SendAutomationSignal_Example_1"></a>

This example illustrates one usage of SendAutomationSignal.

#### Sample Request
<a name="API_SendAutomationSignal_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.SendAutomationSignal
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T162449Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 165

{
    "AutomationExecutionId": "b2bc0e75-4d48-4b7b-be9b-0cb5cEXAMPLE",
    "SignalType": "StopStep",
    "Payload": {
        "StepExecutionId": [
            "33d93afd-9535-4dd5-a06b-c91bdEXAMPLE"
        ]
    }
}
```

#### Sample Response
<a name="API_SendAutomationSignal_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_SendAutomationSignal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/SendAutomationSignal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/SendAutomationSignal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/SendAutomationSignal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/SendAutomationSignal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/SendAutomationSignal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/SendAutomationSignal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/SendAutomationSignal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/SendAutomationSignal)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/SendAutomationSignal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/SendAutomationSignal)
