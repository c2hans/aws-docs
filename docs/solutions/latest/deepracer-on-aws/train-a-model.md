---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/train-a-model.html
---

# Train a model
<a name="train-a-model"></a>

Training is how the model learns optimal driving behaviors by repeatedly interacting with the simulated track environment. During training, the vehicle explores different actions (steering angles and speeds) in response to various track states (camera images), receiving rewards based on a user-defined reward function that incentivizes desired behaviors like staying on the center-line or completing laps quickly. This trial-and-error allows the model to discover which actions maximize rewards, refining its neural network weights with each training iteration until it converges on a policy that consistently navigates the track successfully.

Training automatically begins right after you create the model. After creating a model, you will be redirected to the model detail view, and you will see that the model is in one of the following states as indicated by the label shown in the Training section.
+  **Queued** - the model has been queued for training, and training will begin shortly.
+  **Initializing** - the resources needed for performing the training job are warming up.
+  **Training** - the model is actively being trained against the parameters you provided while creating the model.
+  **Ready** - the model has completed training and can be either submitted for evaluation or submitted to a community race. It can also be exported.
+  **Error** - the model has encountered an error during training.

During training, you can view the progress of how your vehicle attempts to complete the track through the video player in the Training section. After training is completed, you can submit your model for evaluation or to a virtual race.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
