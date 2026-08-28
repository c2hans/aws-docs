---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v1.1.2/programmersguide/elpg-event-handling.html
---

# 7 Event handling
<a name="elpg-event-handling"></a>

## 7.1 Introduction
<a name="elpg-event-handling-introduction"></a>

Events are asynchronous messages on one of the subscribed topics that the ExpressLink module has received and queued. They can also be error messages that reflect an unexpected change in the module's internal state.

Events are appended to the module event queue (FIFO). The host can poll the event queue periodically. Or, if connected, it can poll the event queue following an interrupt (rising edge) on the EVENT pin.

**7.1.1.1**   The event queue depth is an implementation dependent parameter that must be documented by the vendor in the module datasheet.

**7.1.1.2**   The EVENT pin is asserted (HIGH) when the event queue contains one or more events. The EVENT pin is automatically de-asserted as soon as the host processor has emptied the event queue.

**7.1.1.3**   When the event queue is full, and a new event occurs, the oldest event is discarded (circular buffer).

## 7.2 Event handling commands
<a name="elpg-event-handling-commands"></a>

### 7.2.1 EVENT?   »Request the next event in the queue«
<a name="elpg-eventq-command"></a>Returns:

**7.2.1.1**   `OK [{event_identifier} {parameter} {mnemonic [detail]}]{EOL}`
When the queue contains one or more events, the module response returns the first event in order of arrival (FIFO). See Table 4 below for the predefined event types.

**7.2.1.2**   `OK{EOL}`
If the event queue is empty, then the 'OK' response is followed immediately by *{EOL}*.

The following table contains the definition of common event identifiers and error codes implemented by all ExpressLink modules; they should be considered reserved:

**Table 4 - ExpressLink event codes**

| Event Identifier | Parameter | Mnemonic | Description |
| --- | --- | --- | --- |
| 1 | Topic Index | MSG | A message was received on the topic \#. |
| 2 | 0 | STARTUP | The module has entered the active state. |
| 3 | 0 | CONLOST | Connection unexpectedly lost.  |
| 4 | 0 | OVERRUN | Receive buffer Overrun (topic in detail).  |
| 5 | 0 | OTA | OTA event (see the OTA? command for details).  |
| 6 | Connection Hint | CONNECT | A connection was established or failed. |
| 7 | 0 | CONFMODE | CONFMODE exit with success. |
| 8 | Topic Index | SUBACK | A subscription was accepted. |
| 9 | Topic Index | SUBNACK | A subscription was rejected. |
| 10..19 | - | - | RESERVED |
| 20 | Shadow Index | SHADOW INIT | Shadow[Shadow Index] interface was initialized successfully. |
| 21 | Shadow Index | SHADOW INIT FAILED | The SHADOW[Shadow Index] interface initialization failed. |
| 22 | Shadow Index | SHADOW DOC | A Shadow document was received. |
| 23 | Shadow Index | SHADOW UPDATE | A Shadow update result was received. |
| 24 | Shadow Index | SHADOW DELTA | A Shadow delta update was received. |
| 25 | Shadow Index | SHADOW DELETE | A Shadow delete result was received. |
| 26 | Shadow Index | SHADOW SUBACK | A Shadow delta subscription was accepted. |
| 27 | Shadow Index | SHADOW SUBNACK | A Shadow delta subscription was rejected. |
| ≤ 999 | - |  | RESERVED.  |
| ≥1000 | - |  | Available for custom implementation. |

**7.2.1.3**   Sleep, reset, and factory reset commands automatically clear all events pending.

## 7.3 Diagnostic commands (not covered by test)
<a name="elpg-diagnostic-commands"></a>

### 7.3.1 DIAG *{command} [optional parameters]*   »Perform a diagnostic command«
<a name="elpg-diag-command"></a>

A number of diagnostic commands can be added to assist the developer in their debugging efforts. These commands are implementation specific and depend on the media and type of module. See the manufacturer's datasheet for specific details.

Diagnostic commands are not checked as part of the ExpressLink qualification test suite.

Diagnostic commands must be documented in the vendor device datasheet.

The following are examples of possible diagnostic commands for a Wi-Fi module:

Example 1:

```
AT+DIAG PING xxx.xxx.xxx.xxx    # Initiate a Ping of the IP address provided
```

Example 2:

```
AT+DIAG SCAN seconds    # Initiates a SCAN of nearby Wi-Fi access points with a timeout
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
