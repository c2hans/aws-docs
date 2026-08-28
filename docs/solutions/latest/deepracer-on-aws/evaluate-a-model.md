---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/evaluate-a-model.html
---

# Evaluate a model
<a name="evaluate-a-model"></a>

 **Overview**

Evaluation is the process of testing a trained reinforcement learning model’s performance on a track to measure how well it has learned to navigate autonomously. During evaluation, the model is deployed in the simulator (or on a physical DeepRacer car) and runs through multiple laps without further learning, allowing you to assess key performance metrics such as lap completion rate, lap times, and consistency across different track conditions.

Evaluation is critical because it provides objective feedback on whether the model’s learned behaviors translate into successful track navigation, helps identify which checkpoint or iteration produced the best-performing model, and guides decisions about whether to continue training, adjust the reward function, or deploy the model to competitions. Unlike training where the agent explores and learns through trial and error, evaluation focuses purely on measuring the model’s current capabilities in a controlled testing environment.

 **Submitting a model for evaluation**

To submit a trained model for evaluation, click the Evaluation tab in the model detail view, and either click **Start evaluation** or **Start new evaluation**. This will bring you to a page where you will be asked to provide:
+  **Evaluation name** - pick a unique name for the evaluation (i.e. "my-evaluation-001").
+  **Race type** - either time trial or object avoidance.
  + If you select object avoidance, you’ll be asked to specify whether you’d like objects to be placed in fixed or random locations; how many objects you would like placed; and the locations of those objects if you opt to use fixed locations.
+  **Race track** - the type of track to evaluate your model on.
+  **Track direction** - the direction in which you would like your vehicle to travel.
+  **Number of laps** - the number of laps you would like your vehicle to attempt.

When you’re ready to proceed, click **Start evaluation**.

 **Monitoring progress**

After submitting a model for evaluation, you will see a new entry in the **Evaluations** **selector** and details of the evaluation below. The evaluation status will show as "initializing" before beginning, this usually takes a few minutes. You can find the details of the evaluation you have configured below in the **Evaluation configuration** section.

When the evaluation begins, you will be able to see your vehicle’s progress around the selected track in the video player. You will also see lap results being posted in the **Evaluation results** table to the right of the video player as the car completes each lap around the track.

After the evaluation finishes, you can download the logs for that evaluation by clicking the **Download logs** button.

**Note**
Logs are exported in .tar.gz format. If you are using Windows, you will need to install 7-Zip or another program that is capable of extracting this type of file.

To view an existing evaluation, select the evaluation from the list in the **Evaluations** **selector**, then click **Load evaluation** button. This will load details of the selected evaluation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
