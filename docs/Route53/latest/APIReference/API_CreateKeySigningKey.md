---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateKeySigningKey.html
---

# CreateKeySigningKey
<a name="API_CreateKeySigningKey"></a>

Creates a new key-signing key (KSK) associated with a hosted zone. You can only have two KSKs per hosted zone.

## Request Syntax
<a name="API_CreateKeySigningKey_RequestSyntax"></a>

```
POST /2013-04-01/keysigningkey HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateKeySigningKeyRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <CallerReference>{{string}}</CallerReference>
   <HostedZoneId>{{string}}</HostedZoneId>
   <KeyManagementServiceArn>{{string}}</KeyManagementServiceArn>
   <Name>{{string}}</Name>
   <Status>{{string}}</Status>
</CreateKeySigningKeyRequest>
```

## URI Request Parameters
<a name="API_CreateKeySigningKey_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateKeySigningKey_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateKeySigningKeyRequest](#API_CreateKeySigningKey_RequestSyntax) **   <a name="Route53-CreateKeySigningKey-request-CreateKeySigningKeyRequest"></a>
Root level tag for the CreateKeySigningKeyRequest parameters.
Required: Yes

 ** [CallerReference](#API_CreateKeySigningKey_RequestSyntax) **   <a name="Route53-CreateKeySigningKey-request-CallerReference"></a>
A unique string that identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [HostedZoneId](#API_CreateKeySigningKey_RequestSyntax) **   <a name="Route53-CreateKeySigningKey-request-HostedZoneId"></a>
The unique string (ID) used to identify a hosted zone.
Type: String
Length Constraints: Maximum length of 32.
Required: Yes

 ** [KeyManagementServiceArn](#API_CreateKeySigningKey_RequestSyntax) **   <a name="Route53-CreateKeySigningKey-request-KeyManagementServiceArn"></a>
The Amazon resource name (ARN) for a customer managed key in AWS Key Management Service (AWS KMS). The `KeyManagementServiceArn` must be unique for each key-signing key (KSK) in a single hosted zone. To see an example of `KeyManagementServiceArn` that grants the correct permissions for DNSSEC, scroll down to **Example**.
You must configure the customer managed customer managed key as follows:
Status
Enabled
Key spec
ECC\_NIST\_P256
Key usage
Sign and verify
Key policy
The key policy must give permission for the following actions:
+ DescribeKey
+ GetPublicKey
+ Sign
The key policy must also include the Amazon Route 53 service in the principal for your account. Specify the following:
+  `"Service": "dnssec-route53.amazonaws.com"`
For more information about working with a customer managed key in AWS KMS, see [AWS Key Management Service concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html).
Type: String
Required: Yes

 ** [Name](#API_CreateKeySigningKey_RequestSyntax) **   <a name="Route53-CreateKeySigningKey-request-Name"></a>
A string used to identify a key-signing key (KSK). `Name` can include numbers, letters, and underscores (\_). `Name` must be unique for each key-signing key in the same hosted zone.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Required: Yes

 ** [Status](#API_CreateKeySigningKey_RequestSyntax) **   <a name="Route53-CreateKeySigningKey-request-Status"></a>
A string specifying the initial status of the key-signing key (KSK). You can set the value to `ACTIVE` or `INACTIVE`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 150.
Required: Yes

## Response Syntax
<a name="API_CreateKeySigningKey_ResponseSyntax"></a>

```
HTTP/1.1 201
Location: {{Location}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateKeySigningKeyResponse>
   <ChangeInfo>
      <Comment>string</Comment>
      <Id>string</Id>
      <Status>string</Status>
      <SubmittedAt>timestamp</SubmittedAt>
   </ChangeInfo>
   <KeySigningKey>
      <CreatedDate>timestamp</CreatedDate>
      <DigestAlgorithmMnemonic>string</DigestAlgorithmMnemonic>
      <DigestAlgorithmType>integer</DigestAlgorithmType>
      <DigestValue>string</DigestValue>
      <DNSKEYRecord>string</DNSKEYRecord>
      <DSRecord>string</DSRecord>
      <Flag>integer</Flag>
      <KeyTag>integer</KeyTag>
      <KmsArn>string</KmsArn>
      <LastModifiedDate>timestamp</LastModifiedDate>
      <Name>string</Name>
      <PublicKey>string</PublicKey>
      <SigningAlgorithmMnemonic>string</SigningAlgorithmMnemonic>
      <SigningAlgorithmType>integer</SigningAlgorithmType>
      <Status>string</Status>
      <StatusMessage>string</StatusMessage>
   </KeySigningKey>
</CreateKeySigningKeyResponse>
```

## Response Elements
<a name="API_CreateKeySigningKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The response returns the following HTTP headers.

 ** [Location](#API_CreateKeySigningKey_ResponseSyntax) **   <a name="Route53-CreateKeySigningKey-response-Location"></a>
The unique URL representing the new key-signing key (KSK).
Length Constraints: Maximum length of 1024.

The following data is returned in XML format by the service.

 ** [CreateKeySigningKeyResponse](#API_CreateKeySigningKey_ResponseSyntax) **   <a name="Route53-CreateKeySigningKey-response-CreateKeySigningKeyResponse"></a>
Root level tag for the CreateKeySigningKeyResponse parameters.
Required: Yes

 ** [ChangeInfo](#API_CreateKeySigningKey_ResponseSyntax) **   <a name="Route53-CreateKeySigningKey-response-ChangeInfo"></a>
A complex type that describes change information about changes made to your hosted zone.
Type: [ChangeInfo](API_ChangeInfo.md) object

 ** [KeySigningKey](#API_CreateKeySigningKey_ResponseSyntax) **   <a name="Route53-CreateKeySigningKey-response-KeySigningKey"></a>
The key-signing key (KSK) that the request creates.
Type: [KeySigningKey](API_KeySigningKey.md) object

## Errors
<a name="API_CreateKeySigningKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request.
 ** message **

HTTP Status Code: 400

 ** InvalidArgument **
Parameter name is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidKeySigningKeyName **
The key-signing key (KSK) name that you specified isn't a valid name.
HTTP Status Code: 400

 ** InvalidKeySigningKeyStatus **
The key-signing key (KSK) status isn't valid or another KSK has the status `INTERNAL_FAILURE`.
HTTP Status Code: 400

 ** InvalidKMSArn **
The KeyManagementServiceArn that you specified isn't valid to use with DNSSEC signing.
HTTP Status Code: 400

 ** InvalidSigningStatus **
Your hosted zone status isn't valid for this operation. In the hosted zone, change the status to enable `DNSSEC` or disable `DNSSEC`.
HTTP Status Code: 400

 ** KeySigningKeyAlreadyExists **
You've already created a key-signing key (KSK) with this name or with the same customer managed key ARN.
HTTP Status Code: 409

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

 ** TooManyKeySigningKeys **
You've reached the limit for the number of key-signing keys (KSKs). Remove at least one KSK, and then try again.
HTTP Status Code: 400

## Examples
<a name="API_CreateKeySigningKey_Examples"></a>

### KMSArn key policy example
<a name="API_CreateKeySigningKey_Example_1"></a>

The following is an example of a `KeyManagementServiceArn` key policy that grants the correct permissions for DNSSEC.

```
{
    "Version": "2012-10-17",
    "Id": "key-consolepolicy-3",
    "Statement": [
        {
            "Sid": "Allow use of the customer managed key for DNSSEC",
            "Effect": "Allow",
            "Principal": {
                "Service": "dnssec-route53.amazonaws.com"
            },
            "Action": [
                "kms:DescribeKey",
                "kms:GetPublicKey",
                "kms:Sign",
                "kms:Verify"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Allow full access for Key Administrators",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::1234567891234:role/admin"
            },
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

## See Also
<a name="API_CreateKeySigningKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/CreateKeySigningKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/CreateKeySigningKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CreateKeySigningKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/CreateKeySigningKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CreateKeySigningKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/CreateKeySigningKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/CreateKeySigningKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/CreateKeySigningKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/CreateKeySigningKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CreateKeySigningKey)
