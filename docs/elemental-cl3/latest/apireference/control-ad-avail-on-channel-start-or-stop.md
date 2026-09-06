---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/control-ad-avail-on-channel-start-or-stop.html
---

# POST Ad Avail State: Start or Stop Ad Avail on a Channel
<a name="control-ad-avail-on-channel-start-or-stop"></a>

Start or stop the ad avail blanking on a channel.

The channel must be running to change the ad avail state. To check the status, use GET Channel. For information on the status, see [Channel Status Elements](monitoring-manage-channels.md#monitoring-manage-channels-status).

## HTTP Request and Response
<a name="control-ad-avail-on-channel-start-or-stop-http-request-response"></a>

### Request URL
<a name="control-ad-avail-on-channel-start-or-stop-http-request-response-url"></a>

```
POST http://<Conductor IP address>/channels/<channel ID>/ad_avail_state/start
```

or

```
POST http://<Conductor IP address>/channels/<channel ID>/ad_avail_state/stop
```

### Call Header
<a name="control-ad-avail-on-channel-start-or-stop-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type:Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="control-ad-avail-on-channel-start-or-stop-http-request-response-response"></a>

A response is only given if you POST to a channel that is not running or that does not have avail blanking enabled.
