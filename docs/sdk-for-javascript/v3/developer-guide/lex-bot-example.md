---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/lex-bot-example.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Building an Amazon Lex chatbot
<a name="lex-bot-example"></a>

You can create an Amazon Lex chatbot within a web application to engage your web site visitors. An Amazon Lex chatbot is functionality that performs on-line chat conversation with users without providing direct contact with a person. For example, the following illustration shows an Amazon Lex chatbot that engages a user about booking a hotel room.

![Chatbot interface demonstrating a hotel booking conversation with user inputs and bot responses.](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/lex_example/chatintro.png)

The Amazon Lex chatbot created in this AWS tutorial is able to handle multiple languages. For example, a user who speaks French can enter French text and get back a response in French.

![Chatbot interface demonstrating Amazon Lex integration with French language support.](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/lex_example/LanChatBot2.png)

Likewise, a user can communicate with the Amazon Lex chatbot in Italian.

![Chatbot interface showing Italian conversation with user message on left and bot response on right.](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/lex_example/LanChatBot3.png)

This AWS tutorial guides you through creating an Amazon Lex chatbot and integrating it into a Node.js web application. The AWS SDK for JavaScript (v3) is used to invoke these AWS services:
+ Amazon Lex
+ Amazon Comprehend
+ Amazon Translate

**Cost to complete:** The AWS services included in this document are included in the [AWS Free Tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc).

**Note:** Be sure to terminate all of the resources you create while going through this tutorial to ensure that you’re not charged.

**To build the app:**

