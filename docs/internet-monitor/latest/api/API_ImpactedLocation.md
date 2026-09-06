---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_ImpactedLocation.html
---

# ImpactedLocation
<a name="API_ImpactedLocation"></a>

Information about a location impacted by a health event in Internet Monitor.

Geographic regions are hierarchically categorized into country, subdivision, metro and city geographic granularities. The geographic region is identified based on the IP address used at the client locations.

## Contents
<a name="API_ImpactedLocation_Contents"></a>

 ** ASName **   <a name="internetmonitor-Type-ImpactedLocation-ASName"></a>
The name of the internet service provider (ISP) or network (ASN).
Type: String
Required: Yes

 ** ASNumber **   <a name="internetmonitor-Type-ImpactedLocation-ASNumber"></a>
The Autonomous System Number (ASN) of the network at an impacted location.
Type: Long
Required: Yes

 ** Country **   <a name="internetmonitor-Type-ImpactedLocation-Country"></a>
The name of the country where the health event is located.
Type: String
Required: Yes

 ** Status **   <a name="internetmonitor-Type-ImpactedLocation-Status"></a>
The status of the health event at an impacted location.
Type: String
Valid Values: `ACTIVE | RESOLVED`
Required: Yes

 ** CausedBy **   <a name="internetmonitor-Type-ImpactedLocation-CausedBy"></a>
The cause of the impairment. There are two types of network impairments: AWS network issues or internet issues. Internet issues are typically a problem with a network provider, like an internet service provider (ISP).
Type: [NetworkImpairment](API_NetworkImpairment.md) object
Required: No

 ** City **   <a name="internetmonitor-Type-ImpactedLocation-City"></a>
The name of the city where the health event is located.
Type: String
Required: No

 ** CountryCode **   <a name="internetmonitor-Type-ImpactedLocation-CountryCode"></a>
The country code where the health event is located. The ISO 3166-2 codes for the country is provided, when available.
Type: String
Required: No

 ** InternetHealth **   <a name="internetmonitor-Type-ImpactedLocation-InternetHealth"></a>
The calculated health at a specific location.
Type: [InternetHealth](API_InternetHealth.md) object
Required: No

 ** Ipv4Prefixes **   <a name="internetmonitor-Type-ImpactedLocation-Ipv4Prefixes"></a>
The IPv4 prefixes at the client location that was impacted by the health event.
Type: Array of strings
Required: No

 ** Latitude **   <a name="internetmonitor-Type-ImpactedLocation-Latitude"></a>
The latitude where the health event is located.
Type: Double
Required: No

 ** Longitude **   <a name="internetmonitor-Type-ImpactedLocation-Longitude"></a>
The longitude where the health event is located.
Type: Double
Required: No

 ** Metro **   <a name="internetmonitor-Type-ImpactedLocation-Metro"></a>
The metro area where the health event is located.
Metro indicates a metropolitan region in the United States, such as the region around New York City. In non-US countries, this is a second-level subdivision. For example, in the United Kingdom, it could be a county, a London borough, a unitary authority, council area, and so on.
Type: String
Required: No

 ** ServiceLocation **   <a name="internetmonitor-Type-ImpactedLocation-ServiceLocation"></a>
The service location where the health event is located.
Type: String
Required: No

 ** Subdivision **   <a name="internetmonitor-Type-ImpactedLocation-Subdivision"></a>
The subdivision location where the health event is located. The subdivision usually maps to states in most countries (including the United States). For United Kingdom, it maps to a country (England, Scotland, Wales) or province (Northern Ireland).
Type: String
Required: No

 ** SubdivisionCode **   <a name="internetmonitor-Type-ImpactedLocation-SubdivisionCode"></a>
The subdivision code where the health event is located. The ISO 3166-2 codes for country subdivisions is provided, when available.
Type: String
Required: No

## See Also
<a name="API_ImpactedLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/ImpactedLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/ImpactedLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/ImpactedLocation)
