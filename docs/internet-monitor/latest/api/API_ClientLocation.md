---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_ClientLocation.html
---

# ClientLocation
<a name="API_ClientLocation"></a>

The impacted location, such as a city, that AWS clients access application resources from.

## Contents
<a name="API_ClientLocation_Contents"></a>

 ** ASName **   <a name="internetmonitor-Type-ClientLocation-ASName"></a>
The name of the internet service provider (ISP) or network (ASN).
Type: String
Required: Yes

 ** ASNumber **   <a name="internetmonitor-Type-ClientLocation-ASNumber"></a>
The Autonomous System Number (ASN) of the network at an impacted location.
Type: Long
Required: Yes

 ** City **   <a name="internetmonitor-Type-ClientLocation-City"></a>
The name of the city where the internet event is located.
Type: String
Required: Yes

 ** Country **   <a name="internetmonitor-Type-ClientLocation-Country"></a>
The name of the country where the internet event is located.
Type: String
Required: Yes

 ** Latitude **   <a name="internetmonitor-Type-ClientLocation-Latitude"></a>
The latitude where the internet event is located.
Type: Double
Required: Yes

 ** Longitude **   <a name="internetmonitor-Type-ClientLocation-Longitude"></a>
The longitude where the internet event is located.
Type: Double
Required: Yes

 ** Metro **   <a name="internetmonitor-Type-ClientLocation-Metro"></a>
The metro area where the health event is located.
Metro indicates a metropolitan region in the United States, such as the region around New York City. In non-US countries, this is a second-level subdivision. For example, in the United Kingdom, it could be a county, a London borough, a unitary authority, council area, and so on.
Type: String
Required: No

 ** Subdivision **   <a name="internetmonitor-Type-ClientLocation-Subdivision"></a>
The subdivision location where the health event is located. The subdivision usually maps to states in most countries (including the United States). For United Kingdom, it maps to a country (England, Scotland, Wales) or province (Northern Ireland).
Type: String
Required: No

## See Also
<a name="API_ClientLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/ClientLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/ClientLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/ClientLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Internet Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query internet-monitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
