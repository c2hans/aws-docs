---
source_url: https://docs.aws.amazon.com/machine-learning/latest/dg/tutorial.html
---

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Tutorial: Using Amazon ML to Predict Responses to a Marketing Offer
<a name="tutorial"></a>

With Amazon Machine Learning (Amazon ML), you can build and train predictive models and host your applications in a scalable cloud solution. In this tutorial, we show you how to use the Amazon ML console to create a datasource, build a machine learning (ML) model, and use the model to generate predictions that you can use in your applications.

Our sample exercise shows how to identify potential customers for a targeted marketing campaign, but you can apply the same principles to create and use a variety of ML models. To complete the sample exercise, you will use publicly available banking and marketing datasets from the [University of California at Irvine (UCI) Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets.php). These datasets contain general information about customers, and information about how they responded to previous marketing contacts. You will use this data to identify which customers are most likely to subscribe to your new product, a bank term deposit, also known as a certificate of deposit (CD).

**Warning**
This tutorial is not included in the AWS free tier. For more information about Amazon ML pricing, see [*Amazon Machine Learning Pricing*](https://aws.amazon.com/machine-learning/pricing/).

## Prerequisite
<a name="prereqs"></a>

 To perform the tutorial, you need to have an AWS account. If you don't have an AWS account, see [Setting Up Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/setting-up-amazon-machine-learning.html).

## Steps
<a name="steps"></a>
+ [Step 1: Prepare Your Data](step-1-download-edit-and-upload-data.md)
+ [Step 2: Create a Training Datasource](step-2-create-a-datasource.md)
+ [Step 3: Create an ML Model](step-3-create-an-ml-model.md)
+ [Step 4: Review the ML Model's Predictive Performance and Set a Score Threshold](step-4-review-model-and-set-cutoff.md)
+ [Step 5: Use the ML Model to Generate Predictions](step-5-create-predictions.md)
+ [Step 6: Clean Up](step-6-clean-up.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Machine Learning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
