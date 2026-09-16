---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_GetVersions.html
---

# GetVersions
<a name="API_GetVersions"></a>

Returns information about VCF versions, ESX versions and EC2 instance types provided by Amazon EVS. For each VCF version, the response also includes the default ESX version and provided EC2 instance types.

## Response Syntax
<a name="API_GetVersions_ResponseSyntax"></a>

```
{
   "instanceTypeEsxVersions": [
      {
         "esxVersions": [ "string" ],
         "instanceType": "string"
      }
   ],
   "vcfVersions": [
      {
         "defaultEsxVersion": "string",
         "instanceTypes": [ "string" ],
         "status": "string",
         "vcfVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instanceTypeEsxVersions](#API_GetVersions_ResponseSyntax) **   <a name="evs-GetVersions-response-instanceTypeEsxVersions"></a>
A list of EC2 instance types and their available ESX versions.
Type: Array of [InstanceTypeEsxVersionsInfo](API_InstanceTypeEsxVersionsInfo.md) objects

 ** [vcfVersions](#API_GetVersions_ResponseSyntax) **   <a name="evs-GetVersions-response-vcfVersions"></a>
A list of VCF versions with their availability status, default ESX version, and instance types.
Type: Array of [VcfVersionInfo](API_VcfVersionInfo.md) objects

## Errors
<a name="API_GetVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [InternalServerException](API_InternalServerException.md)
An internal server error occurred. Retry your request.
 ** message **
Describes the error encountered.
HTTP Status Code: 500

 [ThrottlingException](API_ThrottlingException.md)
The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.
 ** message **
Describes the error encountered.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 400

## See Also
<a name="API_GetVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/GetVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/GetVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/GetVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/GetVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/GetVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/GetVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/GetVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/GetVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/GetVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/GetVersions)
