---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeyRotations.html
---

# ListKeyRotations
<a name="API_ListKeyRotations"></a>

Returns information about the key materials associated with the specified KMS key. You can use the optional `IncludeKeyMaterial` parameter to control which key materials are included in the response.

You must specify the KMS key in all requests. You can refine the key rotations list by limiting the number of rotations returned.

For detailed information about automatic and on-demand key rotations, see [Rotate AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: No. You cannot perform this operation on a KMS key in a different AWS account.

 **Required permissions**: [kms:ListKeyRotations](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [EnableKeyRotation](API_EnableKeyRotation.md)
+  [DeleteImportedKeyMaterial](API_DeleteImportedKeyMaterial.md)
+  [DisableKeyRotation](API_DisableKeyRotation.md)
+  [GetKeyRotationStatus](API_GetKeyRotationStatus.md)
+  [ImportKeyMaterial](API_ImportKeyMaterial.md)
+  [RotateKeyOnDemand](API_RotateKeyOnDemand.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_ListKeyRotations_RequestSyntax"></a>

```
{
   "IncludeKeyMaterial": "{{string}}",
   "KeyId": "{{string}}",
   "Limit": {{number}},
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListKeyRotations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_ListKeyRotations_RequestSyntax) **   <a name="KMS-ListKeyRotations-request-KeyId"></a>
Gets the key rotations for the specified KMS key.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [IncludeKeyMaterial](#API_ListKeyRotations_RequestSyntax) **   <a name="KMS-ListKeyRotations-request-IncludeKeyMaterial"></a>
Use this optional parameter to control which key materials associated with this key are listed in the response. The default value of this parameter is `ROTATIONS_ONLY`. If you omit this parameter, AWS KMS returns information on the key materials created by automatic or on-demand key rotation. When you specify a value of `ALL_KEY_MATERIAL`, AWS KMS adds the first key material and any imported key material pending rotation to the response. This parameter can only be used with KMS keys that support automatic or on-demand key rotation.
Type: String
Valid Values: `ALL_KEY_MATERIAL | ROTATIONS_ONLY`
Required: No

 ** [Limit](#API_ListKeyRotations_RequestSyntax) **   <a name="KMS-ListKeyRotations-request-Limit"></a>
Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [Marker](#API_ListKeyRotations_RequestSyntax) **   <a name="KMS-ListKeyRotations-request-Marker"></a>
Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of `NextMarker` from the truncated response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`
Required: No

## Response Syntax
<a name="API_ListKeyRotations_ResponseSyntax"></a>

```
{
   "NextMarker": "string",
   "Rotations": [
      {
         "ExpirationModel": "string",
         "ImportState": "string",
         "KeyId": "string",
         "KeyMaterialDescription": "string",
         "KeyMaterialId": "string",
         "KeyMaterialState": "string",
         "RotationDate": number,
         "RotationType": "string",
         "ValidTo": number
      }
   ],
   "Truncated": boolean
}
```

## Response Elements
<a name="API_ListKeyRotations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextMarker](#API_ListKeyRotations_ResponseSyntax) **   <a name="KMS-ListKeyRotations-response-NextMarker"></a>
When `Truncated` is true, this element is present and contains the value to use for the `Marker` parameter in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`

 ** [Rotations](#API_ListKeyRotations_ResponseSyntax) **   <a name="KMS-ListKeyRotations-response-Rotations"></a>
A list of completed key material rotations. When the optional input parameter `IncludeKeyMaterial` is specified with a value of `ALL_KEY_MATERIAL`, this list includes the first key material and any imported key material pending rotation.
Type: Array of [RotationsListEntry](API_RotationsListEntry.md) objects

 ** [Truncated](#API_ListKeyRotations_ResponseSyntax) **   <a name="KMS-ListKeyRotations-response-Truncated"></a>
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the `NextMarker` element in this response to the `Marker` parameter in a subsequent request.
Type: Boolean

## Errors
<a name="API_ListKeyRotations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.
HTTP Status Code: 400

 ** InvalidMarkerException **
The request was rejected because the marker that specifies where pagination should next begin is not valid.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** KMSInvalidStateException **
The request was rejected because the state of the specified resource is not valid for this request.
This exceptions means one of the following:
+ The key state of the KMS key is not compatible with the operation.

  To find the key state, use the [DescribeKey](API_DescribeKey.md) operation. For more information about which key states are compatible with each AWS KMS operation, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * * AWS Key Management Service Developer Guide* *.
+ For cryptographic operations on KMS keys in custom key stores, this exception represents a general failure with many possible causes. To identify the cause, see the error message that accompanies the exception.
HTTP Status Code: 400

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## Examples
<a name="API_ListKeyRotations_Examples"></a>

### Example Request
<a name="API_ListKeyRotations_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 48
X-Amz-Target: TrentService.ListKeyRotations
X-Amz-Date: 20240405T151426Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161107/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=4783e177036ca78627fe0cda9dcfdaf4ad7c8312d0e7c3d71d814b0c4cff1c0b

{"KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"}
```

### Example Response
<a name="API_ListKeyRotations_Example_2"></a>

This example illustrates one usage of ListKeyRotations.

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 05 Apr 2024 15:14:26 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Connection: keep-alive
x-amzn-RequestId: 2077c3bf-a538-11e6-b6fb-794e83344f84

{
    "Rotations": [
        {
          "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
          "KeyMaterialId": "0b7fd7ddbac6eef27907413567cad8c810e2883dc8a7534067a82ee1142fc1e6",
          "KeyMaterialType": "NON_CURRENT",
          "RotationDate": "2024-03-02T10:11:36.564000+00:00",
          "RotationType": "AUTOMATIC"
        },
        {
          "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
          "KeyMaterialId": "2067e8b4da7b0d8ffa80ff7afb5ea4637e103c98c3c110bdb84cc0a9de75e733",
          "KeyMaterialType": "CURRENT",
          "RotationDate":  "2024-04-05T15:14:47.757000+00:00",
          "RotationType": "ON_DEMAND"
        }
    ],
  "Truncated": false
}
```

## See Also
<a name="API_ListKeyRotations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/ListKeyRotations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/ListKeyRotations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/ListKeyRotations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/ListKeyRotations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/ListKeyRotations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/ListKeyRotations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/ListKeyRotations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/ListKeyRotations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/ListKeyRotations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/ListKeyRotations)
