---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/msg-proc-fw-get-started.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Get started with the AWS Message Processing Framework for .NET
<a name="msg-proc-fw-get-started"></a>

Before you begin, be sure you have [set up your environment](net-dg-config.md) and [configured your project](configuring-the-sdk.md). Also review the information in [Using the SDK](net-dg-sdk-features.md).

This topic provides information that will help you get started using the Message Processing Framework. In addition to prerequisite and configuration information, a tutorial is provided that shows you how to implement a common scenario.

## Prerequisites and configuration
<a name="mpf-get-started-prereq"></a>
+ The credentials you provide for your application must have appropriate permissions for the messaging service and operations that it uses. For more information, see the security topics for [SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-authentication-and-access-control.html), [SNS](https://docs.aws.amazon.com/sns/latest/dg/security-iam.html), and [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-iam.html) in their respective developer guides. Also see the portion of the [README](https://github.com/aws/aws-dotnet-messaging/) file on GitHub that discusses specific [permissions](https://github.com/aws/aws-dotnet-messaging/blob/main/README.md#permissions).
+ To use the AWS Message Processing Framework for .NET, you must add the [`AWS.Messaging`](https://www.nuget.org/packages/AWS.Messaging) NuGet package to your project. For example:

  ```
  dotnet add package AWS.Messaging
  ```
+ The framework integrates with .NET's [dependency injection (DI) service container](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection). You can configure the framework during your application's startup by calling `AddAWSMessageBus` to add it to the DI container.

  ```
  var builder = WebApplication.CreateBuilder(args);

  // Register the AWS Message Processing Framework for .NET
  builder.Services.AddAWSMessageBus(builder =>
  {
      // Register that you'll publish messages of type ChatMessage to an existing queue
      builder.AddSQSPublisher<ChatMessage>("https://sqs.us-west-2.amazonaws.com/012345678910/MyAppProd");
  });
  ```

## Tutorial
<a name="mpf-get-started-tutorial"></a>

This tutorial demonstrates how to use the AWS Message Processing Framework for .NET. It creates two applications: an ASP.NET Core Minimal API that sends messages to an Amazon SQS queue when it receives a request at an API endpoint, and a long-running console application that polls for these messages and handles them.
+ The instructions in this tutorial favor the .NET CLI, but you can perform this tutorial by using either cross-platform tools such as the .NET CLI or Microsoft Visual Studio. For information about tools, see [Installing and configuring your toolchain for the AWS SDK for .NET](net-dg-dev-env.md).
+ This tutorial assumes that you're using your `[default]` profile for credentials. It also assumes that short-term credentials are available with appropriate permissions for sending and receiving Amazon SQS messages. For more information, see [Authenticating the AWS SDK for .NET with AWS](creds-idc.md) and the security topics for [SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-authentication-and-access-control.html).

**Note**
By running this tutorial, you might incur costs for SQS messaging.

### Steps
<a name="mpf-tutorial-steps"></a>
+ [Create an SQS queue](#mpf-tutorial-queue)
+ [Create and run the publishing application](#mpf-tutorial-publish)
+ [Create and run the handling application](#mpf-tutorial-handle)
+ [Cleanup](#mpf-tutorial-cleanup)

### Create an SQS queue
<a name="mpf-tutorial-queue"></a>

This tutorial requires an SQS queue to send messages to and receive messages from. A queue can be created by using one of the following commands for the AWS CLI or the AWS Tools for PowerShell. Take note of the queue URL that is returned so that you can specify it in the framework configuration that follows.

------
#### [ AWS CLI ]

```
aws sqs create-queue --queue-name {{DemoQueue}}
```

------
#### [ AWS Tools for PowerShell ]

```
New-SQSQueue -QueueName DemoQueue
```

------

### Create and run the publishing application
<a name="mpf-tutorial-publish"></a>

Use the following procedure to create and run the publishing application.

1. Open a command prompt or terminal. Find or create an operating system folder under which you can create a .NET project.

1. In that folder, run the following command to create the .NET project.

   ```
   dotnet new webapi --name Publisher
   ```

1. Navigate into the new project's folder. Add a dependency on the AWS Message Processing Framework for .NET.

   ```
   cd Publisher
   dotnet add package AWS.Messaging
   ```
**Note**
If you're using AWS IAM Identity Center for authentication, be sure to also add `AWSSDK.SSO` and `AWSSDK.SSOOIDC`.

1. Replace the code in `Program.cs` with the following code.

   ```
   using AWS.Messaging;
   using Microsoft.AspNetCore.Mvc;
   using Publisher;

   var builder = WebApplication.CreateBuilder(args);

   // Add services to the container.
   // Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle.
   builder.Services.AddEndpointsApiExplorer();
   builder.Services.AddSwaggerGen();

   // Configure the AWS Message Processing Framework for .NET.
   builder.Services.AddAWSMessageBus(builder =>
   {
       // Check for input SQS URL.
       // The SQS URL should be passed as a command line argument or set in the Debug launch profile.
       if ((args.Length == 1) && (args[0].Contains("https://sqs.")))
       {
           // Register that you'll publish messages of type GreetingMessage:
           // 1. To a specified queue.
           // 2. Using the message identifier "greetingMessage", which will be used
           //    by handlers to route the message to the appropriate handler.
           builder.AddSQSPublisher<GreetingMessage>(args[0], "greetingMessage");
       }
       // You can map additional message types to queues or topics here as well.
   });
   var app = builder.Build();

   // Configure the HTTP request pipeline.
   if (app.Environment.IsDevelopment())
   {
       app.UseSwagger();
       app.UseSwaggerUI();
   }

   app.UseHttpsRedirection();

   // Create an API Endpoint that receives GreetingMessage objects
   // from the caller and then sends them as an SQS message.
   app.MapPost("/greeting", async ([FromServices] IMessagePublisher publisher, Publisher.GreetingMessage message) =>
       {
           return await PostGreeting(message, publisher);
       })
   .WithName("SendGreeting")
   .WithOpenApi();

   app.Run();

   public partial class Program
   {
       /// <summary>
       /// Endpoint for posting a greeting message.
       /// </summary>
       /// <param name="greetingMessage">The greeting message.</param>
       /// <param name="messagePublisher">The message publisher.</param>
       /// <returns>Async task result.</returns>
       public static async Task<IResult> PostGreeting(GreetingMessage greetingMessage,
           IMessagePublisher messagePublisher)
       {
           if (greetingMessage.SenderName == null || greetingMessage.Greeting == null)
           {
               return Results.BadRequest();
           }

           // Publish the message to the queue configured above.
           await messagePublisher.PublishAsync(greetingMessage);

           return Results.Ok();
       }
   }

   namespace Publisher
   {
       /// <summary>
       /// This class represents the message contents.
       /// </summary>
       public class GreetingMessage
       {
           public string? SenderName { get; set; }
           public string? Greeting { get; set; }
       }
   }
   ```

1. Run the following command. This should open a browser window with the Swagger UI, which allows you to explore and test your API.

   ```
   dotnet watch run {{<queue URL created earlier>}}
   ```

1. Open the `/greeting` endpoint and choose **Try it out**.

1. Specify `senderName` and `greeting` values for the message, and choose **Execute**. This invokes your API, which sends the SQS message.

### Create and run the handling application
<a name="mpf-tutorial-handle"></a>

Use the following procedure to create and run the handling application.

1. Open a command prompt or terminal. Find or create an operating system folder under which you can create a .NET project.

1. In that folder, run the following command to create the .NET project.

   ```
   dotnet new console --name Handler
   ```

1. Navigate into the new project's folder. Add a dependency on the AWS Message Processing Framework for .NET. Also add the `Microsoft.Extensions.Hosting` package, which allows you to configure the framework through the [.NET Generic Host](https://learn.microsoft.com/en-us/dotnet/core/extensions/generic-host).

   ```
   cd Handler
   dotnet add package AWS.Messaging
   dotnet add package Microsoft.Extensions.Hosting
   ```
**Note**
If you're using AWS IAM Identity Center for authentication, be sure to also add `AWSSDK.SSO` and `AWSSDK.SSOOIDC`.

1. Replace the code in `Program.cs` with the following code.

   ```
   using AWS.Messaging;
   using Handler;
   using Microsoft.Extensions.DependencyInjection;
   using Microsoft.Extensions.Hosting;

   var builder = Host.CreateDefaultBuilder(args);

   builder.ConfigureServices(services =>
   {
       // Register the AWS Message Processing Framework for .NET.
       services.AddAWSMessageBus(builder =>
       {
           // Check for input SQS URL.
           // The SQS URL should be passed as a command line argument or set in the Debug launch profile.
           if ((args.Length == 1) && (args[0].Contains("https://sqs.")))
           {
               // Register you'll poll the following queue.
               builder.AddSQSPoller(args[0]);

               // And that messages of type "greetingMessage" should be:
               // 1. Deserialized as GreetingMessage objects.
               // 2. Which are then passed to GreetingMessageHandler.
               builder.AddMessageHandler<GreetingMessageHandler, GreetingMessage>("greetingMessage");

           }
           // You can add additional message handlers here, using different message types.
       });
   });

   var host = builder.Build();
   await host.RunAsync();

   namespace Handler
   {
       /// <summary>
       /// This class represents the message contents.
       /// </summary>
       public class GreetingMessage
       {
           public string? SenderName { get; set; }
           public string? Greeting { get; set; }
       }

       /// <summary>
       /// This handler is invoked each time you receive the message.
       /// </summary>
       public class GreetingMessageHandler : IMessageHandler<GreetingMessage>
       {
           public Task<MessageProcessStatus> HandleAsync(
               MessageEnvelope<GreetingMessage> messageEnvelope,
               CancellationToken token = default)
           {
               Console.WriteLine(
                   $"Received message {messageEnvelope.Message.Greeting} from {messageEnvelope.Message.SenderName}");
               return Task.FromResult(MessageProcessStatus.Success());
           }
       }
   }
   ```

1. Run the following command. This starts a long-running poller.

   ```
   dotnet run {{<queue URL created earlier>}}
   ```

   Shortly after startup the application will receive the message that was sent in the first part of this tutorial and log the following message:

   ```
   Received message {greeting} from {senderName}
   ```

1. Press `Ctrl+C` to stop the poller.

### Cleanup
<a name="mpf-tutorial-cleanup"></a>

Use one of the following commands for the AWS CLI or the AWS Tools for PowerShell to delete the queue.

------
#### [ AWS CLI ]

```
aws sqs delete-queue --queue-url "{{<queue URL created earlier>}}"
```

------
#### [ AWS Tools for PowerShell ]

```
Remove-SQSQueue -QueueUrl "{{<queue URL created earlier>}}"
```

------
