---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_DeleteAgent.html
---

# DeleteAgent
<a name="API_DeleteAgent"></a>

Removes an AWS DataSync agent resource from your AWS account.

Keep in mind that this operation (which can't be undone) doesn't remove the agent's virtual machine (VM) or Amazon EC2 instance from your storage environment. For next steps, you can delete the VM or instance from your storage environment or reuse it to [activate a new agent](https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html).

## Request Syntax
<a name="API_DeleteAgent_RequestSyntax"></a>

```
{
   "AgentArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAgent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AgentArn](#API_DeleteAgent_RequestSyntax) **   <a name="DataSync-DeleteAgent-request-AgentArn"></a>
The Amazon Resource Name (ARN) of the agent to delete. Use the `ListAgents` operation to return a list of agents for your account and AWS Region.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`
Required: Yes

## Response Elements
<a name="API_DeleteAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAgent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/DeleteAgent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/DeleteAgent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/DeleteAgent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/DeleteAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/DeleteAgent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/DeleteAgent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/DeleteAgent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/DeleteAgent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/DeleteAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/DeleteAgent)
