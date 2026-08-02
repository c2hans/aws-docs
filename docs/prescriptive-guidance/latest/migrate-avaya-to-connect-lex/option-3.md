---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-avaya-to-connect-lex/option-3.html
---

# Option 3: Ingress to Connect Customer and egress to Avaya
<a name="option-3"></a>

![Architecture diagram of ingress to Amazon Connect and egress to Avaya for agent transfer](http://docs.aws.amazon.com/prescriptive-guidance/latest/migrate-avaya-to-connect-lex/images/guide-img/93ca74a8-da3b-48f9-a10f-4809a7f3384c/images/524cfd9b-79f8-471e-b0ff-07cf892cd7f9.png)

1. A customer calls the Connect Customer contact center. Connect Customer greets the customer with welcome menu and provides the caller with self-servicing menu options.

1. Connect Customer uses an AWS Lambda function to create a customer record in an Amazon DynamoDB database instance by using the UCID as a primary key.

1. Connect Customer initiates Amazon Lex to start self-servicing the call.

1. Amazon Lex invokes a dialog code hook and fulfills the intent by using a Lambda function.

1. The Lambda function inserts all of the customer attributes during the call and starts the routing process back to Avaya as follows:

   1. Connect Customer makes an API call to Amazon API Gateway.

   1. Amazon API Gateway starts a Lambda function that queries the Amazon DynamoDB database instance and fetches a DNIS outbound dialing number for Avaya. It blocks the DNIS number and passes the dialing number back to Amazon Lex.

   1. Amazon Lex passes the number back to Connect Customer in session attributes.

1. Connect Customer uses this number to dial back to Avaya.

1. Avaya makes an API call to Amazon API Gateway.

1. Amazon API Gateway initiates a Lambda function that fetches the customer attributes associated with this DNIS number and frees up the dialing number for future use.

1. Avaya routes the call and the customer attributes to the agent.

## Advantages
<a name="option-3-advantages"></a>
+ No additional hardware or licensing is required for Avaya.
+ No additional telephony lines are required because calls are direct to Connect Customer.

## Disadvantages
<a name="option-3-disadvantages"></a>
+ After the call is transferred to Avaya, you continue to be billed for voice service charges and telephony charges in Connect Customer because the customer called Connect Customer directly.
