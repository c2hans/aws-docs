---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cloud9.html
---

# Use AWS Cloud9 with the AWS SDK for PHP Version 3
<a name="cloud9"></a>

**Note**
AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/).

AWS Cloud9 is a web-based integrated development environment (IDE) that contains a collection of tools that you use to code, build, run, test, debug, and release software in the cloud. You can use AWS Cloud9 with the AWS SDK for PHP to write and run your PHP code by using a browser. AWS Cloud9 includes tools such as a code editor and terminal. Because the AWS Cloud9 IDE is cloud based, you can work on your projects from your office, home, or anywhere by using an internet-connected machine. For general information about AWS Cloud9, see the [AWS Cloud9 User Guide](https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html).

Follow these instructions to set up AWS Cloud9 with the AWS SDK for PHP:
+  [Step 1: Set up your AWS account to use AWS Cloud9](#cloud9-php-account)
+  [Step 2: Set up your AWS Cloud9 development environment](#cloud9-php-environment)
+  [Step 3: Set up the AWS SDK for PHP](#cloud9-php-sdk)
+  [Step 4: Download example code](#cloud9-php-examples)
+  [Step 5: Run example code](#cloud9-php-run)

## Step 1: Set up your AWS account to use AWS Cloud9
<a name="cloud9-php-account"></a>

To use AWS Cloud9, sign in to the AWS Cloud9 console from the AWS Management Console.

**Note**
If you are using AWS IAM Identity Center to authenticate, you might need to add the required permission of `iam:ListInstanceProfilesForRole` to the user-attached policy in the IAM console.

To set up an IAM entity in your AWS account to access AWS Cloud9 and sign in to the AWS Cloud9 console, see [Team Setup for AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/setup.html) in the *AWS Cloud9 User Guide*.

## Step 2: Set up your AWS Cloud9 development environment
<a name="cloud9-php-environment"></a>

After you sign in to the AWS Cloud9 console, use the console to create an AWS Cloud9 development environment. After you create the environment, AWS Cloud9 opens the IDE for that environment.

For details, see [Creating an Environment in AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment.html) in the *AWS Cloud9 User Guide*.

**Note**
As you create your environment in the console for the first time, we recommend that you choose the option to **Create a new instance for environment (EC2)**. This option tells AWS Cloud9 to create an environment, launch an Amazon EC2 instance, and then connect the new instance to the new environment. This is the fastest way to begin using AWS Cloud9.

If the terminal isn’t already open in the IDE, open it. On the menu bar in the IDE, choose **Window, New Terminal**. You can use the terminal window to install tools and build your applications.

## Step 3: Set up the AWS SDK for PHP
<a name="cloud9-php-sdk"></a>

After AWS Cloud9 opens the IDE for your development environment, use the terminal window to set up the AWS SDK for PHP in your environment.

 Composer is the recommended way to install the AWS SDK for PHP. Composer is a tool for PHP that manages and installs the dependencies of your project.

For more information on how to install Composer, configure autoloading, and follow other best practices for defining dependencies, see [getcomposer.org](http://getcomposer.org).

### Install Composer
<a name="install-composer"></a>

If Composer is not already in your project, download and install Composer on the [Download Composer page](http://getcomposer.org/download).
+ For **Windows**, follow the Windows Installer instructions.
+ For **Linux**, follow the Command-line installation instructions.

### Add AWS SDK for PHP as a dependency via Composer
<a name="add-sdk-php-as-a-dependency-via-composer"></a>

If [Composer is already installed globally](https://getcomposer.org/doc/00-intro.md#globally) on your system, run the following in the base directory of your project to install AWS SDK for PHP as a dependency:

```
$ composer require aws/aws-sdk-php
```

Otherwise, type this Composer command to install the latest version of the AWS SDK for PHP as a dependency.

```
$ php -d memory_limit=-1 composer.phar require aws/aws-sdk-php
```

### Add autoloader to your php scripts
<a name="add-autoloader-to-your-php-scripts"></a>

Installing Composer creates several folders and files in your environment. The primary file you will use is `autoload.php`, which is in the `vendor` folder in your environment.

To utilize the AWS SDK for PHP in your scripts, include the autoloader in your scripts, as follows.

```
<?php
   require '/path/to/vendor/autoload.php';
?>
```

## Step 4: Download example code
<a name="cloud9-php-examples"></a>

Use the terminal window to download example code for the AWS SDK for PHP into the AWS Cloud9 development environment.

To download a copy of all the code examples used in the official AWS SDK documentation into your environment’s root directory, run the following command:

```
$ git clone https://github.com/awsdocs/aws-doc-sdk-examples.git
```

The code examples for the AWS SDK for PHP are located at `ENVIRONMENT_NAME/aws-doc-sdk-examples/php` directory, where `ENVIRONMENT_NAME` is the name of your development environment.

To follow along using an Amazon S3 example, we recommend starting with code example `ENVIRONMENT_NAME/aws-doc-sdk-examples/php/example_code/s3/ListBuckets.php`. This example will list your Amazon S3 buckets. Use the terminal window to navigate to the `s3` directory and list the files.

```
$ cd aws-doc-sdk-examples/php/example_code/s3
$ ls
```

To open the file in AWS Cloud9, you can click on the `ListBuckets.php` directly in the terminal window.

For more support in understanding code examples, see [AWS SDK for PHP Code Examples](examples_index.md).

## Step 5: Run example code
<a name="cloud9-php-run"></a>

To run code in your AWS Cloud9 development environment, choose the **Run** button in the top menu bar. AWS Cloud9 automatically detects the `.php` file extension and uses the **PHP (built-in web server)** runner to run the code. However, for this example we actually want the **PHP (`cli`)** option. For more information about running code in AWS Cloud9, see [Run Your Code](https://docs.aws.amazon.com/cloud9/latest/user-guide/build-run-debug.html#build-run-debug-run) in the *AWS Cloud9 User Guide*.

In the following screenshot, note these basic areas:
+ 1: Run. The **Run** button is located on the top menu bar. This opens a new tab for your results.
**Note**
You can also manually create new run configurations. On the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**.
+ 2: Command. AWS Cloud9 populates the **Command** text box with the path and file name to the file you run. If your code expects any command line parameters to be passed in, these can be added to the command line in the same way that you would when running the code through a terminal window.
+ 3: Runner. AWS Cloud9 detects that your file extension is `.php` and selects the **PHP (built-in web server)** Runner to run your code. Select **PHP (`cli`)** to run this example instead.

![Choosing Run from the top menu bar of the AWS Cloud9 IDE opens a new tab with the Command box populated and the PHP runner already selected.](http://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/images/cloud9_runconfig.png)

Any output generated from the running code displays in the tab.
