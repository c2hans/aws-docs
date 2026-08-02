---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-v3-attributes-interpreting.html
---

# PKCS \#11 library attributes table for AWS CloudHSM Client SDK 3
<a name="pkcs11-v3-attributes-interpreting"></a>

The PKCS \#11 library table for AWS CloudHSM Client SDK 3 contains a list of attributes that differ by key types. It indicates whether a given attribute is supported for a particular key type when using a specific cryptographic function with AWS CloudHSM.

**Legend:**
+ ✔ indicates that CloudHSM supports the attribute for the specific key type.
+ ✖ indicates that CloudHSM does not support the attribute for the specific key type.
+ R indicates that the attribute value is set to read-only for the specific key type.
+ S indicates that the attribute cannot be read by the `GetAttributeValue` as it is sensitive.
+ An empty cell in the Default Value column indicates that there is no specific default value assigned to the attribute.

## GenerateKeyPair
<a name="pkcs11-v3-generatekeypair"></a>

<table>
<thead>
  <tr><th>Attribute</th><th colspan="4">Key Type</th><th>**Default Value**</th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td>**EC private**</td><td>**EC public**</td><td>**RSA private**</td><td>**RSA public**</td><td> </td><td></td></tr>
  <tr><td>`CKA_CLASS`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_KEY_TYPE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_LABEL`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_ID`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_LOCAL`</td><td>R</td><td>R</td><td>R</td><td>R</td><td>True</td><td></td></tr>
  <tr><td>`CKA_TOKEN`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_PRIVATE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>True</td><td></td></tr>
  <tr><td>`CKA_ENCRYPT`</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_DECRYPT`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_DERIVE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_MODIFIABLE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>True</td><td></td></tr>
  <tr><td>`CKA_DESTROYABLE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_SIGN`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_SIGN_RECOVER`</td><td>✖</td><td>✖</td><td>✔[3](#pkcs11-v3-f10)</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VERIFY`</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_VERIFY_RECOVER`</td><td>✖</td><td>✖</td><td>✖</td><td>✔[4](#pkcs11-v3-f11)</td><td> </td><td></td></tr>
  <tr><td>`CKA_WRAP`</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_WRAP_TEMPLATE`</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td> </td><td></td></tr>
  <tr><td>`CKA_TRUSTED`</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_WRAP_WITH_TRUSTED`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_UNWRAP`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_UNWRAP_TEMPLATE`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_SENSITIVE`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>True</td><td></td></tr>
  <tr><td>`CKA_ALWAYS_SENSITIVE`</td><td>R</td><td>✖</td><td>R</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXTRACTABLE`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>True</td><td></td></tr>
  <tr><td>`CKA_NEVER_EXTRACTABLE`</td><td>R</td><td>✖</td><td>R</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_MODULUS`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_MODULUS_BITS`</td><td>✖</td><td>✖</td><td>✖</td><td> ✔[2](#pkcs11-v3-f9)</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIME_1`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIME_2`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_COEFFICIENT`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXPONENT_1`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXPONENT_2`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIVATE_EXPONENT`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PUBLIC_EXPONENT`</td><td>✖</td><td>✖</td><td>✖</td><td>✔[2](#pkcs11-v3-f9)</td><td> </td><td></td></tr>
  <tr><td>`CKA_EC_PARAMS`</td><td>✖</td><td>✔[2](#pkcs11-v3-f9)</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EC_POINT`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VALUE`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VALUE_LEN`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_CHECK_VALUE`</td><td>R</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
</tbody>
</table>

## GenerateKey
<a name="pkcs11-v3-generatekey"></a>

<table>
<thead>
  <tr><th>Attribute</th><th colspan="3">Key Type</th><th>**Default Value**</th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td>**AES**</td><td>**DES3**</td><td>**Generic Secret**</td><td> </td><td></td></tr>
  <tr><td>`CKA_CLASS`</td><td>✔ </td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_KEY_TYPE`</td><td>✔ </td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_LABEL`</td><td>✔ </td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_ID`</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_LOCAL`</td><td>R </td><td>R</td><td>R</td><td>True</td><td></td></tr>
  <tr><td>`CKA_TOKEN`</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_PRIVATE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>True</td><td></td></tr>
  <tr><td>`CKA_ENCRYPT`</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_DECRYPT`</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_DERIVE`</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_MODIFIABLE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>True</td><td></td></tr>
  <tr><td>`CKA_DESTROYABLE`</td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_SIGN`</td><td>✔ </td><td>✔</td><td>✔</td><td>True </td><td></td></tr>
  <tr><td>`CKA_SIGN_RECOVER`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VERIFY`</td><td>✔ </td><td>✔</td><td>✔</td><td>True </td><td></td></tr>
  <tr><td>`CKA_VERIFY_RECOVER`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_WRAP`</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_WRAP_TEMPLATE`</td><td>✔ </td><td>✔</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_TRUSTED`</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_WRAP_WITH_TRUSTED`</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_UNWRAP`</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_UNWRAP_TEMPLATE`</td><td>✔ </td><td>✔</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_SENSITIVE`</td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_ALWAYS_SENSITIVE`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXTRACTABLE`</td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_NEVER_EXTRACTABLE`</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td>`CKA_MODULUS`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_MODULUS_BITS`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIME_1`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIME_2`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_COEFFICIENT`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXPONENT_1`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXPONENT_2`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIVATE_EXPONENT`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PUBLIC_EXPONENT`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EC_PARAMS`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EC_POINT`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VALUE`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VALUE_LEN`</td><td>✔[2](#pkcs11-v3-f9)</td><td>✖</td><td>✔[2](#pkcs11-v3-f9)</td><td> </td><td></td></tr>
  <tr><td>`CKA_CHECK_VALUE`</td><td>R </td><td>R</td><td>R</td><td> </td><td></td></tr>
</tbody>
</table>

## CreateObject
<a name="pkcs11-v3-createobject"></a>

<table>
<thead>
  <tr><th>Attribute</th><th colspan="7">Key Type</th><th>**Default Value**</th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td>**EC private**</td><td>**EC public**</td><td>**RSA private**</td><td>**RSA public**</td><td>**AES**</td><td>**DES3**</td><td>**Generic Secret**</td><td> </td><td></td></tr>
  <tr><td>`CKA_CLASS`</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td></td><td></td></tr>
  <tr><td>`CKA_KEY_TYPE`</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td></td><td></td></tr>
  <tr><td>`CKA_LABEL`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_ID`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_LOCAL`</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>False</td><td></td></tr>
  <tr><td>`CKA_TOKEN`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_PRIVATE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>True</td><td></td></tr>
  <tr><td>`CKA_ENCRYPT`</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_DECRYPT`</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_DERIVE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_MODIFIABLE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>True</td><td></td></tr>
  <tr><td>`CKA_DESTROYABLE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_SIGN`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_SIGN_RECOVER`</td><td>✖</td><td>✖</td><td>✔[3](#pkcs11-v3-f10)</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_VERIFY`</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_VERIFY_RECOVER`</td><td>✖</td><td>✖</td><td>✖</td><td>✔[4](#pkcs11-v3-f11)</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_WRAP`</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_WRAP_TEMPLATE`</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔ </td><td>✔</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_TRUSTED`</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_WRAP_WITH_TRUSTED`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_UNWRAP`</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_UNWRAP_TEMPLATE`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_SENSITIVE`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_ALWAYS_SENSITIVE`</td><td>R</td><td>✖</td><td>R</td><td>✖</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXTRACTABLE`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_NEVER_EXTRACTABLE`</td><td>R</td><td>✖</td><td>R</td><td>✖</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td>`CKA_MODULUS`</td><td>✖</td><td>✖</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_MODULUS_BITS`</td><td>✖</td><td>✖</td><td>✖</td><td> ✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIME_1`</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIME_2`</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_COEFFICIENT`</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXPONENT_1`</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXPONENT_2`</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIVATE_EXPONENT`</td><td>✖</td><td>✖</td><td>✔[2](#pkcs11-v3-f9)</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PUBLIC_EXPONENT`</td><td>✖</td><td>✖</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EC_PARAMS`</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EC_POINT`</td><td>✖</td><td>✔[2](#pkcs11-v3-f9)</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VALUE`</td><td>✔[2](#pkcs11-v3-f9)</td><td>✖</td><td>✖</td><td>✖</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td> </td><td></td></tr>
  <tr><td>`CKA_VALUE_LEN`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_CHECK_VALUE`</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
</tbody>
</table>

## UnwrapKey
<a name="pkcs11-v3-unwrapkey"></a>

<table>
<thead>
  <tr><th>Attribute</th><th colspan="5">Key Type</th><th>**Default Value**</th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td>**EC private**</td><td>**RSA private**</td><td>**AES**</td><td>**DES3**</td><td>**Generic Secret**</td><td> </td><td></td></tr>
  <tr><td>`CKA_CLASS`</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td></td><td></td></tr>
  <tr><td>`CKA_KEY_TYPE`</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td></td><td></td></tr>
  <tr><td>`CKA_LABEL`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_ID`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_LOCAL`</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>False</td><td></td></tr>
  <tr><td>`CKA_TOKEN`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_PRIVATE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>True</td><td></td></tr>
  <tr><td>`CKA_ENCRYPT`</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_DECRYPT`</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_DERIVE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_MODIFIABLE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>True</td><td></td></tr>
  <tr><td>`CKA_DESTROYABLE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_SIGN`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_SIGN_RECOVER`</td><td>✖</td><td>✔[3](#pkcs11-v3-f10)</td><td>✖</td><td>✖</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_VERIFY`</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_VERIFY_RECOVER`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_WRAP`</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_UNWRAP`</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_SENSITIVE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_EXTRACTABLE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_NEVER_EXTRACTABLE`</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td>`CKA_ALWAYS_SENSITIVE`</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td>`CKA_MODULUS`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_MODULUS_BITS`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIME_1`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIME_2`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_COEFFICIENT`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXPONENT_1`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXPONENT_2`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIVATE_EXPONENT`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PUBLIC_EXPONENT`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EC_PARAMS`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EC_POINT`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VALUE`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VALUE_LEN`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_CHECK_VALUE`</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
</tbody>
</table>

## DeriveKey
<a name="pkcs11-v3-derivekey"></a>

<table>
<thead>
  <tr><th>Attribute</th><th colspan="3">Key Type</th><th>**Default Value**</th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td>**AES**</td><td>**DES3**</td><td>**Generic Secret**</td><td> </td><td></td></tr>
  <tr><td>`CKA_CLASS`</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td></td><td></td></tr>
  <tr><td>`CKA_KEY_TYPE`</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td></td><td></td></tr>
  <tr><td>`CKA_LABEL`</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_ID`</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>`CKA_LOCAL`</td><td>R</td><td>R</td><td>R</td><td>True</td><td></td></tr>
  <tr><td>`CKA_TOKEN`</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_PRIVATE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>True</td><td></td></tr>
  <tr><td>`CKA_ENCRYPT`</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_DECRYPT`</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_DERIVE`</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_MODIFIABLE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>True</td><td></td></tr>
  <tr><td>`CKA_DESTROYABLE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>True</td><td></td></tr>
  <tr><td>`CKA_SIGN`</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_SIGN_RECOVER`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VERIFY`</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td>`CKA_VERIFY_RECOVER`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_WRAP`</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_UNWRAP`</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td>`CKA_SENSITIVE`</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_EXTRACTABLE`</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td>`CKA_NEVER_EXTRACTABLE`</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td>`CKA_ALWAYS_SENSITIVE`</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td>`CKA_MODULUS`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_MODULUS_BITS`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIME_1`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIME_2`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_COEFFICIENT`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXPONENT_1`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EXPONENT_2`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PRIVATE_EXPONENT`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_PUBLIC_EXPONENT`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EC_PARAMS`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_EC_POINT`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VALUE`</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td>`CKA_VALUE_LEN`</td><td>✔[2](#pkcs11-v3-f9)</td><td>✖</td><td>✔[2](#pkcs11-v3-f9)</td><td> </td><td></td></tr>
  <tr><td>`CKA_CHECK_VALUE`</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
</tbody>
</table>

## GetAttributeValue
<a name="pkcs11-v3-getattributevalue"></a>

<table>
<thead>
  <tr><th>Attribute</th><th colspan="7">Key Type</th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td>**EC private**</td><td>**EC public**</td><td>**RSA private**</td><td>**RSA public**</td><td>**AES**</td><td>**DES3**</td><td>**Generic Secret**</td><td></td></tr>
  <tr><td>`CKA_CLASS`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_KEY_TYPE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_LABEL`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_ID`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_LOCAL`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_TOKEN`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_PRIVATE`</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td>✔[1](#pkcs11-v3-f8)</td><td></td></tr>
  <tr><td>`CKA_ENCRYPT`</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_DECRYPT`</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_DERIVE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_MODIFIABLE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_DESTROYABLE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_SIGN`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_SIGN_RECOVER`</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_VERIFY`</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_VERIFY_RECOVER`</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_WRAP`</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_WRAP_TEMPLATE`</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_TRUSTED`</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_WRAP_WITH_TRUSTED`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_UNWRAP`</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_UNWRAP_TEMPLATE`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_SENSITIVE`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_EXTRACTABLE`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_NEVER_EXTRACTABLE`</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_ALWAYS_SENSITIVE`</td><td>R</td><td>R;</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td></td></tr>
  <tr><td>`CKA_MODULUS`</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_MODULUS_BITS`</td><td>✖</td><td>✖</td><td>✖</td><td> ✔</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_PRIME_1`</td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_PRIME_2`</td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_COEFFICIENT`</td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_EXPONENT_1`</td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_EXPONENT_2`</td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_PRIVATE_EXPONENT`</td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_PUBLIC_EXPONENT`</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_EC_PARAMS`</td><td>✔</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_EC_POINT`</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td>`CKA_VALUE`</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td>✔[2](#pkcs11-v3-f9)</td><td></td></tr>
  <tr><td>`CKA_VALUE_LEN`</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td></td></tr>
  <tr><td>`CKA_CHECK_VALUE`</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
</tbody>
</table>

**Attribute annotations**
+ [1] This attribute is partially supported by the firmware and must be explicitly set only to the default value.
+ [2] Mandatory attribute.
+ [3] **Client SDK 3 only**. The `CKA_SIGN_RECOVER` attribute is derived from the `CKA_SIGN` attribute. If being set, it can only be set to the same value that is set for `CKA_SIGN`. If not set, it derives the default value of `CKA_SIGN`. Since CloudHSM only supports RSA-based recoverable signature mechanisms, this attribute is currently applicable to RSA public keys only.
+ [4] **Client SDK 3 only**. The `CKA_VERIFY_RECOVER` attribute is derived from the `CKA_VERIFY` attribute. If being set, it can only be set to the same value that is set for `CKA_VERIFY`. If not set, it derives the default value of `CKA_VERIFY`. Since CloudHSM only supports RSA-based recoverable signature mechanisms, this attribute is currently applicable to RSA public keys only.
