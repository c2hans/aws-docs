---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchProperties.html
---

# DescribePatchProperties
<a name="API_DescribePatchProperties"></a>

Lists the properties of available patches organized by product, product family, classification, severity, and other properties of available patches. You can use the reported properties in the filters you specify in requests for operations such as [CreatePatchBaseline](API_CreatePatchBaseline.md), [UpdatePatchBaseline](API_UpdatePatchBaseline.md), [DescribeAvailablePatches](API_DescribeAvailablePatches.md), and [DescribePatchBaselines](API_DescribePatchBaselines.md).

The following section lists the properties that can be used in filters for each major operating system type:

AMAZON\_LINUX
Valid properties: `PRODUCT` \| `CLASSIFICATION` \| `SEVERITY`

AMAZON\_LINUX\_2
Valid properties: `PRODUCT` \| `CLASSIFICATION` \| `SEVERITY`

AMAZON\_LINUX\_2023
Valid properties: `PRODUCT` \| `CLASSIFICATION` \| `SEVERITY`

CENTOS
Valid properties: `PRODUCT` \| `CLASSIFICATION` \| `SEVERITY`

DEBIAN
Valid properties: `PRODUCT` \| `PRIORITY`

MACOS
Valid properties: `PRODUCT` \| `CLASSIFICATION`

ORACLE\_LINUX
Valid properties: `PRODUCT` \| `CLASSIFICATION` \| `SEVERITY`

REDHAT\_ENTERPRISE\_LINUX
Valid properties: `PRODUCT` \| `CLASSIFICATION` \| `SEVERITY`

SUSE
Valid properties: `PRODUCT` \| `CLASSIFICATION` \| `SEVERITY`

UBUNTU
Valid properties: `PRODUCT` \| `PRIORITY`

WINDOWS
Valid properties: `PRODUCT` \| `PRODUCT_FAMILY` \| `CLASSIFICATION` \| `MSRC_SEVERITY`

## Request Syntax
<a name="API_DescribePatchProperties_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OperatingSystem": "{{string}}",
   "PatchSet": "{{string}}",
   "Property": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePatchProperties_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribePatchProperties_RequestSyntax) **   <a name="systemsmanager-DescribePatchProperties-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribePatchProperties_RequestSyntax) **   <a name="systemsmanager-DescribePatchProperties-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [OperatingSystem](#API_DescribePatchProperties_RequestSyntax) **   <a name="systemsmanager-DescribePatchProperties-request-OperatingSystem"></a>
The operating system type for which to list patches.
Type: String
Valid Values: `WINDOWS | AMAZON_LINUX | AMAZON_LINUX_2 | AMAZON_LINUX_2022 | UBUNTU | REDHAT_ENTERPRISE_LINUX | SUSE | CENTOS | ORACLE_LINUX | DEBIAN | MACOS | RASPBIAN | ROCKY_LINUX | ALMA_LINUX | AMAZON_LINUX_2023`
Required: Yes

 ** [PatchSet](#API_DescribePatchProperties_RequestSyntax) **   <a name="systemsmanager-DescribePatchProperties-request-PatchSet"></a>
Indicates whether to list patches for the Windows operating system or for applications released by Microsoft. Not applicable for the Linux or macOS operating systems.
Type: String
Valid Values: `OS | APPLICATION`
Required: No

 ** [Property](#API_DescribePatchProperties_RequestSyntax) **   <a name="systemsmanager-DescribePatchProperties-request-Property"></a>
The patch property for which you want to view patch details.
Type: String
Valid Values: `PRODUCT | PRODUCT_FAMILY | CLASSIFICATION | MSRC_SEVERITY | PRIORITY | SEVERITY`
Required: Yes

## Response Syntax
<a name="API_DescribePatchProperties_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Properties": [
      {
         "string" : "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribePatchProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribePatchProperties_ResponseSyntax) **   <a name="systemsmanager-DescribePatchProperties-response-NextToken"></a>
The token for the next set of items to return. (You use this token in the next call.)
Type: String

 ** [Properties](#API_DescribePatchProperties_ResponseSyntax) **   <a name="systemsmanager-DescribePatchProperties-response-Properties"></a>
A list of the properties for patches matching the filter request parameters.
Type: Array of string to string maps
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 0. Maximum length of 4096.

## Errors
<a name="API_DescribePatchProperties_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribePatchProperties_Examples"></a>

### Example
<a name="API_DescribePatchProperties_Example_1"></a>

This example illustrates one usage of DescribePatchProperties.

#### Sample Request
<a name="API_DescribePatchProperties_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 95
X-Amz-Target: AmazonSSM.DescribePatchProperties
X-Amz-Date: 20240312T010204Z
User-Agent: aws-cli/1.16.96 Python/2.7.15 Windows/10 botocore/1.12.86
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240312/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "OperatingSystem": "Windows",
    "Property": "PRODUCT",
    "PatchSet": "OS"
}
```

#### Sample Response
<a name="API_DescribePatchProperties_Example_1_Response"></a>

```
{
    "Properties": [
        {
            "Name": "WindowsServer2012",
            "ProductFamily": "Windows"
        },
        {
            "Name": "WindowsServer2012R2",
            "ProductFamily": "Windows"
        },
        {
            "Name": "WindowsServer2016",
            "ProductFamily": "Windows"
        },
        {
            "Name": "WindowsServer2019",
            "ProductFamily": "Windows"
        }
    ]
}
```

## See Also
<a name="API_DescribePatchProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribePatchProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribePatchProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribePatchProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribePatchProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribePatchProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribePatchProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribePatchProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribePatchProperties)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribePatchProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribePatchProperties)
