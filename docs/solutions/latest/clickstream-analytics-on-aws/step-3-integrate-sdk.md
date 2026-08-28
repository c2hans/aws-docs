---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/step-3-integrate-sdk.html
---

# Step 3: Integrate SDK
<a name="step-3-integrate-sdk"></a>

 Once pipeline's status becomes `Active`, it is ready to receive clickstream data. Now you need to register an application to the pipeline, then you can integrate SDK into your application to enable it to send data to the pipeline.

## Steps
<a name="steps-2"></a>

1.  Log into **Clickstream Analytics on AWS Management Console**.

1.  In the left navigation pane, choose **Projects**, then select the project (quickstart) you just created in previous steps, click its title, and it will bring you to the project page.

1.  Choose **\+ Add application** to start adding application to the pipeline.

1.  Fill in the form as follows:
   +  App name: **test-app**
   +  App ID: The system will generate one ID based on the name, and you can customize it if needed.
   +  Description: **A test app for Clickstream Analytics on AWS guidance**
   +  Android package name: leave it blank
   +  App Bundle ID: leave it blank

1.  Choose **Register App & Generate SDK Instruction**, and wait for the registration to be completed.

1.  Select the tab **Android**, and you will see the detailed instruction of adding SDK into your application. You can follow the steps to add SDK.

1.  Choose **Download the config json file** to download the config file, and keep this file open, which will be used later.

 It will take about 3 \~ 5 minutes to update the pipeline with the application you just add. When you see the pipeline status become **Active** again, it is ready to receive data from your application.

 We have completed all the steps of adding an application to a project.

## Generate sample data
<a name="generate-sample-data"></a>

 You might not have immediate access to integrate SDK with your app. In this case, we provide a Python script to generate sample data to the pipeline you just configured, so that you can view and experience the analytics dashboards.

**Important**
Python 3.8\+ is required.

1.  Clone the repository to your local environment.

   ```
   git clone https://github.com/aws-solutions-library-samples/guidance-for-clickstream-analytics-on-aws.git
   ```

1.  After you cloned the repository, change directory into the `examples/standalone-data-generator` project folder.

1.  Install the dependencies of the project.

   ```
   pip3 install requests
   ```

1.  Put `amplifyconfiguration.json` into the root of `examples/standalone-data-generator` which you downloaded in **register an app** step. See the `examples/standalone-data-generator/README.md` for more information.

1.  Open an terminal at this project folder location. For example, if you are using Visual Studio Code IDE, at the top of **Visual Studio Code**, click **Terminal** -> **New Terminal** to open a terminal.

1.  Copy the following command and paste it to the terminal:

   ```
   python3 create_event.py
   ```

 Let‘s enter the `Enter` key in terminal to execute the program. If you see the following output, this means that the program execution is completed.

```
job finished, upload 4360476 events, cost: 95100ms
```

This process will take about 10 minutes with default configuration. After job is finished, you can move to next step.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
