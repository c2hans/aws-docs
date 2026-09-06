---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/troubleshooting-runtime-errors.html
---

# Getting started troubleshooting runtime errors in the AWS SDK for C\+\+
<a name="troubleshooting-runtime-errors"></a>

As you learn to develop applications with the AWS SDK for C\+\+, it's also valuable to get comfortable in using both the AWS Management Console and the AWS CLI. These tools can be used interchangeably for various troubleshooting and diagnostics when runtime errors are encountered.

The following tutorial shows you an example of these troubleshooting and diagnostics tasks. It focuses on the `Access denied` error, which can be encountered for several different reasons. The tutorial shows an example of how you might determine the actual cause of the error. It focuses on two of the possible causes: incorrect permissions for the current user and a resource that isn't available to the current user.

**To get the project source and executables**

1. Download the Amazon S3 code example folder from [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code) on GitHub.

1. Open `delete_bucket.cpp` and notice that there are two methods: `main()` and `DeleteBucket()`. `DeleteBucket()` uses the SDK to delete the bucket.

1. Build the Amazon S3 example, using the same build steps explained in [Getting started using the AWS SDK for C\+\+](getting-started.md). The build process generates an executable for each source file.

1. Open a command prompt to the folder where your build system generated your build executables. Run the executable `run_create_bucket` (your actual executable filename will differ based on your operating system). This creates a bucket in your account (so that you have one to delete).

1. In the command prompt, run the executable `run_delete_bucket`. This example expects a parameter of the name of the bucket that you want to delete. Provide an incorrect bucket name; intentionally create a typo in this bucket name for now, so that we can explore troubleshooting.

1. Confirm that you get an `Access Denied` error message. *Getting an `Access Denied` error message leads you to question whether you created a user with full permissions for Amazon S3, which you'll verify next.*

**To install the AWS CLI and find the **username** that is making calls to AWS**

1. To install the latest AWS CLI to your development machine, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the *AWS Command Line Interface User Guide*.

1. To verify the AWS CLI is working, open a command prompt and run command `aws -\-version`

   ```
   $ aws -\-version
   aws-cli/2.1.29 Python/3.8.8 Windows/10 exe/AMD64 prompt/off
   ```

1. To obtain the username that is actually making the calls to AWS, run the AWS CLI command `aws sts get-caller-identity`. In the following example output, that username is *userX*

   ```
   $ aws sts get-caller-identity
   {
       "UserId": "A12BCD34E5FGHI6JKLM",
       "Account": "1234567890987",
       "Arn": "arn:aws:iam::1234567890987:user/userX"
   }
   ```

   There are many ways to specify credentials, but if you followed the approach in [Authenticating with AWS using AWS SDK for C\+\+](credentials.md) then this username comes from your AWS shared credentials file. During that procedure you granted your user **AmazonS3FullAccess** permissions.
**Note**
Generally, most AWS CLI commands follow the syntax structure of:

   ```
   $ aws <{{command}}> <{{subcommand}}> [{{options and parameters}}]
   ```
where {{command}} is the service, and {{subcommand}} is the method being called on that service. For more details, see [Command structure in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-commandstructure.html) in the *AWS Command Line Interface User Guide*.

**To verify whether a user has permission to delete a bucket**

1. Open the [AWS Management Console](https://console.aws.amazon.com/) and log in. For more details, see [Getting Started with the AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html).

1. In the main navigation bar, for **Search for services...**, enter **IAM** and select the IAM service from the results.

1. From the **Dashboard** sidebar, or under **IAM Resources**, select **Users**.

1. From the table of users available for your account, select the username obtained in the preceding procedure.

1. Choose the **Permissions** tab of the **Summary** page, under the **Policy name** table, select **AmazonS3FullAccess**.

1. Look at the **Policy summary** and the JSON data. Verify that this user has full rights for the Amazon S3 service.

   ```
               "Effect": "Allow",
               "Action": "s3:*",
               "Resource": "*"
   ```

This process of elimination is common in ruling *out* where the problem might be. In this case, you've veriﬁed that the user does have the correct permissions, so the problem must be something else. That is, since you have the correct permissions to access your buckets, the `Access Denied` error may mean that you are trying to access a bucket that isn't yours. When troubleshooting, you'd next review the bucket name that was provided to the program, and notice that a bucket with that name doesn't exist in your account, and thus, you cannot 'access' it.

**To update the code example so it runs successfully**

1. Back in `delete_bucket.cpp`'s `main()` function, change the Region, using the enum, to the Region of your account. To find your Region of your account, log into the AWS Management Console, and locate the Region in the upper right-hand corner. Also in `main()`, change the bucket name to a bucket that **does** exist in your account. There are several ways to find your current bucket names:
   + You can use the `run_list_buckets` executable that also exists in this code example's folder to programatically get the names of your buckets.
   + Alternatively, you can also use the following AWS CLI command to list your Amazon S3 buckets.

     ```
     $ aws s3 ls
     2022-01-05 14:27:48 {{amzn-s3-demo-bucket}}
     ```
   + Alternatively, you can also use the [AWS Management Console](https://console.aws.amazon.com/). In the main navigation bar, in **Search for services...**, enter **S3**. The Buckets page lists your account's buckets.

1. Rebuild the code and run the updated executable `run_delete_bucket`.

1. Using either the AWS Management Console or the AWS CLI, verify that the Amazon S3 bucket that you created earlier has been deleted.
