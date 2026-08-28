---
source_url: https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-step-stop-model.html
---

# Step 5: Stop your model
<a name="gs-step-stop-model"></a>

In this step you stop running your model. You are charged for the amount of time your model is running. If you have finished using the model, you should stop it.

**To stop your model**

1. In the **Start or stop model** section choose **Stop**.
![Console screenshot including Stop button to stop the running custom label detection model.](http://docs.aws.amazon.com/rekognition/latest/customlabels-dg/images/get-started-stop-model.jpg)

1. In the **Stop model** dialog box, enter **stop** to confirm that you want to stop the model.
![Stop model dialog with text field to enter "stop" and confirm stopping the model.](http://docs.aws.amazon.com/rekognition/latest/customlabels-dg/images/get-started-stop-model-dialog.jpg)

1. Choose **Stop** to stop your model. The model has stopped when the status in the **Start or stop model** section is **Stopped**. In the following screenshot, the User interface section has the option to start or stop a machine learning model. The model's status shows as "Stopped" with a "Start" button to start the model and a dropdown to select the number of inference units.
![User interface section to start or stop a machine learning model, showing the model's status as "Stopped" with a "Start" button to start the model and a dropdown to select the number of inference units.](http://docs.aws.amazon.com/rekognition/latest/customlabels-dg/images/get-started-stopped-model.jpg)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
