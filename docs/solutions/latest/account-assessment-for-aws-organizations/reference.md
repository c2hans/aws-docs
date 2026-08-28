---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/reference.html
---

# Reference
<a name="reference"></a>

This section includes information about an optional feature for collecting anonymized metrics for this solution and a [list of builders](#contributors) who contributed to this solution.

## Operational metrics
<a name="operational-metrics"></a>

This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products.

When a Trusted Access or Delegate Admin scan is started, the following information is collected and sent to AWS:
+  **Solution ID** – The AWS solution identifier
+  **Unique ID (UUID)** – Randomly generated, unique identifier for each Account Assessment for AWS Organizations deployment
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
Unique ID (UUID) - Randomly generated, unique identifier for each Account Assessment for AWS Organizations deployment
Timestamp - Data-collection timestamp
Verion - Solution version deployed
Assessment type - "PolicyExplorerSearch"
Region - The region used as search filter
*Filters - The key for each search filter input, as well as the length of its input value.  The user entered value is not collected.*
```

AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the Hub stack CloudFormation template:

1. Download the `account-assessment-for-aws-organizations-hub.template`[AWS CloudFormation template](aws-cloudformation-templates.md) to your local hard drive.

1. Open the CloudFormation template with a text editor.

1. Modify the CloudFormation template mapping section from:

   ```
   AnonymousData:
       SendAnonymousData:
         Data: Yes
   ```

   to:

   ```
   AnonymousData:
       SendAnonymousData:
         Data: No
   ```

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. Select **Create stack**.

1. On the **Create stack** page, **Specify template** section, select **Upload a template file**.

1. Under **Upload a template file**, select **Choose file**, then select the edited template from your local drive.

1. Choose **Next** and follow the steps in [Launch the Hub stack](step-2-launch-the-spoke-stack.md).

## Contributors
<a name="contributors"></a>
+ Lalit Grover
+ Thiemo Belmega
+ Nikhil Reddy
+ Mykhailo Markhain

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account Assessment for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
