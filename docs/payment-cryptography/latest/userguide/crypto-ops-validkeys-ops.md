---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html
---

# Valid keys for cryptographic operations
<a name="crypto-ops-validkeys-ops"></a>

Certain keys can only be used for certain operations. Additionally, some operations may limit the key modes of use for keys. Please see the following table for allowed combinations.

**Note**
Certain combinations, although permitted, may create unusable situations such as generating CVV codes `(generate)` but then unable to verify them `(verify)`.

**Topics**
+ [GenerateCardData](#w2aac15c31b9)
+ [VerifyCardData](#w2aac15c31c11)
+ [GeneratePinData (for VISA/ABA schemes)](#w2aac15c31c15)
+ [GeneratePinData (for `IBM3624`)](#w2aac15c31c17)
+ [VerifyPinData (for VISA/ABA schemes)](#w2aac15c31c21)
+ [VerifyPinData (for `IBM3624`)](#w2aac15c31c23)
+ [Decrypt Data](#w2aac15c31c27)
+ [Encrypt Data](#w2aac15c31c33)
+ [Translate Pin Data](#w2aac15c31c39)
+ [Generate/Verify MAC](#crypto-ops-validkeys.generatemac)
+ [GenerateMacEmvPinChange](#crypto-ops-validkeys.generatemacemvpinchange)
+ [VerifyAuthRequestCryptogram](#w2aac15c31c51)
+ [Import/Export Key](#crypto-ops-validkeys.importexport)
+ [Unused key types](#w2aac15c31c57)

## GenerateCardData
<a name="w2aac15c31b9"></a>

| API Endpoint | Cryptographic Operation or Algorithm | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- | --- |
| GenerateCardData |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | TR31\_C0\_CARD\_VERIFICATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | { Generate = true },{ Generate = true, Verify = true } |
| GenerateCardData |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | TR31\_C0\_CARD\_VERIFICATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | { Generate = true },{ Generate = true, Verify = true } |
| GenerateCardData |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | TR31\_E6\_EMV\_MKEY\_OTHER |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | { DeriveKey = true } |
| GenerateCardData |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | TR31\_E4\_EMV\_MKEY\_DYNAMIC\_NUMBERS |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | { DeriveKey = true } |
| GenerateCardData |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | TR31\_E6\_EMV\_MKEY\_OTHER |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | { DeriveKey = true } |

## VerifyCardData
<a name="w2aac15c31c11"></a>

| Cryptographic Operation or Algorithm | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | TR31\_C0\_CARD\_VERIFICATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | { Generate = true },{ Generate = true, Verify = true } |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | TR31\_C0\_CARD\_VERIFICATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | { Generate = true },{ Generate = true, Verify = true } |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | TR31\_E6\_EMV\_MKEY\_OTHER |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | { DeriveKey = true } |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | TR31\_E4\_EMV\_MKEY\_DYNAMIC\_NUMBERS |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | { DeriveKey = true } |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | TR31\_E6\_EMV\_MKEY\_OTHER |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | { DeriveKey = true } |

## GeneratePinData (for VISA/ABA schemes)
<a name="w2aac15c31c15"></a>

`VISA_PIN or VISA_PIN_VERIFICATION_VALUE`

| Key Type | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- |
| PIN Encryption Key | TR31\_P0\_PIN\_ENCRYPTION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| PIN Generation Key | TR31\_V2\_VISA\_PIN\_VERIFICATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |

## GeneratePinData (for `IBM3624`)
<a name="w2aac15c31c17"></a>

`IBM3624_PIN_OFFSET,IBM3624_NATURAL_PIN,IBM3624_RANDOM_PIN, IBM3624_PIN_FROM_OFFSET)`

| Key Type | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- |
| PIN Encryption Key | TR31\_P0\_PIN\_ENCRYPTION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | For IBM3624\_NATURAL\_PIN, IBM3624\_RANDOM\_PIN, IBM3624\_PIN\_FROM\_OFFSET[See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)<br />For IBM3624\_PIN\_OFFSET[See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| PIN Generation Key | TR31\_V1\_IBM3624\_PIN\_VERIFICATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |

## VerifyPinData (for VISA/ABA schemes)
<a name="w2aac15c31c21"></a>

`VISA_PIN`

| Key Type | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- |
| PIN Encryption Key | TR31\_P0\_PIN\_ENCRYPTION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| PIN Generation Key | TR31\_V2\_VISA\_PIN\_VERIFICATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |

## VerifyPinData (for `IBM3624`)
<a name="w2aac15c31c23"></a>

`IBM3624_PIN_OFFSET,IBM3624_NATURAL_PIN,IBM3624_RANDOM_PIN, IBM3624_PIN_FROM_OFFSET)`

| Key Type | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- |
| PIN Encryption Key | TR31\_P0\_PIN\_ENCRYPTION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | For IBM3624\_NATURAL\_PIN, IBM3624\_RANDOM\_PIN, IBM3624\_PIN\_FROM\_OFFSET[See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| PIN Verification Key | TR31\_V1\_IBM3624\_PIN\_VERIFICATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |

## Decrypt Data
<a name="w2aac15c31c27"></a>

| Key Type | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- |
| DUKPT | TR31\_B0\_BASE\_DERIVATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| EMV | TR31\_E1\_EMV\_MKEY\_CONFIDENTIALITY<br />TR31\_E6\_EMV\_MKEY\_OTHER |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |
| RSA | TR31\_D1\_ASYMMETRIC\_KEY\_FOR\_DATA\_ENCRYPTION |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| Symmetric keys | TR31\_D0\_SYMMETRIC\_DATA\_ENCRYPTION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |

## Encrypt Data
<a name="w2aac15c31c33"></a>

| Key Type | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- |
| DUKPT | TR31\_B0\_BASE\_DERIVATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| EMV | TR31\_E1\_EMV\_MKEY\_CONFIDENTIALITY<br />TR31\_E6\_EMV\_MKEY\_OTHER |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |
| RSA | TR31\_D1\_ASYMMETRIC\_KEY\_FOR\_DATA\_ENCRYPTION |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| Symmetric keys | TR31\_D0\_SYMMETRIC\_DATA\_ENCRYPTION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |

## Translate Pin Data
<a name="w2aac15c31c39"></a>

| Direction | Key Type | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- | --- |
| Inbound Data Source | DUKPT | TR31\_B0\_BASE\_DERIVATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| Inbound Data Source | non-DUKPT (PEK, AWK, IWK, etc) | TR31\_P0\_PIN\_ENCRYPTION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| Outbound Data Target | DUKPT | TR31\_B0\_BASE\_DERIVATION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| Outbound Data Target | non-DUKPT (PEK, IWK, AWK, etc) | TR31\_P0\_PIN\_ENCRYPTION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |

## Generate/Verify MAC
<a name="crypto-ops-validkeys.generatemac"></a>

 MAC keys are used for creating cryptographic hashes of a message/body of data. It is not recommended to create a key with limited key modes of use as you will be unable to perform the matching operation. However, you may import/export a key with only one operation if the other system is intended to perform the other half of the operation pair.

| Allowed Key Usage | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- |
| MAC Key  | TR31\_M1\_ISO\_9797\_1\_MAC\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| MAC Key (Retail MAC)  | TR31\_M1\_ISO\_9797\_3\_MAC\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| MAC Key (CMAC)  | TR31\_M6\_ISO\_9797\_5\_CMAC\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| MAC Key (HMAC)  | TR31\_M7\_HMAC\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| MAC Key (AS2805)  | TR31\_M0\_ISO\_16609\_MAC\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |

## GenerateMacEmvPinChange
<a name="crypto-ops-validkeys.generatemacemvpinchange"></a>

 GenerateMacEmvPinChange combines MAC generation and PIN encryption for EMV offline PIN change operations. This operation requires two different key types: an integrity key for MAC generation and a confidentiality key for PIN encryption.

| Key Type | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- |
| Secure Messaging Integrity Key  | TR31\_E2\_EMV\_MKEY\_INTEGRITY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| Secure Messaging Confidentiality Key  | TR31\_E1\_EMV\_MKEY\_CONFIDENTIALITY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| Current PIN PEK (PIN Encryption Key)  | TR31\_P0\_PIN\_ENCRYPTION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| New PIN PEK (PIN Encryption Key)  | TR31\_P0\_PIN\_ENCRYPTION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| ARQC Key  Only applies for Visa and Amex derivation schemes.  | TR31\_E0\_EMV\_MKEY\_APP\_CRYPTOGRAMS |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |

## VerifyAuthRequestCryptogram
<a name="w2aac15c31c51"></a>

| Allowed Key Usage | EMV Option | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- |
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  | TR31\_E0\_EMV\_MKEY\_APP\_CRYPTOGRAMS |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |

## Import/Export Key
<a name="crypto-ops-validkeys.importexport"></a>

| Operation Type | Allowed Key Usage | Allowed Key Algorithm | Allowed combination of key modes of use |
| --- | --- | --- | --- |
| TR-31 Wrapping Key | TR31\_K1\_KEY\_BLOCK\_PROTECTION\_KEY<br />TR31\_K0\_KEY\_ENCRYPTION\_KEY |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| Import of trusted CA | TR31\_S0\_ASYMMETRIC\_KEY\_FOR\_DIGITAL\_SIGNATURE |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| Import of public key certificate for asymmetric encryption | TR31\_D1\_ASYMMETRIC\_KEY\_FOR\_DATA\_ENCRYPTION |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |
| Key used to key agreement algorithms such as ECDH | TR31\_K3\_ASYMMETRIC\_KEY\_FOR\_KEY\_AGREEMENT |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) |

## Unused key types
<a name="w2aac15c31c57"></a>

The following key types are not currently used by AWS Payment Cryptography
+  TR31\_P1\_PIN\_GENERATION\_KEY
