---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetConnectionStatus.html
---

# GetConnectionStatus
<a name="API_GetConnectionStatus"></a>

Retrieves the Session Manager connection status for a managed node to determine whether it is running and ready to receive Session Manager connections.

## Request Syntax
<a name="API_GetConnectionStatus_RequestSyntax"></a>

```
{
   "Target": "{{string}}"
}
```

## Request Parameters
<a name="API_GetConnectionStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Target](#API_GetConnectionStatus_RequestSyntax) **   <a name="systemsmanager-GetConnectionStatus-request-Target"></a>
The managed node ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: Yes

## Response Syntax
<a name="API_GetConnectionStatus_ResponseSyntax"></a>

```
{
   "Status": "string",
   "Target": "string"
}
```

## Response Elements
<a name="API_GetConnectionStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_GetConnectionStatus_ResponseSyntax) **   <a name="systemsmanager-GetConnectionStatus-response-Status"></a>
The status of the connection to the managed node.
Type: String
Valid Values: `connected | notconnected`

 ** [Target](#API_GetConnectionStatus_ResponseSyntax) **   <a name="systemsmanager-GetConnectionStatus-response-Target"></a>
The ID of the managed node to check connection status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.

## Errors
<a name="API_GetConnectionStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_GetConnectionStatus_Examples"></a>

### Example
<a name="API_GetConnectionStatus_Example_1"></a>

This example illustrates one usage of GetConnectionStatus.

#### Sample Request
<a name="API_GetConnectionStatus_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetConnectionStatus
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240221T180655Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240221/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 33

{
    "Target": "i-02573cafcfEXAMPLE"
}
```

#### Sample Response
<a name="API_GetConnectionStatus_Example_1_Response"></a>

```
{
    "Status": "connected",
    "Target": "i-02573cafcfEXAMPLE"
}
```

## See Also
<a name="API_GetConnectionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetConnectionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetConnectionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetConnectionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetConnectionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetConnectionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetConnectionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetConnectionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetConnectionStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetConnectionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetConnectionStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
