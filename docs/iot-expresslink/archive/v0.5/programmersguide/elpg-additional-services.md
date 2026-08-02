---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-additional-services.html
---

# 9 Additional services
<a name="elpg-additional-services"></a>

## 9.1.1 TIME?: Request current time information
<a name="elpg-timeq-command"></a>

ExpressLink modules must provide time information as available from SNTP, GPS, or cellular network sources. Note that devices can choose to maintain a time reference internally, even when disconnected or in sleep mode, depending on implementation-specific software or hardware capabilities.Returns:

9.1.1.1 `OK {date YYYY/MM/DD} {time hh:mm:ss.xx} {source}`
If time information is available and recently obtained.

9.1.1.2 `ERR15 TIME NOT AVAILABLE`
If a recent time fix could not be obtained.

## 9.1.2 WHERE?: Request location information
<a name="elpg-whereq-command"></a>

ExpressLink modules can *optionally* provide last location information as available from GPS, GNSS, cellular networks, or other triangulation methods. A timestamp is provided to let the host determine the currency of the information. The implementation of this command is optional.Returns:

9.1.2.1 `OK {date} {time} {lat} {long} {elev} {accuracy} {source}`
If location coordinates could be obtained at date/time.

9.1.2.2 `ERR16 LOCATION NOT AVAILABLE`
If a location fix could not be obtained.
