---
source_url: https://docs.aws.amazon.com/marketplace/latest/userguide/supplemental-tax-registrations.html
---

# Supplemental tax registrations

If you use a local Tax Registration Number (TRN) for sales in a specific locality, you can add it as a supplemental TRN to your AWS Marketplace account. For example, a supplemental Swiss TRN is used to manage tax collection and invoicing for Swiss buyers. The business address associated with supplemental TRN may be shared with independent software vendors, channel partners, and buyers.

Without a supplemental TRN, AWS Marketplace determines tax jurisdiction using the primary TRN. For more information, see [How does AWS determine the location of your account?](https://aws.amazon.com/tax-help/location/)

You manage supplemental tax registrations for each jurisdiction on the **Global tax management** tab of the **Tax and invoices** page. Each jurisdiction lists its **Invoicing entity**, **Status**, and **Tax requirement** (for example, Switzerland – AWS Switzerland Sàrl – Tax ID (multiple tax profiles)). Sellers based outside India also use the India jurisdiction on this tab to upload their India tax documents. For more information, see [Provide India tax documents](tax-services.md#tax-services-india-tax-documents).

**To add a supplemental tax registration**

1. Sign in to AWS Partner Central at [https://us-east-1.console.aws.amazon.com/partnercentral/home](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. In the left navigation pane, under **Settings**, choose **Tax and invoices**.

1. Choose the **Global tax management** tab.

1. Select the jurisdiction (for example, Switzerland), and then choose **View details**, or choose the jurisdiction name. The tax details page for that country opens.

1. Choose **Add registration** (or **Add supplemental tax registration**).

1. Under **Tax registration details**, enter the **Tax registration number (TRN)** and **Business name** (up to 200 characters). **Country or region** is filled in for you. For example, a Swiss TRN looks like CHE-123.456.789MWST.

1. Under **Business address**, enter the address to use for reports and invoices (**Address line 1**, **Address line 2** (optional), **City**, **State or province** (optional), and the remaining fields).

1. Choose **Submit**. The registration appears in the **Supplemental tax registration** section with its **Status**, TRN, business name, and business address. The **Tax summary** on the tax details page shows the **Supplemental tax registration status** and **Tax compliance status**.

**To delete a supplemental tax registration**

1. On the tax details page for the country, in the **Supplemental tax registration** section, select the registration.

1. Choose **Delete**.

**Note**
You can't delete a registration while its status is **Pending**. **Delete** becomes available after verification completes.
A TRN can be a value-added tax (VAT) number, VAT ID, VAT registration number, or Business Registration Number.
