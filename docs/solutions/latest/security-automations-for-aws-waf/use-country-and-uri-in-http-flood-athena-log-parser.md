---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/use-country-and-uri-in-http-flood-athena-log-parser.html
---

# Use country and URI in HTTP flood Athena log parser
<a name="use-country-and-uri-in-http-flood-athena-log-parser"></a>

You can group by IPs along with country and URI in the Athena query to detect and block HTTP flood attacks that have unpredictable URI patterns. To do so, select one of the options (`Country`, `URI`, `Country and URI`) for the **Group By Requests in HTTP Flood Athena Query** parameter when [launching the stack](step-1.-launch-the-stack.md).

You can also enter a request threshold by country using the **Request Threshold by Country** parameter. For example, `{"TR": 50,"ER":150}`. The solution uses these thresholds on the requests originated from these specified countries. The solution uses the default threshold on the requests from other countries.

**Note**
If you define a threshold by country, the solution automatically includes the country in the Athena query group-by clause. For more information, see the parameters table in [Step 1. Launch the stack](step-1.-launch-the-stack.md).

The solution counts the request threshold in a five-minute period by default. This is configurable with the **Athena Query Run Time Schedule (Minute)** parameter.

**Note**
The Athena query calculates threshold per minute by dividing the request threshold by the time period. For example:
 *Request threshold (default threshold or threshold by country): 100*
 *Athena Query Run Time Schedule: 5*
 *Request threshold per minute: 20 = 100 / 5*
