---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/reference.html
---

# Reference
<a name="reference"></a>

This section includes information about an optional feature for collecting unique metrics for this guidance and a [list of builders](#contributors) who contributed to this guidance.

## Anonymized data collection
<a name="anonymized-data-collection"></a>

This guidance includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this guidance and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID** - The AWS solution identifier
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each Scalable Analytics using Apache Druid on AWS deployment
+  **Timestamp** - Data-collection timestamp

AWS owns the data gathered though this survey. Data collection is subject to the [Privacy Notice](https://aws.amazon.com/privacy/).

## Opt out of operational metrics collection
<a name="opt-out-of-operational-metrics-collection"></a>

To opt out of this feature, for the guidance parameters, in cdk.json, set the **sendAnonymousData** parameter to `No`.

## Contributors
<a name="contributors"></a>
+ Frank Cao
+ Van Vo Thanh
+ Hafiz Saadullah
+ Marc Teichtahl
+ Swapnil Ogale
+ APJ Solutions Engineering team
+ Jason Wreath
+ James Ousby
+ Matt Jobson
+ Chris Merrigan
+ Gaurav Bhatnagar
+ Verinder Singh
+ Steven Hogarth
