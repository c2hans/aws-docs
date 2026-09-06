---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/edit-voicecon.html
---

# Editing Amazon Chime SDK Voice Connector settings
<a name="edit-voicecon"></a>

After you create an Amazon Chime SDK Voice Connector, you must edit the termination and origination settings that allow outbound and inbound calls. You can also configure a number of other settings, such as streaming to Kinesis and using emergency call routing. You use the Amazon Chime console to edit all settings.

**To edit Amazon Chime SDK Voice Connector settings**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose the name of the Amazon Chime SDK Voice Connector to edit.

1. The Amazon Chime console groups Voice Connector settings on a set of tabs. Expand the sections below for information about using each tab.

## Editing general settings
<a name="edit-general"></a>

Use the **General** tab to change a Voice Connector's name, and enable or disable encryption.

**Note**
If the Voice Connector is dual-stack and you use a host name that supports IPv6, media and signaling will go over IPv6.
If the Voice Connector is IPv4 it will not fall back or attempt IPv6, it is only IPv4.

**To change general settings**

1. (Optional) Under **Details**, enter a new name for the Voice Connector.

1. (Optional) Under **Encryption**, choose **Enabled** or **Disabled**. For more information about encryption, expand the next section.

1. Choose **Save**.

## Using encryption with Voice Connectors
<a name="use-encryption"></a>

When you enable encryption for an Amazon Chime SDK Voice Connector, you use TLS for SIP signaling and Secure RTP (SRTP) for media. The Voice Connector service uses TLS port 5061.

When enabled, all inbound calls use TLS, and unencrypted outbound calls are blocked.

