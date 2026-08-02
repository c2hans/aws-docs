---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/lambda-iam-auth.html
---

# Publishing from a NodeJS Lambda function with IAM auth using AppSyncJs
<a name="lambda-iam-auth"></a>

AWS AppSync Events allows you to create Event APIs to enable real-time capabilities in your applications. In this tutorial, you use AWS CDK to create your API and a Lambda function that publishes messages. You'll use IAM auth as the authorization mode to publish to your configured channel.

## Before you begin
<a name="prerequisites"></a>

To get started, make sure you have gone through the *prerequisites*. You will need an AWS account. You will also work from the command line.

## Installing AWS CDK and creating up your project
<a name="installing-cdk"></a>

The AWS Cloud Development Kit (AWS CDK) (AWS CDK) is an open-source software development framework for defining cloud infrastructure as code with modern programming languages and deploying it through AWS CloudFormation.

From your terminal, install CDK.

```
npm install -g aws-cdk
```

Next, create a new folder for your application

**Note**
Be sure to use the exact name as AWS CDK uses the folder name to name your app.

```
mkdir publish-from-lambda
```

From the `publish-from-lambda` directory, init a new app:

```
cd publish-from-lambda
cdk init app --language typescript
```

The AWS CDK CLI creates a AWS CDK app containing a single AWS CDK stack. You'll be using TypeScript in this project, so install `esbuild` to bundle your code:

```
npm i -D esbuild@0
```

Now, update the `lib/publish-from-lambda-stack.ts` file with this code:

```
import * as cdk from 'aws-cdk-lib'
import * as appsync from 'aws-cdk-lib/aws-appsync'
import { Runtime } from 'aws-cdk-lib/aws-lambda'
import * as nodejs from 'aws-cdk-lib/aws-lambda-nodejs'
import type { Construct } from 'constructs'
import * as path from 'node:path'

export class PublishFromLambdaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const { IAM, API_KEY } = appsync.AppSyncAuthorizationType
    const apiKeyProvider = { authorizationType: API_KEY }
    const iamProvider = { authorizationType: IAM }

    // 1. Create a new AppSync Events API
    const api = new appsync.EventApi(this, 'api', {
      apiName: 'messages-api',
      authorizationConfig: {
        authProviders: [apiKeyProvider, iamProvider],
        connectionAuthModeTypes: [API_KEY],
        defaultSubscribeAuthModeTypes: [API_KEY],
        defaultPublishAuthModeTypes: [IAM],
      },
    })

    // 2. Create a channel namespace called `messages`
    const ns = api.addChannelNamespace('messages')

    // 3. Create the Lambda function: publisher
    const publisher = new nodejs.NodejsFunction(this, 'publisher', {
      entry: path.join(__dirname, 'lambda', 'publisher.ts'),
      runtime: Runtime.NODEJS_22_X,
      timeout: cdk.Duration.minutes(1),
      bundling: { externalModules: ['@aws-sdk/*'] },
      environment: {
        NAMESPACE: 'messages',
        HTTP_ENDPOINT: api.httpDns,
      },
    })

    // 4. Grant publisher IAM permissions to publish messages to the namespace
    ns.grantPublish(publisher)

    // 5. Output the API ID and the function name
    new cdk.CfnOutput(this, 'apiId', { value: api.apiId })
    new cdk.CfnOutput(this, 'fnName', { value: publisher.functionName })
  }
}
```

Let's recap the stack implementation:
+ You create a new AWS AppSync Events API called `messages-api`. With this API, you can connect to the WebSocket endpoint and subscribe to a channel using an API Key. You can only publish to a channel using IAM authorization.
+ You create a name space called `messages`. This allows you to publish and subscribes to channel paths like starting with `/messages`.
+ You create a NodeJS Lambda function running on `NODEJS_22`. The function can run up to 1 minute. You configure the environment variable and pass the API's http endpoint and namespace.
+ You grant the function permissions to publish to any channel in the namespace.
+ Finally, you output the id of the API and the name of the function. This makes it easy to reference them later, and find the resources in the console.

## Create your Lambda function
<a name="create-lambda-function"></a>

Next, create you'll create a Lambda function that can publish events to the provided channel using IAM authorization. To do so, you will use the *ob-appsync-events-request* [library](https://www.npmjs.com/package/ob-appsync-events-request). This small library implements a `Request` object that is signed with the available IAM credentials. You can review the implementation on [Github](https://github.com/onlybakam/ob-appsync-events-request).

In your `publish-from-lambda` directory, create a new file `publisher.ts` in the `lib/lambda` folder and install the library.

```
mkdir -p lib/lambda
touch lib/lambda/publisher.ts
npm i -D ob-appsync-events-request @types/aws-lambda
```

Update `publisher.ts` with the following code.

```
import type { Handler } from 'aws-lambda'
import { PublishRequest } from 'ob-appsync-events-request'

const ENV = process.env as {
  NAMESPACE: string
  HTTP_ENDPOINT: string
}

export const handler: Handler = async (event) => {
  const createdAt = new Date().toISOString()

  // Create a signed request
  const request = await PublishRequest.signed(
    `https://${ENV.HTTP_ENDPOINT}/event`,
    `${ENV.NAMESPACE}/lambda`,
    { message: 'Hello, world!', createdAt },
    { message: 'Bonjour le monde!', createdAt },
    { message: '¡Hola Mundo!', createdAt },
  )

  // Send the request using fetch
  const response = await fetch(request)
  const result = await response.json()
  console.log(result)
  return result
}
```

When triggered, the Lambda function publishes 3 messages to the channel path `/messages/lambda`. The request is signed using the function's IAM permissions. This is possible because you granted the permissions to the function in your AWS CDK stack configuration\!

## Deploy the stack
<a name="deploy-stack"></a>

You can deploy the stack at this point from your `publish-from-lambda` folder:

```
npm run cdk deploy
```

Review the prompts to proceed with the deployment, once done, you should see the output:

```
Outputs:
PublishFromLambdaStack.apiId = your_api_id
PublishFromLambdaStack.fnName = your_function_name
```

## Subscribe and publish
<a name="subscribe-publish"></a>

Open the AWS AppSync console in the region you deployed your stack in. On the APIs page, you can locate your API by pasting in your `apiId` value in the search bar under *APIs*. Select your messages-api, then select *Pub/Sub Editor*. Scroll down to the *Subscribe* section, and choose *Connect*. Under *Channel*, you choose `messages`, then choose *Subscribe*.

Back in your terminal, invoke the Lambda function with the AWS CLI, using the output `fnName`.

```
aws lambda invoke \
  --function-name "your_function_name" \
  --output text /dev/stdout
```

The function handler is executed, and in your AWS AppSync Events console, you receive the 3 messages\!

## Cleaning up
<a name="cleaning-up"></a>

Once you are done with this tutorial, you can clean up your resources by running the command:

```
npm run cdk destroy
```
