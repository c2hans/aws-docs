---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-messaging.html
---

# 4 Messaging
<a name="elpg-messaging"></a>

## 4.1 Messaging topic model
<a name="elpg-messaging-topic"></a>

The ExpressLink messaging system relies on a list of topics defined in the configuration dictionary (see [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2)). Each topic is assigned an index that can be used to dereference the assigned string value. Index 0 has a special meaning, while all other index values up to an implementation-specific maximum index can be used by the host to define additional topics. Messaging topics defined in this list are managed independently from other topics eventually used by ExpressLink to handle Jobs, OTA, and shadow updates.

**4.1.1.1**
Topic Index 0 is reserved as a catch-all for messages that do not match other existing topics (the list of topics must not contain an entry for Topic0).

**4.1.1.2**
Topic *Index{MaxTopic}* is an implementation-dependent value ≥ 16.

### 4.1.2 Topic usage rules
<a name="elpg-messaging-topic-usage"></a>

ExpressLink uses the following rules for creating the topics used to publish and subscribe.

4.1.2.1 Default *TopicRoot*
The default topic root is used to prefix topics that are used in SEND/GET and SUBSCRIBE commands. The *TopicRoot* is meant to simplify the work the host must do to assemble a path that contains its UID/ThingName (whose default value is as shown in [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2)).

4.1.2.2 Topic Strings prefixed with '/' are complete
Topic strings that are prefixed with '/' are considered complete. The topic root will not be prepended to the topic name. The leading '/' will be stripped before using the topic to publish or subscribe.

4.1.2.3 Publish Data Topics are *<TopicRoot>/<Topic@Index>*
Topic names used for publishing are created by combining the TopicRoot (set in the CONF dictionary) with the values at the indexed position in the topic table.

4.1.2.4 Receive Data Topics are *<TopicRoot>/<Topic@Index>*
Topic names used for subscriptions are created by combining the *TopicRoot* (set in the CONF dictionary) with the value at the indexed position in the topic.

### 4.1.3 SEND *{topic} message*: Publish msg on the specified topic
<a name="elpg-send-command"></a>Where:

*{topic}*
A string formatted according to topic rules.

*message*
The message to publish (string).

Example 1:

```
AT+SEND data Hello World    # Publish the classic 'Hello World' message on topic 'data'
OK                          # Message sent
```

### 4.1.4 SEND*{\#} message*: Publish msg on a topic selected from topic list
<a name="elpg-sendh-command"></a>Where:

