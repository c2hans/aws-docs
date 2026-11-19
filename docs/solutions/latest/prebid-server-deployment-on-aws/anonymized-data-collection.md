---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/anonymized-data-collection.html
---

# Anonymized data collection

This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID** - The AWS solution identifier
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each solution deployment
+  **Timestamp** - Data-collection timestamp

We collect metrics directly from the various resources in the solution. These are filtered for the last 24 hours. The name of each metric comes from the service and is defined by that service. **DeleteEfsFiles** and **StartGlueJob** are our counts.

AWS owns the data gathered through this survey. Data collection is subject to the [Privacy Notice](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before deploying using AWS CDK.

1. In your local copy of the repository, open [source/infrastructure/lib/shared/solution-stack.ts](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws/blob/main/source/infrastructure/lib/shared/solution-stack.ts).

1. In the `Solution` mapping, change the value of `SendAnonymizedData` from `"Yes"` to `"No"`.

1. Follow the deployment steps documented in the readme.
