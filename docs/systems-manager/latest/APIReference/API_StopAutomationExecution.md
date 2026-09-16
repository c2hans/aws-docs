---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StopAutomationExecution.html
---

# StopAutomationExecution
<a name="API_StopAutomationExecution"></a>

Stop an Automation that is currently running.

## Request Syntax
<a name="API_StopAutomationExecution_RequestSyntax"></a>

```
{
   "AutomationExecutionId": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_StopAutomationExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutomationExecutionId](#API_StopAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StopAutomationExecution-request-AutomationExecutionId"></a>
The execution ID of the Automation to stop.
Type: String
Length Constraints: Fixed length of 36.
Required: Yes

 ** [Type](#API_StopAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StopAutomationExecution-request-Type"></a>
The stop request type. Valid types include the following: Cancel and Complete. The default type is Cancel.
Type: String
Valid Values: `Complete | Cancel`
Required: No

## Response Elements
<a name="API_StopAutomationExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopAutomationExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AutomationExecutionNotFoundException **
There is no automation execution information for the requested automation execution ID.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidAutomationStatusUpdateException **
The specified update status operation isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_StopAutomationExecution_Examples"></a>

### Example
<a name="API_StopAutomationExecution_Example_1"></a>

This example illustrates one usage of StopAutomationExecution.

#### Sample Request
<a name="API_StopAutomationExecution_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.StopAutomationExecution
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T171100Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 65

{
    "AutomationExecutionId": "f7d1f82d-6cde-4f7a-aa53-d485bEXAMPLE"
}
```

#### Sample Response
<a name="API_StopAutomationExecution_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_StopAutomationExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/StopAutomationExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/StopAutomationExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/StopAutomationExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/StopAutomationExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/StopAutomationExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/StopAutomationExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/StopAutomationExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/StopAutomationExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/StopAutomationExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/StopAutomationExecution)
