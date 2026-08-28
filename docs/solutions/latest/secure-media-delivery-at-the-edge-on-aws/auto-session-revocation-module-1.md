---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/auto-session-revocation-module-1.html
---

# Auto session revocation module
<a name="auto-session-revocation-module-1"></a>

 CDK deployment model offers additional module that can be deployed as part of the solution, which gives a reference for how to automate the process of detecting suspicious sessions based on the set of selectable criteria and threshold adequate for your workload. Solution overview describes the end-to-end workflow of this module which is built around running Athena SQL queries against CloudFront access logs to collect session level metrics used to calculate suspicion score. You must provide multiple inputs before you start using auto session revocation as shown in the table.

|  Value  |  Description  |
| --- | --- |
|  Frequency of running auto session revocation module  |  In the range of minutes, express how often auto session revocation workflow will be initiated.  |
|  Athena Database name  |  Database name Athena SQL query will run against when initiated.  |
|  Athena Table name  |  Table name Athena SQL query will run against when initiated.  |
|  Request IP column  |  Name of the column in table schema which stores viewer’s IP.  |
|  UA column name  |  Name of the column in table schema which stores viewer’s user-agent header value.  |
|  Referer column name  |  Name of the column in table schema which stores viewer’s referrer header value.  |
|  URI column name  |  Name of the column in table schema which stores request URL path.  |
|  Status column name  |  Name of the column in table schema which indicates HTTP status code returned in the response returned to the request.  |
|  Response bytes column name  |  Name of the column in table schema which specifies response size in bytes sent to the viewer.  |
|  Data column name  |  nName of the column in table schema with representing the date when request was made.  |
|  Time column name  |  Name of the column in table schema representing the time when request was made.  |
|  Lookback period  |  Expressed in minutes, used to derive a time window for the log entries that will be considered for analysis. It spans from the current time back to the specific number of minutes as specified in this parameter.  |
|  IP penalty  |  Assumes true or false value. It informs whether the presence of multiple source IPs which used the same session ID should be considered as a suspicious factor.  |
|  IP rate  |  Assumes true or false value. It informs whether the request rate calculated for the session ID should be included in calculating suspicious factor.  |
|  Referer penalty  |  Assumes true or false value. It informs whether the presence of multiple referer headers which used the same session ID should be considered as a suspicious factor.  |
|  Multiple User-Agent penalty  |  Assumes true or false value. It informs whether the presence of multiple referer headers which used the same session ID should be considered as a suspicious factor.  |
|  Minimum sessions number  |  The minimal number of active playback sessions in the inspected time frame that must be met in order to produce any output.  |
|  Minimum session duration threshold  |  Expressed in minutes. A minimum period of time session must be active during analyzed time frame to be included for further analysis.  |
|  Score threshold  |  Suspicion score threshold. Any session that yields higher result will be included in the output and pushed to revocation table.  |
|  Partitioned access logs  |  True or false. Specify if your access logs are partitioned in S3 bucket per year, month, day and hour.  |

 Each of these inputs is used in one of the stages auto session revocation workflows which works as follows:

 **Prerequisites**

1.  Turn on [CloudFront access logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) and start collecting them in the target S3 bucket.

