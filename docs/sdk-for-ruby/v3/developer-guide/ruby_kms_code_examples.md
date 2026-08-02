---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/ruby_kms_code_examples.html
---

# AWS KMS examples using SDK for Ruby
<a name="ruby_kms_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Ruby with AWS KMS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `CreateKey`
<a name="kms_CreateKey_ruby_topic"></a>

The following code example shows how to use `CreateKey`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/kms#code-examples).

```
require 'aws-sdk-kms' # v2: require 'aws-sdk'

# Create a AWS KMS key.
# As long we are only encrypting small amounts of data (4 KiB or less) directly,
# a KMS key is fine for our purposes.
# For larger amounts of data,
# use the KMS key to encrypt a data encryption key (DEK).

client = Aws::KMS::Client.new

resp = client.create_key({
                           tags: [
                             {
                               tag_key: 'CreatedBy',
                               tag_value: 'ExampleUser'
                             }
                           ]
                         })

puts resp.key_metadata.key_id
```
+  For API details, see [CreateKey](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/CreateKey) in *AWS SDK for Ruby API Reference*.

### `Decrypt`
<a name="kms_Decrypt_ruby_topic"></a>

The following code example shows how to use `Decrypt`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/kms#code-examples).

```
require 'aws-sdk-kms' # v2: require 'aws-sdk'

# Decrypted blob

blob = '01020200785d68faeec386af1057904926253051eb2919d3c16078badf65b808b26dd057c101747cadf3593596e093d4ffbf22434a6d00000068306606092a864886f70d010706a0593057020100305206092a864886f70d010701301e060960864801650304012e3011040c9d629e573683972cdb7d94b30201108025b20b060591b02ca0deb0fbdfc2f86c8bfcb265947739851ad56f3adce91eba87c59691a9a1'
blob_packed = [blob].pack('H*')

client = Aws::KMS::Client.new(region: 'us-west-2')

resp = client.decrypt({
                        ciphertext_blob: blob_packed
                      })

puts 'Raw text: '
puts resp.plaintext
```
+  For API details, see [Decrypt](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/Decrypt) in *AWS SDK for Ruby API Reference*.

### `Encrypt`
<a name="kms_Encrypt_ruby_topic"></a>

The following code example shows how to use `Encrypt`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/kms#code-examples).

```
require 'aws-sdk-kms' # v2: require 'aws-sdk'

# ARN of the AWS KMS key.
#
# Replace the fictitious key ARN with a valid key ID

keyId = 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'

text = '1234567890'

client = Aws::KMS::Client.new(region: 'us-west-2')

resp = client.encrypt({
                        key_id: keyId,
                        plaintext: text
                      })

# Display a readable version of the resulting encrypted blob.
puts 'Blob:'
puts resp.ciphertext_blob.unpack('H*')
```
+  For API details, see [Encrypt](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/Encrypt) in *AWS SDK for Ruby API Reference*.

### `ReEncrypt`
<a name="kms_ReEncrypt_ruby_topic"></a>

The following code example shows how to use `ReEncrypt`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/kms#code-examples).

```
require 'aws-sdk-kms' # v2: require 'aws-sdk'

# Human-readable version of the ciphertext of the data to reencrypt.

blob = '01020200785d68faeec386af1057904926253051eb2919d3c16078badf65b808b26dd057c101747cadf3593596e093d4ffbf22434a6d00000068306606092a864886f70d010706a0593057020100305206092a864886f70d010701301e060960864801650304012e3011040c9d629e573683972cdb7d94b30201108025b20b060591b02ca0deb0fbdfc2f86c8bfcb265947739851ad56f3adce91eba87c59691a9a1'
sourceCiphertextBlob = [blob].pack('H*')

# Replace the fictitious key ARN with a valid key ID

destinationKeyId = 'arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321'

client = Aws::KMS::Client.new(region: 'us-west-2')

resp = client.re_encrypt({
                           ciphertext_blob: sourceCiphertextBlob,
                           destination_key_id: destinationKeyId
                         })

# Display a readable version of the resulting re-encrypted blob.
puts 'Blob:'
puts resp.ciphertext_blob.unpack('H*')
```
+  For API details, see [ReEncrypt](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/ReEncrypt) in *AWS SDK for Ruby API Reference*.
