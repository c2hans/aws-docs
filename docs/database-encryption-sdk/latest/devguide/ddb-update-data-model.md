---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-update-data-model.html
---

# Updating your data model
<a name="ddb-update-data-model"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

When you configure the AWS Database Encryption SDK for DynamoDB, you provide [attribute actions](concepts.md#crypt-actions). On encrypt, AWS Database Encryption SDK uses the attribute actions to identify which attributes to encrypt and sign, which attributes to sign (but not encrypt), and which to ignore. You also define [allowed unsigned attributes](ddb-java-using.md#allowed-unauth) to explicitly tell the client which attributes are excluded from the signatures. On decrypt, the AWS Database Encryption SDK uses the allowed unsigned attributes that you defined to identify which attributes are not included in the signatures. Attribute actions are not saved in the encrypted item and the AWS Database Encryption SDK does not update your attribute actions automatically.

Choose your attribute actions carefully. When in doubt, use **Encrypt and sign**. After you have used the AWS Database Encryption SDK to protect your items, you cannot change an existing `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attribute to `DO_NOTHING`. However, you can safely make the following changes.
+ [Add new `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, and `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes](#ddb-add-auth-attribute)
+ [Remove existing attributes](#ddb-remove-attribute)
+ [Change an existing `ENCRYPT_AND_SIGN` attribute to `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`](#ddb-encrypt-to-sign)
+ [Change an existing `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attribute to `ENCRYPT_AND_SIGN`](#ddb-sign-to-encrypt)
+ [Add a new `DO_NOTHING` attribute](#ddb-add-unauth-attribute)
+ [Change an existing `SIGN_ONLY` attribute to `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`](#ddb-signOnly-to-signInclude)
+ [Change an existing `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attribute to `SIGN_ONLY`](#ddb-signInclude-to-signOnly)

**Considerations for searchable encryption**
Before you update your data model, carefully consider how your updates might impact any [beacons](beacons.md) you constructed from the attributes. After you have written new records with a beacon, you cannot update the beacon's configuration. You cannot update the attribute actions associated with the attributes you used to construct beacons. If you remove an existing attribute and its associated beacon, you will not be able to query existing records using that beacon. You can create new beacons for new fields that you add to your record, but you cannot update existing beacons to include the new field.

**Considerations for `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes**
By default, the partition and sort keys are the only attribute included in the encryption context. You might consider defining additional fields as `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` so that the branch key ID supplier for your [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md) can identify which branch key is required for decryption from the encryption context. For more information, see [branch key ID supplier](use-hierarchical-keyring.md#branch-key-id-supplier). If you specify any `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

**Note**
To use the `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` cryptographic action, you must use version 3.3 or later of the AWS Database Encryption SDK. Deploy the new version to all readers before [updating your data model](#ddb-update-data-model) to include `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

## Add new `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, and `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes
<a name="ddb-add-auth-attribute"></a>

To add a new `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attribute, define the new attribute in your attribute actions.

You cannot remove an existing `DO_NOTHING` attribute and add it back as an `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attribute.

**Using an annotated data class**
If you defined your attribute actions with a `TableSchema`, add the new attribute to your annotated data class. If you do not specify an attribute action annotation for the new attribute, the client will encrypt and sign the new attribute by default (unless the attribute is part of the primary key). If you only want to sign the new attribute, you must add the new attribute with the `@DynamoDbEncryptionSignOnly` or `@DynamoDbEncryptionSignAndIncludeInEncryptionContext` annotation.

**Using an object model**
If you manually defined your attribute actions, add the new attribute to the attribute actions in your object model and specify `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` as the attribute action.

## Remove existing attributes
<a name="ddb-remove-attribute"></a>

If you decide that you no longer need an attribute, you can stop writing data to that attribute or you can formally remove it from your attribute actions. When you stop writing new data to an attribute, the attribute still shows up in your attribute actions. This can be helpful if you need to start using the attribute again in the future. Formally removing the attribute from your attribute actions does not remove it from your dataset. Your dataset will still contain items that include that attribute.

To formally remove an existing `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`, or `DO_NOTHING` attribute, update your attribute actions.

If you remove a `DO_NOTHING` attribute, you must not remove that attribute from your [allowed unsigned attributes](ddb-java-using.md#allowed-unauth). Even if you are no longer writing new values to that attribute, the client still needs to know that the attribute is unsigned to read existing items that contain the attribute.

**Using an annotated data class**
If you defined your attribute actions with a `TableSchema`, remove the attribute from your annotated data class.

**Using an object model**
If you manually defined your attribute actions, remove the attribute from the attribute actions in your object model.

## Change an existing `ENCRYPT_AND_SIGN` attribute to `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`
<a name="ddb-encrypt-to-sign"></a>

To change an existing `ENCRYPT_AND_SIGN` attribute to `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`, you must update your attribute actions. After you deploy the update, the client will be able to verify and decrypt existing values written to the attribute, but will only sign new values written to the attribute.

**Note**
Carefully consider your security requirements before changing an existing `ENCRYPT_AND_SIGN` attribute to `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. Any attribute that can store sensitive data should be encrypted.

**Using an annotated data class**
If you defined your attribute actions with a `TableSchema`, update the existing attribute to include the `@DynamoDbEncryptionSignOnly` or `@DynamoDbEncryptionSignAndIncludeInEncryptionContext` annotation in your annotated data class.

**Using an object model**
If you manually defined your attribute actions, update the attribute action associated with the existing attribute from `ENCRYPT_AND_SIGN` to `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` in your object model.

## Change an existing `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attribute to `ENCRYPT_AND_SIGN`
<a name="ddb-sign-to-encrypt"></a>

To change an existing `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attribute to `ENCRYPT_AND_SIGN`, you must update your attribute actions. After you deploy the update, the client will be able to verify the existing values written to the attribute, and will encrypt and sign new values written to the attribute.

**Using an annotated data class**
If you defined your attribute actions with a `TableSchema`, remove the `@DynamoDbEncryptionSignOnly` or `@DynamoDbEncryptionSignAndIncludeInEncryptionContext` annotation from the existing attribute.

**Using an object model**
If you manually defined your attribute actions, update the attribute action associated with the attribute from `SIGN_ONLY` or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` to `ENCRYPT_AND_SIGN` in your object model.

## Add a new `DO_NOTHING` attribute
<a name="ddb-add-unauth-attribute"></a>

To reduce the risk of error when adding a new `DO_NOTHING` attribute, we recommend specifying a distinct prefix when naming your `DO_NOTHING` attributes, and then using that prefix to define your [allowed unsigned attributes](ddb-java-using.md#allowed-unauth).

You cannot remove an existing `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attribute from your annotated data class and then add the attribute back as a `DO_NOTHING` attribute. You can only add entirely new `DO_NOTHING` attributes.

The steps you take to add a new `DO_NOTHING` attribute depend on whether your defined your allowed unsigned attributes explicitly in a list or with a prefix.

**Using an allowed unsigned attributes prefix**
If you defined your attribute actions with a `TableSchema`, add the new `DO_NOTHING` attribute to your annotated data class with the `@DynamoDbEncryptionDoNothing` annotation. If you manually defined your attribute actions, update your attribute actions to include the new attribute. Be sure to explicitly configure the new attribute with the `DO_NOTHING` attribute action. You must include the same distinct prefix in the new attribute's name.

**Using an allowed unsigned attributes list**

1. Add the new `DO_NOTHING` attribute to your allowed unsigned attributes list and deploy the updated list.

1. Deploy the change from **Step 1**.

   You cannot move on to **Step 3** until the change has propagated to all hosts that need to read this data.

1. Add the new `DO_NOTHING` attribute to your attribute actions.

   1. If you defined your attribute actions with a `TableSchema`, add the new `DO_NOTHING` attribute to your annotated data class with the `@DynamoDbEncryptionDoNothing` annotation.

   1. If you manually defined your attribute actions, update your attribute actions to include the new attribute. Be sure to explicitly configure the new attribute with the `DO_NOTHING` attribute action.

1. Deploy the change from **Step 3**.

## Change an existing `SIGN_ONLY` attribute to `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`
<a name="ddb-signOnly-to-signInclude"></a>

To change an existing `SIGN_ONLY` attribute to `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`, you must update your attribute actions. After you deploy the update, the client will be able to verify the existing values written to the attribute, and will continue to sign new values written to the attribute. New values written to the attribute will be included in the [encryption context](concepts.md#encryption-context).

If you specify any `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attributes, then the partition and sort attributes must also be `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.

**Using an annotated data class**
If you defined your attribute actions with a `TableSchema`, update the attribute action associated with the attribute from `@DynamoDbEncryptionSignOnly` to `@DynamoDbEncryptionSignAndIncludeInEncryptionContext`.

**Using an object model**
If you manually defined your attribute actions, update the attribute action associated with the attribute from `SIGN_ONLY` to `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` in your object model.

## Change an existing `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attribute to `SIGN_ONLY`
<a name="ddb-signInclude-to-signOnly"></a>

To change an existing `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attribute to `SIGN_ONLY`, you must update your attribute actions. After you deploy the update, the client will be able to verify the existing values written to the attribute, and will continue to sign new values written to the attribute. New values written to the attribute will not be included in the [encryption context](concepts.md#encryption-context).

Before changing an existing `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` attribute to `SIGN_ONLY`, carefully consider how your updates might impact the functionality of your [branch key ID supplier](use-hierarchical-keyring.md#branch-key-id-supplier).

**Using an annotated data class**
If you defined your attribute actions with a `TableSchema`, update the attribute action associated with the attribute from `@DynamoDbEncryptionSignAndIncludeInEncryptionContext` to `@DynamoDbEncryptionSignOnly`.

**Using an object model**
If you manually defined your attribute actions, update the attribute action associated with the attribute from `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` to `SIGN_ONLY` in your object model.
