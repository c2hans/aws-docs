---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/quick-start-s3-1-cross.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Simple cross-platform application using the AWS SDK for .NET
<a name="quick-start-s3-1-cross"></a>

This tutorial uses the AWS SDK for .NET and .NET Core for cross-platform development. The tutorial shows you how to use the SDK to list the [Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) that you own and, optionally, create a bucket.

You'll perform this tutorial using cross-platform tools such as the .NET command line interface (CLI). For other ways to configure your development environment, see [Installing and configuring your toolchain for the AWS SDK for .NET](net-dg-dev-env.md).

**Required for cross-platform .NET development on Windows, Linux, or macOS:**
+ Microsoft [.NET Core SDK](https://learn.microsoft.com/en-us/dotnet/fundamentals/), version 2.1, 3.1, or later, which includes the .NET command line interface (CLI) (**`dotnet`**) and the .NET Core runtime.
+ A code editor or integrated development environment (IDE) that is appropriate for your operating system and requirements. This is typically one that provides some support for .NET Core.

  Examples include [Microsoft Visual Studio Code (VS Code)](https://code.visualstudio.com/), [JetBrains Rider](https://www.jetbrains.com/rider/), and [Microsoft Visual Studio](https://visualstudio.microsoft.com/vs/).

**Note**
Before you use these tutorials, you must have first [installed your toolchain](net-dg-dev-env.md) and [configured SDK authentication](creds-idc.md).

## Steps
<a name="s3-1-cross-steps"></a>
+ [Create the project](#s3-1-cross-create-project)
+ [Create the code](#s3-1-cross-code)
+ [Run the application](#s3-1-cross-run)
+ [Cleanup](#s3-1-cross-clean-up)

## Create the project
<a name="s3-1-cross-create-project"></a>

1. Open the command prompt or terminal. Find or create an operating system folder under which you can create a .NET project.

1. In that folder, run the following command to create the .NET project.

   ```
   dotnet new console --name S3CreateAndList
   ```

1. Go to the newly created `S3CreateAndList` folder and run the following commands:

   ```
   dotnet add package AWSSDK.S3
   dotnet add package AWSSDK.SecurityToken
   dotnet add package AWSSDK.SSO
   dotnet add package AWSSDK.SSOOIDC
   ```

   The preceding commands install the NuGet packages from the [NuGet package manager](https://www.nuget.org/profiles/awsdotnet). Because we know exactly what NuGet packages we need for this tutorial, we can perform this step now. It's also common that the required packages become known during development. When this happens, a similar command can be run at that time.

## Create the code
<a name="s3-1-cross-code"></a>

1. In the `S3CreateAndList` folder, find and open `Program.cs` in your code editor.

1. Replace the contents with the following code and save the file.

   ```
   using System;
   using System.Threading.Tasks;

   // NuGet packages: AWSSDK.S3, AWSSDK.SecurityToken, AWSSDK.SSO, AWSSDK.SSOOIDC
   using Amazon.Runtime;
   using Amazon.Runtime.CredentialManagement;
   using Amazon.S3;
   using Amazon.S3.Model;
   using Amazon.SecurityToken;
   using Amazon.SecurityToken.Model;

   namespace S3CreateAndList
   {
       class Program
       {
           // This code is part of the quick tour in the developer guide.
           // See https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/quick-start.html
           // for complete steps.
           // Requirements:
           // - An SSO profile in the SSO user's shared config file with sufficient privileges for
   		//   STS and S3 buckets.
           // - An active SSO Token.
           //    If an active SSO token isn't available, the SSO user should do the following:
           //    In a terminal, the SSO user must call "aws sso login".

           // Class members.
           static async Task Main(string[] args)
           {
               // Get SSO credentials from the information in the shared config file.
               // For this tutorial, the information is in the [default] profile.
               var ssoCreds = LoadSsoCredentials("default");

               // Display the caller's identity.
               var ssoProfileClient = new AmazonSecurityTokenServiceClient(ssoCreds);
               Console.WriteLine($"\nSSO Profile:\n {await ssoProfileClient.GetCallerIdentityArn()}");

               // Create the S3 client is by using the SSO credentials obtained earlier.
               var s3Client = new AmazonS3Client(ssoCreds);

               // Parse the command line arguments for the bucket name.
               if (GetBucketName(args, out String bucketName))
               {
                   // If a bucket name was supplied, create the bucket.
                   // Call the API method directly
                   try
                   {
                       Console.WriteLine($"\nCreating bucket {bucketName}...");
                       var createResponse = await s3Client.PutBucketAsync(bucketName);
                       Console.WriteLine($"Result: {createResponse.HttpStatusCode.ToString()}");
                   }
                   catch (Exception e)
                   {
                       Console.WriteLine("Caught exception when creating a bucket:");
                       Console.WriteLine(e.Message);
                   }
               }

               // Display a list of the account's S3 buckets.
               Console.WriteLine("\nGetting a list of your buckets...");
               var listResponse = await s3Client.ListBucketsAsync();
               Console.WriteLine($"Number of buckets: {listResponse.Buckets.Count}");
               foreach (S3Bucket b in listResponse.Buckets)
               {
                   Console.WriteLine(b.BucketName);
               }
               Console.WriteLine();
           }

           //
           // Method to parse the command line.
           private static Boolean GetBucketName(string[] args, out String bucketName)
           {
               Boolean retval = false;
               bucketName = String.Empty;
               if (args.Length == 0)
               {
                   Console.WriteLine("\nNo arguments specified. Will simply list your Amazon S3 buckets." +
                     "\nIf you wish to create a bucket, supply a valid, globally unique bucket name.");
                   bucketName = String.Empty;
                   retval = false;
               }
               else if (args.Length == 1)
               {
                   bucketName = args[0];
                   retval = true;
               }
               else
               {
                   Console.WriteLine("\nToo many arguments specified." +
                     "\n\ndotnet_tutorials - A utility to list your Amazon S3 buckets and optionally create a new one." +
                     "\n\nUsage: S3CreateAndList [bucket_name]" +
                     "\n - bucket_name: A valid, globally unique bucket name." +
                     "\n - If bucket_name isn't supplied, this utility simply lists your buckets.");
                   Environment.Exit(1);
               }
               return retval;
           }

           //
           // Method to get SSO credentials from the information in the shared config file.
           static AWSCredentials LoadSsoCredentials(string profile)
           {
               var chain = new CredentialProfileStoreChain();
               if (!chain.TryGetAWSCredentials(profile, out var credentials))
                   throw new Exception($"Failed to find the {profile} profile");
               return credentials;
           }
       }

       // Class to read the caller's identity.
       public static class Extensions
       {
           public static async Task<string> GetCallerIdentityArn(this IAmazonSecurityTokenService stsClient)
           {
               var response = await stsClient.GetCallerIdentityAsync(new GetCallerIdentityRequest());
               return response.Arn;
           }
       }
   }
   ```

## Run the application
<a name="s3-1-cross-run"></a>

1. Run the following command.

   ```
   dotnet run
   ```

1. Examine the output to see the number of Amazon S3 buckets that you own, if any, and their names.

1. Choose a name for a new Amazon S3 bucket. Use "dotnet-quicktour-s3-1-cross-" as a base and add something unique to it, such as a GUID or your name. Be sure to follow the rules for bucket names, as described in [Rules for bucket naming](https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html#bucketnamingrules) in the [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. Run the following command, replacing {{amzn-s3-demo-bucket}} with the name of the bucket that you chose.

   ```
   dotnet run {{amzn-s3-demo-bucket}}
   ```

1. Examine the output to see the new bucket that was created.

## Cleanup
<a name="s3-1-cross-clean-up"></a>

While performing this tutorial, you created some resources that you can choose to clean up at this time.
+ If you don't want to keep the bucket that the application created in an earlier step, delete it by using the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).
+ If you don't want to keep your .NET project, remove the `S3CreateAndList` folder from your development environment.

## Where to go next
<a name="s3-1-cross-next"></a>

Go back to the [quick-tour menu](quick-start.md) or go straight to the [end of this quick tour](quick-start-next-steps.md).
