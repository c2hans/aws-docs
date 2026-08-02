---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-avaya-to-connect-lex/option-1.html
---

# Option 1: Ingress to Avaya and egress to Amazon Lex
<a name="option-1"></a>

![Architecture diagram of ingress to Avaya and egress to Amazon Lex by using call transfers](http://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-avaya-to-connect-lex/images/guide-img/93ca74a8-da3b-48f9-a10f-4809a7f3384c/images/bc4c83c0-0c4d-489e-a376-8bf6d09f7053.png)

1. A customer calls the on-premises Avaya contact center. Avaya greets the caller with the welcome menu and provides the caller with self-servicing menu options.

1. Avaya uses an on-premises API to send the customer information and a unique customer identifier (UCID) to the Concentrix IVR.

1. The Concentrix IVR starts the process of transferring the call to Connect Customer as follows:

   1. The Concentrix IVR makes an API call to Amazon API Gateway. This initiates an AWS Lambda function.

   1. The Lambda function queries the Amazon DynamoDB database instance and fetches an available Dialed Number Identification Service (DNIS) outbound dialing number for transferring the call to Connect Customer. After the number is selected, the Lambda function blocks the number in DynamoDB so that it can't be used for other calls.

1. Avaya calls Connect Customer by using the number retrieved in the previous step and passes the DNIS number and the UCID to Connect Customer.

1. When the call is connected with Connect Customer, an Connect Customer contact flow initiates a Lambda function that fetches the customer data from the DynamoDB table by using the DNIS number of the current interaction.

1. Connect Customer passes the customer attributes to Amazon Lex. Amazon Lex starts self-servicing the call.

1. Amazon Lex invokes a [dialog code hook](https://docs.aws.amazon.com/lexv2/latest/dg/paths-code-hook.html) and fulfills the intent by using a Lambda function.

1. The Lambda function inserts all of the customer attributes during the call and starts the routing process back to Avaya as follows:

   1. Connect Customer makes a call to a Lambda function.

   1. The Lambda function selects the available outbound dialing number for Avaya, blocks the DNIS number, and passes the dialing number back to Amazon Lex.

   1. Amazon Lex passes the number back to Connect Customer in session attributes.

1. Connect Customer uses this number to return the call back to Avaya.

1. Avaya makes an API call to Amazon API Gateway.

1. Amazon API Gateway initiates a Lambda function that fetches the customer attributes associated with the DNIS number and frees up the number for future use.

1. Avaya routes the call and the customer attributes to the agent.

## Advantages
<a name="option-1-advantages"></a>
+ Better customer experience
+ No additional hardware or licensing required
+ No additional telephony lines required because calls are transferred to Connect Customer
+ Quick turn-around time to implement

## Disadvantages
<a name="option-1-disadvantages"></a>
+ Data** **can't be passed over a public switched telephone network (PSTN) line. This architecture depends on the exchange of customer data between the on-premises and AWS contact center systems, which can't be done over a PSTN line.
+ Additional costs are incurred for the duration of the active call session in Connect Customer and for call transfers to other telephonic systems.
+ Additional effort is required to build the flows in Connect Customer.
