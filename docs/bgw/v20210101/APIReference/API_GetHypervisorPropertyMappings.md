---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_GetHypervisorPropertyMappings.html
---

# GetHypervisorPropertyMappings
<a name="API_GetHypervisorPropertyMappings"></a>

This action retrieves the property mappings for the specified hypervisor. A hypervisor property mapping displays the relationship of entity properties available from the hypervisor to the properties available in AWS.

## Request Syntax
<a name="API_GetHypervisorPropertyMappings_RequestSyntax"></a>

```
{
   "HypervisorArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetHypervisorPropertyMappings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HypervisorArn](#API_GetHypervisorPropertyMappings_RequestSyntax) **   <a name="bgw-GetHypervisorPropertyMappings-request-HypervisorArn"></a>
The Amazon Resource Name (ARN) of the hypervisor.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: Yes

## Response Syntax
<a name="API_GetHypervisorPropertyMappings_ResponseSyntax"></a>

```
{
   "HypervisorArn": "string",
   "IamRoleArn": "string",
   "VmwareToAwsTagMappings": [
      {
         "AwsTagKey": "string",
         "AwsTagValue": "string",
         "VmwareCategory": "string",
         "VmwareTagName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetHypervisorPropertyMappings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HypervisorArn](#API_GetHypervisorPropertyMappings_ResponseSyntax) **   <a name="bgw-GetHypervisorPropertyMappings-response-HypervisorArn"></a>
The Amazon Resource Name (ARN) of the hypervisor.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

 ** [IamRoleArn](#API_GetHypervisorPropertyMappings_ResponseSyntax) **   <a name="bgw-GetHypervisorPropertyMappings-response-IamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::([0-9]+):role/(\S+)`

 ** [VmwareToAwsTagMappings](#API_GetHypervisorPropertyMappings_ResponseSyntax) **   <a name="bgw-GetHypervisorPropertyMappings-response-VmwareToAwsTagMappings"></a>
This is a display of the mappings of VMware tags to the AWS tags.
Type: Array of [VmwareToAwsTagMapping](API_VmwareToAwsTagMapping.md) objects

## Errors
<a name="API_GetHypervisorPropertyMappings_Errors"></a>

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
<a name="API_GetHypervisorPropertyMappings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-gateway-2021-01-01/GetHypervisorPropertyMappings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-gateway-2021-01-01/GetHypervisorPropertyMappings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/GetHypervisorPropertyMappings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-gateway-2021-01-01/GetHypervisorPropertyMappings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/GetHypervisorPropertyMappings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/GetHypervisorPropertyMappings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-gateway-2021-01-01/GetHypervisorPropertyMappings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-gateway-2021-01-01/GetHypervisorPropertyMappings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-gateway-2021-01-01/GetHypervisorPropertyMappings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/GetHypervisorPropertyMappings)
