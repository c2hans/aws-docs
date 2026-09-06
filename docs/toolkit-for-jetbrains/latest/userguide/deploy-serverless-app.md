---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/deploy-serverless-app.html
---

# Creating an AWS serverless application by using the AWS Toolkit for JetBrains
<a name="deploy-serverless-app"></a>

To complete this procedure, you must first install the AWS Toolkit and, if you haven't yet, connect to an AWS account for the first time. Then with IntelliJ IDEA, PyCharm, WebStorm, or JetBrains Rider already running, do the following."?>

1. With IntelliJ IDEA, PyCharm, WebStorm, or JetBrains Rider already running, do one of the following:
   + For IntelliJ IDEA or WebStorm, choose **File**, **New**, **Project**.
   + For PyCharm, choose **File**, **New Project**.
   + For JetBrains Rider, choose **File**, **New** for a new solution. Or right-click an existing solution in the **Explorer** tool window, and then choose **Add**, **New Project**.

1. For IntelliJ IDEA, choose **AWS**, **AWS Serverless Application**, and then choose **Next**.
![Choosing to create an AWS serverless application in IntelliJ IDEA](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/sam-create-intellij.png)

   For PyCharm, choose **AWS Serverless Application**.
![Choosing to create an AWS serverless application in PyCharm](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/sam-create-pycharm.png)

   For WebStorm, choose **AWS Serverless Application**.
![Choosing to create an AWS serverless application in WebStorm](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/sam-create-webstorm.png)

   For JetBrains Rider, choose **AWS Serverless Application**.
![Choosing to create an AWS serverless application in JetBrains Rider](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/sam-create-rider.png)

1. Complete the [New Project dialog box (or the New Solution dialog box for JetBrains Rider)](new-project-dialog.md), and then choose **Finish** (for IntelliJ IDEA) or **Create** (for PyCharm, WebStorm, or JetBrains Rider). The AWS Toolkit for JetBrains creates the project and adds the serverless application's code files to the new project.

1. If you're using IntelliJ IDEA, with the **Project** tool window already open and displaying the project that contains the serverless application's files, do one of the following:
   + For Maven-based projects, right-click the project's `pom.xml` file, and then choose **Add as Maven Project**.
![Choosing to add the POM file as a Maven project](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/add-as-maven-project.png)
   + For Gradle-based projects, right-click the project's `build.gradle` file, and then choose **Import Gradle project**.
![Choosing to import the Gradle project](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/import-gradle-project.png)

     Complete the **Import Module from Gradle** dialog box, and then choose **OK**.

After you create the serverless application, you can run (invoke) or debug the local version of an AWS Lambda function that is contained in that application.

You can also deploy the serverless application. After you deploy it, you can (invoke) the remote version of a Lambda function that is part of that deployed application.
