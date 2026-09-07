---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/creating-production-ready-ml-pipelines-on-aws/step5.html
---

# Step 5. Run the pipeline
<a name="step5"></a>

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/creating-production-ready-ml-pipelines-on-aws/images/guide-img/38c6f8a0-9908-46ce-9db4-ad6b4c4bc218/images/9164a5b0-a802-43af-b53e-b8183952aa1a.png)

This step runs the training or inference pipeline that was created in the AWS CloudFormation stacks in step 4. The pipeline can't be run until its internal placeholder parameters have been populated with concrete values. This action of assigning values to placeholder parameters is the primary activity of step 5. Example placeholder parameters include:
+ The location of input, output, and intermediate datasets
+ The Amazon S3 location of the runtime scripts and other preprocessing or evaluation code that was developed in step 2 (for example, sm\_submit\_url for the training pipeline)
+ The name of the AWS Region

You have to make sure that these path values point to valid data or code before you run the pipeline. For example, if you populate the placeholder parameter that represents the Amazon S3 URL of the Python runtime scripts, you must upload those scripts to that URL. The person who runs the pipeline is responsible for consistency checking and data uploading. People who define or create the pipeline do not have to worry about any of this.  Depending on the maturity of the pipeline, this step may be automated to run on a regular  (weekly or monthly) basis. Automation also requires robust monitoring, which is an important area but outside the scope of this guide. For the training pipeline run, it would be appropriate to monitor evaluation metrics. For the inference pipeline, it would be appropriate to monitor the input data distribution drift, and, if possible, collect labels periodically and measure the drift in prediction accuracy. These records from the training and inference runs should be recorded in a database for analysis at a later point in time.
