---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/reference.html
---

# Reference
<a name="reference"></a>

This section includes information about an optional feature for collecting anonymized metrics for this guidance and a [list of builders](#contributors) who contributed to this guidance.

## Operational metrics
<a name="operational-metrics"></a>

This guidance includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this guidance and related services and products.

When a Trusted Access or Delegate Admin scan is started, the following information is collected and sent to AWS:
+  **Solution ID** – The AWS solution identifier
+  **Unique ID (UUID)** – Randomly generated, unique identifier for each Guidance for Account Assessment for AWS Organizations deployment
+  **Timestamp** – Data-collection timestamp
+  **Version** – Solution version deployed
+  **Assessment type** – `DelegatedAdmin`, `TrustedAccess`
+  **Findings count** – Number of findings found during scan
+  **Services count** – Number of AWS services found during scan
+  **Accounts count** – Number of accounts found during scan
+  **Regions count** – Number of AWS Regions found during scan

When a search is conducted using the Policy Explorer, the following information is collected and sent to AWS:

Example data:

```
Solution ID: The AWS solution identifier
Unique ID (UUID) - Randomly generated, unique identifier for each Guidance for Account Assessment for AWS Organizations deployment
Timestamp - Data-collection timestamp
Version - Solution version deployed
Assessment type - "PolicyExplorerSearch"
Region - The region used as search filter
*Filters - The key for each search filter input, as well as the length of its input value.  The user entered value is not collected.*
```

AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/). To opt out, change the `AnonymousData` mapping in the Hub stack’s AWS CDK source code before you build and deploy the guidance. For instructions, see [Deployment process overview](deploy-the-guidance.md#deployment-process-overview).

## Contributors
<a name="contributors"></a>
+ Lalit Grover
+ Thiemo Belmega
+ Nikhil Reddy
+ Mykhailo Markhain
