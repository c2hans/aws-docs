---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-table-integration-tutorial.html
---

# Persist user messages with a DynamoDB table integration using AppSyncJs
<a name="dynamodb-table-integration-tutorial"></a>

In this tutorial, you'll learn how to create an AWS AppSync Events API that stores user messages in a DynamoDB table as they are published and before they are broadcasted to connected users. You'll create a simple messaging system where users can send messages and then later retrieve their message history.

You will complete this tutorial using only the AWS Management Console. Before you begin, complete the following set up prerequisites.

**Sign up for an AWS account**
If you are not already an AWS customer, you need to [create an AWS account](https://portal.aws.amazon.com/billing/signup#/start/email) by following the online instructions. Signing up enables you to access AWS AppSync and other AWS services that you can use with your AWS AppSync GraphQL and Event APIs.

**Understand how to access the AWS Management Console**
The AWS AppSync console is available at [https://console.aws.amazon.com/appsync](https://console.aws.amazon.com/appsync/).

**Understand the AWS AppSync and DynamoDB services**
For more information about DynamoDB, see [What is Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) in the *Amazon DynamoDB Developer Guide*.

## Step 1: Create a DynamoDB-backed AWS AppSync GraphQL API
<a name="step-1-create-graphql-api"></a>

In this step, you create an AWS AppSync GraphQL API along with the DynamoDB table to store the messages.

**Create a GraphQL API**

1. Sign in to the AWS Management Console and open the AWS AppSync console at [AWS AppSync console](https://console.aws.amazon.com/appsync/).

1. On the AWS AppSync home page, choose **Create API**, then choose **GraphQL API**.

1. On the **Select API type** page, choose **Design from scratch**. Then choose **Next**.

1. In the **Specify API details** section, for **API name**, enter **graphql-messages-api**. Then choose **Next**.

1. On the **Specify GraphQL resources** page, in the **Create a GraphQL type** section, choose **Create type backed by a DynamoDB table now**.

1. In the **Configure model information** section, do the following:

   1. For **Model name**, enter **Message**.

   1. For **Fields**, do the following to add a channel field to your model:

      1. Choose **Add new field**.

      1. For **Name**, enter **channel**.

      1. For **Type**, choose **String**.

      1. For **Array**, choose **No**.

      1. For **Required**, choose **Yes**.

   1. Do the following to add an id field to your model:

      1. Choose **Add new field**.

      1. For **Name**, enter **id**.

      1. For **Type**, choose **String**.

      1. For **Array**, choose **No**.

      1. For **Required**, choose **Yes**.

   1. Do the following to add a user field to your model:

      1. Choose **Add new field**.

      1. For **Name**, enter **user**.

      1. For **Type**, choose **String**.

      1. For **Array**, choose **No**.

      1. For **Required**, choose **Yes**.

   1. Do the following to add a content field to your model:

      1. Choose **Add new field**.

      1. For **Name**, enter **content**.

      1. For **Type**, choose **String**.

      1. For **Array**, choose **No**.

      1. For **Required**, choose **Yes**.

   1. Do the following to add a createdAt field to your model:

      1. Choose **Add new field**.

      1. For **Name**, enter **createdAt**.

      1. For **Type**, choose **DateTime**.

      1. For **Array**, choose **No**.

      1. For **Required**, choose **Yes**.

      The following screenshot shows how your fields should be configured:
![The channel, id, user, content, and createdAt fields configured in the AWS AppSync console.](http://docs.aws.amazon.com/appsync/latest/eventapi/images/tutorial-ddb-persist-messages-1.png)

1. **In the Configure model table** section, do the following:

   1. For **Table name** enter **tutorial-events-messages**.

   1. For **Primary key**, select **user**.

   1. For **Sort key**, select **id**.

   The following screenshot shows how your fields should be configured:
![The Configure model table fields configured in the AWS AppSync console.](http://docs.aws.amazon.com/appsync/latest/eventapi/images/tutorial-ddb-persist-messages-3.png)

1. Choose **Next**.

1. On the **Review and create** page, review your API details, and choose **Create API**.

   The AWS AppSync console creates a DynamoDB table and an AWS AppSync GraphQL API to query the table. Wait for the API creation process to complete before continuing to Step 2 of this tutorial.

## Step 2: Create an AWS AppSync Events API
<a name="step-2-create-events-api"></a>

In this step, you create the AWS AppSync Events API that you can use to publish messages. Other clients will be able to subscribe to a channel on the API to receive messages.

**Create the AWS AppSync Events API**

1. In the left navigation menu, choose **API** to return to the **APIs** page.

1. In the **API types** section, choose **Create Event API**.

1. On the **Create Event API** page, in the **API details** section, for **API name**, enter **events-messages-api**.

1. Choose **Create**.

   The AWS AppSync console creates an Event API with API key authorization mode configured, and a channel namespace called `default`.

Next, create a data source for your DynamoDB table that you created in Step 1.

**To create a data source for the DynamoDB table**

1. Choose the **Data sources** tab.

1. Choose **Create data source**.

1. On the **Create data source** page, do the following:

   1. For **Name**, enter **messages**.

   1. For **Data source type**, choose **Amazon DynamoDB**.

   1. The configuration automatically selects the current AWS Region.

   1. For **Table name**, select **tutorial-events-messages** from the list.

1. Choose **Create**.

Now you can create your data source integration in your namespace.

**To create a data source integration with a namespace**

1. From your **messages** data source page, you need to return to the settings page for **my-event-api**. You can either use your browser's back button or you can choose **my-event-api** from the top menu in the console window. The following screenshot shows the location of the menu with **my-event-api** circled.
![The location of my-event-api in the console window's top menu.](http://docs.aws.amazon.com/appsync/latest/eventapi/images/tutorial-ddb-persist-messages-2.png)

1. Choose the **Namespaces** tab, then choose the **default** namespace.

1. Choose **Edit**.

1. On the **Edit default** page, in the **Handler** section, choose **Code with data source**.

1. For **Publish configuration**, **Data source name**, choose **messages**. For **Behavior**, choose **Code**.

1. For **Subscribe configuration**, leave the **Data source name** blank.

1. In the code editor, enter the following code:

   ```
   import { util } from '@aws-appsync/utils'
   import * as ddb from '@aws-appsync/utils/dynamodb'

   export const onPublish = {
     request(ctx) {
       const channel = ctx.info.channel.path
       const createdAt = util.time.nowISO8601()
       return ddb.batchPut({
         tables: {
           'tutorial-events-messages': ctx.events.map(({ payload }) => {
             return { channel, id: util.autoKsuid(), createdAt, ...payload }
           }),
         },
       })
     },
     // simply forward the events for broadcast
     response: (ctx) => ctx.events
   }
   ```

   The code uses the `ddb.batchPut` function to save multiple events to the “tutorial-events-messages” using a DynamoDB `BatchWrite` operation. It adds the channel path, creates an id, and a timestamp before saving the items.

1. Choose **Save** to confirm your code changes.

## Step 3: Test the AWS AppSync Events API
<a name="step-3-test-events-api"></a>

**To test the API**

1. From your **default** namespace page, you need to return to the settings page for **my-event-api**. You can either use your browser's back button or you can choose **my-event-api** from the top menu in the console window.

1. On the **my-event-api** page, choose the **Pub/Sub Editor** tab.

1. In the **Subscrib** section, choose **Connect** and **Subscribe** to the `default/*` channel.

1. In the **Publish** section, paste the following in the code editor:

   ```
   {
     "user": "john",
     "content": "Hello, world!"
   }
   ```

1. Choose **Publish**.

1. Update the content in the editor with the following:

   ```
   [
     {
       "user": "sarah",
       "content": "Working on a fresh batch of cookies!"
     },
     {
       "user": "harry",
       "content": "Yum, can't wait!"
     }
   ]
   ```

1. Choose **Publish** again. After each time you publish, the events are displayed in the **Subscribe** table.

## Step 4: Retrieve your messages
<a name="step-4-retrieve-messages"></a>

You can view your messages directly in the DynamoDB table. However, there is a simple process for querying the data with GraphQL. This step demonstrates how to do this using your **graphql-messages-api** AWS AppSync GraphQL API.

**To query data with a GraphQL API**

1. From your **my-event-api** **Pub/Sub Editor** page, you need to go to your **graphql-messages-api**. In the left navigation, choose **APIs**. In the **APIs** section, choose **graphql-messages-api**.

1. In the left navigation menu, choose **Queries**.

1. On the **Queries** page, clear the contents of the editor and enter the following query.

   ```
   query byChannel {
     queryMessagesByChannelIdIndex(channel: "/default/channel", first: 10) {
       items {
         channel
         id
         user
         content
         createdAt
       }
     }
   }
   ```

1. Choose the orange **Execute query** button on the upper right. The query returns the first ten items in your DynamoDB table.

## Step 5: (Optional) Delete the resources you created
<a name="step-5-clean-up-resources"></a>

If you no longer need the resources that you created for this tutorial, you can delete them. This step helps ensure that you aren't charged for resources that you aren't using.

You can delete all of the following resources directly in the AWS AppSync console:
+ The AWS AppSync Events API **my-event-api**
+ The AWS AppSync GraphQL API **graphql-messages-api**
+ The DynamoDB table **tutorial-events-messages**
