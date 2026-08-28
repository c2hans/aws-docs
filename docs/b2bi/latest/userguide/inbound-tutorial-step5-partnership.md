---
source_url: https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-tutorial-step5-partnership.html
---

# Step 5: Create a partnership
<a name="inbound-tutorial-step5-partnership"></a>

A partnership represents your trading relationship with a business partner. It combines your profile with trading capabilities and defines how to handle inbound EDI documents, including acknowledgment generation settings.

**To create a partnership**

1. In the AWS B2B Data Interchange console, choose **Partnerships**.

1. Choose **Create partnership**.

1. In the **Partnership details** section, enter:
   + **Partnership name**: **SupplierABC-Partnership**
   + **Email**: **edi@supplierabc.example.com**
   + **Profile**: Select **AcmeCorpProfile**
   + **Trading capabilities**: Select **Inbound-850-Processing**

1. In the **Inbound EDI configuration** section:
   + **TA1 Technical Acknowledgments**: Select **Do not generate**
   + **Functional (997 and 999) Acknowledgments**: Select **Generate 997**
   + **Include AK2 loop**: Leave unchecked

1. Optionally, add tags:
   + Key: **Partner**, Value: **SupplierABC**
   + Key: **DocumentType**, Value: **PurchaseOrder**

1. Choose **Create partnership**.

## Required fields
<a name="inbound-step5-required-fields"></a>
+ Partnership name
+ Email address
+ Profile selection
+ Trading capabilities selection

## Example data used
<a name="inbound-step5-example-data"></a>
+ Partnership name: SupplierABC-Partnership
+ Email: edi@supplierabc.example.com
+ Profile: AcmeCorpProfile
+ Trading capability: Inbound-850-Processing

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
