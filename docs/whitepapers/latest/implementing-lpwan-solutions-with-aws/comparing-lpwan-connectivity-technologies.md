---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/comparing-lpwan-connectivity-technologies.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Comparing LPWAN connectivity technologies
<a name="comparing-lpwan-connectivity-technologies"></a>

 The following table provides a short overview of the key characteristics of LPWAN technologies covered in this whitepaper. Refer to [Appendix: Characteristics of LPWAN technologies](appendix-characteristics-of-lpwan-technologies.md) for a detailed description of each mentioned technology.

* Table 1 – LPWAN connectivity technologies *

|  Technology  |  LoRaWAN  |  NB-IoT (LTE Cat NB1)  |  LTE-M (LTE Cat M1)  |  Sigfox  |
| --- | --- | --- | --- | --- |
|  Range and coverage  |  \~5 km urban \~20 km rural  |  \~1 km urban \~10 km rural  |  \~1 km urban \~10 km rural  |  \~10 km urban \~40 km rural  |
|  Support for device mobility  |  Yes  |  Limited  |  Yes  |  Yes  |
|  Uplink latency (order of magnitude)  |  Seconds  |  1.2–100 s  |  < 60 ms  |  Seconds  |
|  Data rate  |  0,3 (SF12)–5,47 (SF7) kilobit/s  |  < 66 kilobit/s (uplink) < 26 kilobit/s (downlink)  |  1 megabit/s  |  0.1 kilobit/s  |
|  Allow private networks  |  Yes  |  No  |  No  |  No (however, customers can deploy their own gateways)  |
|  Battery life and power consumption  |  Years (when operating as a Class A device)  |  Years (when using eDRX and PSM features)  |  Years (when using eDRX and PSM features)  |  Years  |
|  Maximum payload size  |  11–242 bytes, depending on regional regulations and spread factor  |  1,280 bytes recommended  |  1,280 bytes recommended  |  12 bytes (uplink) 8 bytes (downlink)  |
|  Support for indoor and underground coverage  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Reachability  |  Depends on device class (high for Class A, low for Class C)  |  Depends on power saving model configuration (PSM/eDRX)  |  Depends on power saving model configuration (PSM/eDRX)  |  High (downlink transmission allowed only during <br /> 30 seconds after uplink)  |
|  Licensed spectrum  |  No  |  Yes  |  Yes  |  No  |
|  Maximum messages per day  |  Depends on regional regulations of duty cycle  |  Unlimited  |  Unlimited  |  140 per day (uplink) 4 per day (downlink)  |
