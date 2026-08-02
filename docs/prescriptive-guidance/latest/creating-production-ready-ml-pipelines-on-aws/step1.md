---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/creating-production-ready-ml-pipelines-on-aws/step1.html
---

# Step 1. Perform EDA and develop the initial model
<a name="step1"></a>

In this step, data scientists perform exploratory data analysis (EDA) in order to understand the ML use case and data. They then develop the ML models (for example, classification and regression models) to solve the problem in a given use case. During model development, the data scientist often makes assumptions about inputs and outputs, such as data formats, the data lifecycle, and locations of intermediate output. These assumptions should be documented so that they can be used for verification during unit tests in step 2.

Although this step focuses on model development, data scientists often have to write a minimum amount of helper code for preprocessing, training, evaluation, and inference. The data scientist should be able to run this code in the development environment. We also recommend providing optional runtime arguments so that this helper code can be dynamically configured to run in other environments without extensive manual changes. This will accelerate the integration between the model and the pipeline in steps 2 and 3. For example, code for reading the raw data should be encapsulated in functions so that data can be preprocessed in a consistent manner.

We recommend that you start with a framework such as [scikit-learn](https://scikit-learn.org), [XGBoost](https://xgboost.ai/), [PyTorch](https://pytorch.org/), [Keras](https://keras.io/), or [TensorFlow](https://www.tensorflow.org/) to develop the ML model and its helper code. For example, scikit-learn is a a free ML library that's written in Python. It provides a uniform API convention for objects, and includes four main objects—*estimator*, *predictor*, *transformer,* and *model*—that cover lightweight data transforms, support label and feature engineering, and encapsulate preprocessing and modeling steps. These objects help avoid boilerplate code proliferation and prevent validation and test data from leaking into the training dataset. Similarly, every ML framework has its own implementation of key ML artifacts, and we recommend that you comply with the API conventions of your selected framework when you develop ML models.
