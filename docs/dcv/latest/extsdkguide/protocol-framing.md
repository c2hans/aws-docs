---
source_url: https://docs.aws.amazon.com/dcv/latest/extsdkguide/protocol-framing.html
---

# Protocol and framing
<a name="protocol-framing"></a>

 When Amazon DCV components start the extension on either server or client side, DCV uses standard input (`stdin`) and standard output (`stdout`), also known as anonymous pipes, to communicate with the extension.

The Amazon DCV component and extension are treated as peers and use the same wire protocol. Communication is bidirectional.

Extensions receive binary frames from Amazon DCV from their standard input stream and must write binary frames for Amazon DCV to their standard output stream.

**Important**
Extensions must refrain from writing any output to their standard error stream. Failure to do so may cause their process to be terminated.

## Frame
<a name="frame"></a>

A frame that is sent by either peer consists of a mandatory header followed by the payload message.

```
				FRAME
 +--------+------------------------------------···--+
 | header | message                                 |
 +--------+------------------------------------···--+
  4 bytes     variable length
```

## Header
<a name="header"></a>

A binary header is consisting of a single 4 bytes little-endian unsigned integer, representing the size in bytes of the following message.

```
				HEADER
+------------+------------+------------+------------+
|byte 0 (LSB)|   byte 1   |   byte 2   |byte 3 (MSB)|
+------------+------------+------------+------------+
```

## Message
<a name="message"></a>

Amazon DCV and Amazon DCV Extension SDK use Protocol Buffers (protobuf) protocol to send messages in both directions. The definition of the messages are contained in the file `extensions.proto`.

Messages are exchanged in binary form. Also, the protobuf provides for serializers and deserializers to and from binary streams for many programming languages.

```
				MESSAGE
+----------------------------------------------···--+
| bytes                                             |
+----------------------------------------------···--+
  number of bytes as specified in the header
```
