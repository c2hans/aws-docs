---
source_url: https://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/working-with-proposals.html
---

End of support notice: On May 28, 2026, AWS will end support for AWS IQ. After May 28, 2026, you will no longer be able to access the AWS IQ console or AWS IQ resources. For more information, see [AWS IQ end of support](https://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/aws-iq-end-of-support.html).

# Working with proposals in AWS IQ
<a name="working-with-proposals"></a>

To formalize an agreement with a customer in AWS IQ, create a proposal. The proposal can include details about the work to be performed, the project milestones, the timeline for payments, and any additional terms. The proposal also includes the maximum amount to charge the customer.

Customers review and accept or decline proposals in the AWS IQ console.

You can withdraw a proposal, or a customer can decline a proposal if the proposal doesn't meet their needs. You and the customer can discuss what changes are needed through a chat session or a call, and then you submit a new proposal for approval.

**Note**
AWS IQ doesn't support modifying a proposal after it's created. If you need to make changes to a proposal, withdraw the proposal and create a new one.

## Create a proposal
<a name="expert-guide-create-proposal"></a>

Create a proposal in the AWS IQ console after you have enough information to understand a customer request. If you need more information before proceeding, chat with the customer or set up a call to discuss the details.

## To create a customer proposal in AWS IQ

1. Sign in to the AWS IQ console at [https://iq.aws.amazon.com/](https://iq.aws.amazon.com/).

1. On the **Requests** page, choose **Conversations**.

1. Choose the customer request for the proposal you are creating.

1. In the **Proposals** pane, choose **Create**.

1. Choose your **Payment Type** by selecting **Milestone**, **Upfront**, or **Schedule**. For more information about payment types, see [Working with payment types in AWS IQ](payment-types.md).

   1. If you select **Schedule**, choose a date and amount to charge the customer. Choose **Add payment** to enter a new scheduled payment. The total amount of this proposal is the sum of all payments.

   1. If you select **Upfront**, specify a total amount for the proposal.

      This is the amount your customer is charged when they approve the proposal. You can't request additional payments on this proposal.

   1. If you select **Milestone**, specify a total amount for the proposal.

      This is the maximum amount you can request in payments. To request more, you must create an additional proposal. For more information, see [Working with milestone payment requests in AWS IQ](working-with-payment-requests.md).

1. In the **Proposal Terms** text box, describe what you will deliver to the customer. Include the terms for this project, milestones, and any necessary changes to the Engagement Agreement.

   Limited Markdown styling is supported. For more details, see the following [Markdown guide](#expert-proposals-supported-markdown).

1. When you're finished writing your proposal, choose **Send**.

   The customer will receive the proposal and accept or decline it.

## Complete a proposal
<a name="expert-guide-complete-a-proposal"></a>

After you have completed the work or collected all payments, you can close a proposal by using the AWS IQ console. You can close a proposal by sending the final payment request or closing without a payment request. After completing a proposal, you can't send payment requests and any previously scheduled payment requests will be canceled.

## To complete a customer proposal in AWS IQ

1. Sign in to the AWS IQ console at [https://iq.aws.amazon.com/](https://iq.aws.amazon.com/).

1. On the **Requests** page, choose **Conversations**.

1. Choose the customer request for the proposal that you're completing.

1. Close the proposal by sending a final payment request to the customer. For more information, see [Working with milestone payment requests in AWS IQ](working-with-payment-requests.md).

1. If there are no additional payments needed, select the proposal that you want to close, and then choose **Complete**.

**Note**
If there are open payment requests for the proposal, you won't be able to use the **Complete** feature. After you complete the proposal, you won't have access to the customer's account and can't request additional payments.

## Markdown guide
<a name="expert-proposals-supported-markdown"></a>

You can format the text in your proposal using the following Markdown styles.

| Formatting | Markdown | Display |
| --- | --- | --- |
| Bold text | \*\*Apples\*\* | Apples |
| Italic text | \*Apples\* or \_Apples\_ | Apples |
| Hyperlinks | [Amazon](https://smile.amazon.com) | [Amazon](https://smile.amazon.com) |
| Bulleted lists |  <pre>* Apples<br />* Oranges<br />* Pears</pre>  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/working-with-proposals.html)  |
| Numbered lists |  <pre>1. Apples<br />2. Oranges<br />3. Pears</pre>  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/working-with-proposals.html)  |
