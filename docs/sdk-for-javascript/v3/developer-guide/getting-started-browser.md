---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started-browser.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Get started in the browser
<a name="getting-started-browser"></a>

This section walks you through an example that demonstrates how to run version 3 (V3) of the AWS SDK for JavaScript in the browser.

**Note**
Running V3 in the browser is slightly different from version 2 (V2). For more information, see [Using browsers in V3](welcome.md#v3_browsers).

For other examples of using (V3) of the AWS SDK for JavaScript, see [SDK for JavaScript (v3) code examples](javascript_code_examples.md).

**This web application example shows you:**
+ How to access AWS services using Amazon Cognito for authentication.
+ How to read a listing of objects in a Amazon Simple Storage Service (Amazon S3) bucket using a AWS Identity and Access Management (IAM) role.

**Note**
This example does not use AWS IAM Identity Center for authentication.

## The Scenario
<a name="getting-started-browser-scenario"></a>

Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance. You can use Amazon S3 to store data as objects within containers called buckets. For more information about Amazon S3, see the [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

This example shows you how to set up and run a web app that assumes a IAM role to read from a Amazon S3 bucket. The example uses React front-end library and Vite front-end tooling to provide a JavaScript development environment. The web app uses an Amazon Cognito identity pool to provide credentials needed to access AWS services. The included code example demonstrates the basic patterns for loading and using the AWS SDK for JavaScript in web apps.

## Step 1: Create an Amazon Cognito identity pool and IAM role
<a name="getting-started-browser-create-identity-pool"></a>

In this exercise, you create and use an Amazon Cognito identity pool to provide unauthenticated access to your web app for the Amazon S3 service. Creating an identity pool also creates a AWS Identity and Access Management (IAM) role to support unauthenticated guest users. For this example, we will only work with the unauthenticated user role to keep the task focused. You can integrate support for an identity provider and authenticated users later. For more information about adding a Amazon Cognito identity pool, see [Tutorial: Creating an identity pool](https://docs.aws.amazon.com/cognito/latest/developerguide/tutorial-create-identity-pool.html) in the *Amazon Cognito Developer Guide*.

**To create an Amazon Cognito identity pool and associated IAM role**

1. Sign in to the AWS Management Console and open the Amazon Cognito console at [https://console.aws.amazon.com/cognito/](https://console.aws.amazon.com/cognito/).

1. In the left navigation pane, choose **Identity pools**.

1. Choose **Create identity pool**.

1. In **Configure identity pool trust**, choose **Guest access** for user authentication.

1. In **Configure permissions**, choose **Create a new IAM role** and enter a name (for example, *getStartedRole*) in the **IAM role name**.

1. In **Configure properties**, enter a name (for example, *getStartedPool*) in **Identity pool name**.

1. In **Review and create**, confirm the selections that you made for your new identity pool. Select **Edit** to return to the wizard and change any settings. When you're done, select **Create identity pool**.

1. Note the **Identity pool ID** and the **Region** of the newly created Amazon Cognito identity pool. You need these values to replace {{IDENTITY\_POOL\_ID}} and {{REGION}} in [Step 4: Set up the browser code](#getting-started-browser-create-html).

After you create your Amazon Cognito identity pool, you're ready to add permissions for Amazon S3 that are needed by your web app.

## Step 2: Add a policy to the created IAM role
<a name="getting-started-browser-iam-role"></a>

To enable access to a Amazon S3 bucket in your web app, use the unauthenticated IAM role (for example, *getStartedRole*) created for your Amazon Cognito identity pool (for example, *getStartedPool*). This requires you to attach an IAM policy to the role. For more information about modifying IAM roles, see [Modifying a role permissions policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-modify_permissions-policy) in the *IAM User Guide*.

**To add an Amazon S3 policy to the IAM role associated with unauthenticated users**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Roles**.

1. Choose the name of the role that you want to modify (for example, *getStartedRole*), and then choose the **Permissions** tab.

1. Choose **Add permissions** and then choose **Attach policies**.

1. In the **Add permissions** page for this role, find and then select the check box for **AmazonS3ReadOnlyAccess**.
**Note**
You can use this process to enable access to any AWS service.

1. Choose **Add permissions**.

After you create your Amazon Cognito identity pool and add permissions for Amazon S3 to your IAM role for unauthenticated users, you are ready to add and configure a Amazon S3 bucket.

## Step 3: Add a Amazon S3 bucket and object
<a name="getting-started-browser-create-s3-bucket"></a>

In this step, you will add a Amazon S3 bucket and object for the example. You will also enable cross-origin resource sharing (CORS) for the bucket. For more information about creating Amazon S3 buckets and objects, see [Getting started with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) in the *Amazon S3 User Guide*.

**To add an Amazon S3 bucket and object with CORS**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Buckets** and choose **Create bucket**.

1. Enter a bucket name that conforms to [bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) (for example, *getstartedbucket*) and choose **Create bucket**.

1. Choose the bucket you created, and then choose the **Objects** tab. Then choose **Upload**.

1. Under **Files and folders**, choose **Add files**.

1. Choose a file to upload, and then choose **Open**. Then choose **Upload** to complete uploading the object to your bucket.

1. Next, choose the **Permissions** tab of your bucket, and then choose **Edit** in the **Cross-origin resource sharing (CORS)** section. Enter the following JSON:

   ```
   [
     {
       "AllowedHeaders": [
         "*"
       ],
       "AllowedMethods": [
         "GET"
       ],
       "AllowedOrigins": [
         "*"
       ],
       "ExposeHeaders": []
     }
   ]
   ```

1. Choose **Save changes**.

After you have added a Amazon S3 bucket and added an object, you're ready to set up the browser code.

## Step 4: Set up the browser code
<a name="getting-started-browser-create-html"></a>

The example application consists of a single-page React application. The files for this example can be found [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/web/s3/list-objects).

**To set up the example application**

1. Install [Node.js](https://nodejs.org/en/download).

1. From the command line, clone the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/):

   ```
   git clone --depth 1 https://github.com/awsdocs/aws-doc-sdk-examples.git
   ```

1. Navigate to the example application:

   ```
   cd aws-doc-sdk-examples/javascriptv3/example_code/web/s3/list-objects/
   ```

1. Run the following command to install the required packages:

   ```
   npm install
   ```

1. Next, open `src/App.tsx` in a text editor and complete the following:
   + Replace {{YOUR\_IDENTITY\_POOL\_ID}} with the Amazon Cognito identity pool ID you noted in [Step 1: Create an Amazon Cognito identity pool and IAM role](#getting-started-browser-create-identity-pool).
   + Replace the value for region to the region assigned for your Amazon S3 bucket and Amazon Cognito identity pool. Note that the regions for both service must be the same (for example, *us-east-2*).
   + Replace {{bucket-name}} with bucket name you created in [Step 3: Add a Amazon S3 bucket and object](#getting-started-browser-create-s3-bucket).

After you have replaced the text, save the `App.tsx` file. You're now ready to run the web app.

## Step 5: Run the Example
<a name="getting-started-browser-run-sample"></a>

**To run the example application**

1. From the command line, navigate to the example application:

   ```
   cd aws-doc-sdk-examples/javascriptv3/example_code/web/s3/list-objects/
   ```

1. From the command line, run the following command:

   ```
   npm run dev
   ```

   The Vite development environment will run with the following message:

   ```
   VITE v4.3.9  ready in 280 ms

   ➜  Local:   http://localhost:5173/
   ➜  Network: use --host to expose
   ➜  press h to show help
   ```

1. In your web browser, navigate to the URL shown above (for example, http://localhost:5173). The example app will show you a list of object filenames in your Amazon S3 bucket.

## Cleanup
<a name="getting-started-browser-cleanup"></a>

To clean up the resources you created during this tutorial, do the following:
+ In [the Amazon S3 console](https://console.aws.amazon.com/s3/), delete any objects and any buckets created (for example, *getstartedbucket*).
+ In [the IAM console](https://console.aws.amazon.com/iam/home#/roles), delete the role name (for example, *getStartedRole*).
+ In [the Amazon Cognito console](https://console.aws.amazon.com/cognito/home#/identity), delete the identity pool name (for example, *getStartedPool*).
