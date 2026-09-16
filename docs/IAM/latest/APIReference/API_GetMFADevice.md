---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetMFADevice.html
---

# GetMFADevice
<a name="API_GetMFADevice"></a>

Retrieves information about an MFA device for a specified user.

## Request Parameters
<a name="API_GetMFADevice_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SerialNumber **
Serial number that uniquely identifies the MFA device. For this API, we only accept FIDO security key [ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html).
Type: String
Length Constraints: Minimum length of 9. Maximum length of 256.
Pattern: `[\w+=/:,.@-]+`
Required: Yes

 ** UserName **
The friendly name identifying the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: No

## Response Elements
<a name="API_GetMFADevice_ResponseElements"></a>

The following elements are returned by the service.

 **Certifications** Certifications.entry.N.key (key)Certifications.entry.N.value (value)
The certifications of a specified user's MFA device. We currently provide FIPS-140-2, FIPS-140-3, and FIDO certification levels obtained from [ FIDO Alliance Metadata Service (MDS)](https://fidoalliance.org/metadata/).
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\u0020-\u00FF]+`
Value Length Constraints: Minimum length of 1. Maximum length of 32.
Value Pattern: `[\u0020-\u00FF]+`

 ** EnableDate **
The date that a specified user's MFA device was first enabled.
Type: Timestamp

 ** SerialNumber **
Serial number that uniquely identifies the MFA device. For this API, we only accept FIDO security key [ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html).
Type: String
Length Constraints: Minimum length of 9. Maximum length of 256.
Pattern: `[\w+=/:,.@-]+`

 ** UserName **
The friendly name identifying the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`

## Errors
<a name="API_GetMFADevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetMFADevice_Examples"></a>

### Example
<a name="API_GetMFADevice_Example_1"></a>

This example illustrates one usage of GetMFADevice.

#### Sample Request
<a name="API_GetMFADevice_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetMFADevice
&SerialNumber=arn:aws:iam::123456789012:u2f/root/testFidoKey-R1234
&UserName=Bob
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetMFADevice_Example_1_Response"></a>

```
<GetMFADeviceResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetMFADeviceResult>
    <EnableDate>2023-04-27T20:58:13Z</EnableDate>
    <SerialNumber>arn:aws:iam::123456789012:u2f/root/testFidoKey-R1234</SerialNumber>
    <Certifications>
      <entry>
        <key>FIDO-FIPS-140-2</key>
        <value>L2</value>
      </entry>
      <entry>
        <key>FIDO</key>
        <value>L1</value>
      </entry>
    </Certifications>
    <UserName>Bob</UserName>
  </GetMFADeviceResult>
  <ResponseMetadata>
    <RequestId>df37e965-9967-11e1-a4c3-270EXAMPLE04</RequestId>
  </ResponseMetadata>
</GetMFADeviceResponse>
```

## See Also
<a name="API_GetMFADevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetMFADevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetMFADevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetMFADevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetMFADevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetMFADevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetMFADevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetMFADevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetMFADevice)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetMFADevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetMFADevice)
