---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v1.2/programmersguide/elpg-additional-services.html
---

# 10 Additional services
<a name="elpg-additional-services"></a>

## 10.1.1 TIME?   »Request current time information«
<a name="elpg-additional-services-time-command"></a>

ExpressLink modules *must* provide time information as available from SNTP, GPS or cellular network sources. Devices can choose to maintain a time reference internally even when disconnected or in sleep mode, depending on implementation specific software or hardware capabilities. Returns:

**10.1.1.1**   `OK {date YYYY/MM/DD} {time hh:mm:ss.xx} {source}`
If time information is available and recently obtained, the module returns 'OK' followed by that information.

**10.1.1.2**   `ERR15 TIME NOT AVAILABLE`
A recent time fix could not be obtained.

## 10.1.2 WHERE?   »Request location information«
<a name="elpg-additional-services-where-command"></a>

ExpressLink modules can optionally provide last location information as available from GPS, GNSS, cellular network or other triangulation method. A time stamp is provided to allow the host determine whether the information is current. The implementation of this command is optional.Returns:

**10.1.2.1**   `OK {date} {time} {lat} {long} {elev} {accuracy} {source}`
If location coordinates could be obtained at date/time, the module returns 'OK' followed by the information.

**10.1.2.2**   `ERR16 LOCATION NOT AVAILABLE`
A location fix could not be obtained.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
