---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/DDB-encrypted-and-signed.html
---

# Which fields are encrypted and signed?
<a name="DDB-encrypted-and-signed"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

The AWS Database Encryption SDK for DynamoDB is a client-side encryption library designed especially for Amazon DynamoDB applications. Amazon DynamoDB stores data in [tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.TablesItemsAttributes), which are a collection of items. Each *item* is a collection of *attributes*. Each attribute has a name and a value. The AWS Database Encryption SDK for DynamoDB encrypts the values of attributes. Then, it calculates a signature over the attributes. You can specify which attribute values to encrypt and which to include in the signature.

Encryption protects the confidentiality of the attribute value. Signing provides integrity of all signed attributes and their relationship to each other, and provides authentication. It enables you to detect unauthorized changes to the item as a whole, including adding or deleting attributes, or substituting one encrypted value for another.

In an encrypted item, some data remains in plaintext, including the table name, all attribute names, the attribute values that you don't encrypt, the names and values of the primary key (partition key and sort key) attributes, and the attribute types. Do not store sensitive data in these fields.

For more information on how the AWS Database Encryption SDK for DynamoDB works, see [How the AWS Database Encryption SDK works](how-it-works.md).

**Note**
All mentions of *attribute actions* in the AWS Database Encryption SDK for DynamoDB topics refer to [cryptographic actions](concepts.md#crypt-actions).

**Topics**
+ [Encrypting attribute values](#encrypt-attribute-values)
+ [Signing the item](#sign-the-item)

## Encrypting attribute values
<a name="encrypt-attribute-values"></a>

The AWS Database Encryption SDK for DynamoDB encrypts the values (but not the attribute name or type) of the attributes that you specify. To determine which attribute values are encrypted, use [attribute actions](concepts.md#crypt-actions).

For example, this item includes `example` and `test` attributes.

```
'example': 'data',
'test': 'test-value',
...
```

If you encrypt the `example` attribute, but don't encrypt the `test` attribute, the results look like the following. The encrypted `example` attribute value is binary data, instead of a string.

```
'example': Binary(b"'b\x933\x9a+s\xf1\xd6a\xc5\xd5\x1aZ\xed\xd6\xce\xe9X\xf0T\xcb\x9fY\x9f\xf3\xc9C\x83\r\xbb\\"),
'test': 'test-value'
...
```

The primary key attributes—partition key and sort key—of each item must remain in plaintext because DynamoDB uses them to find the item in the table. They should be signed, but not encrypted.

The AWS Database Encryption SDK for DynamoDB identifies the primary key attributes for you and ensures that their values are signed, but not encrypted. And, if you identify your primary key and then try to encrypt it, the client will throw an exception.

The client stores the [material description](concepts.md#material-description) in a new attribute (`aws_dbe_head`) that it adds to the item. The material description describes how the item was encrypted and signed. The client uses this information to verify and decrypt the item. The field that stores the material description is not encrypted.

## Signing the item
<a name="sign-the-item"></a>

After encrypting the specified attribute values, the AWS Database Encryption SDK for DynamoDB calculates Hash-Based Message Authentication Codes (HMACs) and a [digital signature](concepts.md#digital-sigs) over the canonicalization of the material description, [encryption context](concepts.md#encryption-context), and each field marked `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` in the [attribute actions](concepts.md#crypt-actions). ECDSA signatures are enabled by default, but are not required. The client stores the HMACs and signatures in a new attribute (`aws_dbe_foot`) that it adds to the item.