*{\#}*
The index of a topic in CONFIG dictionary (1..MaxTopic).

*message*
The message to publish (string).

Example 2:

```
AT+SEND2 Hello World    # Publish 'Hello World' on Topic2
OK                      # Message Sent
```Returns:

4.1.4.1 `OK`
If the message is sent successfully, then the module returns 'OK'.

4.1.4.2 `ERR6 NO CONNECTION`
If no connection has been made, then the module returns 'NO CONNECTION'.
Example 3:

```
AT+SEND1 Hello World    # Publish Hello World on Topic1
ERR6 NO CONNECTION      # A connection has not been established
```

4.1.4.3 `ERR7 TOPIC OUT OF RANGE`
If the supplied topic index is larger than the maximum allowed topic number, the module returns 'TOPIC OUT OF RANGE'.
Example 4:

```
AT+SEND99 Hello World      # Publish Hello World on Topic99
ERR7 TOPIC OUT OF RANGE    # Topic 99 is not within the available range of topics
```

4.1.4.4 `ERR8 TOPIC UNDEFINED`
If the supplied topic index points to a topic entry that has not been defined, the module returns 'TOPIC NOT DEFINED'.
Example 5:

```
AT+SEND3 Hello World    # Publish Hello World on Topic3
ERR8 TOPIC UNDEFINED    # The key Topic3 was not found in the config dictionary
```

### 4.1.5 GET: Request next message pending on any topic
<a name="elpg-get-command"></a>

Retrieve the next message received in the order of arrival.Returns:

4.1.5.1 `OK{separator}<Topic>{separator}<MESSAGE>{eol}`
If a message is available on any topic, the module responds with 'OK' followed by the topic and the message.
Example 1:

```
AT+GET                 # poll for messages received on any topic
OK data Hello World    # a message was received from topic 'data'
```

4.1.5.2 `OK{eol}`
If no message was received on any topic, the module responds with 'OK' followed by {eol}.

### 4.1.6 GET0: Request next message pending on an unassigned topic
<a name="elpg-get0-command"></a>

Retrieve the next message received on a topic that was not in the topic list.Returns:

4.1.6.1 `OK{separator}<Topic>{separator}<MESSAGE>{eol}`
Example 2:

```
AT+GET0                # poll for messages received on any unassigned topic
OK data Hello World    # a message was received from topic 'data'
```

4.1.6.2 `OK{eol}`
If no message was received on any unassigned topic, the module returns 'OK' followed by {eol}.

### 4.1.7 GET*{\#}*: Request next message pending on the indicated topic
<a name="elpg-geth-command"></a>

Retrieve the next message received on a topic at the specified index \# (1..MaxTopic) in the topic list.Returns:

4.1.7.1 `OK{separator}{MESSAGE}{eol}`
If a message is available on the indicated topic, the module responds with 'OK' followed immediately by the message.
Example 3:

```
AT+GET2           # select messages received on Topic2
OK Hello World    # a message received on the topic at index 2 in the list of topics
```

4.1.7.2 `OK{eol}`
If a message is NOT available matching the requested topic, the module responds with 'OK' followed by {eol}.

**4.1.7.3**
Even if there is no active connection, a normal read from the message queue takes place.

4.1.7.4 `ERR7 TOPIC OUT OF RANGE`
If the supplied topic index is larger than the maximum allowed topic number, then the module returns 'TOPIC OUT OF RANGE'.

4.1.7.5 `ERR8 TOPIC UNDEFINED`
If the requested topic is not defined, then the module returns 'TOPIC UNDEFINED'.

4.1.7.6 Message queue overflow conditions
If the host fails to retrieve a message and does not free up space and the buffer capacity is exceeded, an overrun occurs. The oldest message in the buffer will be lost. The condition will be reported as a new (OVERFLOW) event and added to the event queue. It is then accessible to the host processor by means of the EVENT? command. Also, the overflow condition is reported in the status dictionary and can be verified by using the STAT? Overflow command. If there is overflow, the number of messages-received events in the queue will exceed the actual number of messages that are present.

### 4.1.8 SUBSCRIBE*{\#}*: Subscribe to the indicated topic
<a name="elpg-subscribeh-command"></a>

The module subscribes to the topic and start receiving messages. Incoming messages trigger events. The messages can be read with a GET{\#} command.

Note that this is a stateless feature; the ExpressLink module will request a subscription to the MQTT broker, but will not retain information about its current state.

4.1.8.1 If a topic number is provided, use the topic at the specified index.

**Note**
Sending a message to a topic to which a module is subscribed results in the broker sending a copy back to the module.

Example 1:

```
AT+CONF TopicRoot=building1/floor1
AT+CONF Topic1=sensor1/state
AT+SUBSCRIBE1    # The module will subscribe to the topic building1/floor1/sensor1/state
```

Example 2:

```
AT+CONF Topic2=/sensor1/state
AT+SUBSCRIBE2    # The module will subscribe to the topic sensor1/state
```Returns:

4.1.8.2 `ERR6 NO CONNECTION`
If no connection has been made, then the module returns 'NO CONNECTION'.

4.1.8.3 `ERR8 TOPIC UNDEFINED`
If the requested topic is not defined, then the module returns 'TOPIC NOT DEFINED'.

4.1.8.4 `ERR7 TOPIC OUT OF RANGE`
If the supplied topic index is larger than the maximum allowed topic number, then the module returns 'TOPIC OUT OF RANGE'.

### 4.1.9 UNSUBSCRIBE*{\#}*: Unsubscribe from Topic\#
<a name="elpg-unsubscribeh-command"></a>

The device unsubscribes from the selected topic and stops receiving its messages/events.

4.1.9.1 Use the topic at the specified index.

**Note**
Sending a message to a topic to which the module is subscribed results in the broker sending a copy back to the module.

Example 1:

```
AT+CONF TopicRoot=building1/floor1
AT+CONF Topic1=sensor1/state
AT+SUBSCRIBE1      # The module will subscribe to topic building1/floor1/sensor1/state
...
AT+UNSUBSCRIBE1    # The module will unsubscribe topic building1/floor1/sensor1/state
```Returns:

4.1.9.2 `ERR6 NO CONNECTION`
If no connection has been made, then the module returns 'NO CONNECTION'.

4.1.9.3 `ERR8 TOPIC UNDEFINED`
If the requested topic is not defined, then the module returns 'TOPIC NOT DEFINED'.

4.1.9.4 `ERR7 TOPIC INDEX OUT OF RANGE`
If the supplied topic index is larger than the maximum allowed topic number, then the module returns 'TOPIC OUT OF RANGE'.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