1. [Prerequisites](#lex-bot-example-prerequisites)

1. [Provision resources](#lex-bot-provision-resources)

1. [Create Amazon Lex chatbot](#lex-bot-example-create-lex-bot)

1. [Create the HTML](#lex-bot-example-html)

1. [Create the browser script](#lex-bot-example-script)

1. [Next steps](#lex-bot-example-next-steps)

## Prerequisites
<a name="lex-bot-example-prerequisites"></a>

To set up and run this example, you must first complete these tasks:
+ Set up the project environment to run these Node TypeScript examples, and install the required AWS SDK for JavaScript and third-party modules. Follow the instructions on[ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cross-services/lambda-scheduled-events/README.md).
+ Create a shared configurations file with your user credentials. For more information about providing a shared credentials file, see [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

**Important**
This example uses ECMAScript6 (ES6). This requires Node.js version 13.x or higher. To download and install the latest version of Node.js, see [Node.js downloads.](https://nodejs.org/en/download).
However, if you prefer to use CommonJS syntax, please refer to [JavaScript ES6/CommonJS syntax](sdk-example-javascript-syntax.md).

## Create the AWS resources
<a name="lex-bot-provision-resources"></a>

This tutorial requires the following resources.
+ An unauthenticated IAM role with attached permissions to:
  + Amazon Comprehend
  + Amazon Translate
  + Amazon Lex

You can create this resources manually, but we recommend provisioning these resources using AWS CloudFormation as described in this tutorial.

### Create the AWS resources using CloudFormation
<a name="lex-bot-example-resources-cli"></a>

CloudFormation enables you to create and provision AWS infrastructure deployments predictably and repeatedly. For more information about CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/).

To create the CloudFormation stack using the AWS CLI:

1. Install and configure the AWS CLI following the instructions in the [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).

1. Create a file named `setup.yaml` in the root directory of your project folder, and copy the content [ here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascriptv3/example_code/cross-services/lex-bot/setup.yaml) into it.
**Note**
The CloudFormation template was generated using the AWS CDK available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/resources/cdk/lex_bot_example_iam_unauth_role). For more information about the AWS CDK, see the [AWS Cloud Development Kit (AWS CDK) Developer Guide](https://docs.aws.amazon.com/cdk/latest/guide/).

1. Run the following command from the command line, replacing {{STACK\_NAME}} with a unique name for the stack.
**Important**
The stack name must be unique within an AWS Region and AWS account. You can specify up to 128 characters, and numbers and hyphens are allowed.

   ```
   aws cloudformation create-stack --stack-name STACK_NAME --template-body file://setup.yaml --capabilities CAPABILITY_IAM
   ```

   For more information on the `create-stack` command parameters, see the [AWS CLI Command Reference guide](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html), and the [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.html).

   To view the resources created, open the Amazon Lex console, choose the stack, and select the **Resources** tab.

## Create an Amazon Lex bot
<a name="lex-bot-example-create-lex-bot"></a>

**Important**
Use V1 of the the Amazon Lex console to create the bot. This exmaple does not work with bots created using V2.

The first step is to create an Amazon Lex chatbot by using the Amazon Web Services Management Console. In this example, the Amazon Lex **BookTrip** example is used. For more information, see [Book Trip](https://docs.aws.amazon.com/lex/latest/dg/ex-book-trip.html).
+ Sign in to the Amazon Web Services Management Console and open the Amazon Lex console at [Amazon Web Services Console](https://console.aws.amazon.com/lex/).
+ On the Bots page, choose **Create**.
+ Choose **BookTrip** blueprint (leave the default bot name **BookTrip**).
![BookTrip sample bot selected with bot name field showing BookTrip as the default name.](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/lex_example/pic2.png)
+ Fill in the default settings and choose **Create** (the console shows the **BookTrip** bot). On the Editor tab, review the details of the preconfigured intents.
+ Test the bot in the test window. Start the test by typing *I want to book a hotel room*.
![Chat interface showing user message about booking hotel room and bot response asking for city.](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/lex_example/ChatBotTest.png)
+ Choose **Publish** and specify an alias name (you will need this value when using the AWS SDK for JavaScript).

**Note**
 You need to reference the **bot name** and the **bot alias** in your JavaScript code.

## Create the HTML
<a name="lex-bot-example-html"></a>

Create a file named `index.html`. Copy and paste the code below in to `index.html`. This HTML references `main.js`. This is a bundled version of index.js, which includes the required AWS SDK for JavaScript modules. You'll create this file in [Create the HTML](#lex-bot-example-html). `index.html` also references `style.css`, which adds the styles.

```
<!doctype html>
<head>
  <title>Amazon Lex - Sample Application (BookTrip)</title>
  <link type="text/css" rel="stylesheet" href="style.css" />
</head>

<body>
  <h1 id="title">Amazon Lex - BookTrip</h1>
  <p id="intro">
    This multiple language chatbot shows you how easy it is to incorporate
    <a
      href="https://aws.amazon.com/lex/"
      title="Amazon Lex (product)"
      target="_new"
      >Amazon Lex</a
    >
    into your web apps. Try it out.
  </p>
  <div id="conversation"></div>
  <input
    type="text"
    id="wisdom"
    size="80"
    value=""
    placeholder="J'ai besoin d'une chambre d'hôtel"
  />
  <br />
  <button onclick="createResponse()">Send Text</button>
  <script type="text/javascript" src="./main.js"></script>
</body>
```

This code is also available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/resources/cdk#running-a-cdk-app).

## Create the browser script
<a name="lex-bot-example-script"></a>

Create a file named `index.js`. Copy and paste the code below into `index.js`. Import the required AWS SDK for JavaScript modules and commands. Create clients for Amazon Lex, Amazon Comprehend, and Amazon Translate. Replace {{REGION}} with AWS Region, and {{IDENTITY\_POOL\_ID}} with the ID of the identity pool you created in the [Create the AWS resources](#lex-bot-provision-resources). To retrieve this identity pool ID, open the identity pool in the Amazon Cognito console, choose **Edit identity pool**, and choose **Sample code** in the side menu. The identity pool ID is shown in red text in the console.

First, create a `libs` directory create the required service client objects by creating three files, `comprehendClient.js`, `lexClient.js`, and `translateClient.js`. Paste the appropriate code below into each, and replace {{REGION}} and {{IDENTITY\_POOL\_ID}} in each file.

**Note**
Use the ID of the Amazon Cognito identity pool you created in [Create the AWS resources using CloudFormation](#lex-bot-example-resources-cli).

```
import { CognitoIdentityClient } from "@aws-sdk/client-cognito-identity";
import { fromCognitoIdentityPool } from "@aws-sdk/credential-provider-cognito-identity";
import { ComprehendClient } from "@aws-sdk/client-comprehend";

const REGION = "REGION";
const IDENTITY_POOL_ID = "IDENTITY_POOL_ID"; // An Amazon Cognito Identity Pool ID.

// Create an Amazon Comprehend service client object.
const comprehendClient = new ComprehendClient({
  region: REGION,
  credentials: fromCognitoIdentityPool({
    client: new CognitoIdentityClient({ region: REGION }),
    identityPoolId: IDENTITY_POOL_ID,
  }),
});

export { comprehendClient };
```

```
import { CognitoIdentityClient } from "@aws-sdk/client-cognito-identity";
import { fromCognitoIdentityPool } from "@aws-sdk/credential-provider-cognito-identity";
import { LexRuntimeServiceClient } from "@aws-sdk/client-lex-runtime-service";

const REGION = "REGION";
const IDENTITY_POOL_ID = "IDENTITY_POOL_ID"; // An Amazon Cognito Identity Pool ID.

// Create an Amazon Lex service client object.
const lexClient = new LexRuntimeServiceClient({
  region: REGION,
  credentials: fromCognitoIdentityPool({
    client: new CognitoIdentityClient({ region: REGION }),
    identityPoolId: IDENTITY_POOL_ID,
  }),
});

export { lexClient };
```

```
import { CognitoIdentityClient } from "@aws-sdk/client-cognito-identity";
import { fromCognitoIdentityPool } from "@aws-sdk/credential-provider-cognito-identity";
import { TranslateClient } from "@aws-sdk/client-translate";

const REGION = "REGION";
const IDENTITY_POOL_ID = "IDENTITY_POOL_ID"; // An Amazon Cognito Identity Pool ID.

// Create an Amazon Translate service client object.
const translateClient = new TranslateClient({
  region: REGION,
  credentials: fromCognitoIdentityPool({
    client: new CognitoIdentityClient({ region: REGION }),
    identityPoolId: IDENTITY_POOL_ID,
  }),
});

export { translateClient };
```

This code is available [here on GitHub.](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cross-services/lex-bot/src/libs).

Next, create an `index.js` file, and paste the code below into it.

 Replace {{BOT\_ALIAS}} and {{BOT\_NAME}} with the alias and name of your Amazon Lex bot respectively, and {{USER\_ID}} with a user id. The `createResponse` asynchronous function does the following:
+ Takes the text inputted by the user into the browser and uses Amazon Comprehend to determine its language code.
+ Takes the language code and uses Amazon Translate to translate the text into English.
+ Takes the translated text and uses Amazon Lex to generate a response.
+ Posts the response to the browser page.

```
import { DetectDominantLanguageCommand } from "@aws-sdk/client-comprehend";
import { TranslateTextCommand } from "@aws-sdk/client-translate";
import { PostTextCommand } from "@aws-sdk/client-lex-runtime-service";
import { lexClient } from "./libs/lexClient.js";
import { translateClient } from "./libs/translateClient.js";
import { comprehendClient } from "./libs/comprehendClient.js";

let g_text = "";
// Set the focus to the input box.
document.getElementById("wisdom").focus();

function showRequest() {
  const conversationDiv = document.getElementById("conversation");
  const requestPara = document.createElement("P");
  requestPara.className = "userRequest";
  requestPara.appendChild(document.createTextNode(g_text));
  conversationDiv.appendChild(requestPara);
  conversationDiv.scrollTop = conversationDiv.scrollHeight;
}

function showResponse(lexResponse) {
  const conversationDiv = document.getElementById("conversation");
  const responsePara = document.createElement("P");
  responsePara.className = "lexResponse";

  const lexTextResponse = lexResponse;

  responsePara.appendChild(document.createTextNode(lexTextResponse));
  responsePara.appendChild(document.createElement("br"));
  conversationDiv.appendChild(responsePara);
  conversationDiv.scrollTop = conversationDiv.scrollHeight;
}

function handletext(text) {
  g_text = text;
  const xhr = new XMLHttpRequest();
  xhr.addEventListener("load", loadNewItems, false);
  xhr.open("POST", "../text", true); // A Spring MVC controller
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded"); //necessary
  xhr.send(`text=${text}`);
}

function loadNewItems() {
  showRequest();

  // Re-enable input.
  const wisdomText = document.getElementById("wisdom");
  wisdomText.value = "";
  wisdomText.locked = false;
}

// Respond to user's input.
const createResponse = async () => {
  // Confirm there is text to submit.
  const wisdomText = document.getElementById("wisdom");
  if (wisdomText?.value && wisdomText.value.trim().length > 0) {
    // Disable input to show it is being sent.
    const wisdom = wisdomText.value.trim();
    wisdomText.value = "...";
    wisdomText.locked = true;
    handletext(wisdom);

    const comprehendParams = {
      Text: wisdom,
    };
    try {
      const data = await comprehendClient.send(
        new DetectDominantLanguageCommand(comprehendParams),
      );
      console.log(
        "Success. The language code is: ",
        data.Languages[0].LanguageCode,
      );
      const translateParams = {
        SourceLanguageCode: data.Languages[0].LanguageCode,
        TargetLanguageCode: "en", // For example, "en" for English.
        Text: wisdom,
      };
      try {
        const data = await translateClient.send(
          new TranslateTextCommand(translateParams),
        );
        console.log("Success. Translated text: ", data.TranslatedText);
        const lexParams = {
          botName: "BookTrip",
          botAlias: "mynewalias",
          inputText: data.TranslatedText,
          userId: "chatbot", // For example, 'chatbot-demo'.
        };
        try {
          const data = await lexClient.send(new PostTextCommand(lexParams));
          console.log("Success. Response is: ", data.message);
          const msg = data.message;
          showResponse(msg);
        } catch (err) {
          console.log("Error responding to message. ", err);
        }
      } catch (err) {
        console.log("Error translating text. ", err);
      }
    } catch (err) {
      console.log("Error identifying language. ", err);
    }
  }
};
// Make the function available to the browser.
window.createResponse = createResponse;
```

This code is available [here on GitHub.](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cross-services/lex-bot/src/index.html).

Now use webpack to bundle the `index.js` and AWS SDK for JavaScript modules into a single file, `main.js`.

1. If you haven't already, follow the [Prerequisites](#lex-bot-example-prerequisites) for this example to install webpack.
**Note**
For information about*webpack*, see [Bundle applications with webpack](webpack.md).

1. Run the the following in the command line to bundle the JavaScript for this example into a file called `main.js`:

   ```
   webpack index.js --mode development --target web --devtool false -o main.js
   ```

## Next steps
<a name="lex-bot-example-next-steps"></a>

Congratulations\! You have created a Node.js application that uses Amazon Lex to create an interactive user experience. As stated at the beginning of this tutorial, be sure to terminate all of the resources you create while going through this tutorial to ensure that you’re not charged. You can do this by deleting the CloudFormation stack you created in the [Create the AWS resources](#lex-bot-provision-resources) topic of this tutorial, as follows:

1. Open the [CloudFormation console]( https://console.aws.amazon.com/cloudformation/home).

1. On the **Stacks** page, select the stack.

1. Choose **Delete**.

For more AWS cross-service examples, see [AWS SDK for JavaScript cross-service examples](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/tutorials.html).
