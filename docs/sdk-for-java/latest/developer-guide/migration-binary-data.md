---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-binary-data.html
---

# Binary data handling changes

In version 1, binary data was handled using `ByteBuffer` objects directly. In version 2, the SDK uses `SdkBytes` objects that provide a more convenient and type-safe way to work with binary data.

You can convert `SdkBytes` to `ByteBuffer` automatically using the [migration tool](migration-tool.md), or you can convert them manually by calling `asByteBuffer()` on the returned `SdkBytes` object.

**Example - Get binary data from a message attribute in version 1**

```java
// Get binary data from a message attribute
MessageAttributeValue messageAttributeValue = new MessageAttributeValue();
ByteBuffer binaryValue = messageAttributeValue.getBinaryValue();
String binaryString = new String(messageAttributeValue.getBinaryValue().array());
```

**Example - Get binary data from a message attribute in version 2**

```java
// Get binary data from a message attribute
MessageAttributeValue messageAttributeValue = MessageAttributeValue.builder().build();
ByteBuffer binaryValue = messageAttributeValue.binaryValue().asByteBuffer();
String binaryString = new String(messageAttributeValue.binaryValue().asByteBuffer().array());
```
