---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/ecr-working.html
---

# Working with Amazon Elastic Container Registry
<a name="ecr-working"></a>

You can access the Amazon Elastic Container Registry (Amazon ECR) service directly from the AWS Explorer in VS Code and use it to push a program image to an Amazon ECR repository. To get started, you need to do these steps:

1. Create a Dockerfile that contains the information necessary to build an image.

1. Build an image from that Dockerfile and tag the image for processing.

1. Create a repository inside your Amazon ECR instance.

1. Push the tagged image to your repository.

## Prerequisites
<a name="prereqs-awstoolkit-vscode-ecr"></a>

You need to complete these steps in order to access the Amazon ECR service from the VS Code Explorer.

### Create an IAM user
<a name="create-an-iam-user"></a>

Before you can access an AWS service, such as Amazon ECR, you must provide credentials. This is so that the service can determine if you have permission to access its resources. We don't recommend that you access AWS directly through the credentials for your root AWS account. Instead, use AWS Identity and Access Management (IAM) to create an IAM user and then add that user to an IAM group with administrative permissions. You can then access AWS using a special URL and the credentials for the IAM user.

If you signed up for AWS but didn't create an IAM user for yourself, you can create one by using the IAM console.

To create an administrator user, choose one of the following options.

| Choose one way to manage your administrator | To | By | You can also |
| --- | --- | --- | --- |
| In IAM Identity Center (Recommended) | Use short-term credentials to access AWS.This aligns with the security best practices. For information about best practices, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) in the *IAM User Guide*. | Following the instructions in [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the AWS IAM Identity Center User Guide. | Configure programmatic access by [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the AWS Command Line Interface User Guide. |
| In IAM (Not recommended) | Use long-term credentials to access AWS. | Following the instructions in [ Create an IAM user for emergency access](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-emergency-iam-user.html) in the IAM User Guide. | Configure programmatic access by [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the IAM User Guide. |

To sign in as this new IAM user, sign out of the AWS console, then use the following URL. In the following URL, where *your\_aws\_account\_id* is your AWS account number without the hyphens (for example, if your AWS account number is `1234-5678-9012`, your AWS account ID is `123456789012`):

```
https://{{your_aws_account_id}}.signin.aws.amazon.com/console/
```

Enter the IAM user name and password that you just created. When you're signed in, the navigation bar displays "*your\_user\_name* @ *your\_aws\_account\_id*".

If you don't want the URL for your sign-in page to contain your AWS account ID, you can create an account alias. From the IAM dashboard, choose **Customize** and enter an **Account Alias**. This can be your company name. For more information, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html) in the IAM User Guide.

To sign in after you create an account alias, use the following URL:

```
https://{{your_account_alias}}.signin.aws.amazon.com/console/
```

To verify the sign-in link for IAM users for your account, open the IAM console and check under **IAM users sign-in link** on the dashboard.

For more information about IAM, see the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/).

### Install and configure Docker
<a name="create-an-iam-user"></a>

You can install and configure Docker by selecting your preferred operating system from the [Install Docker Engine](https://docs.docker.com/engine/install/) user guide and following the instructions.

### Install and configure AWS CLI version 2
<a name="create-an-iam-user"></a>

Install and configure AWS CLI version 2 by selecting your preferred operating system from the [Installing, updating, and uninstalling the AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) user guide.

## 1. Creating a Dockerfile
<a name="dockerfile-ecr-vsctoolkit"></a>

Docker uses a file called a Dockerfile to define an image that can be pushed and stored on a remote repository. Before you can upload an image to an ECR repository, you must create a Dockerfile and then build an image from that Dockerfile.

**Creating a Dockerfile**

1. Use the Toolkit for VS Code explorer to navigate to the directory where you want to store your Dockerfile.

1. Create a new file that's called **Dockerfile**.
**Note**
VS Code could prompt you to select a file type or file extension. If this occurs, select **plaintext**. Vs Code has a "dockerfile" extension. However, we don't recommend you use it. This is because the extension might cause conflicts with certain versions of Docker or other associated applications.

**Edit your Dockerfile using VS Code**

If your Dockerfile has a file extension, open the context (right-click) menu for the file and remove the file extension.

After the file extension is removed from your Dockerfile:

1. Open the empty Dockerfile directly in VS Code.

1. Copy the contents of the following example into your Dockerfile:
**Example Dockerfile image template**

   ```
   FROM ubuntu:18.04

   # Install dependencies
   RUN apt-get update && \
    apt-get -y install apache2

   # Install apache and write hello world message
   RUN echo 'Hello World!' > /var/www/html/index.html

   # Configure apache
   RUN echo '. /etc/apache2/envvars' > /root/run_apache.sh && \
    echo 'mkdir -p /var/run/apache2' >> /root/run_apache.sh && \
    echo 'mkdir -p /var/lock/apache2' >> /root/run_apache.sh && \
    echo '/usr/sbin/apache2 -D FOREGROUND' >> /root/run_apache.sh && \
    chmod 755 /root/run_apache.sh

   EXPOSE 80

   CMD /root/run_apache.sh
   ```

   This is a Dockerfile that uses an Ubuntu 18.04 image. The **RUN** instructions update the package caches. Install software packages for the web server, and then write the "Hello World\!" content to the document root of the web server. The **EXPOSE** instruction exposes port 80 on the container, and the **CMD** instruction starts the web server.

1. Save your Dockerfile.
**Important**
Make sure that your Dockerfile doesn't have an extension attached to the name. A Dockerfile with extensions might cause conflicts with certain versions of Docker or other associated applications.

## 2 . Build your image from your Dockerfile
<a name="build-docker-image"></a>

The Dockerfile that you created contains the information necessary to build an image for a program. Before you can push that image to your Amazon ECR instance, you must first build the image.

**Build an image from your Dockerfile**

1. Use the Docker CLI or a CLI that's integrated with your instance of Docker to navigate into the directory that contains your Dockerfile.

1. Run the **Docker build** command to build the image that's defined in your Dockerfile.

   ```
             docker build -t hello-world .
   ```

1. Run the **Docker images** command to verify that the image was created correctly.

   ```
   docker images --filter reference=hello-world
   ```
**example output:**

   ```
   REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
   hello-world         latest              e9ffedc8c286        4 minutes ago       241MB
   ```

1.
**Note**
This step isn't necessary to create or push your image, but you can see how the program image works when it's run.

   To run the newly built image use the **Docker run** command.

   ```
   docker run -t -i -p 80:80 hello-world
   ```

   The **-p** option that's specified in the preceding example maps the exposed **port 80** on the container to **port 80** of the host system. If you're running Docker locally, navigate to [http://localhost:80](http://localhost:80) using your web browser. If the program ran correctly, a "Hello World\!" statement is displayed.

   For more information about the **Docker run** command, see [Docker run reference](https://docs.docker.com/engine/reference/run/) on the Docker website.

## 3. Create a new repository
<a name="create-repository"></a>

To upload your image into your Amazon ECR instance, create a new repository where it can be stored in.

**Create a new Amazon ECR repository**

1. From the VS Code **Activity Bar**, choose the **AWS Toolkit icon**.

1. Expand the ** AWS Explorer** menu.

1. Locate the default AWS Region that's associated with your AWS account. Then, select it to see a list of the services that are through the Toolkit for VS Code.

1. Choose the **ECR \+** option to begin the **Create new repository** process.

1. Follow the prompts to complete the process.

1. After it's complete, you can access your new repository from the **ECR** section of the AWS Explorer menu.

## 4. Push, pull, and delete images
<a name="push-image"></a>

After you built an image from your Dockerfile and created a repository, you can push your image into your Amazon ECR repository. Additionally, using the AWS Explorer with Docker and the AWS CLI, you can do the following:
+ Pull an image from your repository.
+ Delete an image that's stored in your repository.
+ Delete your repository.

**Authenticate Docker with your default registry**

Authentication is required to exchange data between Amazon ECR and Docker instances. To authenticate Docker with your registry:

1. Open a command line operating system that's connected to your instance of AWS CLI.

1. Use the **get-login-password** method to authenticate to your private ECR registry.

   ```
   aws ecr get-login-password --region region | docker login --username AWS --password-stdin AWS_account_id.dkr.ecr.region.amazonaws.com
   ```
**Important**
In the preceding command, you must update both the **region** and the **AWS\_account\_id** to the information that's specific to your AWS account.

**Tag and push an image to your repository**

After you authenticated Docker with your instance of AWS, push an image to your repository.

1. Use the **Docker images** command to view the images that you stored locally and identify the one you would like to tag.

   ```
   docker images
   ```
**example output:**

   ```
   REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
   hello-world         latest              e9ffedc8c286        4 minutes ago       241MB
   ```

1. Tag your image with the **Docker tag** command.

   ```
   docker tag hello-world:latest AWS_account_id.dkr.ecr.region.amazonaws.com/hello-world:latest
   ```

1. Push the tagged image to your repository with the **Docker tag** command.

   ```
   docker push AWS_account_id.dkr.ecr.region.amazonaws.com/hello-world:latest
   ```
**example output:**

   ```
   The push refers to a repository [AWS_account_id.dkr.ecr.region.amazonaws.com/hello-world] (len: 1)
   e9ae3c220b23: Pushed
   a6785352b25c: Pushed
   0998bf8fb9e9: Pushed
   0a85502c06c9: Pushed
   latest: digest: sha256:215d7e4121b30157d8839e81c4e0912606fca105775bb0636b95aed25f52c89b size: 6774
   ```

After your tagged image has been successfully uploaded to your repository, it's visible in the AWS Explorer menu.

**Pull an image from Amazon ECR**
+ You can pull an image to your local instance of **Docker tag** command.

  ```
  docker pull AWS_account_id.dkr.ecr.region.amazonaws.com/hello-world:latest
  ```
**example output:**

  ```
  The push refers to a repository [AWS_account_id.dkr.ecr.region.amazonaws.com/hello-world] (len: 1)
  e9ae3c220b23: Pushed
  a6785352b25c: Pushed
  0998bf8fb9e9: Pushed
  0a85502c06c9: Pushed
  latest: digest: sha256:215d7e4121b30157d8839e81c4e0912606fca105775bb0636b95aed25f52c89b size: 6774
  ```

**Delete an image from your Amazon ECR repository**

There are two methods for deleting an image from VS Code. The first method is to use the AWS Explorer.

1. From the AWS Explorer, expand the **ECR**menu

1. Expand the repository that you want to delete an image from

1. Choose the image tag associated with the image that you wish to delete, by opening the context menu (right-click)

1. Choose the **Delete Tag...** option to delete all stored images associated with that tag

**Delete an image using the AWS CLI**
+ You can also delete an image from your repository with the **AWS ecr batch-delete-image** command.

  ```
  AWS ecr batch-delete-image \
        --repository-name hello-world \
        --image-ids imageTag=latest
  ```
**example output:**

  ```
  {
      "failures": [],
      "imageIds": [
          {
              "imageTag": "latest",
              "imageDigest": "sha256:215d7e4121b30157d8839e81c4e0912606fca105775bb0636b95aed25f52c89b"
          }
      ]
  }
  ```

**Delete a repository from your Amazon ECR instance**

There are two methods for deleting a repository from VS Code. The first method is to use the AWS Explorer.

1. From the AWS Explorer, expand the **ECR** menu

1. Choose the repository that you want to delete by opening the context (right-click) menu

1. Choose the **Delete Repository...** option to the chosen repository

**Delete an Amazon ECR repository from the AWS CLI**
+ You can delete a repository with the **AWS ecr delete-repository** command.
**Note**
By default, you can't delete a repository that contains images. However, the **--force** flag allows this.

  ```
          AWS ecr delete-repository \
        --repository-name hello-world \
        --force
  ```
**example output:**

  ```
  {
      "failures": [],
      "imageIds": [
          {
              "imageTag": "latest",
              "imageDigest": "sha256:215d7e4121b30157d8839e81c4e0912606fca105775bb0636b95aed25f52c89b"
          }
      ]
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
