---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_GetVirtualMachine.html
---

# GetVirtualMachine
<a name="API_GetVirtualMachine"></a>

By providing the ARN (Amazon Resource Name), this API returns the virtual machine.

## Request Syntax
<a name="API_GetVirtualMachine_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetVirtualMachine_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_GetVirtualMachine_RequestSyntax) **   <a name="bgw-GetVirtualMachine-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the virtual machine.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: Yes

## Response Syntax
<a name="API_GetVirtualMachine_ResponseSyntax"></a>

```
{
   "VirtualMachine": {
      "HostName": "string",
      "HypervisorId": "string",
      "LastBackupDate": number,
      "Name": "string",
      "Path": "string",
      "ResourceArn": "string",
      "VmwareTags": [
         {
            "VmwareCategory": "string",
            "VmwareTagDescription": "string",
            "VmwareTagName": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetVirtualMachine_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VirtualMachine](#API_GetVirtualMachine_ResponseSyntax) **   <a name="bgw-GetVirtualMachine-response-VirtualMachine"></a>
This object contains the basic attributes of `VirtualMachine` contained by the output of `GetVirtualMachine`
Type: [VirtualMachineDetails](API_VirtualMachineDetails.md) object

## Errors
<a name="API_GetVirtualMachine_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The operation did not succeed because an internal error occurred. Try again later.
 ** ErrorCode **
A description of which internal error occured.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A resource that is required for the action wasn't found.
 ** ErrorCode **
A description of which resource wasn't found.
HTTP Status Code: 400

 ** ThrottlingException **
TPS has been limited to protect against intentional or unintentional high request volumes.
 ** ErrorCode **
Error: TPS has been limited to protect against intentional or unintentional high request volumes.
HTTP Status Code: 400

 ** ValidationException **
The operation did not succeed because a validation error occurred.
 ** ErrorCode **
A description of what caused the validation error.
HTTP Status Code: 400

## See Also
<a name="API_GetVirtualMachine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-gateway-2021-01-01/GetVirtualMachine)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-gateway-2021-01-01/GetVirtualMachine)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/GetVirtualMachine)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-gateway-2021-01-01/GetVirtualMachine)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/GetVirtualMachine)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/GetVirtualMachine)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-gateway-2021-01-01/GetVirtualMachine)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-gateway-2021-01-01/GetVirtualMachine)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-gateway-2021-01-01/GetVirtualMachine)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/GetVirtualMachine)