Amazon Chime SDK Voice Connector uses TLS server certificates issued by Amazon Trust Services. Most modern operating systems trust Amazon Trust Services by default. If this is not the case for your SIP infrastructure, you may need to add the Starfield and Amazon Trust Services root CA certificates, excluding the EU roots, to your trust stores. [https://www.amazontrust.com/repository/](https://www.amazontrust.com/repository/)

**Note**
Amazon Chime SDK Voice Connector does not support mutual TLS (mTLS) and your SIP infrastructure should not request a client certificate. If your SIP infrastructure requests a client certificate, the Voice Connector service will respond with a certificate from a private certificate authority, please contact AWS Support if you have any questions.

We implement SRTP as described in [RFC 4568](https://datatracker.ietf.org/doc/html/rfc4568).

**Note**
Voice Connectors support TLS 1.2 and 1.3

For outbound calls, the service uses the SRTP default AWS counter cipher and HMAC-SHA1 message authentication. We support the following cipher suites for inbound and outbound calls:
+ AES\_CM\_128\_HMAC\_SHA1\_80
+ AES\_CM\_128\_HMAC\_SHA1\_32
+ AES\_CM\_192\_HMAC\_SHA1\_80
+ AES\_CM\_192\_HMAC\_SHA1\_32
+ AES\_CM\_256\_HMAC\_SHA1\_80
+ AES\_CM\_256\_HMAC\_SHA1\_32

You must use at least one cipher, but you can include all of them in preference order at no additional charge for Voice Connector encryption.

We also support these additional TLS cipher suites:

**Recommended cipher suites**

You must use at least one cipher, but you can include all of them in preference order at no additional charge for Voice Connector encryption.
+ ECDHE-RSA-AES256-GCM-SHA384
+ ECDHE-RSA-AES128-GCM-SHA256
+ ECDHE-RSA-AES256-SHA384
+ ECDHE-RSA-AES128-SHA256
+ AES256-GCM-SHA384
+ AES128-GCM-SHA256
+ AES128-SHA256

**Deprecated cipher suites (support ends August 1, 2026)**

The following cipher suites are being removed as part of our ongoing security improvements. Update your configurations to use the recommended cipher suites above before this date.
+ AES256-SHA256
+ AES256-SHA
+ AES128-SHA
+ DHE-RSA-AES256-GCM-SHA384
+ DHE-RSA-AES128-GCM-SHA256
+ DHE-RSA-AES256-SHA256
+ DHE-RSA-AES128-SHA256

## Editing termination settings
<a name="edit-termination"></a>

You use the **Termination** settings to enable and configure outbound calls from your Amazon Chime SDK Voice Connector.

**Note**
Your **Outbound host name** resolves to a set of IP addresses that may change as EC2 instances go in or out of service, so don’t cache records for longer than the DNS Time to Live interval. Caching for longer may result in call failures.

Choose **Save** again.

**To edit termination settings**

1. Select **Enabled**.

1. (Optional) Under **Allowed hosts list**, choose **New**, enter the CIDR notations and values that you want to allow, then choose **Add**. Note that the IP address values must be publically routable addresses.

   —OR—

   Choose **Edit** and change the CIDR notation.

   —OR—

   Choose **Delete** to remove the host.

1. Under **Calls per second**, select another value, if available.

1. Under **Calling plan**, open the **Countries** list and choose the countries that the Voice Connector can call.

1. Under **Credentials**, choose **New**, enter a username and password, then choose **Save**.

1. Under **Caller ID override**, choose **Edit**, select a phone number, then choose **Save**.

1. Under **Last options ping**, view the last SIP options message sent by your SIP infrastructure.

## Editing origination settings
<a name="edit-origination"></a>

Origination settings apply to inbound calls to your Amazon Chime SDK Voice Connector. You can configure inbound routes for your SIP hosts to receive inbound calls. Inbound calls are routed to hosts in your SIP infrastructure by the priority and weight you set for each host. Calls are routed in priority order first, with 1 the highest priority. If hosts are equal in priority, calls are distributed among them based on their relative weight.

**Note**
Encryption-enabled Voice Connectors use TLS (TCP) protocol for all calls.

**To edit origination settings**

1. Select **Enabled**.

1. Under **Inbound routes**, choose **New**.

1. Enter the values for **Host**, **Port**, **Protocol**, **Priority**, and **Weight**. Note that IP address values used for **Host** must be publicly routable addresses.

1. Choose **Add**.

1. Choose **Save**.

## Editing emergency calling settings
<a name="edit-emergency"></a>

To enable emergency calling, you first need to enable termination and origination. See the sections above for information about doing so.

You need at least one emergency call routing number from a third-party emergency service provider to complete these steps. For more information about obtaining numbers, see [Setting up third-party emergency routing numbers](chime-voice-connector-emergency-calling.md).

Choose **Add**.

**To edit emergency calling settings**

1. Choose **Add**.

1. Under **Call send method**, select an item from the list, if available.

1. Enter the emergency routing number.

1. Enter the test routing number. We recommend obtaining a test routing number.

1. Under **Country**, choose the routing number's country, if available.

1. Choose **Add**.

## Editing phone numbers
<a name="edit-phone"></a>

You can assign and unassign Voice Connector phone numbers. The following steps assume you have at least one phone number in your Amazon Chime inventory. If not, see [Provisioning phone numbers](provision-phone.md).

**To assign phone numbers**

1. Choose **Assign from inventory**.

1. Select one or more phone numbers.

1. Choose **Assign from inventory**.

The selected number or numbers appear in your list of numbers.

**To unassign phone numbers**

1. Select one or more phone numbers.

1. Choose **Unassign**.

1. When asked to confirm the operation, choose **Unassign**.

## Editing streaming settings
<a name="edit-streaming"></a>

The **Streaming** settings enable Amazon Kinesis Video Streams. The service stores, encrypts, and indexes your streaming audio data.

**To edit streaming settings**

1. Under **details**, choose **Start**.

1. Under **Streaming notification**, select one or more targets from the lists.

1. Under **Data retention period**, choose **No data retention**, or set a retention interval.

1. Under **Call Insights**, choose **Activate**, then do the following:

   1. Under **Access permissions**, select a role from the list.

   1. Under **Kinesis Data Stream**, select a stream from the list.

   1. (Optional) Under **Amazon Transcribe custom language model**, select a model from the list.

   1. Under **Personally identifiable information type**, choose an option.

   1. Under **Filter partial results**, choose an option.

   1. Under **Send real time notification**, choose **Start**, then choose an option from the **Call direction** and **Speaker** lists.

   1. As needed, choose **Add a word/phrase**, then enter the word or phrase that you want to be notified about.

1. Choose **Save**.

## Editing logging settings
<a name="edit-logging"></a>

The Amazon Chime SDK disables logging for Voice Connectors by default. When you enable logging, the system sends the data to an Amazon CloudWatch log group. For more information about logging, see [Monitoring the Amazon Chime SDK with Amazon CloudWatch](monitoring-cloudwatch.md)

**To edit logging settings**

1. Under **SIP metric logs**, choose **Enabled**.

1. Under **Media metric logs**, choose **Enabled**.

## Editing tag settings
<a name="edit-tags"></a>

You can add 50 tags to a Voice Connector, and you can choose the keys and optional values for the tags.

**To edit tag settings**

1. Choose **Manage tags**.

1. Do any of the following:
   + To add a tag, choose **Add new tag**, then enter a key and an optional value.
   + To remove a tag, choose **Remove** next to the tag that you want to delete.

1. When finished, choose **Save changes**.
