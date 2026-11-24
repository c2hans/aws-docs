---
source_url: https://docs.aws.amazon.com/marketplace/latest/userguide/vat-on-deemed-supply.html
---

# VAT on Deemed Supply

Under EU, Norway and UK VAT rules, when AWS Marketplace facilitates the sale of Digital Services (e.g. SaaS, AMI), the law establishes two back-to-back supplies for VAT purposes only:
+ **Deemed Sale 1:** The Seller is treated as having supplied the Digital Service to the applicable branch of Amazon Web Services EMEA SARL ("AWS EMEA") facilitating the transaction.
+ **Deemed Sale 2:** The branch of AWS EMEA facilitating the transaction is treated as having supplied the Digital Service to the Buyer.

As a result of the Deemed Supply provisions, when both the Seller and the Buyer are in the same EU Member State, Norway or in the UK, and the transaction is facilitated by the relevant AWS EMEA branch in the same country, the Seller is expected to issue a VAT invoice to that AWS EMEA branch. AWS EMEA will pay the VAT stated on the invoice, subject to receipt of a valid VAT invoice.

You can submit invoices for transactions of AWS Marketplace sales of Digital Services where all three of the following conditions are met:

1. The Seller AWS account is located in an EU Member State, the UK or Norway.

1. The Buyer AWS account is located in the same country as the Seller.

1. The AWS Marketplace sale is facilitated by the corresponding AWS EMEA SARL branch in that country.

VAT on deemed supply lets EMEA-based sellers recover VAT on eligible AWS Marketplace sales and remit it to their tax authority. AWS Marketplace automatically identifies eligible payables so that you can review and submit them for disbursement. You can start from the **VAT on deemed supply** card (**Get started**) or the **VAT on deemed supply** tab on the **Tax and invoices** page in AWS Partner Central.

## Getting Started — How to view and submit your invoices for VAT on deemed supply
<a name="vat-deemed-supply-getting-started"></a>

### Step 1: Open the VAT on deemed supply tab
<a name="vat-deemed-supply-step1"></a>

1. Sign in to AWS Partner Central at [https://us-east-1.console.aws.amazon.com/partnercentral/home](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. In the left navigation pane, under **Settings**, choose **Tax and invoices**.

1. Choose the **VAT on deemed supply** tab, or choose **Get started** on the **VAT on deemed supply** card.

### Step 2: Select eligible payables
<a name="vat-deemed-supply-step2"></a>

1. In **VAT on deemed supply eligible payables**, select one or more payables in the same currency. To filter the list, use **Date range** and **Find eligible payables**. Each payable shows **Payable ID**, **AWS invoice ID**, **Offer ID**, **Payable status**, **Created on**, and **Offer currency**.

1. Choose **Apply disbursement**. The **Apply VAT on deemed supply** page opens.

### Step 3: Review the summary
<a name="vat-deemed-supply-step3"></a>

1. Review the **VAT on deemed supply summary**. Use the **Business location**, **AWS EMEA local VAT number**, and **Tax registration number** shown here when you issue your invoice to AWS.

1. Review the **Disbursement summary** (**Paid payables**, **Unpaid payables**, **Total VAT disbursement amount**, and **Total eligible VAT disbursement amount**) and the **Selected payables** table (**VAT percentage**, **Net amount**, **VAT amount**, and **Payable total**).

### Step 4: Upload your seller invoice and apply the disbursement
<a name="vat-deemed-supply-step4"></a>

1. Under **Upload seller invoice**, choose **Choose seller invoice** and upload a single invoice that covers every selected payable. The file must be PDF, or XML for transactions in Italy, Poland, Belgium, Romania, or Croatia. The maximum file size is 10 MB. For more information about e-invoicing requirements, see [Do I need to submit an e-invoice instead of a PDF?](vat-deemed-supply-faq.md#faq-e-invoicing).

1. (Optional) Add tags, and then choose **Apply disbursement**.

Only verified, paid payables are disbursed immediately on approval. Unpaid payables are disbursed after the buyer pays. Missing or incorrect information results in rejection and processing delays.

### Step 5: Track your submissions
<a name="vat-deemed-supply-step5"></a>

On the **VAT on deemed supply** tab, the **VAT on deemed supply submissions** table lists each request with **Submission ID**, **Seller invoice ID**, **Submission status**, **VAT amount**, and **Date submitted**. To review a submission, select it and choose **View details**. Submission statuses are:
+ **Accepted** — Your invoice has been validated. No further action is required.
+ **Rejected** — Your invoice could not be validated. Review the submission with **View details**, correct the issue, and submit again.
+ **Pending** — Your submission is under review and is pending AWS for approval. (SLA: up to 3 business days).

**Note**
Disbursed VAT amounts are shown in Insights. To check your disbursement status, visit the Collections and Disbursements dashboard.

Refer to [Deemed Supply FAQs](vat-deemed-supply-faq.md) for more details.

## Submit a credit note for a refund
<a name="vat-deemed-supply-refunds"></a>

If AWS previously disbursed VAT to you for a transaction that is later refunded, you can submit the corresponding credit note directly in AWS Partner Central. When you finish, your credit note is submitted for validation and you can track its status in the submissions table.

### Step 1: Find the refund
<a name="vat-deemed-supply-refunds-step1"></a>

On the **Tax and invoices** page in AWS Partner Central, choose the **VAT on deemed supply** tab. Refunds appear in the same **VAT on deemed supply eligible payables** table as forward charges. Locate the refund that you want to submit a credit note for. Refunds display negative amounts.

If you do not see an expected refund:
+ Confirm that your selected date range includes the transaction.
+ Allow up to 72 hours after the Buyer refund is generated for the refund to appear.

### Step 2: Select the refund and upload your credit note
<a name="vat-deemed-supply-refunds-step2"></a>

Select the refund payables covered by your credit note, and then choose **Apply disbursement**. Under **Upload seller invoice**, choose **Choose seller invoice** and upload the applicable credit-note document:
+ Use PDF where electronic invoicing is not required.
+ Use the applicable XML format where electronic invoicing is required.
+ The maximum file size is 10 MB.

**Note**
You can include multiple eligible refunds in one submission when the portal allows them to be selected together. You can select up to 100 eligible payables in a submission.

### Step 3: Review and submit
<a name="vat-deemed-supply-refunds-step3"></a>

Review the selected refund payables and the details of your credit note. Confirm that the VAT amount on your credit note matches the VAT amount displayed for the selected refunds. When prompted to confirm the total, enter the amount exactly as displayed, including the minus sign where applicable.

Choose **Apply disbursement** and complete the confirmation.

**Note**
Submitting a credit note does not itself trigger VAT recovery. For more information about when AWS recovers VAT, see [Does submitting a credit note trigger VAT recovery?](vat-deemed-supply-faq.md#faq-refund-recovery-trigger).

### Step 4: Track your credit-note submission
<a name="vat-deemed-supply-refunds-step4"></a>

After submitting your credit note, use the VAT on deemed supply submissions table to track its status. Your submission can show:
+ **Pending** – AWS received the document and is reviewing it.
+ **Accepted** – AWS successfully validated the document.
+ **Rejected** – The document did not pass validation and needs to be corrected.

If your credit note is rejected, the applicable refund payables become available again so that you can correct the document and submit a new credit note.

For more information about credit-note requirements, VAT recovery, document formats, and rejected submissions, see [Deemed Supply FAQs](vat-deemed-supply-faq.md).
