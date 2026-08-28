---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/sigfox.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Sigfox
<a name="sigfox"></a>

 Sigfox S.A. is a network operator for a LPWAN connectivity product, which is also called Sigfox. Sigfox is operated as a public network, with coverage in a subset of countries.

 **Range and coverage**

 The range of Sigfox devices is up 40 km outdoors, and 10 km in urban areas.

## Mobility
<a name="mobility-3"></a>

 Sigfox can be used for use cases requiring stationary and moving devices, assuming the Sigfox network coverage is available on the device locations. When using Sigfox, a device payload will be received by all the gateways within reach. Each of gateways receiving payload from the device will forward this payload to the Sigfox. The Sigfox network will perform a deduplication of the message.

## Battery life
<a name="battery-life-2"></a>

 A battery of a Sigfox device can last several years without replacement.

## Spectrum licensing
<a name="spectrum-licensing-3"></a>

 Sigfox devices are operated in license-free ISM (industrial, scientific, and medical) frequency bands in ranges from 862 MHz to 928 MHz. The exact frequency band used by the device depends on the geographical zone.

## Payload size
<a name="payload-size-2"></a>

 Sigfox devices can send payloads of up to 12 bytes size in uplink, and 8 bytes in downlink in a single message. A Sigfox device is allowed to transmit up to 140 uplink messages and receive up to four downlink messages per day.

## Latency
<a name="latency-1"></a>

 When using Sigfox, typical latency is in an order of magnitude of seconds. Reachability depends on the frequency of uplink transmissions. This dependency occurs because Sigfox devices are required to listen for incoming data for only 30 seconds after an uplink transmission. After 30 seconds, the Sigfox device changes into an energy-efficient mode and is not able to receive further incoming messages. For example, if you configure your Sigfox device to send uplink messages once a day, a downlink latency can be up to 24 hours.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
