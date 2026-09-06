---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/create-branch-keys.html
---

# Create an active branch key
<a name="create-branch-keys"></a>

A *branch key* is a data key derived from an AWS KMS key that the AWS KMS Hierarchical keyring uses to reduce the number of calls made to AWS KMS. The *active* branch key is the most recent branch key version. The Hierarchical keyring generates a unique data key for every encrypt request and encrypts each data key with a unique wrapping key derived from the active branch key.

To create a new active branch key, you must [statically configure](keystore-actions.md#static-keystore) your key store actions. `CreateKey` is a privileged operation that adds the KMS key ARN specified in your key store actions configuration to your key store allowlist. Then, the KMS key is used to generate the new active branch key. We recommend limiting access to this operation because once a KMS key is added to the key store, it cannot be deleted.

We recommend using the `CreateKey` operation through the KeyStore Admin interface in your application’s control plane. This approach aligns with best practices for key management.

Don’t create branch keys in the data plane. This practice can result in:
+ Unnecessary calls to AWS KMS
+ Multiple concurrent calls to AWS KMS in high-concurrency environments
+ Multiple TransactWriteItems calls to the backing DynamoDB table.

The `CreateKey` operation includes a condition check in the `TransactWriteItems` call to prevent overwriting existing branch keys. However, creating keys in the data plane can still lead to inefficient resource usage and potential performance issues.

You can allowlist one KMS key in your key store, or you can allowlist multiple KMS keys by updating the KMS key ARN that you specify in your key store actions configuration and calling `CreateKey` again. If you allowlist multiple KMS keys, your key store users should configure their key store actions for discovery so that they can use any of the allowlisted keys in the key store that they have access to. For more information, see [Configure key store actions](keystore-actions.md).

**Required permissions**
To create branch keys, you need [kms:GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) and [kms:ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html) permissions on the KMS key specified in your key store actions.

**Create a branch key**
The following operation creates a new active branch key using the KMS key that you[specified in your key store actions configuration](keystore-actions.md#static-keystore), and adds the active branch key to the DynamoDB table that serves as your key store.

When you call `CreateKey`, you can choose to specify the following optional values.
+ `branchKeyIdentifier`: defines a custom `branch-key-id`.

  To create a custom `branch-key-id`, you must also include an additional encryption context with the `encryptionContext` parameter.
+ `encryptionContext`: defines an optional set of non-secret key–value pairs that provides additional authenticated data (AAD) in the encryption context included in the [kms:GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) call.

  This additional encryption context is displayed with the `aws-crypto-ec:` prefix.

------
#### [ Java ]

```
final Map<String, String> {{additionalEncryptionContext}} = Collections.singletonMap("{{Additional Encryption Context for}}",
	         "{{custom branch key id}}");

	 final String BranchKey = keystore.CreateKey(
	         CreateKeyInput.builder()
	                 .branchKeyIdentifier({{custom-branch-key-id}}) //OPTIONAL
	                 .encryptionContext({{additionalEncryptionContext}}) //OPTIONAL
	                 .build()).branchKeyIdentifier();
```

------
#### [ C\# / .NET ]

```
var additionalEncryptionContext = new Dictionary<string, string>();
	 additionalEncryptionContext.Add("{{Additional Encryption Context for}}", "{{custom branch key id}}");

	 var branchKeyId = keystore.CreateKey(new CreateKeyInput
	 {
	     BranchKeyIdentifier = "{{custom-branch-key-id}}", // OPTIONAL
	     EncryptionContext = additionalEncryptionContext // OPTIONAL
	 });
```

------
#### [ Rust ]

```
let additional_encryption_context = HashMap::from([
    ("{{Additional Encryption Context for}}".to_string(), "{{custom branch key id}}".to_string())
]);

let branch_key_id = keystore.create_key()
    .branch_key_identifier("{{custom-branch-key-id}}") // OPTIONAL
    .encryption_context(additional_encryption_context) // OPTIONAL
    .send()
    .await?
    .branch_key_identifier
    .unwrap();
```

------

First, the `CreateKey` operation generates the following values.
+ A version 4 [Universally Unique Identifier](https://www.ietf.org/rfc/rfc4122.txt) (UUID) for the `branch-key-id` (unless you specified a custom `branch-key-id`).
+ A version 4 UUID for the branch key version
+ A `timestamp` in the [ISO 8601 date and time format](https://www.iso.org/iso-8601-date-and-time-format.html) in Coordinated Universal Time (UTC).

Then, the `CreateKey` operation calls [kms:GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) using the following request.

```
{
	    "EncryptionContext": {
	       "branch-key-id" : "{{branch-key-id}}",
	       "type" : "{{type}}",
	       "create-time" : "{{timestamp}}",
	       "tablename" : "{{the logical table name for your key store}}",
	       "kms-arn" : {{the KMS key ARN}},
	       "hierarchy-version" : "1",
	       "aws-crypto-ec:{{contextKey}}": "{{contextValue}}"
	    },
	    "KeyId": "{{the KMS key ARN you specified in your key store actions}}",
	    "NumberOfBytes": "32"
	 }
```

**Note**
The `CreateKey` operation creates an active branch key and a beacon key, even if you have not configured your database for [searchable encryption](searchable-encryption.md). Both keys are stored in your key store. For more information, see [Using the Hierarchical keyring for searchable encryption](use-hierarchical-keyring.md#searchable-encryption-hierarchical-keyrings).

Next, the `CreateKey` operation calls [kms:ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/AAPI_ReEncrypt.html) to create an active record for the branch key by updating the encryption context.

Last, the `CreateKey` operation calls [ddb:TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html) to write a new item that will persist the branch key in the table you created in **Step 2**. The item has the following attributes.

```
{
	     "branch-key-id" : {{branch-key-id}},
	     "type" : "branch:ACTIVE",
	     "enc" : {{the branch key returned by the GenerateDataKeyWithoutPlaintext call}},
	     "version": "branch:version:{{the branch key version UUID}}",
	     "create-time" : "{{timestamp}}",
	     "kms-arn" : "{{the KMS key ARN you specified in Step 1}}",
	     "hierarchy-version" : "1",
	     "aws-crypto-ec:{{contextKey}}": "{{contextValue}}"
 }
```
