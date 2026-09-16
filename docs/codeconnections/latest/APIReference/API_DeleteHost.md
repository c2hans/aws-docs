---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteHost.html
---

# DeleteHost
<a name="API_DeleteHost"></a>

The host to be deleted. Before you delete a host, all connections associated to the host must be deleted.

**Note**
A host cannot be deleted if it is in the VPC\_CONFIG\_INITIALIZING or VPC\_CONFIG\_DELETING state.

## Request Syntax
<a name="API_DeleteHost_RequestSyntax"></a>

```
{
   "HostArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteHost_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HostArn](#API_DeleteHost_RequestSyntax) **   <a name="codeconnections-DeleteHost-request-HostArn"></a>
The Amazon Resource Name (ARN) of the host to be deleted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:(codestar-connections|codeconnections):.+:[0-9]{12}:host\/.+`
Required: Yes

## Response Elements
<a name="API_DeleteHost_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteHost_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found. Verify the connection resource ARN and try again.
HTTP Status Code: 400

 ** ResourceUnavailableException **
Resource not found. Verify the ARN for the host resource and try again.
HTTP Status Code: 400

## See Also
<a name="API_DeleteHost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/DeleteHost)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/DeleteHost)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/DeleteHost)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/DeleteHost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/DeleteHost)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/DeleteHost)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/DeleteHost)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/DeleteHost)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/DeleteHost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/DeleteHost)
