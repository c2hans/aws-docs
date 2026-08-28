---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-avaya-to-connect-lex/option-2.html
---

# Option 2: Ingress to Avaya and egress to Connect Customer
<a name="option-2"></a>

![Architecture diagram of ingress to Avaya and egress to Amazon Connect by using a conference call](http://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-avaya-to-connect-lex/images/guide-img/93ca74a8-da3b-48f9-a10f-4809a7f3384c/images/80e47f86-d554-4a5a-bdca-ae18710ac9b8.png)

1. A customer calls the on-premises Avaya contact center. Avaya greets the caller with the welcome menu and provides the caller with self-servicing menu options.

1. Avaya uses an on-premises API to send the customer information and a unique customer identifier (UCID) to the Concentrix IVR.

1. The Concentrix IVR starts the process of transferring the call to Connect Customer as follows:

   1. The Concentrix IVR makes an API call to Amazon API Gateway. This initiates an AWS Lambda function.

   1. The Lambda function queries the Amazon DynamoDB database instance and fetches an available DNIS outbound dialing number for transferring the call to Connect Customer. After the number is selected, Avaya blocks the number so that it can't be used for other calls.

1. Avaya starts a conference call to Connect Customer by using the number retrieved in the previous step and passes the DNIS number and UCID to Connect Customer.

1. An Connect Customer contact flow initiates a Lambda function that fetches the customer attributes by using the DNIS number as a primary key. The Lambda function frees the DNIS number so that other calls can consume it.

1. Connect Customer passes the customer attributes to Amazon Lex. Amazon Lex starts self-servicing the call.

1. Amazon Lex invokes a dialog code hook and fulfills the intent by using a Lambda function.

1. The Lambda function inserts all of the customer attributes during the call.

1. If the customer is disconnected from Connect Customer, Avaya can detect the call disconnect and call back the customer to include them in the ongoing conference.

1. Avaya makes an API call to Amazon API Gateway.

1. Amazon API Gateway initiates a Lambda function that fetches the customer attributes associated with the DNIS number.

1. Avaya routes the call and the customer attributes to the agent.

## Advantages
<a name="option-2-advantages"></a>
+ The migration is less complex because Avaya doesn't need to forward the call metadata, such as customer authentication, lookup, configuration, and language selection, to Connect Customer.
+ If you migrate the on-premises systems to AWS at a later time, redesign is not required.
+ Because Avaya is conferencing with Connect Customer and pulling the call back after self-servicing is done, there are no AWS billing costs associated with the agent portion of the call duration.

## Disadvantages
<a name="option-2-disadvantages"></a>
+ Additional hardware and licenses are required, based on the number of concurrent calls.
+ Additional telephony lines are required to transfer the call.
+ If you need to pass data from Avaya to Connect Customer, you need to build additional architecture to support the data transfer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
