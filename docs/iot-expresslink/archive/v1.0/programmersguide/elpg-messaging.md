---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-messaging.html
---

# 4 Messaging
<a name="elpg-messaging"></a>

## 4.1 Messaging topic model
<a name="elpg-messaging-topic"></a>

The ExpressLink messaging system relies on a list of topics defined in the configuration dictionary (see [Table 2 - Configuration dictionary persistent keys](elpg-configuration-dictionary.md#elpg-table2)). Each topic is assigned an index that can be used to dereference the assigned string value. Index 0 has a special meaning, while all other index values up to an implementation-specific maximum index can be used by the host to define additional topics. Messaging topics defined in this list are managed independently from other topics eventually used by ExpressLink to handle Jobs, OTA, and shadow updates.

**4.1.1.1**
Topic Index 0 is reserved as a catch-all for messages that do not match other existing topics (the list of topics must not contain an entry for Topic0). Attempting to send or subscribe to a topic of index 0 will return `ERR7 OUT OF RANGE`.

**4.1.1.2**
Topic *Index{MaxTopic}* is an implementation-dependent value ≥ 16.

### 4.1.2 Topic usage rules
<a name="elpg-messaging-topic-usage"></a>

Topics are defined to be compatible with the MQTT 3.1.1 standard

### 4.1.3 SEND *{topic} message* ⁞  Publish msg on the specified topic
<a name="elpg-send-command"></a>

**Note**
As of version 1.0 the **SEND***{topic}* command has been removed. This resolves an ambiguity that occurred when a topic contained a space (0x20) character (allowed in MQTT3.1.1). Also see a related change in [4.1.6 GET0 ⁞  Request next message pending on an unassigned topic](#elpg-get0-command).

### 4.1.4 SEND*{\#} message* ⁞  Publish msg on a topic selected from topic list
<a name="elpg-sendh-command"></a>

Send a message on a topic provided in the configuration dictionary. The configuration parameter QoS value (only 0 and 1 are supported) at the time the command is issued determines the applicable Quality of Service.Where:

*{\#}*
The index of a topic in CONFIG dictionary (1..MaxTopic).

*message*
The message to publish (string).Returns:

**4.1.4.1**   `OK{EOL}`
If the message is sent successfully, then the module returns 'OK'.
Example 1:

```
AT+SEND2 Hello World    # Publish 'Hello World' on Topic2
OK                      # The message will be sent
```

**4.1.4.2**   `ERR6 NO CONNECTION`
If no connection has been made, then the module returns 'NO CONNECTION'.
Example 2:

```
AT+SEND1 Hello World    # Publish Hello World on Topic1
ERR6 NO CONNECTION      # A connection has not been established
```

**4.1.4.3**   `ERR7 OUT OF RANGE`
If the supplied topic index is larger than the maximum allowed topic number, the module returns 'OUT OF RANGE'.
Example 3:

```
AT+SEND99 Hello World      # Publish Hello World on Topic99
ERR7 OUT OF RANGE    # Topic 99 is not within the available range of topics for this device
```

**4.1.4.4**   `ERR8 PARAMETER UNDEFINED`
If the supplied topic index points to a topic entry that has not been defined (empty), the module returns 'PARAMETER UNDEFINED'.
Example 4:

```
AT+CONF Topic3={EOL}      # Define Topic3 as empty
OK

AT+SEND3 Hello World      # Publish Hello World on Topic3
ERR8 PARAMETER UNDEFINED  # The selected topic was undefined
```

### 4.1.5 GET ⁞  Request next message pending on any topic
<a name="elpg-get-command"></a>

Retrieve the next message received in the order of arrival.Returns:

**4.1.5.1**   `OK1{separator}{topic}{EOL}{message}{EOL}`
If a message is available on any topic, the module responds with 'OK' followed by the topic and the message.
Example:

```
AT+GET            # poll for messages received on any topic
OK1 data{EOL}     # a message was received from topic 'data' (expect another line)
Hello World{EOL}  # the actual message received
```

**4.1.5.2**   `OK{EOL}`
If no message was received on any topic, the module responds with 'OK' followed by *{EOL}*.

### 4.1.6 GET0 ⁞  Request next message pending on an unassigned topic
<a name="elpg-get0-command"></a>

Retrieve the next message received on a topic that was not in the topic list.

Note that the response to this command always produces two output line, an exception to the general format defined in [3.6.1 General response formats:](elpg-commands.md#elpg-responses-formats).Returns:

**4.1.6.1**   `OK1{separator}{topic}{EOL}{message}{EOL}`
Example:

```
AT+GET0            # poll for messages received on any unassigned topic
OK1 data{EOL}      # a message was received from topic 'data' (expect another line)
Hello World{EOL}   # the actual message received
```

**4.1.6.2**   `OK{EOL}`
If no message was received on any unassigned topic, the module returns 'OK' followed by *{EOL}*.

### 4.1.7 GET*{\#}* ⁞  Request next message pending on the indicated topic
<a name="elpg-geth-command"></a>

Retrieve the next message received on a topic at the specified index \# (1..MaxTopic) in the topic list.Returns:

**4.1.7.1**   `OK{separator}{message}{EOL}`
If a message is available on the indicated topic, the module responds with 'OK' followed immediately by the message.
Example:

```
AT+GET2           # select messages received on Topic2
OK Hello World    # a message received on the topic at index 2 in the list of topics
```

**4.1.7.2**   `OK{EOL}`
If a message is NOT available matching the requested topic, the module responds with 'OK' followed by *{EOL}*.

**4.1.7.3**   `OK{message}{EOL}`
Even if there is no active connection, a normal read from the message queue takes place and might return a valid message.

**4.1.7.4**   `ERR7 TOPIC OUT OF RANGE`
If the supplied topic index is larger than the maximum allowed topic number, then the module returns 'TOPIC OUT OF RANGE'.

**4.1.7.5**   `ERR8 PARAMETER UNDEFINED`
If the requested topic is not defined (empty), then the module returns 'PARAMETER UNDEFINED'.

**4.1.7.6**   Message queue overflow conditions
If the host fails to retrieve a message in time and so does not free up space and the buffer capacity is exceeded, an overrun occurs and *new messages arriving from the cloud may be lost*. The condition will be reported as an OVERFLOW event (see [Table 4 - ExpressLink event codes](elpg-event-handling.md#elpg-table4)) and added to the event queue. It is then accessible to the host processor by means of the EVENT? command. If there is an overflow, the number of messages-received events in the queue will exceed the actual number of messages that are present.

### 4.1.8 SUBSCRIBE*{\#}* ⁞  Subscribe to Topic\#
<a name="elpg-subscribeh-command"></a>

The module subscribes to the topic and starts receiving messages. Incoming messages trigger events. The messages can be read with a GET{\#} command.

Note that this is a stateless feature; the ExpressLink module will request a subscription to the MQTT broker, but will not retain information about its current state.

**4.1.8.1**   If a topic number is provided, use the topic at the specified index.

**Note**
Sending a message to a topic to which a module is subscribed results in the broker sending a copy back to the module.

Example 1:

```
AT+CONF Topic1=sensor1/state
OK

AT+SUBSCRIBE1    # The module will subscribe to the topic sensor1/state
OK
```Returns:

**4.1.8.2**   `ERR6 NO CONNECTION`
If no connection has been made, then the module returns 'NO CONNECTION'.

**4.1.8.3**   `ERR8 PARAMETER UNDEFINED`
If the requested topic is not defined (empty), then the module returns 'PARAMETER UNDEFINED'.

**4.1.8.4**   `ERR7 OUT OF RANGE`
If the supplied topic index is larger than the maximum allowed topic number, then the module returns 'OUT OF RANGE'.

### 4.1.9 UNSUBSCRIBE*{\#}* ⁞  Unsubscribe from Topic\#
<a name="elpg-unsubscribeh-command"></a>

The device unsubscribes from the selected topic and stops receiving its messages/events.

**4.1.9.1**   Use the topic at the specified index.

Example:

```
AT+CONF Topic1=sensor1/state
OK

AT+SUBSCRIBE1      # The module will subscribe to topic sensor1/state
OK
...
AT+UNSUBSCRIBE1    # The module will unsubscribe from topic sensor1/state
```Returns:

**4.1.9.2**   `ERR6 NO CONNECTION`
If no connection has been made, then the module returns 'NO CONNECTION'.

**4.1.9.3**   `ERR8 PARAMETER UNDEFINED`
If the requested topic is not defined (empty), then the module returns 'PARAMETER UNDEFINED'.

**4.1.9.4**   `ERR7 OUT OF RANGE`
If the supplied topic index is larger than the maximum allowed topic number, then the module returns 'OUT OF RANGE'.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
