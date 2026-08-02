---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTpmEkPub.html
---

# GetInstanceTpmEkPub
<a name="API_GetInstanceTpmEkPub"></a>

Gets the public endorsement key associated with the Nitro Trusted Platform Module (NitroTPM) for the specified instance.

## Request Parameters
<a name="API_GetInstanceTpmEkPub_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Specify this parameter to verify whether the request will succeed, without actually making the request. If the request will succeed, the response is `DryRunOperation`. Otherwise, the response is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance for which to get the public endorsement key.
Type: String
Required: Yes

 **KeyFormat**
The required public endorsement key format. Specify `der` for a DER-encoded public key that is compatible with OpenSSL. Specify `tpmt` for a TPM 2.0 format that is compatible with tpm2-tools. The returned key is base64 encoded.
Type: String
Valid Values: `der | tpmt`
Required: Yes

 **KeyType**
The required public endorsement key type.
Type: String
Valid Values: `rsa-2048 | ecc-sec-p384`
Required: Yes

## Response Elements
<a name="API_GetInstanceTpmEkPub_ResponseElements"></a>

The following elements are returned by the service.

 **instanceId**
The ID of the instance.
Type: String

 **keyFormat**
The public endorsement key format.
Type: String
Valid Values: `der | tpmt`

 **keyType**
The public endorsement key type.
Type: String
Valid Values: `rsa-2048 | ecc-sec-p384`

 **keyValue**
The public endorsement key material.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetInstanceTpmEkPub_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetInstanceTpmEkPub_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetInstanceTpmEkPub)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetInstanceTpmEkPub)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetInstanceTpmEkPub)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetInstanceTpmEkPub)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetInstanceTpmEkPub)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetInstanceTpmEkPub)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetInstanceTpmEkPub)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetInstanceTpmEkPub)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetInstanceTpmEkPub)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetInstanceTpmEkPub)
