---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/create-event-api-tutorial.html
---

# Creating an AWS AppSync Event API
<a name="create-event-api-tutorial"></a>

AWS AppSync Events allows you to create Event APIs to enable real-time capabilities in your applications. In this section, you create an API with a default channel namespace. You’ll then use the AWS AppSync console to publish messages and subscribe to messages sent to channels in the namespace.

In this tutorial you will complete the following tasks.

**Topics**
+ [Step 1: Create an event API using the AWS AppSync console](#create-event-api-console)
+ [Step 2: Publish and subscribe to receive your first event](#receive-event)
+ [Step 3: Use wildcards in your channel subscription](#use-wildcards)
+ [Step 4: Publish in batches](#publish-batches)

## Step 1: Create an event API using the AWS AppSync console
<a name="create-event-api-console"></a>

1. Sign in to the AWS Management Console and open the [AWS AppSync console](https://console.aws.amazon.com/appsync/).

1. On the AWS AppSync console service page, choose **Create API**, then choose **Event API**.

1. On the **Create Event API** page, in the **API details** section, do the following:

   1. For **API** enter the name of your API.

   1. (optional) Enter the contact name for the API.

1. Choose **Create**.

You have now created an Event API. The API is configured with API Key as an authorization mode for connect, publish, and subscribe actions. A default channel namespace with the name “default” has also been created.

To learn more about customizing authorization, see [Configuring authorization and authentication to secure Event APIs](configure-event-api-auth.md). To learn more about channel namespaces, see [Understanding channel namespaces](channel-namespaces.md)

## Step 2: Publish and subscribe to receive your first event
<a name="receive-event"></a>

Use the following instructions to publish an event.

1. In the AWS AppSync console choose the **Pub/Sub Editor** tab for the Event API that you created in step 1.

1. In the **Publish** section, for **Channel** enter **default** in the first text box and enter **/messages** in the second text box.

1. In the code editor, enter the following JSON payload.

   ```
   [{"message": "Hello world!"}]
   ```

1. Choose **Publish**.

1. The publisher logs table displays a response similar to the following to confirm success.

   ```
   {
     "failed": [],
     "successful": [
       {
         "identifier": "53287bee-ae0d-42e7-8a90-e9d2a49e4bd7",
         "index": 0
       }
     ]
   }
   ```

Now use the following instructions to subscribe to recieve messages.

1. In the **Subscribe** section of the editor, choose **Connect** to connect to your WebSocket endpoint.

1. For **Channel**, enter the name of the channel you want to subscribe to, **/default/messages**, and then choose **Subscribe**.

1. In the code editor, choose **Publish** again. You should receive a new data event in the subscriber logs table with the published event.

## Step 3: Use wildcards in your channel subscription
<a name="use-wildcards"></a>

You can specify a wildcard "\*" at the end of a channel path to receive events published to all channels that match. Use the following instructions to set up a wildcard channel subscription for your Event API.

1. If you are still subscribed to the channel from step 2, choose **Unsubscribe**.

1. In the **Subscribe** section, for **Channel** enter **/default/\***.

1. In the code editor section, choose **Publish** again to send another event. You should receive a new data event in the subscriber logs table

1. In the **Publish** section, change the **Channel** name to **/default/greetings/tutorial**.

1. Choose **Publish**. You receive the message in the **Subscribe** section

## Step 4: Publish in batches
<a name="publish-batches"></a>

You can publish events in batches of up to five. Subscribed clients receive each message individually.

1. In the AWS AppSync console, continue in the **Pub/Sub Editor** tab using the Event API that you were working with in step 3.

1. In the **Publish** section JSON code editor, enter the following:

   ```
   [
     {"message": "Hello world!"},
     {"message": "Bonjour lemonde!"},
     "Hola Mundo!"
   ]
   ```

1. Choose **Publish**.

1. In the **Subscribe** log table, you receive 3 data events.
