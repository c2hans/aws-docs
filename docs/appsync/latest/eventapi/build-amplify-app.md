---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/build-amplify-app.html
---

# Getting started with the Amplify Events client
<a name="build-amplify-app"></a>

You can connect to your AWS AppSync Event API using any HTTP and WebSocket client, and you can also use the Amplify client for JavaScript. This getting started tutorial guides you through connecting to an Event API from a JavaScript React application.

In this tutorial you will complete the following tasks.

**Topics**
+ [Step 1: Create an event API](#create-event-api)
+ [Step 2: Deploy a React app with Vite](#deploy-react-vite-app)
+ [Step 3: Configure the Amplify client](#configure-amplify-client)
+ [Step 4: Connect to a channel and receive messages](#receive-message)
+ [Step 5: Send a message from your app](#send-message)

## Step 1: Create an event API
<a name="create-event-api"></a>

1. Sign in to the AWS Management Console and open the [AWS AppSync console](https://console.aws.amazon.com/appsync/).

1. On the AWS AppSync console service page, choose **Create API**, then choose **Event API**.

1. On the **Create Event API** page, in the **API details** section, do the following:

   1. For **API** enter the name of your API.

   1. (optional) Enter the contact name for the API.

1. Choose **Create**.

You have now created an Event API. The API is configured with API Key as an authorization mode for connect, publish, and subscribe actions. A default channel namespace with the name “default” has also been created.

To learn more about customizing authorization, see [Configuring authorization and authentication to secure Event APIs](configure-event-api-auth.md). To learn more about channel namespaces, see [Understanding channel namespaces](channel-namespaces.md)

## Step 2: Deploy a React app with Vite
<a name="deploy-react-vite-app"></a>

1. From your local work environment, run the following command in a terminal window to create a new Vite app for React.

   ```
   npm create vite@latest appsync-events-app -- --template react
   ```

1. Run the following command to switch to the `appsync-events-app` directory and install the dependencies and the Amplify library.

   ```
   cd appsync-events-app
   npm install
   npm install aws-amplify
   ```

1. Open a different terminal window and `cd` into your `appsync-events-app` directory. Run the following command to start your sever in dev mode.

   ```
   npm run dev
   ```

### (Optional) Configure Tailwind CSS
<a name="configure-tailwindcss"></a>

You can set up Tailwind CSS to style your project.

1. Open a terminal window and run the following commands to install the dependencies.

   ```
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

1. Update the `tailwind.config.js` file with the following code.

   ```
   /** @type {import('tailwindcss').Config} */
   export default {
     content: [
       "./index.html",
       "./src/**/*.{js,ts,jsx,tsx}",
     ],
     theme: {
       extend: {},
     },
     plugins: [],
   }
   ```

1. Set the content of `./src/index.css` to the following.

   ```
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

1. Use the following command to start and restart your Vite app from the terminal where it is currently running.

   ```
   npm run dev
   ```

## Step 3: Configure the Amplify client
<a name="configure-amplify-client"></a>

1. Sign in to the AWS Management Console and open the [AWS AppSync console](https://console.aws.amazon.com/appsync/).

1. Open the **Integration** tab for the Event API that you created in step 1.

1. Download your configuration file.

1. Save the `amplify_outputs.json` file in your project's `src` directory. Your configuration file will look like the following.

   ```
   {
     "API": {
       "Events": {
         "endpoint": "https://abc1234567890.aws-appsync.us-west-2.amazonaws.com/event",
         "region": "us-west-2",
         "defaultAuthMode": "apiKey",
         "apiKey": "da2-your-api-key-1234567890"
       }
     }
   }
   ```
**Important**
You must set `defaultAuthMode` to `apiKey` and *not* `API_KEY`.

## Step 4: Connect to a channel and receive messages
<a name="receive-message"></a>

1. Update your `App.jsx` file with the following code.

   ```
   import { useEffect, useState, useRef } from 'react'
   import './App.css'

   import { Amplify } from 'aws-amplify'
   import { events } from 'aws-amplify/data'
   import config from './amplify_outputs.json'

   Amplify.configure(config)

   export default function App() {
     const [messages, setMessages] = useState([])
     const [room, setRoom] = useState('')
     const counterRef = useRef(null)

     useEffect(() => {
       if (!room || !room.length) {
         return
       }
       let timeoutID
       const pr = events.connect(`/default/${room}`)
       pr.then((channel) => {
         channel.subscribe({
           next: (data) => {
             setMessages((messages) => [...messages, data.message])
             if (timeoutID) {
               clearTimeout(timeoutID);
             }
             counterRef.current?.classList.add('animate-bounce')
             timeoutID = setTimeout(() => {
               counterRef.current?.classList.remove('animate-bounce')
             }, 3000);
           },
           error: (value) => console.error(value),
         })
       })

       return () => {
         pr?.then((channel) => channel?.close())
       }
     }, [room])

     return (
       <div className='max-w-screen-md mx-auto'>
         <h2 className='my-4 p-4 font-semibold text-xl'>AppSync Events - Messages</h2>
         <button
           type="button"
           className='border rounded-md px-4 py-2 items-center text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-sky-200  shadow hover:bg-sky-200/90'
           onClick={() => {
             const room = prompt('Room:')
             if (room && room.length) {
               setMessages([])
               setRoom(room.trim().replace(/\W+/g, '-'))
             }
           }}
         >
           set room
         </button>
         <div className='my-4 border-b-2  border-sky-500 py-1 flex justify-between'>
           <div>
             {room ? (
               <span>
                 Currently in room: <b>{room}</b>
               </span>
             ) : (
               <span>Pick a room to get started</span>
             )}
           </div>
           <div className='flex items-center uppercase text-xs tracking-wider font-semibold'>
             <div className='mr-2'>Messages count:</div>
             <span ref={counterRef} className='transition-all inline-flex items-center rounded-md bg-sky-100 px-2.5 py-0.5 text-xs font-medium text-sky-900'>{messages.length}</span></div>
         </div>
         <section id="messages" className='space-y-2'>
           {messages.map((message, index) => (
             <div
               key={index}
               className='border-b py-1 flex justify-between px-2'
             ><div>
                 {message}
               </div>
               <div> </div>
             </div>
           ))}
         </section>
       </div>
     )
   }
   ```

1. Open the app in your browser and choose the **set room** button to set the room to "greetings".

1. Open the AWS AppSync console, and go to the **Pub/Sub Editor** tab for your API.

1. Set your channel to `/default/greetings`. Choose the "default" namespace and set the rest of the path to `/greetings`.

1. Paste the following into the editor to send the event.

   ```
   [
       {
           "message": "hello world!"
       }
   ]
   ```

1. You should see the message in your app.

1. Choose the **set room** button again to select another room. Send another event in the Pub/Sub Editor to the `/default/greetings` channel. You do not see that message in your app.

## Step 5: Send a message from your app
<a name="send-message"></a>

1. Open your `App` component and add the following line of code at the top of the file.

   ```
   const [message, setMessage] = useState('')
   ```

1. In the same file, locate the last `section` element and add the following code.

   ```
   <section>
           <form
             disabled={!room}
             className='w-full flex justify-between mt-8'
             onSubmit={async (e) => {
               e.preventDefault()
               const event = { message }
               setMessage('')
               await events.post(`/default/${room}`, event)
             }}
           >
             <input
               type="text"
               name="message"
               placeholder="Message:"
               className='flex flex-1 rounded-md border border-input px-3 py-1 h-9 text-sm shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 bg-transparent'
               value={message}
               disabled={!room}
               onChange={(e) => setMessage(e.target.value)}
             />
             <button
               type="submit"
               className='ml-4 border rounded-md px-4 flex items-center text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-sky-200  shadow hover:bg-sky-200/90'
               disabled={!room || !message || !message.length}>
               <svg xmlns="http://www.w3.org/2000/svg" className='size-4' width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z" /><path d="m21.854 2.147-10.94 10.939" /></svg>
             </button>
           </form>
         </section>
   ```

1. You can now send a message to a room that you select, directly from your app.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
