---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-event-handling.html
---

# 6 Event handling
<a name="elpg-event-handling"></a>

Events are asynchronous messages on one of the subscribed topics that the ExpressLink module has received and queued. They can also be error messages that reflect an unexpected change in the module's internal state.

Events can be polled periodically by the host processor using the EVENT? command, or if connected, following an interrupt that is the result of the module activating the EVENT pin. The EVENT pin is automatically deactivated as soon as the host processor has emptied the queue of pending events.

If the event queue contains one or more events, the value returned by an EVENT? command is the last event that occurred. The event queue depth is implementation dependent; a queue length of 1 means that only the last event (or the highest priority error) is reported in case of overrun.

**Note**
Sleep, reset, and factory reset commands automatically clear all pending events.

## 6.1 Event handling commands
<a name="elpg-event-handling-commands"></a>

### 6.1.1 EVENT?: Request the next event in the queue
<a name="elpg-eventq-command"></a>Returns:

6.1.1.1 `OK [{event_identifier} {parameter} {mnemonic [detail] }]{{eol}`

6.1.1.2 `OK{eol}`
If the event queue is empty, then the 'OK' response is followed immediately by {eol}.

The following table contains the definition of common event identifiers and error codes implemented by all ExpressLink modules; they should be considered reserved:

**Table 4 - ExpressLink event codes**

| Event Identifier | Parameter | Mnemonic | Description |
| --- | --- | --- | --- |
| 1 | Topic Index | MSG | A message was received on topic \#. |
| 2 | 0 | STARTUP  | The module has entered the active state. |
| 3 | 0 | CONLOST | Connection lost.  |
| 4 | 0 | OVERRUN | Receive buffer Overrun (topic in detail).  |
| 5 | 0 | OTA | OTA event (see OTA? for detail).  |
| 6 | 0 | SHADOW | SHADOW Event. |
| 7 | 0 | CONFMODE | CONFMODE exit with success. |
| ≤ 999 | - |  | RESERVED.  |
| ≥1000 | - |  | Available for custom implementation. |

## 6.2 Diagnostic commands
<a name="elpg-diagnostic-commands"></a>

### 6.2.1 DIAG *{command} [optional parameters]*: Perform a diagnostic command
<a name="elpg-diag-command"></a>

A number of diagnostic commands can be added to assist the developer in their debugging efforts. These commands are implementation specific and depend on the media and type of module. See the manufacturer's datasheet for specific details.

The following are examples of possible diagnostic commands for a Wi-Fi module:

Example 1:

```
AT+DIAG PING xxx.xxx.xxx.xxx    # Initiate a Ping of the IP address provided
```

Example 2:

```
AT+DIAG SCAN seconds    # Initiates a SCAN of nearby Wi-Fi access points with a timeout of
...
OK {SCANRES} -32db SSID1\n-48db SSID2\n ... -90dB SSIDx
```

In the results, the list of SSIDs is provided in the response detail as a multiline string with the newline characters escaped ('\\n').
