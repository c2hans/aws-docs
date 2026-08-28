---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/license-consumption.html
---

# Check out seller issued licenses in License Manager
<a name="license-consumption"></a>

License Manager allows multiple users to concurrently consume entitlements, with limited capabilities, from a single license. Call the [CheckoutLicense](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CheckoutLicense.html) API action. The following is a description of the parameters.
+ **Key fingerprint** – Trusted license issuer.

  Example: aws:123456789012:issuer:issuer-fingerprint
+ **Product SKU** – Product identifier for this license, as defined by the license issuer when creating the license. The same product SKU might exist across multiple ISVs. Therefore, trusted key fingerprints play an important role.

  Example: 1a2b3c4d2f5e69f440bae30eaec9570bb1fb7358824f9ddfa1aa5a0daEXAMPLE
+ **Entitlements** – Capabilities to check out. If you specify an unlimited capability, the quantity is zero. Example:

  ```
  "Entitlements": [
      {
          "Name": "DataTransfer",
          "Unit": "Gigabytes",
          "Value": 10
      },
      {
          "Name": "DataStorage",
          "Unit": "Gigabytes",
          "Value": 5
      }
  ]
  ```
+ **Beneficiary** – Software as a Service (SaaS) ISVs can check out licenses on behalf of a customer by including the customer identifier. License Manager limits the call to the repository of licenses created in the SaaS ISV account.

  Example: user@domain.com
+ **Node ID** – An identifier used to node-lock the license to a single instance of the application.

  Example: 10.0.21.57

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
