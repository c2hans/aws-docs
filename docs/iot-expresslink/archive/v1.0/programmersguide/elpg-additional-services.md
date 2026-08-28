---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-additional-services.html
---

# 9 Additional services
<a name="elpg-additional-services"></a>

## 9.1.1 TIME? ⁞  Request current time information
<a name="elpg-timeq-command"></a>

ExpressLink modules *must* provide time information as available from SNTP, GPS, or cellular network sources. Note that devices can choose to maintain a time reference internally, even when disconnected or in sleep mode, depending on implementation-specific software or hardware capabilities.Returns:

**9.1.1.1**   `OK {date YYYY/MM/DD} {time hh:mm:ss.xx} {source}`
If time information is available and recently obtained, the module returns it.

**9.1.1.2**   `ERR15 TIME NOT AVAILABLE`
If a recent time fix could not be obtained, the module returns 'TIME NOT AVAILABLE'.

## 9.1.2 WHERE? ⁞  Request location information
<a name="elpg-whereq-command"></a>

ExpressLink modules can *optionally* provide last location information as available from GPS, GNSS, cellular networks, or other triangulation methods. A timestamp is provided to let the host determine the currency of the information. The implementation of this command is optional.Returns:

**9.1.2.1**   `OK {date} {time} {lat} {long} {elev} {accuracy} {source}`
If location coordinates could be obtained at date/time, the module returns it.

**9.1.2.2**   `ERR16 LOCATION NOT AVAILABLE`
If a location fix could not be obtained, the module returns 'LOCATION NOT AVAILABLE'.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
