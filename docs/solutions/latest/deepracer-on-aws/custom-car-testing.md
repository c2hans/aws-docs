---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/custom-car-testing.html
---

# Calibrate and test
<a name="custom-car-testing"></a>

Before deploying a model, calibrate the vehicle’s steering and throttle through the AWS DeepRacer console.

1. In the console, choose **Vehicle**, then choose **Calibration**.

1. Follow the on-screen instructions to set the steering center, maximum left, and maximum right values.

1. Set the throttle minimum, maximum, and stopped values.

To deploy and test a reinforcement learning model:

1. In the console, choose **Models** and upload a model trained using the DeepRacer on AWS solution. Custom cars built using this guide are fully compatible with models trained in the DeepRacer on AWS solution — no retraining is required.

1. Choose the uploaded model, and then choose the **Start vehicle** button.

1. Place the vehicle on your track and observe autonomous driving behavior.

For further customization options and community support, see the [AWS DeepRacer Community custom car repository](https://github.com/aws-deepracer-community/deepracer-custom-car) on the GitHub website.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
