---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteParameters.html
---

# DeleteParameters
<a name="API_DeleteParameters"></a>

Delete a list of parameters. After deleting a parameter, wait for at least 30 seconds to create a parameter with the same name.

## Request Syntax
<a name="API_DeleteParameters_RequestSyntax"></a>

```
{
   "Names": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DeleteParameters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Names](#API_DeleteParameters_RequestSyntax) **   <a name="systemsmanager-DeleteParameters-request-Names"></a>
The names of the parameters to delete. After deleting a parameter, wait for at least 30 seconds to create a parameter with the same name.
You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_DeleteParameters_ResponseSyntax"></a>

```
{
   "DeletedParameters": [ "string" ],
   "InvalidParameters": [ "string" ]
}
```

## Response Elements
<a name="API_DeleteParameters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletedParameters](#API_DeleteParameters_ResponseSyntax) **   <a name="systemsmanager-DeleteParameters-response-DeletedParameters"></a>
The names of the deleted parameters.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [InvalidParameters](#API_DeleteParameters_ResponseSyntax) **   <a name="systemsmanager-DeleteParameters-response-InvalidParameters"></a>
The names of parameters that weren't deleted because the parameters aren't valid.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_DeleteParameters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DeleteParameters_Examples"></a>

### Example
<a name="API_DeleteParameters_Example_1"></a>

This example illustrates one usage of DeleteParameters.

#### Sample Request
<a name="API_DeleteParameters_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 53
X-Amz-Target: AmazonSSM.DeleteParameters
X-Amz-Date: 20240316T010844Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240316/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Names": [
        "EC2TestServerType",
        "EC2ProdServerType"
    ]
}
```

#### Sample Response
<a name="API_DeleteParameters_Example_1_Response"></a>

```
{
    "DeletedParameters": [
        "EC2ProdServerType",
        "EC2TestServerType"
    ],
    "InvalidParameters": []
}
```

## See Also
<a name="API_DeleteParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeleteParameters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeleteParameters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeleteParameters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeleteParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteParameters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeleteParameters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeleteParameters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeleteParameters)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeleteParameters)
