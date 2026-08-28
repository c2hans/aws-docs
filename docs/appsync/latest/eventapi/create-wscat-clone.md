---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/create-wscat-clone.html
---

# Create a wscat clone using NodeJs and IAM auth using AppSyncJs
<a name="create-wscat-clone"></a>

This tutorial shows you how to create a wscat clone that enables real-time messaging using AWS AppSync Events with IAM authorization using [Smithy](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-smithy-signature-v4/) libraries with TypeScript in NodeJS.

## Before you begin
<a name="wscat-clone-nodejs.prerequisites"></a>

Make sure you have completed the prerequisites in the [Getting Started](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-getting-started.html) topic. You will also need to use the AWS CLI.

Your profile must have permissions to run the following actions. For more information about AWS AppSync actions, see [Actions, resources, and condition keys for AWSAWS AppSync](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsappsync.html).
+ `appsync:EventConnect` - Grants permission to connect to an Event API
+ `appsync:EventPublish` - Grants permission to publish events to a channel namespace
+ `appsync:EventSubscribe` - Grants permission to subscribe to a channel namespace

You will also need to have *NodeJS* working in your environment. You need NodeJS version 22.14.0 or higher.

**Note**
You can download the latest version of NodeJs [here](https://nodejs.org/en) or use a tool like [Node Version Manager (nvm](https://github.com/nvm-sh/nvm)).

## The tutorial
<a name="wscat-clone-nodejs.tutorial"></a>

**Implementation steps**

1.

**Create an Event API**

   To begin, create the Event API you will interact with. For more information, see [Creating an AWS AppSync Event API](https://docs.aws.amazon.com/appsync/latest/eventapi/create-event-api-tutorial.html) to create the *Event API*.

1.

**Configure authorization**

   Once created, sign into the AWS AppSync console and configure the IAM authorization in **Settings**.

   1. In the **Authorization modes** section, choose **Add**. On the next screen, choose **AWS Identity and Access Management (IAM)**, and choose **Add** to use IAM as an authorization mode.

   1. In the **Authorization configuration** section, choose **Edit**.

   1. On the next page, add **IAM authorization** to the **Connection authorization modes**, the **default publish authorization** modes, and the **default subscribe authorization modes**. Choose **Update** to save your changes.

1.

**Start a new NodeJs project**

   In your terminal, create a new directory and initialize project:

   ```
   mkdir eventscat
   cd eventscat
   npm init -y
   ```

1.

**Install TypeScript packages**

   Install the required TypeScript packages and bundle them using [esbuild](https://esbuild.github.io/)

   ```
   npm install esbuild typescript
   npm install -D @tsconfig/node20 @types/node
   ```

1.

**Create a new signer library for IAM**

   When using IAM as an authorization mode, you must sign your request using Sigv4. Create a *signer library* handles that task. Start by installing the required packages.

   ```
   npm i @aws-crypto/sha256-js \
     @aws-sdk/credential-providers \
     @smithy/protocol-http \
     @smithy/signature-v4
   ```

   Create a new file: `src/signer.ts` with the following code

   ```
   import { Sha256 } from '@aws-crypto/sha256-js'
   import { fromNodeProviderChain } from '@aws-sdk/credential-providers'
   import { HttpRequest } from '@smithy/protocol-http'
   import { SignatureV4 } from '@smithy/signature-v4'

   /** AppSync Events WebSocket sub-protocol identifier */
   export const AWS_APPSYNC_EVENTS_SUBPROTOCOL = 'aws-appsync-event-ws'

   /** Default headers required for AppSync Events API requests */
   export const DEFAULT_HEADERS = {
     accept: 'application/json, text/javascript',
     'content-encoding': 'amz-1.0',
     'content-type': 'application/json; charset=UTF-8',
   }

   /**
    * Prepares signed material for a request
    * @param httpDomain - the Events API HTTP domain
    * @param region - the API region
    * @param body - the body to sign
    * @returns signed material for a request
    */
   export async function sign(httpDomain: string, region: string, body: string) {
     const credentials = fromNodeProviderChain()

     const signer = new SignatureV4({
       credentials,
       service: 'appsync',
       region,
       sha256: Sha256,
     })

     const url = new URL(`https://${httpDomain}/event`)
     const httpRequest = new HttpRequest({
       method: 'POST',
       headers: { ...DEFAULT_HEADERS, host: url.hostname },
       body,
       hostname: url.hostname,
       path: url.pathname,
     })

     const signedReq = await signer.sign(httpRequest)
     return { host: signedReq.hostname, ...signedReq.headers }
   }

   /**
    * Get the HTTP domain and region or null if it cannot be identified
    * @param wsDomain - the websocket domain
    */
   function getHttpDomain(wsDomain: string) {
     const pattern =
       /^\w{26}\.appsync-realtime-api.(\w{2}(?:(?:-\w{2,})+)-\d)\.amazonaws.com(?:\.cn)?$/

     const match = wsDomain.match(pattern)
     if (match) {
       return {
         httpDomain: wsDomain.replace('appsync-realtime-api', 'appsync-api'),
         region: match[1],
       }
     }
     return null
   }

   /**
    * Transforms an object into a valid based64Url string
    * @param auth - header material
    */
   function getAuthProtocol(auth: unknown): string {
     const based64UrlHeader = btoa(JSON.stringify(auth))
       .replace(/\+/g, '-') // Convert '+' to '-'
       .replace(/\//g, '_') // Convert '/' to '_'
       .replace(/=+$/, '') // Remove padding `=`
     return `header-${based64UrlHeader}`
   }

   /**
    * Gets the protocol array that authorizes connecting to an API
    * @param wsDomain -the WebSocket endpoint domain
    * @param region - the AWS region of the API
    * @returns
    */
   export async function getAuthForConnect(wsDomain: string, region?: string) {
     const domain = getHttpDomain(wsDomain)
     if (!domain && !region) {
       throw new Error('Must provide region when using a custom domain')
     }
     const httpDomain = domain?.httpDomain ?? wsDomain
     const _region = domain?.region ?? region!
     const signed = await sign(httpDomain, _region, '{}')
     const protocol = getAuthProtocol(signed)
     return [AWS_APPSYNC_EVENTS_SUBPROTOCOL, protocol]
   }

   /**
    * Gets the authorization header for a websocket message
    * @param wsDomain -the WebSocket endpoint domain
    * @param body -the request to sign
    * @param region - the AWS region of the API
    * @returns
    */
   export async function getAuthForMessage(wsDomain: string, body: unknown, region?: string) {
     const domain = getHttpDomain(wsDomain)
     if (!domain && !region) {
       throw new Error('Must provide region when using a custom domain')
     }
     const httpDomain = domain?.httpDomain ?? wsDomain
     const _region = domain?.region ?? region!
     return await sign(httpDomain, _region, JSON.stringify(body))
   }
   ```

   The signer uses `fromNodeProviderChain` to retrieve your local credentials and uses SigV4 to sign the request headers and content.

1.

**Create your program**

   1. We recommend to you use the [chalk](https://www.npmjs.com/package/chalk) library to provide some color on your terminal and the [commander ](https://www.npmjs.com/package/commander) library to define and parse your program command options.

      ```
      npm install chalk commander
      ```

   1. Create the file `src/eventscat.ts` with the following code for your program.

      ```
      import chalk from 'chalk'
      import { program } from 'commander'
      import EventEmitter from 'node:events'
      import readline from 'node:readline'
      import { getAuthForConnect, getAuthForMessage } from './signer'

      /**
       * InputReader - processes console input.
       *
       * @extends EventEmitter
       */
      class Console extends EventEmitter {
        stdin: NodeJS.ReadStream & { fd: 0 }
        stdout: NodeJS.WriteStream & { fd: 1 }
        stderr: NodeJS.WriteStream & { fd: 2 }
        readlineInterface: readline.Interface

        constructor() {
          super()

          this.stdin = process.stdin
          this.stdout = process.stdout
          this.stderr = process.stderr

          this.readlineInterface = readline.createInterface({
            input: process.stdin,
            output: process.stdout,
          })

          this.readlineInterface
            .on('line', (data) => {
              this.emit('line', data)
            })
            .on('close', () => {
              this.emit('close')
            })
        }

        prompt() {
          this.readlineInterface.prompt(true)
        }

        message(msg: string) {
          const payload = JSON.parse(msg)
          this.clear()
          if (payload.type === 'ka') {
            this.stdout.write(chalk.magenta('<ka>\n'))
          } else if (payload.type === 'data') {
            this.stdout.write(chalk.blue(`< ${JSON.stringify(JSON.parse(payload.event), null, 2)}\n`))
          } else {
            this.stdout.write(chalk.bgBlack.white(`* ${payload.type} *\n`))
          }
          this.prompt()
        }

        print(msg: any) {
          this.clear()
          this.stdout.write(msg + '\n')
          this.prompt()
        }

        clear() {
          this.stdout.write('\r\u001b[2K\u001b[3D')
        }
      }

      export async function main() {
        program
          .version('demo')
          .option('-r, --realtime <domain>', 'AppSync Events real-time domain')
          .option('-s, --subscribe <channel>', 'Channel to subscribe to')
          .option('-p, --publish [channel]', 'Channel to publish to')
          .parse(process.argv)

        const options = program.opts()
        if (!options.realtime || !options.subscribe) {
          return program.help()
        }

        const wsConsole = new Console()
        const domain = options.realtime
        const channel = options.subscribe

        const protocols = await getAuthForConnect(domain)
        const ws = new WebSocket(`wss://${domain}/event/realtime`, protocols)

        ws.onopen = async () => {
          ws.send(
            JSON.stringify({
              type: 'subscribe',
              id: crypto.randomUUID(),
              channel,
              authorization: await getAuthForMessage(domain, { channel }),
            }),
          )
          wsConsole.print(chalk.green('Connected (press CTRL+C to quit)'))
          wsConsole.on('line', async (data: string) => {
            if (!data || !data.trim().length || !options.publish) {
              return wsConsole.prompt()
            }
            const channel = options.publish
            const events = [JSON.stringify(data.trim())]
            ws.send(
              JSON.stringify({
                type: 'publish',
                id: crypto.randomUUID(),
                channel,
                events,
                authorization: await getAuthForMessage(domain, { channel, events }),
              }),
            )
            wsConsole.prompt()
          })
        }

        ws.onclose = (event) => {
          wsConsole.print(chalk.green(`Disconnected (code: ${event.code}, reason: "${event.reason}")`))
          wsConsole.clear()
          process.exit()
        }

        ws.onerror = (err) => {
          wsConsole.print(chalk.red(err))
          process.exit(-1)
        }

        ws.onmessage = (data) => wsConsole.message(data.data)

        wsConsole.on('close', () => {
          ws.close()
          process.exit()
        })
      }
      ```

   1. Specify the scripts property in `package.json` file.

      ```
      ...
          "scripts": {
          "build": "esbuild --platform=node --target=node20 --bundle --outfile=bin/eventscat.js src/eventscat.ts"
        },
      ...
      ```

   1. Build the code.

      ```
      npm run build
      ```

   1. Add the file `bin/eventscat`.

      ```
      #!/usr/bin/env node

      const { main } = require('./eventscat.js')
      main()
      ```

      Change the mode of the file to execute it

      ```
      chmod +x bin/eventscat
      ```

1.

**Using the program**

   Test the implementation by connecting to your API. To do this, subscribe to `/default/*` *channel*, and publish on the `/default/iam` *channel*. You can find the realtime domain of your API in the **Settings** section of the AWS AppSync console under **Realtime**.

   ```
   ./bin/eventscat --realtime {{1234567890.appsync-api.us-east-2.amazonaws.com}} \
   --subscribe "/default/*" --publish "/default/iam"
   ```

   Once the client is connected, you can start publishing messages simply by entering text and pressing **enter**. You also start receiving messages published to your **subscribe** channel.

1.

**(Optional) Clean up**

   Once you are done with this tutorial, you can delete the API you created by going to the AWS AppSync console, selecting the API and choosing **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