1.  Optionally, apply log processing pipeline to start partitioning log files to improve efficiency of running queries as described in [Analyze your Amazon CloudFront access logs at scale](https://aws.amazon.com/blogs/big-data/analyze-your-amazon-cloudfront-access-logs-at-scale/). Note that the solution assumes predefined partitioning model, in which log files are segregated by year, month, day, hour. All these partition levels must be available. Importantly, respective column names must be set to following values: **year**, **month**, **day**, **hour**.

1.  Create a database and the table which define table schema used when parsing and querying access logs. Take a note of **Athena Database name** and **Athena Table name.**

1.  When following CDK deployment path, provide **Athena Database name** and **Athena Table name** from the previous step in the CDK configuration wizard.

1.  If you implemented log partitioning mechanism in compliance with the mentioned requirements, set **Partitioned access logs** in the CDK configuration wizard to true.

 After auto session revocation module is deployed with the **Frequency of running auto session revocation module** you defined in the wizard, a workflow running SQL query through Athena will be executed.

 **Narrowing down requests in scope**

 If you inspect SQL query processed by Athena, you will find multitude of filtering condition included. It is important step in the process to obtain high signal output by removing access log entries which are irrelevant for outlier analysis and outside of the time boundaries that you want to investigate. For this reasons SQL query applies filtering criteria to scope down set of input log entries for further analysis based on:

1.  Request timestamp – consider only the requests that were recorded within the **Lookback** **period** defining point in time (current time minus **Lookback period**) for which any requests that was registered before is not factored in the calculations

1.  Returned response **Status** code – look only for the requests that were served with 200 or 206 responses

1.  Ignoring the entries when **Response bytes** size was lower than 1KB.

1.  Ruling out the sessions of very short duration within analyzed time frame (for instance newly started session), shorter than **Minimum session duration**

1.  Validating if the number of active sessions is during inspected timeframe is greater than **Minimum sessions number**. If not, no results will be returned

 **Calculate session-level metrics**

 After limiting the scope of the requests represented as log entries as per predefined criteria, for each session a set of metrics will be calculated from the information contained the log entries:
+  Request rate for each session relative to request rate measured at p50 against all the sessions. For this metric, request rate calculated for each session is a count of distinct source IP and request URL pairs for each session. This will keep the result consistent if client retrieves a single object by making multiple byte range requests. Session level request rate is normalized with p50 request value, output result of this metric should be approximately close to 1.0. The greater the value the more requests use the same session ID which suggests that the same session is shared by multiple viewers. This metric will be added to the final suspicion score if **IP Rate** parameter is set to true.
+  Signal of multiple user-agents using the same session ID, based on user-agent header value found in **UA column.** This metric equals to two discrete values: 0 or 1, the latter one indicating presence of more than one user-agent values in the access logs. If **Multiple User-Agent penalty** is set to true, this value will be added to the suspicion score.
+  Signal of multiple referer headers values using the same session ID, based on referer header value found in **Referer column name.** This metric equals to two discrete values: 0 or 1, the latter one indicating presence of more than one user-agent values in the access logs. If **Referer penalty** is set to true, this value will be added to the suspicion score.
+  Signal of multiple source IPs using the same session ID, based on IP information included in **Request IP column.** This metric equals to two discrete values: 0 or 1, the latter one indicating presence of more than one viewer IP values in the access logs. If **IP penalty** is set to true, this value will be added to the suspicion score.

 With all the metrics calculated for each of the of the session that was left in the scope of analysis, the final suspicion score is derived as a sum of all the components mentioned:

 **Suspicion Score = Request IP rate \+ IP penalty \+ Referrer penalty \+ UA penalty **

 The last three components can only have a discrete value of either `0` or `1` each. Request IP rate is linear value that can vary from `0` and is not bounded by upper value. A typical score for a session should stay in close proximity of `1.0` as if session is used by a single viewer all the penalty factors should equal to `0` and Request IP rate should be close to `1.0` as some variance from median (p50 value) is possible. At times, score value can be elevated even when used by a single user. That can occur for a new playback session when player fills the buffer and would request multiple segments in a short period of time, or when viewer switches the network which would set the IP penalty factor to `1`.

 Having suspicion scores in place for each session, the final output list includes only the ones exceeding **Score threshold.** The list is supplied to the Lambda function in the Step Functions workflow, which sorts and prioritizes the sessions that will be eventually placed in the WAF rule group responsible for blocking compromised sessions. Refer to the [Architecture details](architecture-details.md) section for more details.

 Note that the default and suggested value of **Score threshold** is set to `2.2` which accounts for the momentary increase in the score that stems from the situations mentioned before. We recommend that you keep track of the resulting suspicion scores calculated during the tests for a representative viewership and content, and validate whether majority of the sessions yield the score within the threshold you have set.

 **Normalized IP request rate**

 One of the primary components that can impact the suspicion score for all the sessions is **Request IP rate** as this component value is not bounded and is relative to the median value calculated for all the session in the analyzed score. Because the calculation of this metric strongly depends on the normalization factor, it is important that this factor is stable and cannot be easily distorted by a few sessions that have been compromised, even to a large extent. To achieve the desired stability and prevent fluctuation of that factor in the presence of one or few sessions which have been compromised on a significant scale, 50th percentile (p50) measure is used instead of the average as a normalization factor.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
